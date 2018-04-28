# VPP App Assignment

 [Configuration Profile Reference - VPP App Assignment](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html)  
  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/ManagedAppsUpdates/ManagedAppsUpdates.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html)
  
In iOS 7 and later or macOS v10.9 and later, Volume Purchase Program (VPP) App Assignment allows an organization to assign apps to users. At a later date, if a user no longer needs an app, you can reclaim the app license and assign it to a different user. In iOS 9 and later or macOS v10.11 and later, VPP can assign a license to the device serial number, so no Apple ID is required to download the app.  
The Volume Purchase Program provides a number of web services that MDM servers can use to associate volume purchases with particular users or devices. The following services are currently supported:  

* Create a user in the iTunes Store representing a user in the MDM system, against which licenses and an iTunes Store account may be linked: [registerVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW5). 

* Determine the current iTunes account status of one or more VPP users: [getVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW6) or [getVPPUsersSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW7). 

* List the VPP assets for which an organization has licenses, including counts of assigned and unassigned licenses for each asset: [getVPPAssetsSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW302). 

* Query the iTunes Store for information about apps and books: [contentMetadataLookupUrl](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW209). 

* Disassociate a VPP user from their iTunes account and release their revocable licenses: [retireVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW9). 

* Perform batch associations or disassociations of multiple VPP users or devices with their licenses: [manageVPPLicensesByAdamIdSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW301). 

* Fetch or update a VPP user’s email address and optionally link to a Managed Apple ID: [editVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW12). 

* Store and/or return organization-specific information to/from the VPP server: [VPPClientConfigSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW14). 

* Fetch the current list of VPP web service URLs and error numbers: [VPPServiceConfigSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW15). 

* Determine the statuses of a VPP user’s current licenses for software and other products: [getVPPLicensesSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW8). Please note that this service will be deprecated and its use should be avoided. 
  
  

## VPP in Apple School Manager
  

In the Fall of 2017, VPP was added into Apple School Manager. Apple School Manager is a single destination for schools to manage devices and content for their users. Moving VPP into the Apps and Books section of the Apple School Manager enables program facilitators (also referred to as content managers) to purchase content in the same place that they manage Apple IDs and devices for students and teachers. The purchases made in VPP in Apple School Manager are location based, making it much easier for content managers to move licenses between locations as needed.   

To support location based assets, VPP in Apple School Manager uses location tokens. The location tokens are used by content managers the same way as the legacy VPP tokens are used. Content managers download the location token from the settings page in Apple School Manager and upload it into their MDM. The MDM then has access to the licenses available at that location. Allocating the licenses within the MDM uses the same workflow for both types of licenses.  

VPP will continue to support legacy user based sTokens. Depending on the type of token used, VPP will return either the new location-based response or the existing user-based response. VPP API responses that differ by token type will have both the legacy and location based responses documented below.  

  

### Supporting VPP in Apple School Manager 
  

Migrating to VPP in Apple School Manager is recommended, but optional. Licenses assigned when using the legacy token must be managed by the content manager’s legacy token until they are transferred to a location. Therefore, MDMs will need to support both models of licensing at the same time. Failure to support the legacy and location based models of tokens will create discrepancies between user experiences in Apple School Manager and their MDM.  

To update your MDM to support location based tokens, these steps must be taken:  


* Update API calls to handle the location information being returned for the new VPP in Apple School Manager features. Licenses assigned with the legacy token will not have a location. All of the assets purchased with VPP in Apple School Manager will have additional location information in their API responses. Specifically, these API have been updated to return location information: [getVPPAssetsSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW302), [VPPClientConfigSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW14). 

* Update the MDM UI to show location names for the tokens and assets. Location names are not unique (many schools may have the same name) but location UIDs are unique to a specific location. Displaying the location name to the user is particularly important when location token is about to expire. 

* Refresh license status at appropriate times to maintain an accurate UI. Since licenses can be reallocated in the Apple School Manager, license counts will change outside of the MDM. Refreshing on each page load is recommended.  

* Use [getVPPAssetsSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW302), not [getVPPLicensesSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW8), to get license counts. [getVPPAssetsSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW302) is more efficient and will return a summary of adamIds and counts instead of all the licenses. 

* Handle when duplicate tokens are uploaded by different content managers. There is just one location token that needs to be stored, instead of a token per VPP account.  

* Handle new error codes for the location based tokens. 
  
  

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
  

## The Services
  

The following are the web services exposed to the Internet that can be requested by your client.  

  

### registerVPPUserSrv
  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`clientUserIdStr`|Required.|`"810C9B91-DF83-41DA-80A1-408AD7F081A8"`.|
|`email`|Not required.|`"user1@someorg.com"`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
|`managedAppleIDStr`|Not required.|`"user1@someorg.com"`.|
  

`clientUserIdStr` is a string field. It can be, for example, the GUID of the user. The `clientUserIdStr` strings must be unique within the organization and may not be changed once a user is registered. It should not, for example, be an email address, because an email address might be reused by a future user.  

When a user is first registered, the user’s initial status is `Registered`. If the user has already been registered, as identified by `clientUserIdStr`, the following occurs:  


* If the user’s status is `Registered` or `Associated`, that active user account is returned. 

* If the user’s status is `Retired` and the user has never been assigned to an iTunes account, the account’s status is changed to `Registered` and the existing user is returned. 

* If the user’s status is `Retired` and the user has previously been assigned to an iTunes account, a new account is created. 
  

Thus, it is possible for more than one user record to exist for the same `clientUserIdStr` value—one for each iTunes account that the `clientUserIdStr` value has been associated with in the past (in addition to a currently active record or a retired and never-associated record). Each of these users has a unique `userId` value. Over time, with iTunes Store assignment, retirement, and reassignment, it is possible for the `userId` value of the active user for a given `clientUserIdStr` to change.  

Further, if two user identifiers exist for a given `clientUserIdStr`, one assigned to an iTunes account and the other unassigned, and a user accepts an invitation to be associated, it is possible for the user to use the same iTunes account that he or she used previously.  If the user does, the unassigned user record gets marked with the `Retired` status, and the formerly retired user record gets moved to the `Associated` status.  

The `managedAppleIDStr` parameter is discussed in [Managed Apple IDs](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW501).  

When registering multiple users, [registerVPPUserSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW5) requests can be made in parallel.  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|`0` for success, `-1` for error.|
|`user`|`{`</br>`      "userId":100014,`</br>`      "email":"test_reg_user11@test.com",`</br>`      "status":"Registered",`</br>`      "inviteUrl":`</br>`"https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/`</br>`wa\/associateVPPUserWithITSAccount?inviteCode=`</br>`9e8d1ecc57924d9da13b42b4f772a066&mt=8",`</br>`      "inviteCode":"9e8d1ecc57924d9da13b42b4f772a066",`</br>`      "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8",`</br>`}`|
|`errorMessage`|`"\"clientUserIdStr\" or \"email\" is required input parameter"`.|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`errorNumber`|`9600`.|
  

  

### getVPPUserSrv
  

                     The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`userId`|One of these is required, but `userId` is deprecated.|`100001`.|
|`clientUserIdStr`|`810C9B91-DF83-41DA-80A1-408AD7F081A8`.|
|`itsIdHash`|Not required.|`"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
  

If a value is passed for `clientUserIdStr`, an `itsIdHash` (iTunes Store ID hash) value may be passed, but is optional. If a value is passed for `userId` is passed, that value is used, and `clientUserIdStr` and `itsIdHash` are ignored.  

The `getVPPUserSrv` request returns users with any status—`Registered`, `Associated`, `Retired`, and `Deleted`, as described below:  


* A `Registered` status indicates the user has been created in the system by making a `registerVPPUserSrv` request, but is not yet associated with an iTunes account. 

* An `Associated` status indicates that the user has been associated with an iTunes account. When a user is associated with an iTunes account, an `itsIdHash` value is generated for the user record. 

* A `Retired` status indicates that the user has been retired by making a `retireVPPUserSrv` request. 

* A `Deleted` status indicates that a VPP user is retired and its associated iTunes user has since been invited and associated with a new VPP user that shares the same `clientUserIdStr`. Because there are two VPP users with distinct `userId` values but the same `clientUserIdStr` value, the `Deleted` status is used to ensure database consistency. 

* This status appears only in the `getVPPUserSrv` service response, and only when a `userId` value is used to get a VPP user instead of a `clientUserIdStr` value. A user with a `Deleted` status, fetched by `userId`, will never change status again; its sole purpose is to ensure that your software can recognize that the `userId` is no longer associated with the `clientUserIdStr` record, and can update any internal references appropriately. 
  

Thus, it is possible for more than one user record to exist for the same `clientUserIdStr` value—one for each iTunes account that the `clientUserIdStr` value has been associated with in the past (in addition to a currently active record or a retired and never-associated record). However, no more than one of these records can be active at any given time.  

When a new record is associated with a `clientUserIdStr` value that has previously been associated with a different user, because the `clientUserIdStr` is still associated with the same iTunes user when it is retired and associated again, any irrevocable licenses originally associated with the retired VPP user, if any, are moved to the new VPP user (as identified by `userId`) automatically.  

If you use a `clientUserIdStr` value to fetch the VPP user after such a reassociation, the status of that user changes from `Retired` to `Associated`. If you use `userId` values to fetch the VPP users after the association, the status of the first VPP user changes from `Retired` to `Deleted`, and the status of the second VPP user changes from `Registered` to `Associated`.  

To obtain only the record for the currently active user matching a `clientUserIdStr` value, your MDM server passes the `clientUserIdStr` by itself. If no users for the `clientUserIdStr` are active (all are retired or no matching record exists), `getVPPUserSrv` returns a "result not found" error number.  

To obtain an old, retired user record that was previously associated with an iTunes Store account, your MDM server can pass either the `userId` for that record or the `clientUserIdStr` and `itsIdHash` for that record.  

All user record responses for this request include an `itsIdHash` if the user is associated with an iTunes account.  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|0 for success, -1 for error.|
|`user`|`{`</br>`      "userId":2,`</br>`      "email":"user2@test.com",`</br>`      "status":"Associated",`</br>`      "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8",`</br>`      "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc=",`</br>`      "licenses":[`</br>`         {`</br>`            "licenseId":4,`</br>`            "adamId":497799835,`</br>`            "productTypeId":7,`</br>`            "pricingParam":"STDQ",`</br>`            "productTypeName":"Software",`</br>`            "isIrrevocable": false`</br>`         }`</br>`      ]`</br>`}`|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`errorMessage`|`"Result not found"`.|
|`errorNumber`|`9604`.|
  

The `itsIdHash` field is omitted if the account is not yet associated with an iTunes Store account.  

Note the user object returned includes a list of licenses assigned to the user.  

  

### getVPPUsersSrv
  

       The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`batchToken`|Not required.|`EkZQCWOwhDFCwgQsUFJZkA`</br>`oUU0pKLEnOUAIKZOalpFYAR`</br>`YzA7OSc0pTUoNSSzKLUFJAy`</br>`Q6CSWgCS88JnkgAAAA==`.|
|`sinceModifiedToken`|Not required.|`0zJTU5SAEplpMF4wWCozJy`</br>`ezGKjS0NjM0tjUwtTA3MzQ`</br>`1FqhFgBuLPH3TgAAAA==`.|
|`includeRetired`|Not required.|`1`.|
|`includeRetiredOnly`|Not required.|`1`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
  

The `batchToken` and `sinceModifiedToken` values are generated by the server, and the `batchToken` value can be several kilobytes in size.  

You can use this endpoint to obtain a list of all known users from the server and to keep your MDM system up-to-date with changes made on the server. To use this endpoint, your MDM server does the following:  


* Makes an initial request to `getVPPUsersSrv` with no `batchToken` or `sinceModifiedToken` (optionally with the `includeRetired` field). 

* This request returns all user records associated with the provided `sToken`. 

* If the number of users exceeds a server controlled limit (on the order of several hundred), a `batchToken` value is included in the response, along with the first batch of users.  Your MDM server should pass this `batchToken` value in subsequent requests to get the next batch.  As long as additional batches remain, the server returns a new `batchToken` value in its response. 

* Once all records have been returned for the request, the server includes a `sinceModifiedToken` value in the response.  Your MDM server should pass this token in subsequent requests to get users modified since that token was generated. 

* Even if no records are returned, the response still includes a `sinceModifiedToken` for use in subsequent requests. 
  

The `includeRetired` value contains `1` if retired users should be included in the results, otherwise it contains `0`.  

If `includeRetiredOnly` is provided, the value of `includeRetired` is ignored. If `sinceModifiedToken` is provided and `includedRetiredOnly` is `1`, only retired users modified since the date in the token will be returned.  

> **Note:** The `batchToken` value encodes the original value of `includeRetired`; therefore, if a `batchToken` value is present on the request, the `includeRetired` field (if passed) is ignored.  
  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|`0` for success, `-1` for error.|
|`users`|`[`</br>`      {`</br>`         "userId":2,`</br>`         "email":"user2@test.com",`</br>`         "status":"Associated",`</br>`         "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8",`</br>`         "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="`</br>`      },`</br>`      {`</br>`         "userId":3,`</br>`         "email":"user3@test.com",`</br>`         "status":"Registered",`</br>`         "inviteUrl":`</br>`"https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/wa\/`</br>`associateVPPUserWithITSAccount?inviteCode=`</br>`f551b37da07146628e8dcbe0111f0364&mt=8",`</br>`         "inviteCode":"f551b37da07146628e8dcbe0111f0364",`</br>`         "clientUserIdStr":"293C9B02-DF83-41DA-20B7-203KD7F083C9"`</br>`      }`</br>`]`</br>Note that the `inviteUrl` field is present only for users whose status is `Registered`, not for users whose status is `Associated` or `Retired` status.|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`totalCount`|`5`</br>Note that this value is returned only for requests that do not include a `batchToken` value.|
|`errorMessage`|`"Result not found"`.|
|`errorNumber`|`9604`.|
|`batchToken`|`EkZQCWOwhDFCwgQsUFJZkA`</br>`oUU0pKLEnOUAIKZOalpFYAR`</br>`YzA7OSc0pTUoNSSzKLUFJAy`</br>`Q6CSWgCS88JnkgAAAA==`</br>Note that this field is present only if there are more entries left to read.|
|`sinceModifiedToken`|`0zJTU5SAEplpMF4wWCozJy`</br>`ezGKjS0NjM0tjUwtTA3MzQ`</br>`1FqhFgBuLPH3TgAAAA==`</br>Note that this field is present only if `batchToken` is not (that is, only after the last batch of users has been returned).|
  

The `itsIdHash` field is omitted if the account is not yet associated with an iTunes Store account.  

The `totalCount` field contains an estimate of the total number of records that will be returned.  

  

### getVPPLicensesSrv
  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`batchToken`|Not required.|`EkZQCWOwhDFCwgQsUFJZkA`</br>`oUU0pKLEnOUAIKZOalpFYAR`</br>`YzA7OSc0pTUoNSSzKLUFJAy`</br>`Q6CSWgCS88JnkgAAAA==`.|
|`sinceModifiedToken`|Not required.|`0zJTU5SAEplpMF4wWCozJy`</br>`ezGKjS0NjM0tjUwtTA3MzQ`</br>`1FqhFgBuLPH3TgAAAA==`.|
|`adamId`|Not required.|`408709785`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
|`assignedOnly`|Not required.|Defaults to `false`.|
|`pricingParam`|Not required.|”PLUS”|
|`serialNumber`|Not required.|"C9JQ5QWMXRGH”|
|`userAssignedOnly`|Not required.|Defaults to `false`.|
|`deviceAssignedOnly`|Not required.|Defaults to `false`.|
  

The `batchToken` and `sinceModifiedToken` values are generated by the server, and the `batchToken` value can be several kilobytes in size.  

You can use this endpoint to obtain a list of licenses from the server and to keep your MDM system up-to-date with changes made on the server. To use this endpoint, your MDM server does the following:  


* Makes an initial request to `getVPPUsersSrv` with no `batchToken` or `sinceModifiedToken`. 

* This request returns all licenses associated with the provided `sToken`. 

* If the number of licenses exceeds a server controlled limit (on the order of several hundred), a `batchToken` value is included in the response, along with the first batch of users.  Your MDM server should pass this `batchToken` value in subsequent requests to get the next batch.  As long as additional batches remain, the server returns a new `batchToken` value in its response. 

* Once all records have been returned for the request, the server includes a `sinceModifiedToken` value in the response.  Your MDM server should pass this token in subsequent requests to get licenses modified since that token was generated. 

* Even if no records are returned, the response still includes a `sinceModifiedToken` for use in subsequent requests. 
  

> **Note:** The `batchToken` and `sinceModifiedToken` encode whether `adamId` and `pricingParam` were originally passed; therefore, if the `batchToken` or `sinceModifiedToken` is present on the request, the `adamId` and `pricingParam` fields (if passed) are ignored.  
  

If  `pricingParam` is specified, `adamId` must be specified. Otherwise, the pricing parameter is ignored.  

If  `serialNumber` is specified, only licenses assigned to that serial number are returned.  

If the `assignedOnly` parameter is set to `true`, only licenses currently associated with an Apple ID or a device serial number are returned. When the `assignedOnly` parameter is omitted, all license records are returned regardless of association status. It is highly recommended to set the `assignedOnly` parameter to `true`, for performance reasons.  

If  `userAssignedOnly` is specified, only licenses currently assigned to users are returned.  

If  `deviceAssignedOnly` is specified, only licenses currently assigned to devices are returned.  

The parameters `userAssignedOnly` and `deviceAssignedOnly` are exclusive. They should never both be true in the same request.  

If a `pricingParam` parameter is not passed in the `getVPPLicensesSrv` request, the VPP service returns all licenses (both PLUS and STDQ `pricingParam` values).  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|`0` for success, `-1` for error.|
|`licenses`|`[`</br>`    {`</br>`        "licenseIdStr":1,`</br>`        "adamIdStr":408709785,`</br>`        "productTypeId":7,`</br>`        "pricingParam":"STDQ",`</br>`        "productTypeName":"Software",`</br>`        "isIrrevocable": false`</br>`    },`</br>`    {`</br>`        "licenseIdStr":2,`</br>`        "adamIdStr":408709785,`</br>`        "productTypeId":7,`</br>`        "pricingParam":"STDQ",`</br>`        "productTypeName":"Software",`</br>`        "isIrrevocable": false,`</br>`        "userId":1,`</br>`        "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8",`</br>`        "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="`</br>`    }`</br>`]`.|
|`totalCount`|`10`</br>Note that this value is returned only for requests that do not include a token.|
|`totalBatchCount`|`3`</br> Indicates the total number of round trips that will be necessary to get the full result set.|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`errorMessage`|`"Result not found"`.|
|`errorNumber`|`9604`.|
|`batchToken`|`EkZQCWOwhDFCwgQsUFJZkA`</br>`oUU0pKLEnOUAIKZOalpFYAR`</br>`YzA7OSc0pTUoNSSzKLUFJAy`</br>`Q6CSWgCS88JnkgAAAA==`</br>Note that this field is present only if there are more entries left to read.|
|`sinceModifiedToken`|`0zJTU5SAEplpMF4wWCozJy`</br>`ezGKjS0NjM0tjUwtTA3MzQ`</br>`1FqhFgBuLPH3TgAAAA==`</br>Note that this field is present only if `batchToken` is not (that is, only after the last batch of users has been returned).|
  

Licenses that are assigned to a user contain `userId`, `clientUserIdStr`, and `itsIdHashfield` fields, as shown in the second example above. The `totalBatchCount` field contains the total number of round trips that are necessary to get all records in the request. This can be used to provide a progress indicator when compared to the number of batches processed so far.  

> **Note:** 
The `totalCount` value is returned only on the request that started the batch process (the listing request issued without any tokens), because the actual number of licenses or users returned can be different by the time the client has finished.  
  

One of a set of sequential `getVPPLicensesSrv` batch requests may return an error. It is also possible to get a response from a listing call that includes no token but also no error number. Because all listing API requests should return either a batch or `sinceModified` token, do not interpret an error or the lack of a token for an individual batch to mean that the last batch has been received. The last batch is signified by the inclusion of a `sinceModifiedToken`. If an individual batch request fails, the MDM server should retry the same batch using the same `batchToken`.  

Receiving a `9603 'Internal Error'` response typically indicates that the VPP server couldn’t provide timely processing. Nothing is necessarily wrong with the request. When the MDM server receives this response, it should send the current request again. If it continues to receive `9603` errors after more than five attempts, it may mean that the VPP service is unexpectedly down and further retries should be scheduled for minutes later, instead of seconds.  

  

#### Parallel getVPP Requests
  

Both the `getVPPLicensesSrv` and `getVPPUsersSrv` services can accept multiple requests in parallel, instead of sequentially, which can significantly reduce the amount of time required to request all licenses and users. You start by making an initial request to receive a `batchToken`. Subsequent requests can be submitted in parallel by submitting the same `batchToken` and including an `overrideIndex` value from 1 to `totalBatchCount`, which is now returned with `getVPPLicensesSrv` requests. The request in which the `overrideIndex` value is equal to the `totalBatchCount` returns the new `sinceModifiedToken`.  

It is advisable not to submit more than five requests simultaneously.  

  

### getVPPAssetsSrv
  

This service returns an enumeration of the assets (`{adamIdStr, pricingParam}` tuples) for which an organization has licenses, along with an optional count of the total number of licenses and the number of licenses available for each asset.  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`includeLicenseCounts`|Not required. Defaults to `false`.|`true`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`pricingParam`|Not required.|”PLUS” or “STDQ”.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
  

If `includeLicenseCounts` is set to true, the total number of licenses, the number of licenses assigned, and the number of licenses unassigned are included with the response for each asset.  

if `pricingParam` is specified, only assets purchased with that pricing parameter will be included in the result.  


|Field Name|Example of Value|
|-|-|
|`status`|`0 for success, -1 for error.`|
|`assets`|`[`</br>`    {`</br>`        "adamIdStr":"375380948",`</br>`        "assignedCount":2,`</br>`        "availableCount":8,`</br>`        "deviceAssignable":true,`</br>`        "isIrrevocable":false,`</br>`        "pricingParam":"STDQ",`</br>`        "productTypeId":8,`</br>`        "productTypeName":"Application",`</br>`        "retiredCount":0,`</br>`        "totalCount":10`</br>`    },`</br>`    {`</br>`        "adamIdStr":"435160039",`</br>`        "assignedCount":2,`</br>`        "availableCount":8,`</br>`        "deviceAssignable":false,`</br>`        "isIrrevocable":true,`</br>`        "pricingParam":"PLUS",`</br>`        "productTypeId":10,`</br>`        "productTypeName":"Publication",`</br>`        "retiredCount":0,`</br>`        "totalCount":10`</br>`    }`</br>`]`|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`totalCount`|4|
|`errorMessage`|`"Result not found"`|
|`errorNumber`|`9604`|
|`location`|` {`</br> `"locationId": 22222222222,`</br> `"locationName": "Lincoln High School" `</br> `}`|
  

The `location` field is only returned when using a location token with an account that has migrated to VPP in Apple School Manager.  

  

### contentMetadataLookupUrl
  

The `contentMetadataLookupUrl` in the `VPPServiceConfigSrv` response allows an MDM server to query the iTunes Store for app and book metadata. When the VPP `sToken` is included in the request as a cookie, an MDM server can also get authenticated app metadata for B2B apps already owned by the VPP account, as well as apps that can still be redownloaded but can no longer be purchased.  

The URL query string tells the content metadata lookup service what app or book to look up. The VPP `sToken` must be included as a cookie named `itvt` to access the authenticated metadata.   

Content is filtered by platform. The valid platform values for the query parameter are: `itunes`, `ipad`, `iphone`, `atv`, `macappstore`, `macbookstore`, `enterprisestore`, and `volumepurchasestore`. For example, to get B2B app content, append `platform=enterprisestore` to your query string.  

Here is an example of the URL to look up an app: [https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=361309726&p=mdm-lockup&caller=MDM&platform=itunes&cc=us&l=en](https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=361309726&p=mdm-lockup&caller=MDM&platform=itunes&cc=us&l=en).  

Here is an example of what a response might look like:  

```
{
    "isAuthenticated": false,
    "results": {
        "361309726": {
            "artistId": "284417353",
            "artistName": "Apple",
            "artistUrl": "https://itunes.apple.com/us/artist/apple/id284417353?mt=8",
            "artwork": {
                "bgColor": "ffb800",
                "height": 1024,
                "supportsLayeredImage": false,
                "textColor1": "161616",
                "textColor2": "161616",
                "textColor3": "453712",
                "textColor4": "453712",
                "url": "http://is5.mzstatic.com/image/thumb/ Purple3/v4/72/7d/38/727d38ee-9245-eda6-1188-3458133bd99a/source/{w}x{h}bb.{f}",
                "width": 1024
            },
            "bundleId": "com.apple.Pages",
            "contentRatingsBySystem": {
                "appsApple": {
                    "name": "4+",
                    "rank": 1,
                    "value": 100
                }
            },
            "copyright": "\u00a9 2010 - 2015 Apple Inc.",
            "description": {
                "standard": "Pages is the most beautiful word processor you\u2019ve ever seen on a mobile device. This powerful word processor helps you create gorgeous reports, resumes, and documents in minutes. Pages has been designed exclusively for the iPad, iPhone, and iPod touch with support for Multi-Touch gestures and Smart Zoom.\n\nGet a quick start by using one of over 60 Apple-designed templates. Or use a blank document and easily add text, images, shapes, and more with a few taps. Then format using beautiful preset styles and fonts. And use advanced features like change tracking, comments, and highlights to easily review changes in a document.\n\nWith iCloud built in, your documents are kept up-to-date across all your devices. You can instantly share a document using just a link, giving others the latest version and the ability to edit it directly from www.icloud.com using a Mac or PC browser.\n\nPages 2.0 is updated with a stunning new design and improved performance. And with a new unified file format across Mac, iOS, and web, your documents are consistently beautiful everywhere you open them.\n\nGet started quickly\n\u2022 Choose from over 60 Apple-designed templates to instantly create beautiful reports, resumes, cards, and posters\n\u2022 Import and edit Microsoft Word and plain text files using Mail, a WebDAV service, or iTunes File Sharing\n\u2022 Quickly browse your document using the page navigator and see a thumbnail preview of each page\n\u2022 Turn on Coaching Tips for guided in-app help\n\nCreate beautiful documents\n\u2022 Write and edit documents using the onscreen keyboard or a wireless keyboard with Bluetooth\n\u2022 Format your document with gorgeous styles, fonts, and textures\n\u2022 Your most important text formatting options are right in your keyboard, and always just a tap or two away\n\u2022 Easily add images and video to your document using the Media Browser\n\u2022 Use auto-text wrap to flow text around images\n\u2022 Animate data with new interactive column, bar, scatter, and bubble charts\n\u2022 Organize your data easily in tables\n\nAdvanced writing tools\n\u2022 Turn on change tracking to mark up a document as you edit it\n\u2022 Use comments and highlights to share ideas and feedback with others\n\u2022 Create footnotes and endnotes and view word counts with character, paragraph, and page counts\n\u2022 Automatic list making and spellchecking \n\u2022 Create and view impressive 2D, 3D, and interactive bar, line, area, and pie charts\n\u2022 Use Undo to go back through your previous changes\n\niCloud\n\u2022 Turn on iCloud so your documents are automatically available on your Mac, iPad, iPhone, iPod touch, and iCloud.com\n\u2022 Access and edit your documents from a Mac or PC browser at www.icloud.com with Pages for iCloud beta\n\u2022 Pages automatically saves your documents as you make changes\n\nShare your work\n\u2022 Use AirDrop to send your document to anyone nearby\n\u2022 Quickly and easily share a link to your work via Mail, Messages, Twitter, or Facebook \n\u2022 Anyone with a shared document link always has access to the latest version of the document and can edit it with you at iCloud.com using Pages for iCloud beta\n\u2022 Export your document in ePub, Microsoft Word, and PDF format\n\u2022 Use \u201cOpen in Another App\u201d to copy documents to apps such as Dropbox\n\u2022 Print wirelessly with AirPrint, including page range selection, number of copies, and two-sided printing\n\nSome features may require Internet access; additional fees and terms may apply.\nPages does not include support for some Chinese, Japanese, or Korean (CJK) text input features such as vertical text.\nPages for iCloud beta is currently available in English only."
            },
            "deviceFamilies": [
                "iphone",
                "ipad",
                "ipod"
            ],
            "editorialArtwork": {
                "originalFlowcaseBrick": {
                    "bgColor": "ffb700",
                    "height": 600,
                    "supportsLayeredImage": false,
                    "textColor1": "161616",
                    "textColor2": "161616",
                    "textColor3": "453612",
                    "textColor4": "453612",
                    "url": "http://is4.mzstatic.com/image/ thumb/Features5/v4/22/60/94/226094a4-ed02-a234-7576-6de696ead0ba/source/{w}x{h}{c}.{f}",
                    "width": 3200
                }
            },
            "editorialBadgeInfo": {
                "editorialBadgeType": "staffPick",
                "nameForDisplay": "Essentials"
            },
            "genreNames": [
                "Productivity",
                "Business"
            ],
            "genres": [
                {
                    "mediaType": "8",
                    "name": "Productivity",
                    "url": "https://itunes.apple.com/us/genre/id6007"
                },
                {
                    "mediaType": "8",
                    "name": "Business",
                    "url": "https://itunes.apple.com/us/genre/id6000"
                }
            ],
            "id": "361309726",
            "kind": "iosSoftware",
            "latestVersionReleaseDate": "Sep 15, 2015",
            "name": "Pages",
            "nameRaw": "Pages",
            "offers": [
                {
                    "actionText": {
                        "downloaded": "Installed",
                        "downloading": "Installing",
                        "long": "Buy App",
                        "medium": "Buy",
                        "short": "Buy"
                    },
                    "assets": [
                        {
                            "flavor": "iosSoftware",
                            "size": 278782033
                        }
                    ],
                    "buyParams": "productType=C&price=9990&
                    salableAdamId=361309726&pricingParameters=STDQ&appExtVrsId=813292538",
                    "price": 9.99,
                    "priceFormatted": "$9.99",
                    "type": "buy",
                    "version": {
                        "display": "2.5.5",
                        "externalId": 813292538
                    }
                }
            ],
            "releaseDate": "2010-04-01",
            "shortUrl": "https://appsto.re/us/EysIv.i",
            "url": "https://itunes.apple.com/us/app/pages/id361309726?mt=8",
            "userRating": {
                "ratingCount": 24848,
                "ratingCountCurrentVersion": 236,
                "value": 3.5,
                "valueCurrentVersion": 3
            },
            "whatsNew": "This update contains stability improvements and bug fixes."
        }
    },
    "version": 2
}
```  

  

### retireVPPUserSrv
  

This service disassociates a VPP user from its iTunes account and releases the revocable licenses associated with the VPP user. Currently, ebook licenses are irrevocable. The revoked licenses can then be assigned to other users in the organization. A retired VPP user can be reregistered, in the same organization, by making a `registerVPPUserSrv` request.  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`userId`|One of these is required. `userId` takes precedence.|`100001`.|
|`clientUserIdStr`|`"810C9B91-DF83-41DA-80A1-408AD7F081A8"`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
  

If the user passes the `userId` value for an already-retired user, this request returns an error that indicates that the user has already been retired.  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`status`|`0` for success, `-1` for error.|
|`errorMessage`|`"Result not found"`.|
|`errorNumber`|`9604`.|
  

The `itsIdHash` field is omitted if the account is not yet associated with an iTunes Store account.  

  

### manageVPPLicensesByAdamIdSrv
  

This API supersedes the `associateVPPLicenseWithVPPUserSrv` and `disassociateVPPLicenseWithVPPUserSrv` APIs as a more flexible and efficient way of changing license assignments. It offers bulk license association and disassociation in one request, with some optional flags to control back end behavior.  


|Parameter Name|Required or Not|
|-|-|
|`adamIdStr`|Required.|
|`pricingParam`|Required.|
|`associateClientUserIdStrs`|One (and only one) of these is required to associate licenses.|
|`associateSerialNumbers`|
|`disassociateClientUserIdStrs`|One (and only one) of these is required to disassociate licenses.|
|`disassociateLicenseIdStrs`|
|`disassociateSerialNumbers`|
|`notifyDisassociation`|Not required.; defaults to `true`.|
|`sToken`|Required.|
|`facilitatorMemberId`|Not required.|
  


|Parameter Name|Example|
|-|-|
|`adamIdStr`|`"408709785"`|
|`pricingParam`|`"STDQ"`|
|`associateClientUserIdStrs`|`["810C9B91-...-408AD7F081A8", "d735c1cc-...-
c74571007ef6",...]`|
|`associateSerialNumbers`|`["C17DK6D9DDQW", "DLXL6044FPH8",...]`|
|`disassociateClientUserIdStrs`|`["810C9B91-...-408AD7F081A8", "d735c1cc-...-
c74571007ef6",...]`|
|`disassociateLicenseIdStrs`|`["2","3","4",...]`|
|`disassociateSerialNumbers`|`["C17DK6D9DDQW", "DLXL6044FPH8",...]`|
|`notifyDisassociation`|`false`|
|`sToken`|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
  

The request operates on a single asset (specified by the `{adamIdStr, pricingParam}` tuple) for multiple associations and disassociations in a single request. Licenses are disassociated from all users specified by the `disassociateClientUserIdStrs` array, the devices specified by the `disassociateSerialNumbers` array, or the licenses specified by the `disassociateLicenseIdStrs` array (which must only specify licenses assigned to the specified asset). At most one of these `disassociate*` arrays may be specified per request. Then licenses are associated either with the users specified by the `associateClientUserIdStrs` array or the devices specified by the `associateSerialNumbers` array. You must specify either zero or one `associate*` and zero or one `disassociate*` array per request. Specifying more than one of either `associate*` or `disassociate*` arrays result in undefined behavior.  

The maximum number of entries allowed in the `associate*` and `disassociate*` arrays are indicated by the `maxBatchAssociateLicenseCount` or `maxBatchDisassociateLicenseCount` fields added to the `VPPServiceConfigSrv` response. Any request that exceeds these limits is immediately rejected with an error.  

If `notifyDisassociation` is set to `false`, notifications regarding the disassociation of the license are not sent to devices.  


|Field Name|Example of Value|
|-|-|
|`status`|0 for success, -1 if the request failed completely, -3 if any licenses could not be changed as requested.|
|`adamIdStr`|`"408709785"`|
|`pricingParam`|`"STDQ"`|
|`productTypeId`|`7` (see [productTypeId Codes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW802))|
|`productTypeName`|`"Software"`|
|`isIrrevocable`|`false`|
|`associations`|`[{`</br>`  "clientUserIdStr":"810C9B91-...-408AD7F081A8",`</br>`  "licenseIdStr":"2"`</br>`},{`</br>`  "clientUserIdStr":"d735c1cc-...-c74571007ef6",`</br>`  "licenseIdStr":"3",`</br>`  "errorMessage":"License already assigned",`</br>`  "errorNumber": 9616`</br>`},{`</br>`  "serialNumber":"C17DK6D9DDQW",`</br>`  "licenseIdStr":"4"`</br>`},{`</br>`  "serialNumber":"DLXL6044FPH8",`</br>`  "errorMessage":"License not found",`</br>`  "errorNumber": 9610`</br>`}, ...]`|
|`disassociations`|`[{`</br>`  "clientUserIdStr":"810C9B91-...-408AD7F081A8"`</br>`},{`</br>`  "clientUserIdStr":"d735c1cc-...-c74571007ef6",`</br>`  "errorMessage":"Registered user not found",`</br>`  "errorNumber": 9609`</br>`},{`</br>`  "serialNumber":"C17DK6D9DDQW"`</br>`},{`</br>`  "serialNumber":"DLXL6044FPH8",`</br>`  "errorMessage":"License not associated",`</br>`  "errorNumber": 9619`</br>`}, ...]`|
  

  

#### License Counts
  

The following fields are added to the `VPPServiceConfigSrv` response to indicate the maximum number of entries allowed in the `associateClientUserIdStrs`, `associateSerialNumbers`, `disassociateClientUserIdStrs`, `disassociateSerialNumbers`, or `disassociateLicenseIdStrs` arrays:  


|Field Name|Example of Value|
|-|-|
|`maxBatchAssociateLicenseCount`|`20`|
|`maxBatchDisassociateLicenseCount`|`20`|
  

`VPPServiceConfigSrv` must be checked every 5 minutes to update the current `maxBatchAssociateLicenseCount` and `maxBatchDisassociateLicenseCount` values, which may decrease or increase without notice. Requests that exceed the current limits are rejected with the error code `9602 'Invalid Argument'`, and no work is done. If you receive this error code query `VPPServiceConfigSrv` to retrieve new `maxBatchAssociateLicenseCount` and `maxBatchDisassociateLicenseCount` values, correct the last request that was rejected and resend the request.  

  

### associateVPPLicenseSrv
  

> **Note:** This request is **deprecated**. Use [manageVPPLicensesByAdamIdSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW301) instead.   
  

  

### associateVPPLicenseWithVPPUserSrv
  

> **Note:** 
This request is **deprecated**. Use [manageVPPLicensesByAdamIdSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW301) instead.  
  

  

### disassociateVPPLicenseSrv
  

> **Note:** This request is **deprecated**. Use [manageVPPLicensesByAdamIdSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW301) instead.  
  

  

### disassociateVPPLicenseFromVPPUserSrv
  

> **Note:** 
This request is **deprecated**. Use [manageVPPLicensesByAdamIdSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW301) instead.  
  

  

### editVPPUserSrv
  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`userId`|One of these is required. `userId` takes precedence.|`20001`.|
|`clientUserIdStr`|`"810C9B91-DF83-41DA-80A1-408AD7F081A8"`.|
|`email`|Not required.|`"user1@someorg.com"`.|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`facilitatorMemberId`|Not required.|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
|`managedAppleIDStr`|Not required.|`"user1@someorg.com"`.|
  

The `email` field is updated only if the value is provided in the request.  

The `managedAppleIDStr` parameter is discussed in [Managed Apple IDs](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW501).  

The response contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|`0` for success, `-1` for error.|
|`user`|`{`</br>`    "userId":100014,`</br>`    "email":"test_reg_user14_edited@test.com",`</br>`    "status":"Registered",`</br>`    "inviteUrl":`</br>`"https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/wa\/`</br>`associateVPPUserWithITSAccount?inviteCode=`</br>`9e8d1ecc57924d9da13b42b4f772a066&mt=8",`</br>`    "inviteCode":"9e8d1ecc57924d9da13b42b4f772a066",`</br>`    "clientUserIdStr":"810C9B91-DF83-41DA-80A1-408AD7F081A8"`</br>`}`|
|`facilitatorMember`|`    {`</br>`        "appleId":"user1@someorg.com",`</br>`        "countryCode":"US",`</br>`        "email":"user1@someorg.com",`</br>`        "facilitatorMemberId":200843,`</br>`        "organizationId":2168850000179778,`</br>`    },`|
|`errorMessage`|`"Missing \"userId\" input parameter"`.|
|`errorNumber`|`9600`.|
  

  

### VPPClientConfigSrv
  

This service allows the client to store some information on the server on a per-organization basis. The information that currently can be stored is a `clientContext` string. The `clientContext` string is any JSON string less than 256 bytes in length. For format information, see [Service Response](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW21).  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`clientContext`|Not required.|(any string less than 256 bytes)|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
|`verbose`|Not required.|`"true"`.|
  

If a value is provided for `clientContext`, the value is stored by the server and the response contains the current value of this field. To clear the field value, provide an empty string as the input value; that is, `""`. If `"verbose":true"` is included in the request, the response contains the `appleId` field.  

The response to `VPPClientConfigSrv` contains some of these fields:  


|Field Name|Example of Value|
|-|-|
|`status`|`0` for success, `-1` for error.|
|`apnToken`|`OM3oPAbCdEiSC98erJn@F8a8jZGoS9PI=`|
|`clientContext`|`"abc"`|
|`errorMessage`|`"Login required"`.|
|`errorNumber`|`9601`.|
|`countryCode`|`"US"`.|
|`appleId`|`"user1@someorg.com"`.|
|`email`|`"user1@someorg.com"`.|
|`facilitatorMemberId`|`"200841"`.|
|`vppGroupMembers`|See [Program Facilitators](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW502).|
|`organizationId`|`2000000001630588`|
|`organizationIdHash`|`""0420773fb70e423ef77916dee3b381987e6c3fb4d8f19d1fd071b0c48c0cd380"`.|
|`uId`|`"200841"`.|
|`location`|` {`</br>`"locationId": 22222222222,`</br>`"locationName": "Lincoln High School" `</br>`}`|
  

The `countryCode` value in the response is the ISO 3166-1 two-letter code designating the country where the VPP account is located. For example, "US" for United States, "CA" for Canada, "JP" for Japan, and so on.  

The `location` field is only returned when using a location token with an account that has migrated to VPP in Apple School Manager.  

The `uId` field is the unique library identifier. When querying assets using multiple tokens that may share libraries, use the `uId` field to filter duplicates.  

  

### VPPServiceConfigSrv
  

This service returns the full list of web service URLs, the registration URL used in the user invitation email, and a list of error numbers that can be returned from the web services. No parameters or authentication is necessary.  

Clients should make a `VPPServiceConfigSrv` request to retrieve the list of service URLs at the appropriate moment (client restart) to ensure they are up-to-date, because the URLs may change under certain circumstances. The `VPPServiceConfigSrv` service exists to provide a level of indirection so that other service URLs can be changed in a way that is transparent to the clients.  

The request takes the following parameters:  


|Parameter Name|Required or Not|Example|
|-|-|-|
|`sToken`|Required.|`"h40Gte9aQnZFDNM...6ZQ="`.|
  

The response contains the URLs to be used to register VPP users and other web services.  


|Field Name|Example of Value|
|-|-|
|`invitationEmailUrl`|`"https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`associateVPPUserWithITSAccount?`</br>`inviteCode=%inviteCode%&mt=8"`</br>Your MDM server should replace `%inviteCode%` with the actual invitation code.|
|`registerUserSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`registerVPPUserSrv"`.|
|`editUserSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`editVPPUserSrv"`.|
|`getUserSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`getVPPUserSrv"`.|
|`retireUserSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`retireVPPUserSrv"`.|
|`getUsersSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`getVPPUsersSrv"`.|
|`getLicensesSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`getVPPLicensesSrv"`.|
|`getVPPAssetsSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`getVPPAssetsSrv”`.|
|`manageVPPLicensesByAdamIdSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`manageVPPLicensesByAdamIdSrv"`.|
|`associateLicenseSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`associateVPPLicenseWithVPPUserSrv"`.|
|`disassociateLicenseSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`disassociateVPPLicenseFromVPPUserSrv"`.|
|`errorCodes`|`
[
      {
         "errorMessage":"Missing required argument",
         "errorCode":9600
      },
      {
         "errorMessage":"Login required",
         "errorCode":9601
      },
      {
         "errorMessage":"Invalid argument",
         "errorCode":9602
      },
      {
         "errorMessage":"Internal error",
         "errorCode":9603
      },
      {
         "errorMessage":"Result not found",
         "errorCode":9604
      },
      {
         "errorMessage":"Account storefront incorrect",
         "errorCode":9605
      },
      {
         "errorMessage":"Error constructing token",
         "errorCode":9606
      },
      {
         "errorMessage":"License irrevocable",
         "errorCode":9607
      },
      {
         "errorMessage":"Empty SharedData response",
         "errorCode":9608
      },
      {
         "errorMessage":"User not found",
         "errorCode":9609
      },
      {
         "errorMessage":"Lincese not found",
         "errorCode":9610
      },
      {
         "errorMessage":"Admin user not found",
         "errorCode":9611
      },
      {
         "errorMessage":"Fail creating SAPFeeder job for claim",
         "errorCode":9612
      },
      {
         "errorMessage":"Fail creating SAPFeeder job for unclaim",
         "errorCode":9613
      },
      {
         "errorMessage":"Invalid date formate",
         "errorCode":9614
      },
      {
         "errorMessage":"orgCountry not found",
         "errorCode":9615
      },
      {
         "errorMessage":"License already assigned to the iTunes account",
         "errorCode":9616
      },
      {
         "errorMessage":"User already retired",
         "errorCode":9618
      },
      {
         "errorMessage":"License not associated",
         "errorCode":9619
      },
      {
         "errorMessage":"User already deleted",
         "errorCode":9620
      },
      {
         "errorMessage":"The token has expired. You need to generate a new token online using your organization's account at https:\/\/vpp.itunes.apple.com.",
         "errorCode":9621
      },
      {
         "errorMessage":"The authentication token is invalid.",
         "errorCode":9622
      },
      {
         "errorMessage":"The APN token is invalid.",
         "errorCode":9623
      }
      {
         "errorMessage":"License was refunded and is no longer valid.",
         "errorCode":9624
      }
      {
         "errorMessage":"The sToken has been revoked.",
         "errorCode":9625
      }
      {
         "errorMessage":"License already assigned to a different user.",
         "errorCode":9626
      }
   ]`|
|`clientConfigSrvUrl`|`"https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/`</br>`VPPClientConfigSrv"`.|
|`maxBatchAssociateLicenseCount`|`20`|
|`maxBatchDisassociateLicenseCount`|`20`|
  
  

## Examples
  

The following are examples of requests and responses of each service. The requests are made with the curl command from the command line. The response JSON are all formatted with beautifier to facilitate viewing. They were one string without line breaks when received from the web services.  

WIth the introduction of location based libraries, the API responses may differ depending on whether the request was made with a new location-based token or the legacy user-based token. Where responses differ, examples of both are provided.  

  

### Request to VPPServiceConfigSrv
  

The curl command:  

```
curl https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv
```  

 The response:  

```
{
    "associateLicenseSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/associateVPPLicenseSrv",
    "clientConfigSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/VPPClientConfigSrv",
    "contentMetadataLookupUrl":"https://uclient-api.itunes.apple.com/ WebObjects/MZStorePlatform.woa/wa/lookup",
    "disassociateLicenseSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/disassociateVPPLicenseSrv",
    "editUserSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/editVPPUserSrv",
    "errorCodes":[
        {
            "errorMessage":"Missing required argument",
            "errorNumber":9600
        },
        {
            "errorMessage":"Login required",
            "errorNumber":9601
        },
        {
            "errorMessage":"Invalid argument",
            "errorNumber":9602
        },
        {
            "errorMessage":"Internal error",
            "errorNumber":9603
        },
        {
            "errorMessage":"Result not found",
            "errorNumber":9604
        },
        {
            "errorMessage":"Account storefront incorrect",
            "errorNumber":9605
        },
        {
            "errorMessage":"Error constructing token",
            "errorNumber":9606
        },
        {
            "errorMessage":"License is irrevocable",
            "errorNumber":9607
        },
        {
            "errorMessage":"Empty response from SharedData service",
            "errorNumber":9608
        },
        {
            "errorMessage":"Registered user not found",
            "errorNumber":9609
        },
        {
            "errorMessage":"License not found",
            "errorNumber":9610
        },
        {
            "errorMessage":"Admin user not found",
            "errorNumber":9611
        },
        {
            "errorMessage":"Failed to create claim job",
            "errorNumber":9612
        },
        {
            "errorMessage":"Failed to create unclaim job",
            "errorNumber":9613
        },
        {
            "errorMessage":"Invalid date format",
            "errorNumber":9614
        },
        {
            "errorMessage":"OrgCountry not found",
            "errorNumber":9615
        },
        {
            "errorMessage":"License already assigned",
            "errorNumber":9616
        },
        {
            "errorMessage":"The user has already been retired.",
            "errorNumber":9618
        },
        {
            "errorMessage":"License not associated",
            "errorNumber":9619
        },
        {
            "errorMessage":"The user has already been deleted.",
            "errorNumber":9620
        },
        {
            "errorMessage":"The token has expired. You need to generate a new token online using your organization's account at https://vpp.itunes.apple.com.",
            "errorNumber":9621
        },
        {
            "errorMessage":"Invalid authentication token",
            "errorNumber":9622
        },
        {
            "errorMessage":"Invalid APN token",
            "errorNumber":9623
        },
        {
            "errorMessage":"License was refunded and is no longer valid.",
            "errorNumber":9624
        },
        {
            "errorMessage":"The sToken has been revoked",
            "errorNumber":9625
        },
        {
            "errorMessage":"License already assigned to other user",
            "errorNumber":9626
        },
        {
            "errorMessage":"License disassociation fail due to frequent reassociation",
            "errorNumber":9627
        },
        {
            "errorMessage":"License not eligible for device assignment.",
            "errorNumber":9628
        },
        {
            "errorMessage":"The sToken is inapplicable to batchToken",
            "errorNumber":9629
        },
        {
            "errorMessage":"Too many recent identical calls were made to assign a license that failed due to license being already assigned to the user or device",
            "errorNumber":9630
        },
        {
            "errorMessage":"Too many recent identical calls were made to assign a license that failed due to no license being being available.",
            "errorNumber":9631
        },
        {
            "errorMessage":"Too many recent calls to manage licenses with identical requests",
            "errorNumber":9632
        },
        {
            "errorMessage":"No batch data recovered for token.",
            "errorNumber":9633
        },
        {
            "errorMessage":"Service removed.",
            "errorNumber":9634
        },
        {
            "errorMessage":"Apple ID can't be associated with registered user.",
            "errorNumber":9635
        },
        {
            "errorMessage":"No registered user found.",
            "errorNumber":9636
        },
        {
            "errorMessage":"Facilitator operation not allowed.",
            "errorNumber":9637
        },
        {
            "errorMessage":"Facilitator missing Organization ID.",
            "errorNumber":9638
        },
        {
            "errorMessage":"Facilitator group member not found.",
            "errorNumber":9639
        },
        {
            "errorMessage":"Facilitator group member look-up failed.",
            "errorNumber":9640
        },
        {
            "errorMessage":"Apple ID already associated to registered user.",
            "errorNumber":9641
        },
        {
            "errorMessage":"Apple ID passed cannot be used at this time because it's a VPP manager and the iTunes Store account not yet created and such creation requires user to agree to Terms.",
            "errorNumber":9642
        },
        {
            "errorMessage":"Volume Purchase Program is currently in maintenance mode. Please try again later.",
            "errorNumber":9644
        }
    ],
    "getLicensesSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPLicensesSrv",
    "getUserSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPUserSrv",
    "getUsersSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPUsersSrv",
    "getVPPAssetsSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPAssetsSrv",
    "invitationEmailUrl":"https://buy.itunes.apple.com/ WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&inviteCode=%25inviteCode%25&mt=8",
    "manageVPPLicensesByAdamIdSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/manageVPPLicensesByAdamIdSrv",
    "maxBatchAssociateLicenseCount":100,
    "maxBatchDisassociateLicenseCount":100,
    "registerUserSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/registerVPPUserSrv",
    "retireUserSrvUrl":"https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/retireVPPUserSrv",
    "status":0,
    "vppWebsiteUrl":"https://vpp.itunes.apple.com/"
}
```  

  

### Request to getVPPLicensesSrv
  

Content of the get_licenses.json file used in the curl command next:  

```
{"sToken":"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2
a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="}
```  

The curl command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPLicensesSrv -d @get_licenses.json
```  

The response:  

```
[
    {
        "adamId":408709785,
        "adamIdStr":"408709785",
        "clientUserIdStr":"9a17b450-9820-471e-b232-13a479ddede0",
        "isIrrevocable":false,
        "itsIdHash":"LsrJ6NhzbsOzQXShrpUTWGnD/X8=",
        "licenseId":102547,
        "licenseIdStr":"102547",
        "pricingParam":"STDQ",
        "productTypeId":8,
        "productTypeName":"Application",
        "status":"Associated",
        "userId":10715446,
        "userIdStr":"10715446"
    },
    {
        "adamId":435160039,
        "adamIdStr":"435160039",
        "clientUserIdStr":"9a17b450-9820-471e-b232-13a479ddede0",
        "isIrrevocable":true,
        "itsIdHash":"LsrJ6NhzbsOzQXShrpUTWGnD/X8=",
        "licenseId":795047681,
        "licenseIdStr":"795047681",
        "pricingParam":"PLUS",
        "productTypeId":10,
        "productTypeName":"Publication",
        "status":"Associated",
        "userId":6561022,
        "userIdStr":"6561022"
    },
    {
        "adamId":645859810,
        "adamIdStr":"645859810",
        "isIrrevocable":false,
        "licenseId":967494668,
        "licenseIdStr":"967494668",
        "pricingParam":"STDQ",
        "productTypeId":8,
        "productTypeName":"Application",
        "serialNumber":"C39N3035G68P",
        "status":"Associated"
    }
]
```  

  

### Request to getVPPUsersSrv
  

Content of the get_users.json file used in the curl command next:  

```
{"sToken":"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2
a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="}
```  

The curl command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPUsersSrv -d @get_users.json
```  

The response:  

```
{
   "users":[
      {
         "userId":1,
         "email":"user1@test.com",
         "clientUserIdStr":"200006",
         "status":"Associated"
         "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
      },
      {
         "userId":2,
         "email":"user2@test.com",
         "clientUserIdStr":"200007",
         "status":"Associated"
         "itsIdHash":"*leSKk3IaE2vk2KLmv2k3/200D3="
      },
      {
         "userId":3,
         "email":"user3@test.com",
         "clientUserIdStr":"user3@test.com",
         "status":"Registered",
         "inviteCode":"f551b37da07146628e8dcbe0111f0364"
         "inviteUrl":"https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/wa\/
             associateVPPUserWithITSAccount?inviteCode=
             f551b37da07146628e8dcbe0111f0364&mt=8",
      },
      {
         "userId":4,
         "email":"user4@test.com",
         "clientUserIdStr":"user4@test.com",
         "status":"Registered",
         "inviteUrl":"https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/wa\/
             associateVPPUserWithITSAccount?inviteCode=
             859c5aa3485a48918a5f4f70c5629ec8&mt=8",
         "inviteCode":"859c5aa3485a48918a5f4f70c5629ec8"
      }
   ],
   "status":0,
   "totalCount":4
}
```  

  

### Request to getVPPUserSrv
  

Content of the get_user.json file used in the curl command next:  

```
{"userId": 1, "sToken":"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQ
keeb3h2a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="}
```  

The curl command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPUserSrv -d @get_user.json
```  

The response:  

```
{
   "status":0,
   "user":{
      "userId":1,
      "email":"user1@test.com",
      "clientUserIdStr":"200006",
      "status":"Associated",
      "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
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
}
```  

  

### Request to registerVPPUserSrv
  

Content of the reg_user.json file used in the curl command next:  

```
{"email": "test_reg_user11@test.com", "clientUserIdStr": "200002", sToken":
"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+
WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=" }
```  

The curl command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/registerVPPUserSrv -d @reg_user.json
```  

The response:  

```
{
   "status":0,
   "user":{
      "userId":100014,
      "email":"test_reg_user11@test.com",
      "status":"Registered",
      "inviteUrl": "https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/
          wa\/associateVPPUserWithITSAccount?inviteCode=
          89e8d1ecc57924d9da13b42b4f772a066&mt=8",
      "inviteCode":"9e8d1ecc57924d9da13b42b4f772a066",
      "clientUserIdStr":"200002"
   }
}
```  

  

### Request to editVPPUserSrv
  

Content of the edit_user.json file:  

```
{"userId": 100014, "email": "test_reg_user15_edited@test.com", "sToken":
"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+
WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=" }
```  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/editVPPUserSrv -d @edit_user.json
```  

The response:  

```
{
   "status":0,
   "user":{
      "userId":100014,
      "email":"test_reg_user15_edited@test.com",
      "status":"Registered",
      "inviteUrl": "https:\/\/buy.itunes.apple.com\/WebObjects\/MZFinance.woa\/
          wa\/associateVPPUserWithITSAccount?inviteCode=
          9e8d1ecc57924d9da13b42b4f772a066&mt=8",
 
      "inviteCode":"9e8d1ecc57924d9da13b42b4f772a066",
      "clientUserIdStr":"200015",
      "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
   }
}
```  

  

### Request to retireVPPUserSrv
  

Content of the retire_user.json file:  

```
{"userId": 1, "sToken":
"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+
WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=" }
```  

The command:  

```
 
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/retireVPPUserSrv -d @retire_user.json
```  

The response:  

```
{
   "status":0,
   "user":{
      "userId":1,
      "email":"user1@test.com",
      "clientUserIdStr":"200006",
      "status":"Retired",
      "licenses":[
          {
              "licenseId":2,
              "adamId":408709785,
              "productTypeId":10,
              "pricingParam":"STDQ",
              "productTypeName":"Publication",
              "isIrrevocable":true
          }
      ]
   }
}
```  

  

### Request to getVPPAssetsSrv
  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/getVPPAssetsSrv -d @get_assets.json
```  

The response using a location token:  

```
{
   "assets": [
       {
           "adamIdStr": "748057890",
           "assignedCount": 0,
           "availableCount": 25,
           "deviceAssignable": true,
           "isIrrevocable": false,
           "pricingParam": "STDQ",
           "productTypeId": 8,
           "productTypeName": "Application",
           "retiredCount": 0,
           "totalCount": 25
       },
       {
           "adamIdStr": "635851129",
           "assignedCount": 0,
           "availableCount": 40,
           "deviceAssignable": true,
           "isIrrevocable": false,
           "pricingParam": "STDQ",
           "productTypeId": 8,
           "productTypeName": "Application",
           "retiredCount": 0,
           "totalCount": 40
       },
       {
           "adamIdStr": "284035177",
           "assignedCount": 0,
           "availableCount": 0,
           "deviceAssignable": false,
           "isIrrevocable": false,
           "pricingParam": "STDQ",
           "productTypeId": 8,
           "productTypeName": "Application",
           "retiredCount": 10,
           "totalCount": 0
       }
   ],
   "location": {
       "locationId": 22222222222,
       "locationName": “LocationName”
   },
   "status": 0,
   "totalCount": 3,
   "uId": "103614"
}
```  

The response using a legacy token (migrated or non-migrated to VPP in ASM account):  

```
{
   "assets": [
       {
           "adamIdStr": "748057890",
           "assignedCount": 0,
           "availableCount": 10,
           "deviceAssignable": true,
           "isIrrevocable": false,
           "pricingParam": "STDQ",
           "productTypeId": 8,
           "productTypeName": "Application",
           "retiredCount": 0,
           "totalCount": 10
       }
   ],
   "status": 0,
   "totalCount": 1,
   "uId": "103299"
}
```  

  

### Request to VPPClientConfigSrv 
  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/VPPClientConfigSrv -d @client_config.json
```  

The response using a location token:  

```
{
   "appleId": “testuser1@test.org”,
   "countryCode": "US",
   "email": "testuser1@test.org",
   "location": {
       "locationId": 22222222222,
       "locationName": “LocationName”
   },
   "organizationId": 2000000001630588,
   "organizationIdHash": "0420773fb70e423ef77916dee3b381987e6c3fb4d8f19d1fd071b0c48c0cd380",
   "status": 0,
   "uId": "103614"
}
```  

The response using a legacy token for an account which has not been migrated to VPP in ASM:  

```
{
   "apnToken": "4IbRbXpge3ySkchugcf",
   "appleId": “test1@test.org”,
   "clientContext": "{\"guid\":\"b92\",\"hostname\”:\”test.test.org\”,\”ac2\":1}",
   "countryCode": "US",
   "email": “test1@test.org”,
   "facilitatorMemberId": 123456,
   "libraryId": 123456,
   "organizationId": 2222222222,
   “organizationIdHash”:”2555009cd3e53bd69b50723d2baec9f49558cbd90de2a1aa420dacdbff12cc8e",
   "status": 0,
   "uId": “123456”
}
```  

The response using a legacy token for an account which has been migrated to VPP in ASM:  

```
{
   "appleId": “test2@test.org”,
   "countryCode": "US",
   "email": "test2@test.org",
   "facilitatorMemberId": 11111,
   "libraries": [
       {
           "appleId": “test3@test3.org”,
           "email": "test3@test3.org",
           "libraryId": 11112,
           "location": {
               "locationId": 2222221,
               "locationName": “Elementary School”
           }
       },
       {
           "appleId": “test4@test.org”,
           "email": "test4@test.org",
           "libraryId": 11113,
           "location": {
               "locationId": 2222221,
               "locationName": “Elementary School”
           }
       },
       {
           "appleId": “test2@test.org”,
           "email": "test2@test.org",
           "libraryId": 11111,
           "location": {
               "locationId": 2222221,
               "locationName": “Elementary School”
           }
       },
       {
           "appleId": “test2@test.org”,
           "email": "test2@test.org",
           "libraryId": 11114,
           "location": {
               "locationId": 2222222,
               "locationName": “Middle School”
           }
       },
     "libraryId": 11111,
     "organizationId": 200000000,
     "organizationIdHash": "7a002fe8b88fc00738c4d74382b94a1e464b65",
     "status": 0,
     "uId": "11111”,
     "vppGroupMembers": [
       {
           "appleId": "test3@test3.org",
           "email": "test3@test3.org",
           "facilitatorMemberId": 11112,
           "locationId": 2222221,
           "locationName": “Elementary School“,
           "organizationId": 200000000
       },
       {
           "appleId": "test4@test.org",
           "email": "test4@test.org",
           "facilitatorMemberId": 11113,
           "locationId": 2222221,
           "locationName": "Elementary School",
           "organizationId": 200000000
       },
       {
           "appleId": "test2@test.org",
           "email": "test2@test.org",
           "facilitatorMemberId": 11111,
           "locationId": 2222221,
           "locationName": "Elementary School",
           "organizationId": 200000000
       },
       {
           "appleId": "test2@test.org",
           "email": "test2@test.org",
           "facilitatorMemberId": 11114,
           "locationId": 2222222,
           "locationName": “Middle School“,
           "organizationId": 200000000
       }
    ]
}
```  

  

### Request to manageVPPLicensesByAdamIdSrv
  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/manageVPPLicensesByAdamIdSrv -d @manage.json
```  

The response using `associateClientUserIdStrs`:  

```
{
   "associations": [
      {
         "adamId": 869183446,
         "clientUserIdStr": "userIdStr",
         "isIrrevocable": false,
         "licenseId": 840998,
         "pricingParam": "STDQ",
         "productTypeId": 8,
         "productTypeName": "Application",
         "status": "Associated",
         "userId": 204701
      }
   ],
   "status": 0,
   “uId”:”111123”
}
```  

The response using `associateSerialNumbers`:  

```
{
   "associations": [
      {
         "adamId": 869183446,
         "isIrrevocable": false,
         "licenseId": 840999,
         "pricingParam": "STDQ",
         "productTypeId": 8,
         "productTypeName": "Application",
         "serialNumber": "MERD1",
         "status": "Associated"
      },
      {
         "adamId": 869183446,
         "isIrrevocable": false,
         "licenseId": 841000,
         "pricingParam": "STDQ",
         "productTypeId": 8,
         "productTypeName": "Application",
         "serialNumber": "MERD2",
         "status": "Associated"
      }
   ],
   "status": 0,
   “uId”:”11234”
}
 
```  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/ManagedAppsUpdates/ManagedAppsUpdates.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html)

  



