# Distributing Client Identities

 [Configuration Profile Reference - Distributing Client Identities](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW16)  
  

## Distributing Client Identities
  

Each device must have a unique client identity certificate. You may deliver these certificates as PKCS#12 containers or via SCEP. Using SCEP is recommended because the protocol ensures that the private key for the identity exists only on the device.  

Consult your organization’s Public Key Infrastructure policy to determine which method is appropriate for your installation.