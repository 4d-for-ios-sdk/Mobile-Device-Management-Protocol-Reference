# Error Responses

 [Configuration Profile Reference - Error Responses](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html#//apple_ref/doc/uid/TP40017387-CH9-SW40)  
  

## Error Responses
  

Instead of the information responses described earlier in this chapter, MDM roster requests may return system errors. You must read and respond to three kinds of errors:  


* Server failures 

* Client failures 

* MDM errors 
  

Server failures are mainly HTTP 500 and HTTP 503 errors:  

```
HTTP/1.1 500 Internal Server Error
Content-Type: text/plain;charset=UTF8
Content-Length: 0
Date: Thu, 22 Oct 2015 21:23:57 GMT
Connection: close,
 
HTTP/1.1 503 Service Unavailable
Content-Type: text/plain;charset=UTF8
Retry-After: 120
Content-Length: 0
Date: Thu, 22 Oct 2015 21:23:57 GMT
Connection: close
```  

Client failures are HTTP 4xx-series or HTTP 429 errors:  

```
HTTP/1.1 4xx <Error Reason>
Content-Type: text/plain;Charset=UTF8
Content-Length: 10
Date: Thu, 22 Oct 2015 21:23:57 GMT
Connection: close
 
<ERROR CODE>
 
HTTP/1.1 429 <Error Reason>
Content-Type: text/plain;Charset=UTF8
Content-Length: 10
Retry-After: 10
Date: Thu, 22 Oct 2015 21:23:57 GMT
Connection: close
 
<ERROR CODE>
```  

Client failures may return MDM error codes. When combined with HTTP codes, these errors give you the following information:  


* UNAUTHORIZED + HTTP 401: Auth token has expired. The client should retry with a new auth token. 

* FORBIDDEN + HTTP 403: Auth token is invalid. 

* MALFORMED_REQUEST_BODY + HTTP 400: The request body is malformed. 

* CURSOR_REQUIRED + HTTP 400: The cursor is missing in the request. 

* INVALID_CURSOR + HTTP 400: The cursor in the request is invalid. 

* EXPIRED_CURSOR + HTTP 400: The cursor is older than 1 day.  

* TOO_MANY_REQUESTS + HTTP 429: Too many requests. Retry after time mentioned in “Retry-After” HTTP response header as per RFC 6585. 
