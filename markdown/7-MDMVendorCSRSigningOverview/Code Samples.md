# Code Samples

 [Configuration Profile Reference - Code Samples](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html#//apple_ref/doc/uid/TP40017387-CH6-SW11)  
  

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