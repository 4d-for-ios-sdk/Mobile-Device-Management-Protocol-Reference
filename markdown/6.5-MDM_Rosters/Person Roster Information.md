# Person Roster Information

 [Configuration Profile Reference - Person Roster Information](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW11)  
  

## Person Roster Information
  

This API returns roster information for an organization. Besides instructors and students, this list may contain additional people who do not belong to any class.  

  

### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/class/person`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request. This is used for pagination. On the initial request, this should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/class/person HTTP/1.1
User-Agent:<client-software-information>
Accept-Encoding: gzip, deflate
X-Server-Protocol-Version:2
X-ADM-Auth-Session: 87a235815b8d6661ac73329f75815b8d6661ac73329f815
Content-Type: application/json;charset=UTF8
Content-Length: <Content-Length>
{
"limit": 1000,
"cursor": "1ac73329f75817"
}
```  

  

### Responses
  

In response, the MDM service returns a JSON dictionary with following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that should be used for the next request to paginate. This field data type has a maximum length of 512 UTF-8 characters. |
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of persons. If true, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`persons`|Array of dictionaries|Provides information about persons, both teachers and students, sorted in lexical order by a person source_system_identifier. The organization must provide this identifier to Apple.|
  

Each `persons` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`first_name`|String|Person’s first name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`middle_name`|String|Optional. Person’s middle name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`last_name`|String|Person’s last name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`name`|String|Person’s name. Maximum length 1024 UTF-8 characters.|
|`managed_apple_id`|String|Managed Apple ID for the person. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the person. Maximum length 256 UTF-8 characters.|
|`passcode_type`|String|The password policy of the person. Possible values are “complex”, “four”, or “six”. Available in protocol version 3 and above.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," "SYSTEM," and “MANUAL.” Maximum length is 64 UTF-8 characters.|
|`source_system_identifier`|String|Identifier configured by organization for the person. Maximum length 256 UTF-8 characters.|
|`grade`|String|Optional; not used for instructors. Student grade information. Maximum length 256 UTF-8 characters. Value can be null.|
|`status`|String|Indicates the status of the person. Possible values are `Active` and `InActive`. **Availability: **Available in X-Protocol Version 3 and later.|
|`person_id`|String|Optional. Indicates the `personid` of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 4 and later.|
|`sis_username`|String|Optional. Indicates the SIS usernname of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 5 and later.|
|`email_address`|String|Optional. Indicates the email address of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 5 and later.|
  

The response contains a list of persons. The `more_to_follow` Boolean indicates if more information about persons remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of persons.  

The person list could be huge. If modifications are performed while the response is being returned, it will not return any persons enrolled after it started responding. If any updates are applied on any of the entities or attributes, you must send the request again to get the latest snapshot of personnel.  

One record in a typical response might look like this:  

```
HTTP/1.1 200 OK
Date: Mon,12 Oct 2015 02:25:30 GMT
Content-Type: application/json;charset=UTF8
X-ADM-Auth-Session: 87a235815b8d6661ac73329f75815b8d6661ac73329f815
Content-Length: ...
Connection: Keep-Alive
 
{
  "persons": [
    {
      "unique_identifier": "UNIINSTID1003",
      "source": "CSV",
      "source_system_identifier": "INSTID1003",
      "name": "Miss Will Smith",
      "managed_apple_id": "smith@example.com"
      "first_name": "Miss",
      "middle_name": "Will",
      "last_name": "Smith",
      "passcode_type": "complex",
      "person_id": "6378376667",
      "status": "Active"
    },
    {
      "unique_identifier": "UNISTUDID1003",
      "source": "SIS",
      "source_system_identifier": "INSTSTUDID1003",
      "name": "John Smith",
      "managed_apple_id": "john@example.com",
      "grade": "K"
      "first_name": "John",
      "last_name": "Smith",
      "passcode_type": "four",
      "person_id": "4909090667",
      "status": "Active"
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
}
```  

  

### Person Roster Sync Service
  

This sync service uses a cursor returned by the full person roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, up to 7 days.  

This service may return the same person more than once. You can identify duplicates by matching their `unique_identifier` values.  

  

#### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/class/person/sync`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request, used for pagination. This position should not be older than 7 days. On the initial request, it should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/class/person/sync HTTP/1.1
User-Agent:<client-software-information>
Accept-Encoding: gzip, deflate
X-Server-Protocol-Version:2
X-ADM-Auth-Session: 87a235815b8d6661ac73329f75815b8d6661ac73329f815
Content-Type: application/json;charset=UTF8
Content-Length: <Content-Length>
Host: <vip-name>
Cookie: ...
{
"limit": 1000,
"cursor": "1ac73329f75817"
}
```  

Only content of type `application/json` in UTF-8 charset will be accepted by the server.  

  

#### Responses
  

In response, the MDM service returns a JSON dictionary with following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that should be used for the next request to paginate. This field data type has a maximum length of 512 UTF-8 characters. |
|`fetched_until`|String|A time and date stamp in ISO 8601 format specifying the latest date of data being fetched.|
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of persons. If `true`, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`persons`|Array of dictionaries|Provides information about persons, both teachers and students, sorted in lexical order by a person source_system_identifier. The organization must provide this identifier to Apple.|
  

Each `persons` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Person’s name. Maximum length 1024 UTF-8 characters.|
|`managed_apple_id`|String|Managed Apple ID for the person. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the person. Maximum length 256 UTF-8 characters.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," "SYSTEM," and “MANUAL.” Maximum length is 64 UTF-8 characters.|
|`source_system_identifier`|String|Identifier configured by organization for the person. Maximum length 256 UTF-8 characters.|
|`grade`|String|Optional; not used for instructors. Student grade information. Maximum length 256 UTF-8 characters. Value can be null. This field is omitted for instructors.|
|`first_name`|String|Person’s first name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`middle_name`|String|Optional. Person’s middle name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`last_name`|String|Person’s last name. Maximum length 1024 UTF-8 characters. Available in protocol version 3 and above.|
|`passcode_type`|String|The password policy of the person. Possible values are “complex”, “four”, or “six”. Available in protocol version 3 and above.|
|`status`|String|Indicates the status of the person. Possible values are `Active` and `InActive`. **Availability: **Available in X-Protocol Version 3 and later.|
|`person_id`|String|Optional. Indicates the `personid` of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 4 and later.|
|`sis_username`|String|Optional. Indicates the SIS usernname of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 5 and later.|
|`email_address`|String|Optional. Indicates the email address of the person as displayed in ASM. **Availability: **Available in X-Protocol Version 5 and later.|
  

One record in a typical successful Person Roster Sync Service response might look like this:  

```
{
  "persons": [
    {
      "unique_identifier": "UNIINSTID1003",
      "source": "CSV",
      "source_system_identifier": "INSTID1003",
      "name": "Miss Will Smith",
      "managed_apple_id": "smith@example.com"
      "first_name": "Miss",
      "middle_name": "Will",
      "last_name": "Smith",
      "passcode_type": "complex",
      "person_id": "627626672",
      "status": "Active"
    },
    {
      "unique_identifier": "UNISTUDID1003",
      "source": "SIS",
      "source_system_identifier": "INSTSTUDID1003",
      "name": "John Smith",
      "managed_apple_id": "john@example.com",
      "grade": "K"
      "first_name": "John",
      "last_name": "Smith",
      "passcode_type": "four",
      "person_id": "7873878737",
      "status": "Active"
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
  "fetched_until": "2016-05-09T02:30:00Z"
}
```  

Note these features and cautions:  


* The response contains a list of persons. 

* The `more_to_follow` Boolean indicates if more information remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of persons. 

* The server will issue a cursor in all responses. If the cursor is sent in the next request, the server will return next set of records in chronological order and issue a new cursor. 

* Data changes will be delayed by a few minutes. 

* This service does not return deleted data. The client is expected to do a full sync and compare once every few days to identify deletes. 

* For a discussion of potential problems with using the Person Roster Sync Service, see [Error Responses](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW40). 
