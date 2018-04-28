# Course Roster Information

 [Configuration Profile Reference - Course Roster Information](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW31)  
  

## Course Roster Information
  

This API returns course information for an organization.  

  

### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/course`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request. This is used for pagination. On the initial request, this should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/course HTTP/1.1
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
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of courses. If true, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`courses`|Array of dictionaries|Provides information about courses, sorted in lexical order by a course source_system_identifier. The organization must provide this identifier to Apple.|
  

Each `courses` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Course name. Maximum length 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the course. Maximum length 256 UTF-8 characters.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," and “MANUAL.” Maximum length 64 UTF-8 characters.|
|`source_system_identifier`|String|Optional. Identifier configured by organization for the course. Maximum length is 256 UTF-8 characters. Value can be null.|
  

The response contains a list of courses. The `more_to_follow` Boolean indicates if more information about courses remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of courses.  

If modifications to the course catalog are performed while the response is being returned, it will not return any courses rostered after it started responding. If any updates are applied on any of the entities or attributes, you must send the request again to get the latest snapshot of courses.  

One record in a typical response might look like this:  

```
HTTP/1.1 200 OK
Date: Mon,12 Oct 2015 02:25:30 GMT
Content-Type: application/json;charset=UTF8
X-ADM-Auth-Session: 87a235815b8d6661ac73329f75815b8d6661ac73329f815
Content-Length: ...
Connection: Keep-Alive
 
{
  "courses": [
    {
      "unique_identifier": "UNICOURID1003",
      "source": "SIS",
      "source_system_identifier": "INSTCOURSEID1003",
      "name": "Biology 101"
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
}
```  

  

### Course Roster Sync Service
  

This sync service uses a cursor returned by the full course roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, up to 7 days.  

This service may return the same course more than once. You can identify duplicates by matching their `unique_identifier` values.  

  

#### Requests
  

To access this information, POST a request in JSON format and UTF-8 charset to the following URL: `https://mdmenrollment.apple.com/roster/course/sync`. The request body should contain a JSON dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`cursor`|String|Optional. A hex string that represents the starting position for a request, used for pagination. This position should not be older than 7 days. On the initial request, it should be omitted. |
|`limit`|Integer|Optional. The maximum number of entries to return. The default value is 1000 and the maximum value is 1000.|
  

With its required header, a typical request looks like this:  

```
POST /roster/course/sync HTTP/1.1
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
|`more_to_follow`|Boolean|Indicates whether the request’s limit and cursor values resulted in only a partial list of courses. If `true`, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.|
|`courses`|Array of dictionaries|Provides information about courses, sorted in lexical order by a course `source_system_identifier`. The organization must provide this identifier to Apple.|
  

Each dictionary in the `courses` array contains these keys:  


|Key|Type|Content|
|-|-|-|
|`name`|String|Optional. Course name. Maximum length is 1024 UTF-8 characters.|
|`unique_identifier`|String|Unique identifier for the course. Maximum length is 256 UTF-8 characters.|
|`source`|String|Data source where class was created. Possible values include “iTunes U,” “SIS,” “CSV,” "SFTP," and “MANUAL.” Maximum length is 64 UTF-8 characters.|
|`source_system_identifier`|String|Optional. Identifier configured by the organization for its courses, with a maximum length of 256 UTF-8 characters. Its value is not guaranteed to be unique and can potentially change.|
  

One record in a typical successful Course Roster Sync Service response might look like this:  

```
{
  "courses": [
    {
      "unique_identifier": "UNICOURID1003",
      "source": "SIS",
      "source_system_identifier": "INSTCOURSEID1003",
      "name": "Biology 101",
    }
  ],
  "cursor": "1ac73329f75816",
  "more_to_follow": "false"
  "fetched_until": "2016-05-09T02:30:00Z"
}
```  

Note these features and cautions:  


* The response contains a list of courses. 

* The `more_to_follow` Boolean indicates if more course information remains to be fetched. The client should read this flag to determine if subsequent requests are necessary to get the next batch of courses. 

* The server will issue a cursor in all responses. If the cursor is sent in the next request, the server will return next set of records in chronological order and issue a new cursor. 

* Data changes will be delayed by a few minutes. 

* This service does not return deleted data. The client is expected to do a full sync and compare once every few days to identify deletes. 

* For a discussion of potential problems with using the Course Roster Sync Service, see [Error Responses](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW40), below. 
