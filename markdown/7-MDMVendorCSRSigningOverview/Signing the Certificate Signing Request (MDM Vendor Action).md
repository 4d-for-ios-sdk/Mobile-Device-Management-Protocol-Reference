# Signing the Certificate Signing Request (MDM Vendor Action)

 [Configuration Profile Reference - Signing the Certificate Signing Request (MDM Vendor Action)](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW7)  
  

## Signing the Certificate Signing Request (MDM Vendor Action)
  

Before you receive a CSR from your customer, download an MDM Signing Certificate and the associated trust certificates via the iOS Provisioning Portal.  

Next, you must create a script based on the instructions below to sign the customer’s CSR:  


1. If the CSR is in PEM format, convert CSR to DER (binary) format. 

2. Sign the CSR (in binary format) with the private key of the MDM Signing Cert using the `SHA1WithRSA` signing algorithm. 

   > **Note:** 
Do not share the private key from your MDM Signing Cert with anyone, including customers or resellers of your solution. The process of signing the CSR should take place within your internal infrastructure and should not be accessible to customers.  
 

3. Base64 encode the signature used in Step 2. 

4. Base64 encode the CSR (in binary format). 

5. Create a Push Certificate Request plist and Base64 encode it. 

5. Be certain that the `PushCertCertificateChain` value contains a *complete* certificate chain all the way back to a recognized root certificate (including the root certificate itself). This means it must contain your MDM signing certificate, the WWDR intermediate certificate (available from [http://developer.apple.com/certificationauthority/AppleWWDRCA.cer](http://developer.apple.com/certificationauthority/AppleWWDRCA.cer)), and the Apple Inc. root certificate (available from [http://www.apple.com/appleca/AppleIncRootCertificate.cer](http://www.apple.com/appleca/AppleIncRootCertificate.cer)). 

5. Also, be sure that every certificate complies with PEM formatting standards; each line except the last must contain exactly 64 printable characters, and the last line must contain 64 or fewer printable characters. 

5. It may be helpful to save the certificate and its chain into a file ending in `.pem` and then verify your certificate chain with the a target="_self" certtool/a (`certtool -e < filename.pem`) or a target="_self" openssl/a (`openssl verify filename.pem`) command-line tools. To learn more about certificates and chains of trust, read the Apple book [Security Overview](https://developer.apple.com/library/content/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000976), available at [developer.apple.com/library/content/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html](https://developer.apple.com/library/content/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html). 

5. Refer to the code samples in [Listing 1](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW1), [Listing 2](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW2), and [Listing 3](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW3) for additional instructions. 

   > **Note:** 
To minimize the risk of errors, you should use Xcode or the standalone Property List Editor application when editing property lists.  
> 
Alternatively, on the command line, you can make changes to property lists with the a target="_self" plutil/a tool or check the validity of property lists with the a target="_self" xmllint/a tool.  
 

6. Deliver the Push Certificate Request plist file created in Step 5 back to the customer and direct the customer to [https://identity.apple.com/pushcert](https://identity.apple.com/pushcert) to upload it to Apple. 
  

Be sure to use a separate push certificate for each customer. There are two reasons for this:  


* If multiple customers shared the same push topic, they would be able to see each other’s device tokens. 

* When a push certificate expires, gets invalidated or revoked, gets blocked, or otherwise becomes unusable, any customers sharing that certificate lose their ability to use MDM. 
  

All devices for the same customer should share a single push certificate. This same certificate should also be used to connect to the APNS feedback service.