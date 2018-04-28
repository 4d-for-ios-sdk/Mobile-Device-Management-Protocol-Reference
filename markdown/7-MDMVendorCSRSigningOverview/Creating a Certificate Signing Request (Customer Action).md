# Creating a Certificate Signing Request (Customer Action)

 [Configuration Profile Reference - Creating a Certificate Signing Request (Customer Action)](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW5)  
  

## Creating a Certificate Signing Request (Customer Action)
  


1. During the setup process for your service, create an operation that generates a Certificate Signing Request for your customer. 

2. This process should take place within the instance of your MDM service that your customer has access to. 

   > **Note:** 
The private key associated with this CSR should remain within the instance of your MDM service that the customer has access to. This private key is used to sign the MDM push certificate. The MDM service instance should not make this private key available to you (the vendor).  
 
  

Via your setup process, the CSR should be uploaded to your internal infrastructure to be signed as outlined below.