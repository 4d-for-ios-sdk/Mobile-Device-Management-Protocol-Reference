# Terminating a Management Relationship

 [Configuration Profile Reference - Terminating a Management Relationship](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW22)  
  

## Terminating a Management Relationship
  

You can terminate a management relationship with a device by performing one of these actions:  


* Remove the profile that contains the MDM payload. An MDM server can always remove this profile, even if it does not have the access rights to add or remove configuration profiles. 

* Respond to any device request with a `401 Unauthorized` HTTP status. The device automatically removes the profile containing the MDM payload upon receiving a `401` status code. 
