# Passing the Client Identity Through Proxies

 [Configuration Profile Reference - Passing the Client Identity Through Proxies](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW1)  
  

## Passing the Client Identity Through Proxies
  

If your MDM server is behind an HTTPS proxy that does not convey client certificates, MDM provides a way to tunnel the client identity in an additional HTTP header.  

If the value of the `SignMessage` field in the MDM payload is set to true, each message coming from the device carries an additional HTTP header named `Mdm-Signature`. This header contains a BASE64-encoded CMS Detached Signature of the message.  

Your server can validate the body with the detached signature in the `SignMessage` header. If the validation is successful, your server can assume that the message came from the signer, whose certificate is stored in the signature.  

Keep in mind that this option consumes a lot of data relative to the typical message body size. The signature is sent with every message, adding almost 2 KB of data to each outgoing message from the device. Use this option only if necessary.