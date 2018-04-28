# The Services

 [Configuration Profile Reference - The Services](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW3)  
  

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
