# Class Roster Information

 [Configuration Profile Reference - Class Roster Information](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW3)  
  

## Class Roster Information
  

This API returns class roster information for an organization at a given location.  

  

### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/class`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request. This is used for pagination. On the initial request, this should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/class HTTP/1.1
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
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of classes. If true, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`classes`|Array of dictionaries|Provides information about classes, sorted in lexical order by a class source_system_identifier. The organization must provide this identifier to Apple.|
  

Each dictionary in the `classes` array contains these keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Class name. Maximum length is 1024 UTF-8 characters.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," and “MANUAL.” Maximum length is 64 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the class. Maximum length is 256 UTF-8 characters.|
|`source_system_identifier`|String|Optional. Identifier configured by the organization for its classes. Maximum length is 256 UTF-8 characters. See Note below.|
|`room`|String|Optional. Room where class is held. Maximum length is 512 UTF-8 characters.|
|`location`|Dictionary|Geographical or organizational location where class is held (see below).|
|`course`|Dictionary|Course definition for the class (see below).|
|`instructor_unique_identifiers`|Array of strings|Unique identification for instructors. Each string in the array has a maximum length of 256 UTF-8 characters.|
|`student_unique_identifiers`|Array of strings|Unique identification for students. Each string in the array has a maximum length of 256 UTF-8 characters.|
|`class_number`|String|Optional. Indicates the class number. Maximum string length is 256 UTF-8 characters. **Availability: **Available in X-Protocol Version 4 and later.|
  

> **Note:** 
The value of `source_system_identifier` in this and other roster API responses is not guaranteed to be unique and can potentially change.  
  

The `location` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Location name. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the location. Maximum length 256 UTF-8 characters.|
  

The `course` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Course name. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the course. Maximum length 256 UTF-8 characters.|
  

The response contains a list of classes. Each class record contains the location where the class is held and the instructors and students that are registered for that class. It also identifies the course with which the class is associated. The `more_to_follow` Boolean indicates if more class information remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of classes.  

The class list could be huge. If modifications are performed while the response is being returned, it will not return any classes created after it started responding. If any updates are applied on any of the entities or attributes, you must send the request again to get the latest snapshot of classes.  

One record in a typical response might look like this:  

```
{
  "classes": [
    {
      "unique_identifier": "UNICLS1003",
      "source": "SIS",
      "source_system_identifier": "CLSBIO101",
      "name": "Miss Smith's Biology 101",
      "class_number": "1A",
      "room": "Hall 101",
      "location": {
        "unique_identifier": "UNILOC1003",
        "name": "Biology department"
      },
      "instructor_unique_identifiers": [
        "UNIINSTID1003",
        "UNIINSTID1003"
      ],
      "student_unique_identifiers": [
        "UNISTUDID1003",
        "UNISTUDID1004"
      ],
      "course": {
        "unique_identifier": "UNICOURID1003",
        "name": "Biology 101"
      }
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
}
```  

  

### Class Roster Sync Service
  

This sync service uses a cursor returned by the full class roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, up to 7 days.  

This service may return the same class more than once. You can identify duplicates by matching their `unique_identifier` values.  

  

#### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/class/sync`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request, used for pagination. This position should not be older than 7 days. On the initial request, it should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/class/sync HTTP/1.1
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
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of classes. If `true`, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`fetched_until`|String|A time and date stamp in ISO 8601 format specifying the latest date of data being fetched.|
|`classes`|Array of dictionaries|Provides information about classes, sorted in lexical order by a class `source_system_identifier`. The organization must provide this identifier to Apple.|
  

Each dictionary in the `classes` array contains these keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Class name. Maximum length is 1024 UTF-8 characters.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," and “MANUAL.” Maximum length is 64 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the class. Maximum length is 256 UTF-8 characters.|
|`source_system_identifier`|String|Optional. Identifier configured by the organization for its classes, with a maximum length of 256 UTF-8 characters. Its value is not guaranteed to be unique and can potentially change.|
|`room`|String|Optional. Room where class is held. Maximum length is 512 UTF-8 characters.|
|`location`|Dictionary|Geographical or organizational location where class is held (see below).|
|`course`|Dictionary|Course definition for the class (see below).|
|`instructor_unique_identifiers`|Array of strings|Unique identification for instructors. Each string in the array has a maximum length of 256 UTF-8 characters.|
|`student_unique_identifiers`|Array of strings|Unique identification for students. Each string in the array has a maximum length of 256 UTF-8 characters.|
|`class_number`|String|Optional. Indicates the class number. Maximum string length is 256 UTF-8 characters. **Availability: **Available in X-Protocol Version 4 and later.|
  

The `location` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Location name. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the location. Maximum length 256 UTF-8 characters.|
  

The `course` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Course name. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the course. Maximum length 256 UTF-8 characters.|
  

One record in a typical successful Class Roster Sync Service response might look like this:  

```
{
  "classes": [
    {
      "unique_identifier": "UNICLS1003",
      "source": "SIS",
      "source_system_identifier": "CLSBIO101",
      "name": "Miss Smith's Biology 101",
      "room": "Hall 101",
      "class_number": "1A",
      "location": {
        "unique_identifier": "UNILOC1003",
        "name": "Biology department"
      },
      "instructor_unique_identifiers": [
        "UNIINSTID1003",
        "UNIINSTID1003"
      ],
      "student_unique_identifiers": [
        "UNISTUDID1003",
        "UNISTUDID1004"
      ],
      "course": {
        "unique_identifier": "UNICOURID1003",
        "name": "Biology 101"
      }
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
  "fetched_until": "2016-05-09T02:30:00Z"
}
```  

Note these features and cautions:  


* The response contains a list of classes. Each class record contains the location where the class is held and the instructors and students that are registered for that class. It also identifies the course with which the class is associated. 

* The `more_to_follow` Boolean indicates if more class information remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of classes. 

* The server will issue a cursor in all responses. If the cursor is sent in the next request, the server will return next set of records in chronological order and issue a new cursor. 

* Data changes will be recognized up to the `fetched_until` time, which may be a few minutes behind real time. 

* This service does not return deleted data. The client is expected to do a full sync and compare once every few days to identify deletes. 

* For a discussion of potential problems with using the Class Roster Sync Service, see [Error Responses](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW40). 
