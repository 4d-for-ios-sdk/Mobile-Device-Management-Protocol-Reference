# Creating the APNS Certificate for MDM (Customer Action)

 [Configuration Profile Reference - Creating the APNS Certificate for MDM (Customer Action)](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW10)  
  

## Creating the APNS Certificate for MDM (Customer Action)
  

Once you have delivered the signed CSR back to the customer, the customer must log in to [https://identity.apple.com/pushcert](https://identity.apple.com/pushcert) using a verified Apple ID and upload the CSR to the Apple Push Certificates Portal.  

The portal creates a certificate titled “MDM_*<VendorName>*_Certificate.pem.” At this point, the customer returns to your setup process to upload the APNS Certificate for MDM.