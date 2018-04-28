# SSL Certificate Trust

 [Configuration Profile Reference - SSL Certificate Trust](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW15)  
  

## SSL Certificate Trust
  

MDM only connects to servers that have valid SSL certificates. If your server’s SSL certificate is rooted in your organization’s root certificate, the device must trust the root certificate before MDM will connect to your server.  

You may include the root certificate and any intermediate certificates in the same profile that contains the MDM payload. Certificate payloads are installed before the MDM payload.  

You can also install a `trust_profile_url`, as described in [Adding MDMServiceConfig Functionality](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW101).  

Your MDM server should replace the profile that contains the MDM payload well before any of the certificates in that profile expire. Remember: If any certificate in the SSL trust chain expires, the device cannot connect to the server to receive its commands. When this occurs, you lose the ability to manage the device.