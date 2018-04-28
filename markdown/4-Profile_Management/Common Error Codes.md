# Common Error Codes

 [Configuration Profile Reference - Common Error Codes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW5)  
  

## Common Error Codes
  

If the request could not be validated, the server returns one of the following errors.  


* An HTTP `400` error with `MALFORMED_REQUEST_BODY` in the response body indicates that the request body was not valid JSON. 

* An HTTP `401` error with `UNAUTHORIZED` in the response body indicates that the authentication token has expired. This error indicates that the MDM server should obtain a new auth token from the [https://mdmenrollment.apple.com/session](https://configbuddy.apple.com/session) endpoint. 

* An HTTP `403` error with `FORBIDDEN` in the response body indicates that the authentication token is invalid. 

* An HTTP `405` error means that the method (query type) is not valid. 
  

For example, the following is the response when an authentication token has expired.  

```
HTTP/1.1 401 Unauthorized
Content-Type: text/plain;Charset=UTF8
Content-Length: 12
Date: Thu, 31 May 2012 21:23:57 GMT
Connection: close
 
UNAUTHORIZED
```  

> **Note:** The Device Enrollment Program service periodically issues a new `X-ADM-Auth-Session` in its response to a service call; the MDM server can use this new header value for any subsequent calls.  
  

After a period of extended inactivity, this token expires, and the MDM server must obtain a new auth token from the [https://mdmenrollment.apple.com/session](https://configbuddy.apple.com/session) endpoint.  

All responses may return a new `X-ADM-Auth-Session` token, which the MDM server should use in subsequent requests.