# MDM Vendor CSR Signing Overview

 [Configuration Profile Reference - MDM Vendor CSR Signing Overview](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html)  
  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/RevHist_Index/RevisionHistory.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html)
  
The process of generating an APNS push certificate can be completed using the Apple Push Notification Portal.  
Customers can learn how the process works at [http://www.apple.com/business/mdm](http://www.apple.com/business/mdm).  
  

## Creating a Certificate Signing Request (Customer Action)
  


1. During the setup process for your service, create an operation that generates a Certificate Signing Request for your customer. 

2. This process should take place within the instance of your MDM service that your customer has access to. 

   > **Note:** 
The private key associated with this CSR should remain within the instance of your MDM service that the customer has access to. This private key is used to sign the MDM push certificate. The MDM service instance should not make this private key available to you (the vendor).  
 
  

Via your setup process, the CSR should be uploaded to your internal infrastructure to be signed as outlined below.  
  

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
  

## Creating the APNS Certificate for MDM (Customer Action)
  

Once you have delivered the signed CSR back to the customer, the customer must log in to [https://identity.apple.com/pushcert](https://identity.apple.com/pushcert) using a verified Apple ID and upload the CSR to the Apple Push Certificates Portal.  

The portal creates a certificate titled “MDM_*<VendorName>*_Certificate.pem.” At this point, the customer returns to your setup process to upload the APNS Certificate for MDM.  
  

## Code Samples
  

The following code snippets demonstrate the CSR signing process.  

**Listing 1**  Sample Java Code  

```
/**
* Sign the CSR ( DER format ) with signing private key.
* SHA1WithRSA is used for signing. SHA1 for message digest and RSA to encrypt the message digest.
*/
byte[] signedData = signCSR(signingCertPrivateKey, csr);
 
String certChain = ”-----BEGIN CERTIFICATE----”;
/**
* Create the Request Plist. The CSR and Signature is Base64 encoded.
*/
byte[] reqPlist = createPlist(new String(Base64.encodeBase64(csr)),certChain, new String(Base64.encodeBase64(signedData)));
 
 
/**
* Signature actually uses two algorithms--one to calculate a message digest and one to encrypt the message digest
* Here is Message Digest is calculated using SHA1 and encrypted using RSA.
* Initialize the Signature with the signer's private key using initSign().
* Use the update() method to add the data of the message into the signature.
*
* @param privateKey Private key used to sign the data
* @param data    Data to be signed.
* @return Signature as byte array.
* @throws Exception
*/
private byte[] signCSR( PrivateKey privateKey, byte[] data ) throws Exception{
    Signature sig = Signature.getInstance("SHA1WithRSA");
    sig.initSign(privateKey);
    sig.update(data);
    byte[] signatureBytes = sig.sign();
    return signatureBytes;
}
```  

**Listing 2**  Sample .NET Code  

```
var privateKey = new PrivateKey(PrivateKey.KeySpecification.AtKeyExchange, 2048, false, true);
var caCertificateRequest = new CaCertificateRequest();
string csr = caCertificateRequest.GenerateRequest("cn=test", privateKey);
 
//Load signing certificate from MDM_pfx.pfx, this is generated using signingCertificatePrivate.pem and SigningCert.pem.pem using openssl
var cert = new X509Certificate2(MY_MDM_PFX, PASSWORD, X509KeyStorageFlags.Exportable);
 
//RSA provider to generate SHA1WithRSA
var crypt = (RSACryptoServiceProvider)cert.PrivateKey;
var sha1 = new SHA1CryptoServiceProvider();
byte[] data = Convert.FromBase64String(csr);
byte[] hash = sha1.ComputeHash(data);
//Sign the hash
byte[] signedHash = crypt.SignHash(hash, CryptoConfig.MapNameToOID("SHA1"));
var signedHashBytesBase64 = Convert.ToBase64String(signedHash);
```  

**Listing 3**  Sample Request property list  

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>PushCertRequestCSR</key>
<string>
MIIDjzCCAncCAQAwDzENMAsGA1UEAwwEdGVzdDCCASIwDQYJKoZIhvcNAQEBBQAD
</string>
<key>PushCertCertificateChain</key>
<string>
-----BEGIN CERTIFICATE-----
MIIDkzCCAnugAwIBAgIIQcQgtHQb9wwwDQYJKoZIhvcNAQEFBQAwUjEaMBgGA1UE
AwwRU0FDSSBUZXN0IFJvb3QgQ0ExEjAQBgNVBAsMCUFwcGxlIElTVDETMBEGA1UE
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDlTCCAn2gAwIBAgIIBInl9fQbaAkwDQYJKoZIhvcNAQEFBQAwXDEkMCIGA1UE
AwwbU0FDSSBUZXN0IEludGVybWVkaWF0ZSBDQSAxMRIwEAYDVQQLDAlBcHBsZSBJ
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDpjCCAo6gAwIBAgIIKRyFYgyyFPgwDQYJKoZIhvcNAQEFBQAwXDEkMCIGA1UE
AwwbU0FDSSBUZXN0IEludGVybWVkaWF0ZSBDQSAxMRIwEAYDVQQLDAlBcHBsZSBJ
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDiTCCAnGgAwIBAgIIdv/cjbnBgEgwDQYJKoZIhvcNAQEFBQAwUjEaMBgGA1UE
AwwRU0FDSSBUZXN0IFJvb3QgQ0ExEjAQBgNVBAsMCUFwcGxlIElTVDETMBEGA1UE
-----END CERTIFICATE-----
</string>
<key>PushCertSignature</key>
<string>
CGt6QWuixaO0PIBc9dr2kJpFBE1BZx2D8L0XH0Mtc/DePGJOjrM2W/IBFY0AVhhEx
</string>
```  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/RevHist_Index/RevisionHistory.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html)

  



