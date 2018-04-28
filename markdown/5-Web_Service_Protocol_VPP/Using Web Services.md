# Using Web Services

 [Configuration Profile Reference - Using Web Services](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW16)  
  

## Using Web Services
  

You access the services described in this chapter through the MDM payloads described in [Structure of MDM Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW50).  

  

### Service Request URL
  

The service URL has the form of:  

[https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/<serviceName](http://livepage.apple.com/)>  

It is recommended that you obtain the service URLs from the `VPPServiceConfigSrv` service rather than using hard-coded values in the client. All service URLs are subject to change except for the `VPPServiceConfigSrv` URL.  

  

### Providing Parameters
  

Parameters to the service requests should be provided as a JSON string in the request body, and the `Content-Type` header value should contain `application/json`.  

The value of a parameter can be in primitive type or string type. When the web services receive input parameters, all primitive types are converted to string type first before they are parsed into primitive types as required by the specific parameter. For example, `licenseId` requires a long type; the input in JSON format can be either `{"licenseId":1}` or `{"licenseId":"1"}`. The responses of the services use primitive type for non-string values.  

  

### Authentication
  

All services except `VPPServiceConfigSrv` require an `sToken` parameter to authenticate the client user. This parameter takes a secret token (in string format). A Program Facilitator can obtain such a token by logging in to [https://vpp.itunes.apple.com/](https://vpp.itunes.apple.com/).  

On the Account Summary page, click the Download button to generate and download a text file containing the new token. Each token is valid for one year from the time you generate it. Once created, tokens are listed on the Account Summary page.  

The MDM server should store the user’s token along with its other private, protected properties and should send this token value in the `sToken` field of all VPP requests described in this chapter.  

The `sToken` blob itself is a JSON object in Base64 encoding. When decoded, the resulting JSON object contains three fields: `token`, `expDate`, and `orgName`. For example, the following is an `sToken` value (with line breaks inserted):  

```
eyJ0b2tlbiI6InQxWG9VenBMRXRwZGxhK25zeENkd3JjdDBS
andkaWNOaGRreW5STW05VVAyc2hSYTBMUnVGcVpQM0pLQmJU
TWxDSE42ajNta1R6WVlQbVVkVXJXV2x3PT0iLCJleHBEYXRl
IjoiMjAxNC0wOC0xNVQxODoxMzo1Mi0wNzAwIiwib3JnTmFt
ZSI6Ik9SRy4yMDA5MDcxNjAwIn0=
```  

After Base64 decoding, this is the JSON string (with line breaks inserted):  

```
{"token":"t1XoUzpLEtpdla+nsxCdwrct0RjwdicNhdkynRMm9UP
2shRa0LRuFqZP3JKBbTMlCHN6j3mkTzYYPmUdUrWWlw==",
"expDate":"2014-08-15T18:13:52-0700",
"orgName":"ORG.2009071600"}
```  

The `expDate` field contains the expiration date of the token in ISO 8601 format. The `orgName` field contains the name of the organization for which the token is issued.  

  

### Service Response
  

Response content is in JSON format.  

As a convention, fields with `null` values are not included in the response. For example, the user object has an `email` field that is optional. The following example doesn’t have the `email` field in the user object, so the `email` field value is `null`.  

```
   "user":{
      "userId":1,
      "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8",
      "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc=",
      "status":"Associated",
      "licenses":[
         {
            "licenseId":2,
            "adamId":408709785,
            "productTypeId":7,
            "pricingParam":"STDQ",
            "productTypeName":"Software",
            "isIrrevocable":false
         },
         {
            "licenseId":4,
            "adamId":497799835,
            "productTypeId":7,
            "pricingParam":"STDQ",
            "productTypeName":"Software",
            "isIrrevocable":false
         }
      ]
   }
```  

Note the licenses associated with the user are returned as an array. If the user doesn’t have a license, the “licenses” field does not show up. The license object in this context is a subfield of the user object. To avoid a cyclic reference, the user object is not included in the license object. But if the license is the top object returned, it includes a `user` object with `id` and `clientUserIdStr` fields and, if the user is already associated with an iTunes account, an `itsIdHash` field.  

JSON escapes some special characters including slash (`/`). So a URL returned in JSON looks like: `"https:\/\/vpp.itunes.apple.com\/WebObjects\/MZFinance.woa\/wa\/registerVPPUserSrv"`.  

For any service that requires authentication with an `sToken` value, if the provided token is within the expiration warning period (currently 15 days before the expiration date), then the response contains an additional field, `tokenExpDate`. The value of this field is the expiration date in ISO 8601 format. For example:  

"tokenExpDate":"2013-07-26T18:12:09-0700"  

If this field is present in the response, it should serve as a reminder that it is time to get a new `sToken` blob in order to avoid any service disruption.  

  

### Retry-After Header
  

The VPP service may return a 503 Service Unavailable status to clients whose requests result in an unusually high load on the VPP service, or when the VPP service is experiencing loads beyond its current capacity to respond to requests. A Retry-After header may be included in this response, indicating how long the client must wait before making additional requests. Clients who make requests before this time may be rejected for even longer periods of time, or (in extreme cases) may have their VPP account suspended.  

Avoid triggering the Retry-After header by setting the `assignedOnly` parameter `true` in calls to `getVPPLicensesSrv`.   

The Retry-After response-header field may also be used with any 3xx (Redirection) response to indicate the minimum time the user-agent is asked to wait before issuing the redirected request (see [RFC 2616: HTTP/1.1](http://www.rfc-base.org/txt/rfc-2616.txt), Section 14.37). The value of this field can be either an HTTP-date or an integer number of seconds (in decimal) after the time of the response.  

`    Retry-After = "Retry-After" ":" ( HTTP-date | delta-seconds )`  

Two examples of its use are:  

`    Retry-After: Fri, 31 Dec 1999 23:59:59 GMT`  

`    Retry-After: 120`  

In the latter example, the delay is 2 minutes.  

  

### VPP Account Protection
  

It is reasonable behavior for a product that manages VPP app assignments to reset the VPP account by retiring all users and revoking all app assignments when it is first configured to use a VPP account. Therefore, it is very important that your product always sets the `clientContext` data as documented below so that other products that manage VPP accounts can know that the VPP account is being managed by another product and not reset the VPP account without warning.  

To ensure that a VPP account is not being managed by another product, follow these steps every time your product starts a VPP session:  


* During initial setup, check the `clientContext` attribute returned from the `VPPClientConfigSrv` request. 

 

   * If `clientContext` is empty, create a JSON string with these keys and values: 

   * `    {"hostname":<my.servername.com>, "guid":<random_uuid>}` 

   * The UUID should be a standard 8-4-4-4-12 formatted UUID string and must be unique for each installation of your product. 

   * Write this JSON string to `clientContext` to claim this VPP account for your product. 

   * If `clientContext` is not empty and does not match the `guid` value of your product, report the `hostname` returned by `clientContext` and confirm that your product should take over from it. Do not rely on `hostname` to confirm that your product still has a proper claim on the VPP account. 
 

* At the start of every subsequent VPP session, check `clientContext` to ensure that it still represents the correct installation of your product. 

* If `clientContext` no longer refers to your product, do not make any further requests to the VPP service for that VPP account until the account has been reactivated by administrator commands. Your product should report this isolation action to an administrator, giving the `hostname` of the server that now claims to manage the VPP account. 
  

  

### Initial Import of VPP Managed Distribution Assigned Licenses Using getVPPLicensesSrv
  

It is not necessary to sync every single app license for a specific VPP account. In fact, you only need to track the assigned licenses. The recommended procedure for importing assigned licenses is to skip importing all of the licenses and instead start importing license counts and then changes. This can be accomplished in the following way:  


1. Send a request using `getVPPAssetsSrv` with `includeLicenseCounts : true`. This returns the current license count by `adamID`. 

2. Send one request using `getVPPLicensesSrv`. Record the `batchToken` and `totalBatchCount`. Always set `assignedOnly=true`. 

3. Send another request to `getVPPLicensesSrv` using the `batchToken` value from Step 2 and an `overrideIndex` value equal to `totalBatchCount`. Always set `assignedOnly=true`. 

4. Record the `sinceModifiedToken` value and begin syncing license updates and changes instead of all licenses. Always set `assignedOnly=true`. 
  

**Note:** Using `sinceModifiedToken` can result in batches with zero records in them. This is not an error or an end signal; just move to the next batch.  

For further information, see [Parallel getVPP Requests](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW22) and [getVPPLicensesSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW8).  

  

### productTypeId Codes
  

Some service requests may return the ID of an Apple product type as a decimal integer, with one of these values:  


|productTypeId|Meaning|
|-|-|
|`7`|macOS software.|
|`8`|iOS or macOS App Store app.|
|`10`|book.|
  

  

### Managed Apple IDs
  

Managed Apple IDs were introduced in iOS 9.3. These accounts can be tied to the same organization as the VPP Program Facilitator users who manage licenses. When this is the case, the MDM server may choose to instruct the VPP service to associate Managed Apple IDs with given VPP users. This removes the need to send out an invitation (email or push) to users and wait for them to join by going through an acceptance process.  

Managed Apple IDs are implemented through the following services by adding an optional parameter, `managedAppleIDStr`:  


* [registerVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW5) 

* [editVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW12) 
  

Apple uses the Apple ID passed in `managedAppleIDStr` to look up the user’s `organizationId`. If the VPP Program Facilitator account associated with the `sToken` making the request is also a Managed Apple ID and that Apple ID’s `organizationId` is the same as the user’s, the VPP user will be linked to that Apple ID.  

If the user cannot be found in the iTunes database, or the user is found but the user’s `organizationId` does not match the `organizationId` of the `sToken`’s associated user, the service response returns error 9635, `APPLE_ID_CANT_BE_USED`.  

  

### Program Facilitators
  

As described in [Authentication](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW20), Program Facilitators obtain from the iTunes VPP website the `sToken` parameters that must be passed in VPP service requests. Each `sToken` authenticates an organization through the associated Program Facilitator account that generated it.  

Managed Apple IDs make it possble for multiple Program Facilitators to be linked together into a group. Each Program Facilitator in the group is assigned a `facilitatorMemberId`. An `sToken` can use this `facilitatorMemberId` to access and change data associated with different Program Facilitators as long as the other Program Facilitators are in the same group. Using [VPPClientConfigSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW14), the MDM server can discover member info about all the other Program Facilitators whose data its `sToken` can access, including the `facilitatorMemberId` of each member.  

All VPP service calls, except `VPPClientConfigSrv`, accept an optional  `facilitatorMemberId` parameter. It is subject to these rules:  


* If a Program Facilitator’s `facilitatorMemberId` is passed in a service request, the service is executed as if the request had been made with that Facilitator’s `sToken` instead. 

* If a service request passes the `facilitatorMemberId` of a Program Facilitator that was never associated with the requesting organization, or left it, or is no longer managed, an error is returned. 
  

Here is an example of a `VPPClientConfigSrv` response when the `sToken` passed to it is associated with a group of three users, each of which has a different Program Facilitator:  

```
{
    "apnToken": "aJQGSAd+H7FrmIZn9K4IbRbXpge3ySkchugcfYK/ZXg=",
    "appleId": "user1@someorg.com",
    "clientContext": "{\"guid\":\"e91e570f-3eba-4b43-97d3-0f39450c8b92\",
       \"hostname\":\"vpp-integrations2.apple.com\",\"ac2\":1}",
    "countryCode": "US",
    "email": "user1@someorg.com",
    "facilitatorMemberId": 200841,
    "organizationId": 2168850000179778,
    "status": 0,
    "vppGroupMembers": [
        {
            "appleId": "user3@someorg.com",
            "clientContext": "test123test123test123",
            "email": "user3@someorg.com",
            "facilitatorMemberId": 200844,
            "organizationId": 2168850000179778,
            "locationId": 2167975000001686,
            "locationName": "Central School"
        },
        {
            "appleId": "user1@someorg.com",
            "clientContext": "{\"guid\":\"e91e570f-3eba-4b43-97d3-0f39450c8b92\",
               \"hostname\":\"vpp-integrations2.apple.com\",\"ac2\":1}",
            "email": "user1@someorg.com",
            "facilitatorMemberId": 200841,
            "organizationId": 2168850000179778,
            "locationId": 2167975000001686,
            "locationName": "Central School"
        },
        {
            "appleId": "user2@someorg.com",
            "email": "user2@someorg.com",
            "facilitatorMemberId": 200843,
            "organizationId": 2168850000179778,
            "locationId": 2167975000001686,
            "locationName": "Central School"
        }
    ]
}
```  

Note that `vppGroupMembers` contains all of the members of the Program Facilitator’s group, including the calling member.  

  

#### Read-Only Access
  

Using [Apple School Manager](https://help.apple.com/schoolmanager/) and Managed Apple IDs, you can tailor different sets of privileges for individual Program Facilitators. This allows a finer range of control on what such users can do. For example, a Program Facilitator that has only the “Read Only” privilege can use the `getVPPUserSrv`, `getVPPUsersSrv`, and `getVPPAssetsSrv` services but not use `retireVPPUserSrv`, `disassociateVPPLicenseSrv`, or `manageVPPLicensesByAdamIdSrv`. You can also assign Program Facilitators “Can Purchase” and/or “Can Manage” privileges, so an individual Program Facilitator could manage licenses but not buy them. (Note that purchasing users and managing users automatically have read privileges.)  

  

### Error Codes
  

When a service request results in error, there are normally two fields containing the error information in the response: an `errorNumber` field and an `errorMessage` field. There could be additional fields depending on the error. The `errorMessage` field contains human-readable text explaining the error. The `errorNumber` field is intended for software to interpret. Any `errorMessage` value uniquely maps to an `errorNumber` value, but not the other way around. The possible `errorNumber` values are defined as follows:  


|errorNumber|Meaning|
|-|-|
|`9600`|Missing required argument|
|`9601`|Login required|
|`9602`|Invalid argument|
|`9603`|Internal error|
|`9604`|Result not found|
|`9605`|Account storefront incorrect|
|`9606`|Error constructing token|
|`9607`|License is irrevocable|
|`9608`|Empty response from SharedData service|
|`9609`|Registered user not found|
|`9610`|License not found|
|`9611`|Admin user not found|
|`9612`|Failed to create claim job|
|`9613`|Failed to create unclaim job|
|`9614`|Invalid date format|
|`9615`|OrgCountry not found|
|`9616`|License already assigned (see [Error Code 9616](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW403))|
|`9618`|The user has already been retired|
|`9619`|License not associated|
|`9620`|The user has already been deleted|
|`9621`|The token has expired. You need to generate a new token online using your organization’s account at [https://vpp.itunes.apple.com/](https://vpp.itunes.apple.com/).|
|`9622`|Invalid authentication token|
|`9623`|Invalid Apple push notification token|
|`9624`|License was refunded and is no longer valid.|
|`9625`|The sToken has been revoked.|
|`9626`|License already assigned to a different user. The MDM server should retry the assignment with a different license.|
|`9628`|Ineligible device assignment: MDM tried to assign an item to a serial number but device assignment is not allowed for that item.|
|`9630`|Too many recent already-assigned errors: If MDM gets the same 9616 error from assignments for the same organization, user identifier, and item identifier (license ID, adam ID, or pricing parameter) and does so within too short a time (generally several minutes), it may return this error code.|
|`9631`|Too many recent no-license errors: If MDM gets the same 9610 error from assignments for the same organization, user identifier, and item identifier (license ID, adam ID, or pricing parameter) and does so within too short a time (generally several minutes), it may return this error code.|
|`9632`|Too many recent manage-license calls with identical request: If MDM gets precisely the same request to `manageVPPLicensesByAdamIdSrv` too many times within too short a time (generally several minutes), it may return this error code.|
|`9633`|Data for a batch token passed could not be recovered.|
|`9634`|Returned when a caller tries to use a formerly deprecated featured that has been removed.|
|`9635`|Apple ID passed for iTunes Store association cannot be found or is not applicable to organization of the user (see [Managed Apple IDs](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW501)).|
|`9636`|Registered user not found.|
|`9637`|`sToken` is not allowed to perform the operation requested.|
|`9638`|Facilitator account that generated `sToken` has no Managed ID organization ID and cannot manipulate the facilitator member requested.|
|`9639`|No facilitator member could be found for the facilitator member ID requested.|
|`9640`|Account details of the facilitator member ID requested could not be recovered (likely a transient issue).|
|`9641`|Apple ID already associated to registered user.|
|`9642`|Apple ID passed cannot be used at this time because it's a VPP manager and the iTunes Store account not yet created and such creation requires user to agree to Terms.|
  

Additional error types may be added in the future.  

  

#### Error Code 9616
  

Error number `9616` is returned when an attempt is made to assign a license to a user that already has a license for the specified app or book, in which case there is no need to retry the assignment.  

Additional information is returned to  MDM when a `9616` error occurs. Sometimes it’s because the specific user in the request is already assigned to the item in question. When that happens the `9616` error is accompanied by a `licenseAlreadyAssigned` entry with details about the user and the license. For example,  

```
{"licenseAlreadyAssigned":{"pricingParam":"STDQ","itsIdHash":
"XuHVGvasXcfEVUUn4EP2wjHEUK00s=","userId":9918783273,"productTypeId":8,
"isIrrevocable":false,"adamIdStr":"778658393","userIdStr":"9918783273",
"licenseIdStr":"99147599840","productTypeName":"Application",
"clientUserIdStr":"xxutt8-e079-4b05-b403-a0792890",
"licenseId":9147599840,"adamId":778658393,"status":"Associated"},
"errorMessage":"License already assigned","errorNumber":9616,"status":-1}
```  

Alternatively, a `9616` error may have a `regUsersAlreadyAssigned` entry in the response with information about the one or more other users who already have the item in question. In these cases, the VPP user specified by the user ID or the `clientUserIdStr` does not have the item, but some other users in the organization associated with the same iTunes Store account has the item. If that happens, the server returns `9616` and information about those other users:  

```
{"errorMessage":"License already assigned",
"regUsersAlreadyAssigned":[{"itsIdHash":"XXX2CVvZar9YZnpqJxV0SHOUCU=",
"clientUserIdStr":"jjjCXhHHee0e3c-x999-43a9-Xe04-1dcax80ac01x",
"userId":9991992450,"email”:”user@example.apple.com","status":"Associated"}],"
"errorNumber":9616,"status":-1}
```