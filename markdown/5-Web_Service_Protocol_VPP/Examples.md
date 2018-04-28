# Examples

 [Configuration Profile Reference - Examples](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW24)  
  

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