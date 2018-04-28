# Structure of MDM Payloads

 [Configuration Profile Reference - Structure of MDM Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW50)  
  

## Structure of MDM Payloads
  

The Mobile Device Management (MDM) payload, a simple property list, is designated by the `com.apple.mdm` value in the `PayloadType` field. This payload defines the following keys specific to MDM payloads:  



||||
|-|-|-|
|`IdentityCertificateUUID`|String|*Mandatory.* UUID of the certificate payload for the device’s identity. It may also point to a SCEP payload.|
|`Topic`|String|*Mandatory.* The topic that MDM listens to for push notifications. The certificate that the server uses to send push notifications must have the same topic in its subject. The topic must begin with the `com.apple.mgmt.` prefix.|
|`ServerURL`|String|*Mandatory.* The URL that the device contacts to retrieve device management instructions. Must begin with the `https://` URL scheme, and may contain a port number (`:1234`, for example).|
|`ServerCapabilities`|Array|Optional. An array of strings indicating server capabilities. If the server manages macOS devices or a Shared iPad, this field is mandatory and must contain the value `com.apple.mdm.per-user-connections`. This indicates that the server supports both device and user connections. See [MDM Protocol Extensions](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW62).|
|`SignMessage`|Boolean|Optional. If `true`, each message coming from the device carries the additional `Mdm-Signature` HTTP header. Defaults to `false`.</br>See [Passing the Client Identity Through Proxies](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW1) for details.|
|`CheckInURL`|String|Optional. The URL that the device should use to check in during installation. Must begin with the `https://` URL scheme and may contain a port number (`:1234`, for example). If this URL is not given, the `ServerURL` is used for both purposes.|
|`CheckOutWhenRemoved`|Boolean|Optional. If `true`, the device attempts to send a `CheckOut` message to the check-in server when the profile is removed. Defaults to `false`.</br>Note: macOS v10.8 acts as though this setting is always `true`.</br>**Availability: **Available in iOS 5.0 and later|
|`AccessRights`|Integer, flags|*Required.* Logical OR of the following bit-flags:<ul><li>1: Allow inspection of installed configuration profiles.</li><li>2: Allow installation and removal of configuration profiles.</li><li>4: Allow device lock and passcode removal.</li><li>8: Allow device erase.</li><li>16: Allow query of Device Information (device capacity, serial number).</li><li>32: Allow query of Network Information (phone/SIM numbers, MAC addresses).</li><li>64: Allow inspection of installed provisioning profiles.</li><li>128: Allow installation and removal of provisioning profiles.</li><li>256: Allow inspection of installed applications.</li><li>512: Allow restriction-related queries.</li><li>1024: Allow security-related queries.</li><li>2048: Allow manipulation of settings. **Availability:** Available in iOS 5.0 and later. Available in macOS 10.9 for certain commands.</li><li>4096: Allow app management. **Availability:** Available in iOS 5.0 and later. Available in macOS 10.9 for certain commands.</li></ul></br>May not be zero. If 2 is specified, 1 must also be specified. If 128 is specified, 64 must also be specified.|
|`UseDevelopmentAPNS`|Boolean|Optional. If `true`, the device uses the development APNS servers. Otherwise, the device uses the production servers. Defaults to `false`. Note that this property must be set to false if your Apple Push Notification Service certificate was issued by the Apple Push Certificate Portal ([identity.apple.com/pushcert](https://identity.apple.com/pushcert)). That portal only issues certificates for the production push environment.|
|`ServerURLPinningCertificateUUIDs`|Array|Optional. Array of strings containing the `PayloadUUIDs` of certificates to be used when evaluating trust to the `.../connect/` URLs of MDM servers. **Availability:** Available in macOS 10.13 and later.|
|`CheckInURLPinningCertificateUUIDs`|Array|Optional. Array of strings containing the `PayloadUUIDs` of certificates to be used when evaluating trust to the `.../checkin/` URLs of MDM servers. **Availability:** Available in macOS 10.13 and later.|
|`PinningRevocationCheckRequired`|Boolean|Optional. If `true`, connection will fail unless a verified positive response is obtained during certificate revocation checks. If `false`, revocation checking is done on a best attempt basis and failure to reach the server is not considered fatal. Default is `false`.**Availability:** Available in macOS 10.13 and later.|
  

In addition, four standard payload keys must be defined:  


|Key|Value|
|-|-|
|`PayloadType`|`com.apple.mdm`.|
|`PayloadVersion`|`1`.|
|`PayloadIdentifier`|A value must be provided.|
|`PayloadUUID`|A globally unique value must be provided.|
  

These keys are documented in [Payload Dictionary Keys Common to All Payloads](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW1) in [Configuration Profile Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).  

For the general structure of the payload and an example, see [Configuration Profile Key Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1) in [Configuration Profile Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).  

> **Note:** 
Profile payload dictionary keys that are prefixed with “Payload” are reserved key names and must never be treated as managed preferences. Any other key in the payload
dictionary may be considered a managed preference for that preference domain.  
