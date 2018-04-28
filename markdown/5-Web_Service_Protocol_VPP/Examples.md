# Examples

 [Configuration Profile Reference - Examples](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW24)  
  

## Examples
  

The following are examples of requests and responses of each service. The requests are made with the curl command from the command line. The response JSON are all formatted with beautifier to facilitate viewing. They were one string without line breaks when received from the web services.  

  

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

  

### Request to associateVPPLicenseWithVPPUserSrv
  

Content of the associate_license.json file:  

```
{"userId": 2, "licenseId": 4, "sToken":
"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+
WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=" }
```  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/associateVPPLicenseWithVPPUserSrv -d @associate_license.json
```  

The response:  

```
{
   "status":0,
   "license":{
       "licenseId":4,
       "adamId":497799835,
       "productTypeId":7,
       "pricingParam":"STDQ",
       "productTypeName":"Software",
       "isIrrevocable":false,
       "userId": 2,
       "clientUserIdStr":"200007",
       "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
   },
   "user":{
       "userId":2,
       "email":"user2@test.com",
       "clientUserIdStr":"200007",
       "status":"Associated",
       "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
   }
}
```  

  

### Request to disassociateVPPLicenseFromVPPUserSrv
  

Content of the `disassociate_license.json` file:  

```
{"userId": 2, "licenseId": 4, "sToken":
"h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+
WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=" }
```  

The command:  

```
curl https://vpp.itunes.apple.com/ WebObjects/MZFinance.woa/wa/disassociateVPPLicenseFromVPPUserSrv -d
@disassociate_license.json
```  

The response:  

```
{
   "status":0,
   "license":{
      "licenseId":4,
      "adamId":497799835,
      "productTypeId":7,
      "pricingParam":"STDQ",
      "isIrrevocable":false,
      "productTypeName":"Software",
   },
   "user":{
      "userId":2,
      "email":"user2@test.com",
      "clientUserIdStr":"user2@test.com",
      "itsIdHash":"C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
      "status":"Associated",
      "inviteCode":"a5ea54beb2954d4dadc65cf19cee5e58",
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