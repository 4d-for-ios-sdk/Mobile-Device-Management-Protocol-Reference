# Identifying Devices

 [Configuration Profile Reference - Identifying Devices](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW17)  
  

## Identifying Devices
  

An MDM server should identify a connecting device by examining the device’s client identity certificate. The server should then cross-check the UDID reported in the message to ensure that the UDID is associated with the certificate.  

The device’s client identity certificate is used to establish the SSL/TLS connection to the MDM server. If your server sits behind a proxy that strips away (or does not ask for) the client certificate, read [Passing the Client Identity Through Proxies](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW1).