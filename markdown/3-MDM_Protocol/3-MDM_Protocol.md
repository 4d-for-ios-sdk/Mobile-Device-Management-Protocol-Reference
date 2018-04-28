# Mobile Device Management (MDM) Protocol

 [Configuration Profile Reference - Mobile Device Management (MDM) Protocol](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html)  
  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/2-MDM_Check_In_Protocol/MDM_Check_In_Protocol..html)
  
The Mobile Device Management (MDM) protocol provides a way to tell a device to execute certain management commands remotely. The way it works is straightforward.  
**During installation:**  

* The user or administrator tells the device to install an MDM payload. The structure of this payload is described in [Structure of MDM Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW50). 

* The device connects to the check-in server. The device presents its identity certificate for authentication, along with its UDID and push notification topic. 

   > **Note:** Although UDIDs are used by MDM, the use of UDIDs is deprecated for iOS apps.  
 

* If the server accepts the device, the device provides its push notification device token to the server. The server should use this token to send push messages to the device. This check-in message also contains a `PushMagic` string. The server must remember this string and include it in any push messages it sends to the device. 
  
**During normal operation:**  

* The server (at some point in the future) sends out a push notification to the device. 

* The device polls the server for a command in response to the push notification. 

* The device performs the command. 

* The device contacts the server to report the result of the last command and to request the next command. 
  
From time to time, the device token may change. When a change is detected, the device automatically checks in with the MDM server to report its new push notification token.  
> **Note:** The device polls only in response to a push notification; it does not poll the server immediately after installation. The server must send a push notification to the device to begin a transaction.  
  
The device initiates communication with the MDM server in response to a push notification by establishing a TLS connection to the MDM server URL. The device validates the server’s certificate, then uses the identity specified in its MDM payload as the client authentication certificate for the connection.  
> **Note:** MDM follows HTTP `3xx` redirections without user interaction. However, it does not remember the URL given by HTTP `301 (Moved Permanently)` redirections. Each transaction begins at the URL specified in the MDM payload.  
  
Mobile Device Management, as its name implies, was originally developed for embedded systems. To support environments where a computer is bound to an Open Directory server and various network users may log in, extensions to the MDM protocol were developed to identify and authenticate the network user logging in so that any network user is also managed by the MDM server (via their user profiles). The extensions made to the MDM protocol are described in [MDM Protocol Extensions](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW62).  
> **Note:** 
Login may be blocked momentarily while the MDM server is contacted for its latest settings. Device enrollment can also be performed later, after the computer is connected to the Internet.  
  
  

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
  
  

## Structure of MDM Messages
  

Once the MDM payload is installed, the device listens for a push notification. The topic that MDM listens to corresponds to the contents of the `User ID` parameter in the Subject field of the push notification client certificate.  

To cause the device to poll the MDM server for commands, the MDM server sends a notification through the APNS gateway to the device. The message sent with the push notification is JSON-formatted and must contain the `PushMagic` string as the value of the `mdm` key. For example:  

```
{"mdm":"PushMagicValue"}
```  

In place of `PushMagicValue` above, substitute the actual `PushMagic` string that the device sends to the MDM server in the `TokenUpdate` message. That should be the whole message. There should not be an `aps` key. (The `aps` key is used only for third-party app push notifications.)  

The device responds to this push notification by contacting the MDM server using HTTP PUT over TLS (SSL). This message may contain an `Idle` status or may contain the result of a previous operation. If the connection is severed while the device is performing a task, the device will try to report its result again once networking is restored.  

 shows an example of an MDM request payload.  

**Listing 1**  MDM request payload example  

```
PUT /your/url HTTP/1.1
Host: www.yourhostname.com
Content-Length: 1234
Content-Type: application/x-apple-aspen-mdm; charset=UTF-8
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>UDID</key>
    <string>...</string>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Status</key>
    <string>Acknowledged</string>
  </dict>
</plist>
 
```  

The server responds by sending the next command that the device should perform by enclosing it in the HTTP reply.  

 shows an example of the server’s response payload.  

**Listing 2**  MDM response payload example  

```
HTTP/1.1 200 OK
Content-Length: 1234
Content-Type: application/xml; charset=UTF-8
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Command</key>
    <dict>
      ...
    </dict>
  </dict>
</plist>
 
```  

The device performs the command and sends its reply in another HTTP PUT request to the MDM server. The MDM server can then reply with the next command or end the connection by sending a `200` status (OK) with an empty response body.  

> **Note:** An empty response body must be zero bytes in length, not an empty property list.  
  

If the connection is broken while the device is performing a command, the device caches the result of the command and re-attempts connection to the server until the status is delivered.  

It is safe to send several push notifications to the device. APNS coalesces multiple notifications and delivers only the last one to the device.  

You can monitor the MDM activity in the device console using Xcode or [Apple Configurator 2](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12). A healthy (but empty) push activity should look like this:  

```
Wed Sep 29 02:09:05 unknown mdmd[1810] <Warning>: MDM|mdmd starting...
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Network reachability has changed.
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Polling MDM server https://10.0.1.4:2001/mdm for commands
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Transaction completed. Status: 200
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Server has no commands for this device.
Wed Sep 29 02:09:08 unknown mdmd[1810] <Warning>: MDM|mdmd stopping...
```  
  

## MDM Command Payloads
  

A host may send a command to the device by sending a plist-encoded dictionary that contains the following required keys:  


|Key|Type|Content|
|-|-|-|
|`CommandUUID`|String|UUID of the command.|
|`Command`|Dictionary|The command dictionary.|
  

The content of the `Command` dictionary must include the following required key, as well as other keys defined by each command.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|Request type. See each command’s description.|
|`RequestRequiresNetworkTether`|Boolean|Optional. If `true`, the command is executed only if the device has a tethered network connection; otherwise an MCMDM error value of 12081 is returned (see [MCMDMErrorDomain](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-TRANSLATED_DEST_13)). Default value is `false`.|
  
  

## MDM Result Payloads
  

The device replies to the host by sending a plist-encoded dictionary containing the following keys, as well as other keys returned by each command.  


|Key|Type|Content|
|-|-|-|
|`Status`|String|Status. Legal values are described in [Table 1](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW31).|
|`UDID`|String|UDID of the device.|
|`CommandUUID`|String|UUID of the command that this response is for (if any).|
|`ErrorChain`|Array|Optional. Array of dictionaries representing the chain of errors that occurred. The content of these dictionaries is described in [Table 2](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW33).|
  

The `Status` key contains one of the following strings:  


|Status value|Description|
|-|-|
|`Acknowledged`|Everything went well.|
|`Error`|An error has occurred. See the `ErrorChain` array for details.|
|`CommandFormatError`|A protocol error has occurred. The command may be malformed.|
|`Idle`|The device is idle (there is no status).|
|`NotNow`|The device received the command, but cannot perform it at this time. It will poll the server again in the future. For details, see [Error Handling](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW34).|
  

The `ErrorChain` key contains an array. The first item is the top-level error. Subsequent items in the array are the underlying errors that led up to that top-level error.  

Each entry in the `ErrorChain` array contains the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`LocalizedDescription`|String|Description of the error in the device’s localized language.|
|`USEnglishDescription`|String|Optional. Description of the error in US English.|
|`ErrorDomain`|String|The error domain.|
|`ErrorCode`|Number|The error code.|
  

The `ErrorDomain` and `ErrorCode` keys contain internal codes used by Apple that may be useful for diagnostics. Your host should not rely on these values, as they may change between software releases. However, for reference, the current codes are listed in [Error Codes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW77).  
  

## MDM Protocol Extensions
  

  

### macOS Extensions
  

Unlike iOS clients, a macOS client on an MDM server enrolls devices and users as separate entities. macOS supports several extensions to the MDM protocol to allow managing the device and logged-in user independently. When enrolled in this manner, the MDM server receives requests for the device and for each logged-in user.  

Device requests are sent from the `mdmclient` daemon, while user requests are sent from the `mdmclient` agent. If multiple users are logged in, there is one instance of an `mdmclient` agent for each logged-in user, and each may be sending requests concurrently in addition to device requests from the daemon.  

Devices and users are assigned different push tokens. The server can use this difference to determine whether the device or a specific user is to contact the server with an Idle request.  

To indicate that an MDM server supports both device and user connections, its MDM enrollment payload must contain the string `com.apple.mdm.per-user-connections`; see [Structure of MDM Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW50). The MDM enrollment profile should be delivered as any other manually-installed profile, but MDM promotes it to a device profile once it is installed. This will have the following consequences:  


* The device will be managed. 

* The local user that installed the profile will be managed. 

* No other local users will be managed. The server will never get requests from a local user other than the one that installed the enrollment profile. 

* Network users logging into the device will be managed if the server responds successfully to their `UserAuthenticate` messages. If the server does not want to manage a network client, it should return a `410` HTTP status code. 
  

During enrollment, the client sends the standard `Authenticate` request to the `CheckInURL` specified in the MDM payload. Once that request completes, the client sends one `TokenUpdate` request for the device and another for the user that performed the enrollment. The same client certificate is used to authenticate both device and user connections.  

To help the server differentiate requests coming from a device versus a user, user requests contain additional keys in their request plists:  

```
      <key>UDID</key>
      <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
      <key>UserID</key>
      <string>F17C470A-3ADC-47EC-A7CC-D432867F4793</string>
      <key>UserLongName</key>
      <string>Jimmy Smith</string>
      <key>UserShortName</key>
      <string>jimmys</string>
      <key>NeedSyncResponse</key>
      <boolean>true</boolean>
```  

Note the following conditions for including the foregoing keys:  


* Requests from a device contain only the `UDID` key. 

* `NeedSyncResponse` is optional. If it is present and true, it indicates that the client is in a state where the user is waiting for the completion of an MDM transaction. In macOS 10.9 and later versions, this key is added during user login when the login is blocked while the client checks in with the MDM server to ensure it has the latest settings and profiles. The key is meant as a hint to the server that it should send all commands in the current set of Idle/Acknowledged/Error transactions instead of relying on push notifications. During login, the client blocks the transaction only until the server sends an empty response to an Idle/Acknowledged/Error sequence. 

* `UserConfiguration` is optional. If it is present and true, it indicates that the macOS client is trying to obtain user-specific settings while in Setup Assistant during Device Enrollment (see [Device Enrollment Program](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW1)). After a macOS client obtains device-specific settings, it also attempts to determine if the server has any user-specific settings that may affect Setup Assistant. Currently, only password policies fall into this category. The password policies are used if Setup Assistant prompts to create a local user account. After the client receives a DeviceConfigured command on the device connection, it starts a normal Idle/Acknowledged/Error connection on the user connection. If the server sends commands or profiles during this time, nothing the client receives persists, because the user account hasn’t been created on the system yet. The client always responds `NotNow` to any commands it received during this time. It continues to respond with `NotNow` until it receives a reply with no additional commands (an empty body) or a `DeviceConfigured` command on the user connection. The client passes any password policies to Setup Assistant and discards everything else. After Setup Assistant creates the user account and the user logs in, the client initiates a new series of Idle/Acknowledged/Error connections. The server should then resend all commands and profiles. The client processes them normally and they will persist. 
  

  

### Network User Authentication Extensions
  

To support environments where a macOS computer is bound to an Open Directory server and various network users may log in, extensions to the MDM protocol were developed to identify and authenticate the network user logging in. This way, network users are also managed by the MDM server via their user profiles.  

At login time, if the user is a network user or has a mobile home, the MDM client issues a request to the server to authenticate the current user to the MDM server and obtain an `AuthToken` value that is used in subsequent requests made by this user to the server.  

The authentication happens using a transaction similar in structure to existing transactions with the server, as an HTTP `PUT` request to the `CheckInURL` address specified in the MDM payload.  

The first request to the server is sent to the `CheckInURL` specified in the MDM payload, with the same identity used for all other MDM requests. The message body contains a property list with the following keys:  


|Key|Type|Content|
|-|-|-|
|`MessageType`|String|`UserAuthenticate`.|
|`UDID`|String|UDID used on all MDM requests.|
|`UserID`|String|Local user’s GUID, or  network user’s GUID from Open Directory Record (see below).|
  

If the macOS device being enrolled has an owner, the `UserID` key may designate a local user instead of a network user. If the local request succeeds, an `-MDM-is-owned` header is added to the response to all requests to the `checkinURL`, except `CheckOut` requests where it is optional. To this header may be added a value of 1 to indicate the device is owned; this is also the default behavior if the header is omitted. Only if the header is present with a value of 0 will requests from the client be optimized.  

The response from the server should contain a dictionary with:  


|Key|Type|Content|
|-|-|-|
|`DigestChallenge`|String|`Standard HTTP Digest`.|
  

If the server provides a `200` response but a zero-length `DigestChallenge` value, the server does not require any AuthToken to be generated for this user.  

Otherwise, with a `200` response and `DigestChallenge` value that is non-empty, the client generates a digest from the user’s shortname, the user’s clear-text password, and the `DigestChallenge` value obtained from the server. The resulting digest is sent in a second request to the server, which validates the response and returns an `AuthToken` value that is sent on subsequent requests to the server.  

If the server does not want to manage this user, it should return a `410` HTTP status code. The client will not make any additional requests to the server on behalf of this user for the duration of this login session. The next time that user logs in, however, the client will again send a `UserAuthenticate` request and the server can optionally return `410` again.  

The second request to the server is also sent to the `CheckInURL` specified in the MDM payload and sent with the same identity used for all other MDM requests. The message body contains:  


|Key|Type|Content|
|-|-|-|
|`MessageType`|String|`UserAuthenticate`.|
|`UDID`|String|UDID used on all MDM requests.|
|`UserID`|String|User’s GUID from Open Directory Record.|
|`DigestResponse`|String|Obtained from generating digest above.|
  

The response from the server should contain a dictionary with:  


|Key|Type|Content|
|-|-|-|
|`AuthToken`|String|The token used for authentication.|
  

If the server responds with a `200` response and a non-empty `AuthToken` value is present, the `AuthToken` value is sent to the server on subsequent requests. The `AuthToken` value is included in the message body of subsequent requests along with the additional keys:  


|Key|Type|Value|
|-|-|-|
|`UDID`|String|Device ID.|
|`UserID`|String|GUID attribute from the user’s Open Directory record.|
|`UserShortName`|String|Record name from user’s Open Directory record.|
|`UserLongName`|String|Full name from user’s Open Directory record.|
|`AuthToken`|String|Token obtained from above.|
  

It is assumed that the `AuthToken` remains valid until the next time the client sends a `UserAuthenticate` request. The client initiates a `UserAuthenticate` handshake each time a network user logs in.  

If the server rejects the `DigestResponse` value because of an invalid password, it returns a `200` response and an empty `AuthToken` value.  

The following is an example of a `UserAuthenticate` handshake:  

```
// UserAuthenticate request from client to server:
<dict>
      <key>MessageType</key>
      <string>UserAuthenticate</string>
      <key>UDID</key>
      <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
      <key>UserID</key>
      <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string>
</dict>
 
// Server sends challenge:
<dict>
      <key>DigestChallenge</key>
      <string>Digest nonce="8BrAkk4GZgrG//
            2XaDLMSSSo89VenjV5E8Se73z98RvSW7Rs",realm="fusion.home"<string>
</dict>
 
// Client sends response:
<dict>
      <key>DigestResponse</key>
      <string>Digest username="net1",realm="fusion.home",
            nonce="8BrAkk4GZgrG2XaDLMSSSo89VenjV5E8Se73z98RvSW7Rs",
            uri="/",response="84db40bbaf5e0d49cabb0ef7d8cac369"</string>
      <key>MessageType</key>
      <string>UserAuthenticate</string>
      <key>UDID</key>
      <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
      <key>UserID</key>
      <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string>
</dict>
 
// Server responds with AuthToken for client session:
<key>AuthToken</key>
<string>uEOcQRJrXGbMJUDAkDZSCny5e90=</string>
 
// From this point on, all user requests from that network user will include an AuthToken key:
<dict>
      <key>AuthToken</key>
      <string>uEOcQRJrXGbMJUDAkDZSCny5e90=</string>
      <key>Status</key>
      <string>Idle</string>
      <key>UDID</key>
      <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
      <key>UserID</key>
      <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string>
      <key>UserLongName</key>
      <string>Net One</string>
      <key>UserShortName</key>
      <string>net1</string>
</dict>
```  

For push notifications, the client uses different push tokens for device and user connections. Each token is sent to the server using the `TokenUpdate` request. The server can tell for whom the token is intended based on the `UDID` and `UserID` values in the request. If the user is a network/mobile user, the `AuthToken` is provided.  

> **Warning:** These push tokens should not be confused with the “AuthToken” mentioned above.  
  

  

### iOS Support for Per-User Connections
  

A device running iOS 9.3 or later, and its logged-in users, can be managed independently as a Shared iPad, using a technique similar to [Network User Authentication Extensions](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW736). The device and its users are assigned different push tokens. The server can use this difference to determine whether the device or a specific user is to contact the server with an `Idle` request.  

In general, the following types of MDM commands can be sent on the user channel:  


* `
kMCMDMPRequestTypeProfileList` 

* `
kMCMDMPRequestTypeInstallProfile` 

* `
kMCMDMPRequestTypeRemoveProfile` 

* `
kMCMDMPRequestTypeRestrictions` 

* `
kMCMDMPRequestTypeInviteToProgram` 

* `
kMCMDMPRequestTypeDeviceInformation` 
  

To indicate that an MDM server supports both device and user connections, the `ServerCapabilities` array in its MDM enrollment payload must contain the string `com.apple.mdm.per-user-connections`, indicating support for Shared iPad. Then when a user logs in, the device sends a `TokenUpdate` request on the user channel.  

To help the server differentiate requests coming from a device versus a user, user requests must contain additional keys:  


|Key|Type|Content|
|-|-|-|
|`UserID`|String|Always set to `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that no authentication will occur.|
|`UserLongName`|String|The full name of the user.|
|`UserShortName`|String|The Managed Apple ID of the user.|
  

If the server is configured to manage the user, it stores the user push token and returns a 200 response. At this point the device polls the server for a command on the user channel.  

If the server is not configured to manage the user, it should return a 410 HTTP status code. The client will not make any additional requests to the server on behalf of this user for the duration of the login session. The next time the user logs in, however, the client will again send a `UserAuthenticate` request and the server can optionally return a 410 code again.  
  

## Error Handling
  

There are certain times when the device is not able to do what the server requests. For example, databases cannot be modified while the device is locked with Data Protection. When a device cannot perform a command due to situations like this, it sends a `NotNow` status without performing the command. The server may send another command immediately after receiving this status. See “Handling a NotNow Response,” below, for more details.  

The following commands are guaranteed to execute in iOS, and never return `NotNow`:  


* `DeviceInformation` 

* `ProfileList` 

* `DeviceLock` 

* `EraseDevice` 

* `ClearPasscode` 

* `CertificateList` 

* `ProvisioningProfileList` 

* `InstalledApplicationList` 

* `Restrictions` 
  

The macOS MDM client may respond with `NotNow` when:  


* The system is in Power Nap (dark wake) and a command other than `DeviceLock` or `EraseDevice` is received. 

* An `InstallProfile` or `RemoveProfile` request is made on the user connection and the user’s keychain is locked. 
  

In macOS, the client may respond with `NotNow` if it is blocking the user’s login while it contacts the server, and if the server sends a request that may take a long time to answer (such as `InstalledApplicationList` or `DeviceInformation`).  
  

## Handling a NotNow Response
  

If the device’s response to the previous command sent has a status of `NotNow`, your server has two response choices:  


* It may immediately stop sending commands to the device. In this case the device automatically polls your server when conditions change and it is able to process the last requested command. The server does not need to send another push notification in response to this status. However, the server may send another push notification to the device to have it poll the server immediately. The device does not cache the command that was refused. If the server wants the device to retry the command, it must send the command again when the device polls the server. 

* It may send another command on the same connection, but if this new command returns anything other than a `NotNow` response, the device will *not* automatically poll the server as it would have with the first response choice. The server must send a push notification at a later time to make the device reconnect. The device polls the server in response to a `NotNow` status only if that is the last status sent by the device to the server. 
  

The three example flowcharts below illustrate the foregoing choices.  

**Example 1:** The final command results in the server receiving a `NotNow` response. The device will poll the server later, when the `InstallApplication` command might succeed.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow1_2x.png" height="400" width="407">  

**Example 2:** The final command results in the server receiving something other than a `NotNow` response. The device will not poll the server later, because the last response was not `NotNow`.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow2_2x.png" height="322" width="407">  

**Example 3:** The connection to the device is unexpectedly interrupted. Because the last status the server received was not `NotNow`, the server should send a push notification to the device to retry the `InstallApplication` command. The server must not assume that the device will automatically poll the server later.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow3_2x.png" height="357" width="454">  
  

## Request Types
  

This section describes the MDM protocol request types for Apple devices that run iOS. Support for the equivalent request types used with Apple computers that run macOS is summarized in [Support for macOS Requests](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW901).  

  

### ProfileList Commands Return a List of Installed Profiles
  

To send a `ProfileList` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ProfileList`.|
  

The device replies with a property list that contains the following key:  


|Key|Type|Content|
|-|-|-|
|`ProfileList`|Array|Array of dictionaries. Each entry describes an installed profile.|
  

Each entry in the `ProfileList` array contains a dictionary with a profile. For more information about profiles, see [Configuration Profile Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).  

> **Security Note:** `ProfileList` queries are available only if the MDM host has an Inspect Profile Manifest access right.  
  

If you want to update a profile in place by installing a new one where there is already an existing one, follow these rules:  


* The new MDM profile must be signed with the same identity as the existing profile. 

* You cannot change the topic or server URL of the profile. 

* You cannot add rights to a profile that replaces an existing one. 
  

  

### InstallProfile Commands Install a Configuration Profile
  

The profile to install may be encrypted using any installed device identity certificate. The profile may also be signed.  

To send an `InstallProfile` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstallProfile`|
|`Payload`|Data|The profile to install. May be signed and/or encrypted for any identity installed on the device.|
  

Note that in the definition of the InstallProfile command, the Payload is of type Data, meaning that the entire Payload must be base64-encoded, including the XML headers. This is true for any Data type items in a property list. See [Understanding XML Property Lists](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/PropertyLists/UnderstandXMLPlist/UnderstandXMLPlist.html#//apple_ref/doc/uid/10000048i-CH6) in [Property List Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i) for more information.  

> **Security Note:** This query is available only if the MDM host has a Profile Installation and Removal access right.  
  

  

### RemoveProfile Commands Remove a Profile from the Device
  

By sending the `RemoveProfile` command, the server can ask the device to remove any profile originally installed through MDM.  

To send a `RemoveProfile` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RemoveProfile`.|
|`Identifier`|String|The `PayloadIdentifier` value for the profile to remove.|
  

> **Security Note:** This query is available only if the MDM host has a Profile Installation and Removal access right.  
  

  

### ProvisioningProfileList Commands Get a List of Installed Provisioning Profiles
  

To send a `ProvisioningProfileList` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ProvisioningProfileList`.|
  

The device replies with:  


|Key|Type|Content|
|-|-|-|
|`ProvisioningProfileList`|Array|Array of dictionaries. Each entry describes one provisioning profile.|
  

Each entry in the `ProvisioningProfileList` array contains the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`Name`|String|The display name of the profile.|
|`UUID`|String|The UUID of the profile.|
|`ExpiryDate`|Date|The expiry date of the profile.|
  

> **Security Note:** This query is available only if the MDM host has an Inspect Provisioning Profiles access right.  
  

> **Note:** The macOS MDM client responds with an empty `ProvisioningProfileList` array.  
  

  

### InstallProvisioningProfile Commands Install Provisioning Profiles
  

To send an `InstallProvisioningProfile` command to an iOS device, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstallProvisioningProfile`|
|`ProvisioningProfile`|Data|The provisioning profile to install.|
  

> **Note:** No error occurs if the specified provisioning profile is already installed.  
  

> **Security Note:** This query is available only if the MDM host has a Provisioning Profile Installation and Removal access right.  
  

  

### RemoveProvisioningProfile Commands Remove Installed Provisioning Profiles
  

To send a `RemoveProvisioningProfile` command to an iOS device, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RemoveProvisioningProfile`|
|`UUID`|String|The UUID of the provisioning profile to remove.|
  

> **Security Note:** This query is available only if the MDM host has a Provisioning Profile Installation and Removal access right.  
  

  

### CertificateList Commands Get a List of Installed Certificates
  

To send a `CertificateList` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`CertificateList`|
  

The device replies with:  


|Key|Type|Content|
|-|-|-|
|`CertificateList`|Array|Array of certificate dictionaries. The dictionary format is described in [Table 3](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW27).|
  

Each entry in the `CertificateList` array is a dictionary containing the following fields:  


|Key|Type|Content|
|-|-|-|
|`CommonName`|String|Common name of the certificate.|
|`IsIdentity`|Boolean|Set to `true` if this is an identity certificate.|
|`Data`|Data|The certificate in DER-encoded X.509 format.|
  

> **Note:** The `CertificateList` command requires that the server have the Inspect Profile Manifest privilege.  
  

  

### InstalledApplicationList Commands Get a List of Third-Party Applications
  

To send an `InstalledApplicationList` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstalledApplicationList`.|
|`Identifiers`|Array|Optional. An array of app identifiers as strings. If provided, the response contains only the status of apps whose identifiers appear in this array. Available in iOS 7 and later.|
|`ManagedAppsOnly`|Boolean|Optional. If `true`, only managed app identifiers are returned. Available in iOS 7 and later.|
  

The device replies with:  


|Key|Type|Content|
|-|-|-|
|`InstalledApplicationList`|Array|Array of installed applications. Each entry is a dictionary as described in [Table 4](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW28).|
  

Each entry in the `InstalledApplicationList` is a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The application’s ID.|
|`Version`|String|The application’s version.|
|`ShortVersion`|String|The application’s short version.</br>**Availability:** Available in iOS 5.0 and later.|
|`Name`|String|The application’s name.|
|`BundleSize`|Integer|The app’s static bundle size, in bytes.|
|`DynamicSize`|Integer|The size of the app’s document, library, and other folders, in bytes.</br>**Availability:** Available in iOS 5.0 and later.|
|`IsValidated`|Boolean|If `true`, the app has validated as allowed to run and is able to run on the device. If an app is enterprise-distributed and is not validated, it will not run on the device until validated.</br>**Availability:** Available in iOS 9.2 and later.|
  

  

### DeviceInformation Commands Get Information About the Device
  

To send a `DeviceInformation` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DeviceInformation`|
|`Queries`|Array|Array of strings. Each string is a value from [Table 5](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW24), [Table 7](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW25), or [Table 9](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW26).|
  

The device replies with:  


|Key|Type|Content|
|-|-|-|
|`QueryResponses`|Dictionary|Contains a series of key-value pairs. Each key is a query string from [Table 5](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW24), [Table 7](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW25), or [Table 9](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW26). The associated value is the response for that query.|
  

Queries for which the device has no response or that are not permitted by the MDM host’s access rights are dropped from the response dictionary.  

  

#### General Queries Are Always Available
  

The queries described in  are available without any special access rights:  


|Query|Reply Type|Comment|
|-|-|-|
|`UDID`|String|The unique device identifier (UDID) of the device.|
|`Languages`|Array|Array of strings. The first entry in this array indicates the current language. **Availability:** Available in Apple TV software 6.0 and later. Supported in macOS 10.10 and 10.11 but will be removed in a future macOS release.|
|`Locales`|String|Array of strings. The first entry in this array indicates the current locale. **Availability:** Available in Apple TV software 6.0 and later. Supported in macOS 10.10 and 10.11 but will be removed in a future macOS release.|
|`DeviceID`|String|The Apple TV device ID. Available in iOS 7 (Apple TV software 6.0) and later, on Apple TV only.|
|`OrganizationInfo`|Dictionary|The contents (if any) of a previously set `OrganizationInfo` setting. Available in iOS 7 and later.|
|`LastCloudBackupDate`|Date|The date of the last iCloud backup. **Availability:** Available in iOS 8.0 and later.|
|`AwaitingConfiguration`|Boolean|If `true`, device is still waiting for a DeviceConfigured message from MDM to continue through Setup Assistant. **Availability:** Available in iOS 9 and later and the response is only generated by devices enrolled in MDM via DEP (see [Device Enrollment Program](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW1)).|
|`AutoSetupAdminAccounts`|Array of Dictionaries|Returns the local admin users (if any) created automatically by Setup Assistant during DEP enrollment via the `AccountConfiguration` command. **Availability:** Available in macOS 10.11 and later and the response is only generated by devices enrolled in MDM via DEP (see [Device Enrollment Program](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW1)).</br>Each dictionary in the array contains two keys: a key `GUID` with a string value of the Global Unique Identifier of a local admin account, and a key `shortName` with a string value of the short name of the admin account.|
  

  

#### iTunesStoreAccountIsActive Commands Tell Whether an iTunes Account Is Logged In
  

The queries in  are available if the MDM host has an Install Applications access right:  


|Query|Reply Type|Content|
|-|-|-|
|`iTunesStoreAccountIsActive`|Boolean|`true` if the user is currently logged into an active iTunes Store account. Available in iOS 7 and later and in macOS 10.9.|
|`iTunesStoreAccountHash`|String|Returns a hash of the iTunes Store account currently logged in. This string is identical to the `itsIdHash` returned by the VPP App Assignment web service. **Availability:** Available in iOS 8.0 and later and macOS 10.10 and later.|
  

  

#### Device Information Queries Provide Information About the Device
  

The queries in  are available if the MDM host has a Device Information access right:  


|Query|Reply Type|Comment|
|-|-|-|
|`DeviceName`|String|The iOS device name or the macOS hostname.|
|`OSVersion`|String|The version of iOS the device is running.|
|`BuildVersion`|String|The build number (8A260b, for example).|
|`ModelName`|String|Name of the device model, e.g., “MacBook Pro.”|
|`Model`|String|The device’s model number (`MC319LL`, for example).|
|`ProductName`|String|The model code for the device (iPhone3,1, for example).|
|`SerialNumber`|String|The device’s serial number.|
|`DeviceCapacity`|Number|Floating-point gigabytes (base-1024 gigabytes).|
|`AvailableDeviceCapacity`|Number|Floating-point gigabytes (base-1024 gigabytes).|
|`BatteryLevel`|Number|Floating-point percentage expressed as a value between 0.0 and 1.0, or -1.0 if battery level cannot be determined.</br>**Availability:** Available in iOS 5.0 and later.|
|`CellularTechnology`|Number|Returns the type of cellular technology.<ul><li>`0`: none</li><li>`1`: GSM</li><li>`2`: CDMA</li><li>`3`: both</li></ul></br>**Availability: **Available in iOS 4.2.6 and later.|
|`IMEI`|String|The device’s IMEI number. Ignored if the device does not support GSM.</br>**Availability:** Not supported in macOS.|
|`MEID`|String|The device’s MEID number. Ignored if the device does not support CDMA.</br>**Availability:** Not supported in macOS.|
|`ModemFirmwareVersion`|String|The baseband firmware version.</br>**Availability:** Not supported in macOS.|
|`IsSupervised`|Boolean|If `true`, the device is supervised.</br>**Availability:** Available in iOS 6 and later.|
|`IsDeviceLocatorServiceEnabled`|Boolean|If `true`, the device has a device locator service (such as Find My iPhone) enabled.</br>**Availability:** Available in iOS 7 and later.|
|`IsActivationLockEnabled`|Boolean|If true, the device has Activation Lock enabled. **Availability:** Available in iOS 7 and later and macOS 10.9 and later.|
|`IsDoNotDisturbInEffect`|Boolean|If `true`, Do Not Disturb is in effect. This returns `true` whenever Do Not Disturb is turned on, even if the device is not currently locked.</br>**Availability:** Available in iOS 7 and later.|
|`DeviceID`|String|Device ID.</br>**Availability:** Available in Apple TV software 6.0 and later only.|
|`EASDeviceIdentifier`|String|The Device Identifier string reported to Exchange Active Sync (EAS).</br>**Availability:** Available in iOS 7 and later and macOS 10.9 and later.|
|`IsCloudBackupEnabled`|Boolean|If true, the device has iCloud backup enabled.</br>**Availability:** Available in iOS 7.1 and later.|
|`OSUpdateSettings`|Dictionary|Returns the OS Update settings (see [Table 8](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW25a)).</br>**Availability:** Available in macOS 10.11 and later.|
|`LocalHostName`|String|Returns the local host name as reported by Bonjour.</br>**Availability:** Available in macOS 10.11 and later.|
|`HostName`|String|Returns the host name.</br>**Availability:** Available in macOS 10.11 and later.|
|`SystemIntegrityProtectionEnabled`|Boolean|Whether System Integrity Protection is enabled on the device.</br>**Availability:** Available in macOS 10.12 and later.|
|`ActiveManagedUsers`|Array of strings|Returns an array of the directory GUIDs (as strings) of the logged-in managed users. This query can be sent only to a device.</br>An additional key, `CurrentConsoleManagedUser`, is sent in the reply; its string value is the GUID of the managed user active on the console. If no user listed in the `ActiveManagedUsers` array is currently active on the console, this additional key is omitted from the reply.</br>**Availability:** Available in macOS 10.11 and later.|
|`IsMDMLostModeEnabled`|Boolean|If true, the device has MDM Lost Mode enabled. Defaults to false.</br>**Availability:** Available in iOS 9.3 and later.|
|`MaximumResidentUsers`|Integer|Returns the maximum number of users that can use this Shared iPad mode device.</br>**Availability:** Available in iOS 9.3 and later.|
  


|Key|Type|Content|
|-|-|-|
|`CatalogURL`|String|The URL to the software update catalog currently in use by the client.|
|`IsDefaultCatalog`|Boolean|
|`PreviousScanDate`|Date|
|`PreviousScanResult`|String|
|`PerformPeriodicCheck`|Boolean|
|`AutomaticCheckEnabled`|Boolean|
|`BackgroundDownloadEnabled`|Boolean|
|`AutomaticAppInstallationEnabled`|Boolean|
|`AutomaticOSInstallationEnabled`|Boolean|
|`AutomaticSecurityUpdatesEnabled`|Boolean|
  

  

#### Network Information Queries Provide Hardware Addresses, Phone Number, and SIM Card and Cellular Network Info
  

The queries in  are available if the MDM host has a Network Information access right.  

> **Note:** Not all devices understand all queries. For example, queries specific to GSM (IMEI, SIM card queries, and so on) are ignored if the device is not GSM-capable. The macOS MDM client responds only to `BluetoothMAC`, `WiFiMAC`, and `EthernetMACs`.  
  


|Query|Reply Type|Comment|
|-|-|-|
|`ICCID`|String|The ICC identifier for the installed SIM card.|
|`BluetoothMAC`|String|Bluetooth MAC address.|
|`WiFiMAC`|String|Wi-Fi MAC address.|
|`EthernetMACs`|Array of strings|Ethernet MAC addresses.</br>**Availability:** Available in macOS v10.8 and later, and in iOS 7 and later.|
|`CurrentCarrierNetwork`|String|Name of the current carrier network.|
|`SIMCarrierNetwork`|String|Name of the home carrier network. (Note: this query *is* supported on CDMA in spite of its name.)|
|`SubscriberCarrierNetwork`|String|Name of the home carrier network. (Replaces `SIMCarrierNetwork`.)</br>**Availability:** Available in iOS 5.0 and later.|
|`CarrierSettingsVersion`|String|Version of the currently-installed carrier settings file.|
|`PhoneNumber`|String|Raw phone number without punctuation, including country code.|
|`VoiceRoamingEnabled`|Boolean|The current setting of the Voice Roaming setting. This is only available on certain carriers.</br>**Availability:** iOS 5.0 and later.|
|`DataRoamingEnabled`|Boolean|The current setting of the Data Roaming setting.|
|`IsRoaming`|Boolean|Returns whether the device is currently roaming.</br>**Availability: **Available in iOS 4.2 and later. See note below.|
|`PersonalHotspotEnabled`|Boolean|True if the Personal Hotspot feature is currently turned on. This value is available only with certain carriers.</br>**Availability:** iOS 7.0 and later.|
|`SubscriberMCC`|String|Home Mobile Country Code (numeric string).</br>**Availability: **Available in iOS 4.2.6 and later.|
|`SubscriberMNC`|String|Home Mobile Network Code (numeric string).</br>**Availability: **Available in iOS 4.2.6 and later.|
|`CurrentMCC`|String|Current Mobile Country Code (numeric string).|
|`CurrentMNC`|String|Current Mobile Network Code (numeric string).|
  

> **Note:** For older versions of iOS, if the `SIMMCC`/`SMMNC` combination does not match the `CurrentMCC`/`CurrentMNC` values, the device is probably roaming.  
  

  

### SecurityInfo Commands Request Security-Related Information
  

To send a `SecurityInfo` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`SecurityInfo`.|
  

Response:  


|Key|Type|Content|
|-|-|-|
|`SecurityInfo`|Dictionary|Response dictionary.|
  

In iOS only, the `SecurityInfo` dictionary contains the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`HardwareEncryptionCaps`|Integer|Bitfield. Describes the underlying hardware encryption capabilities of the device. Values are described in [Table 10](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW23).|
|`PasscodePresent`|Boolean|Set to `true` if the device is protected by a passcode.|
|`PasscodeCompliant`|Boolean|Set to `true` if the user’s passcode is compliant with all requirements on the device, including Exchange and other accounts.|
|`PasscodeCompliantWithProfiles`|Boolean|Set to `true` if the user’s passcode is compliant with requirements from profiles.|
|`PasscodeLockGracePeriodEnforced`|Integer|The current enforced value for the amount of time in seconds the device must be locked before unlock will require the device passcode.|
|`FDE_Enabled`|Boolean|Device channel only. Whether Full Disk Encryption (FDE) is enabled or not.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_HasPersonalRecoveryKey`|Boolean|Device channel only. If FDE has been enabled, returns whether a personal recovery key has been set.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_HasInstitutionalRecoveryKey`|Boolean|Device channel only. If FDE has been enabled, returns whether an institutional recovery key has been set.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_PersonalRecoveryKeyCMS`|Data|If FileVault Personal Recovery Key (PRK) escrow is enabled and a recovery key has been set up, this key will contain the PRK encrypted with the certificate from the `com.apple.security.FDERecoveryKeyEscrow` payload and wrapped as a CMS blob.</br>**Availability:** Available in macOS 10.13 and later.|
|`FDE_PersonalRecoveryKeyDeviceKey`|String|If FileVault PRK escrow is enabled and a recovery key has been set up, this key contains a short string that is displayed to the user in the EFI login window as part of the help message if the user enters an incorrect password three times. The server can use this string as an index when saving the device PRK. Currently, this string is the device serial number, which replaces the `recordNumber` that was returned by the server in the earlier escrow mechanism.</br>**Availability:** Available in macOS 10.13 and later.|
|`FirewallSettings`|Dictionary|(macOS 10.12 and later): the current Firewall settings. This information will be returned only when the command is sent to the device channel. The response is a dictionary with the following keys:<ul><li>`FirewallEnabled` (Boolean): Whether firewall is on or off.</li><li>`BlockAllIncoming` (Boolean): Whether all incoming connections are blocked.</li><li>`StealthMode` (Boolean): Whether stealth mode is enabled.</li><li>`Applications` (array of dictionaries): Blocking status for specific applications. Each dictionary contains these keys:</li><li></br><ul>   <li>`BundleID` (string) : identifies the application</li>   <li>`Allowed` (Boolean) : specifies whether or not incoming connections are allowed</li>   <li>`Name` (string) : descriptive name of the application for display purposes only (may be missing if no corresponding app is found on the client computer).</li></ul></li></ul>|
|`SystemIntegrityProtectionEnabled`|Boolean|Device channel only. Whether System Integrity Protection is enabled on the device. In macOS 10.11 or later, this information may also be retrieved using a `DeviceInformation` query.</br>**Availability:** Available in macOS 10.12 and later.|
|`FirmwarePasswordStatus`|Dictionary|State of EFI firmware password; see .</br>**Availability:** Available in macOS 10.13 and later.|
  

Hardware encryption capabilities are described using the logical OR of the values in . Bits set to `1` (one) indicate that the corresponding feature is present, enabled, or in effect.  


|Value|Feature|
|-|-|
|`1`|Block-level encryption.|
|`2`|File-level encryption.|
  

EFI firmware status is returned as a dictionary that contains the fields listed below.  


|Key|Value|Description|
|-|-|-|
|`PasswordExists`|`Boolean`|Whether an EFI firmware password is set or not.|
|`ChangePending`|`Boolean`|If `true`, a firmware password change is pending and the device requires rebooting; attempts to set, change, or delete the password will fail.|
|`AllowOroms`|`Boolean`|Whether or not option ROMs are enabled.|
  

For a device to be protected with Data Protection, `HardwareEncryptionCaps` must be `3`, and `PasscodePresent` must be `true`.  

> **Security Note:** Security queries are available only if the MDM host has a Security Query access right.  
  

  

### DeviceLock Command Locks the Device Immediately
  

The `DeviceLock` command is intended to lock lost devices remotely; it should not be used for other purposes. To send one, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DeviceLock`|
|`PIN`|String|The Find My Mac PIN. Must be 6 characters long.</br>**Availability:** Available in macOS 10.8 and later.|
|`Message`|String|Optional. If provided, this message is displayed on the lock screen and should contain the words “lost iPad.” Available in iOS 7 and later.|
|`PhoneNumber`|String|Optional. If provided, this phone number is displayed on the lock screen. Available in iOS 7 and later.|
  

> **Security Note:** This command requires both Device Lock and Passcode Removal access rights.  
  

If a passcode has been set on the device, the device is locked and the text and phone number passed with the `DeviceLock` command are displayed on the locked screen. The device returns a `Status` of `Acknowledged` and a `MessageResult` of `Success`. If a passcode has not been set on the device, the device is locked but the message and phone number are not displayed on the screen. The device returns a `Status` of `Acknowledged` and a `MessageResult` of `NoPasscodeSet`.  

  

### RestartDevice Commands Restart Devices
  

To send a `RestartDevice` command, the server sends the following key:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RestartDevice`|
  

This command is supervised only and requires the Device Lock access right. The device will restart immediately. Available in iOS 10.3 and later. Passcode-locked iOS devices do not rejoin Wi-Fi networks after restarting, so they may not be able to communicate with the server.  

  

### ShutDownDevice Commands Shut Down Devices
  

To send a `ShutDownDevice` command, the server sends the following key:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ShutDownDevice`|
  

This command is supervised only and requires the Device Lock access right. The device will shut down immediately. Available in iOS 10.3 and later.  

  

### ClearPasscode Commands Clear the Passcode for a Device
  

To send a `ClearPasscode` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ClearPasscode`|
|`UnlockToken`|Data|The `UnlockToken` value that the device provided in its [TokenUpdate](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/2-MDM_Check_In_Protocol/MDM_Check_In_Protocol..html#//apple_ref/doc/uid/TP40017387-CH4-SW1) check-in message.|
  

> **Security Note:** This command requires both Device Lock and Passcode Removal access rights.  
  

> **Note:** The macOS MDM client generates an `Error` response to the server.  
  

  

### EraseDevice Commands Remotely Erase a Device
  

Upon receiving this command, the device immediately erases itself. No warning is given to the user. This command is performed immediately even if the device is locked.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`EraseDevice`|
|`PIN`|String|The Find My Mac PIN. Must be 6 characters long.</br>**Availability:** Available in macOS 10.8 and later.|
  

The device attempts to send a response to the server, but unlike other commands, the response cannot be resent if initial transmission fails. Even if the acknowledgement did not make it to the server (due to network conditions), the device will still be erased.  

> **Security Note:** This command requires a Device Erase access right.  
  

  

### RequestMirroring and StopMirroring Control AirPlay Mirroring
  

In iOS 7 and later and in macOS 10.10 and later, the MDM server can send the `RequestMirroring` and `StopMirroring` commands to start and stop AirPlay mirroring.  

> **Note:** The `StopMirroring` command is supported in supervised mode only.  
  

To send a `RequestMirroring` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RequestMirroring`.|
|`DestinationName`|String|Optional. The name of the AirPlay mirroring destination. For Apple TV, this is the name of the Apple TV.|
|`DestinationDeviceID`|String|Optional. The device ID (hardware address) of the AirPlay mirroring destination, in the format "xx:xx:xx:xx:xx:xx". This field is not case sensitive.|
|`ScanTime`|String|Optional. Number of seconds to spend searching for the destination. The default is 30 seconds. This value must be in the range 10–300.|
|`Password`|String|Optional. The screen sharing password that the device should use when connecting to the destination.|
  

> **Note:** Either `DestinationName` or `DestinationDeviceID` must be provided. If both are provided, `DestinationDeviceID` is used.  
  

In response, the device provides a dictionary with the following key:  


|Key|Type|Content|
|-|-|-|
|`MirroringResult`|String|The result of this request. The returned value is one of:<ul><li>`Prompting`: The user is being prompted to share his or her screen.</li><li>`DestinationNotFound`: The destination cannot be reached by the device.</li><li>`Cancelled`: The request was cancelled.</li><li>`Unknown`: An unknown error occurred.</li></ul>|
  

To send a `StopMirroring` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`StopMirroring`.|
  

  

### Restrictions Commands Get a List of Installed Restrictions
  

This command allows the server to determine what restrictions are being enforced by each profile on the device, and the resulting set of restrictions from the combination of profiles.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`Restrictions`|
|`ProfileRestrictions`|Boolean|Optional. If `true`, the device reports restrictions enforced by each profile.|
  

The device responds with:  


|Key|Type|Content|
|-|-|-|
|`GlobalRestrictions`|Dictionary|A dictionary containing the global restrictions currently in effect.|
|`ProfileRestrictions`|Dictionary|A dictionary of dictionaries, containing the restrictions enforced by each profile. Only included if `ProfileRestrictions` is set to `true` in the command. The keys are the identifiers of the profiles.|
  

The `GlobalRestrictions` dictionary and each entry in the `ProfileRestrictionList` dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`restrictedBoolean`|Dictionary|A dictionary of boolean restrictions.|
|`restrictedValue`|Dictionary|A dictionary of numeric restrictions.|
|`intersection`|Dictionary|A dictionary of intersected restrictions.|
|`union`|Dictionary|A dictionary of unioned restrictions.|
  

The `restrictedBoolean` and `restrictedValue` dictionaries have the following keys:  


|Key|Type|Content|
|-|-|-|
|*restriction name*|Dictionary|Restriction parameters.|
  

The restriction names (keys) in the dictionary correspond to the keys in the Restriction and Passcode Policy payloads. For more information, see [Configuration Profile Key Reference](https://developer.apple.com/library/ios/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).  

Each entry in the dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|*restriction_name*|Dictionary|Restriction parameters.|
  

> **Security Note:** This command requires a Restrictions Query access right.  
> Per-profile restrictions queries require an Inspect Configuration Profiles access right.  
  

> **Note:** Restrictions commands are not supported on the macOS MDM client.  
  

The `intersection` and `union` dictionaries have the following keys:  


|Key|Type|Content|
|-|-|-|
|`value`|Bool or Integer|The value of the restriction.|
  

The restriction names (keys) in the dictionary correspond to the keys in the Restriction and Passcode Policy payloads.  

Each entry in the dictionary contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`values`|Array of strings|The values of the restriction.|
  

With intersected restrictions, new restrictions can only reduce the number of strings in the set. With unioned restrictions, new restrictions can add to the set.  

  

#### Clear Restrictions Password
  

The `ClearRestrictionsPassword` command allows the server to clear the restrictions password and restrictions set by the user on the device. Supervised only. **Availability:** Available in iOS 8 and later.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ClearRestrictionsPassword`.|
  

  

### Shared iPad User Commands Manage User Access
  

Three MDM Protocol commands—`UsersList`, `LogOutUser`, and `DeleteUser`—let the MDM server exercise control over the access of users to MDM devices in an educational environment. These commands are all available in iOS 9.3 and later and may be used only in Shared iPad mode.  

> **Note:** 
Enterprise apps are not supported on Shared iPads; only device-based apps installed under the Volume Purchase Program may be used.  
  

  

#### UserList
  

This command allows the server to query for a list of users that have active accounts on the current device.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`UserList`.|
  

The device replies with either an error response of code 12070 if the device cannot return a list of users, or the following response dictionary:  


|Key|Type|Content|
|-|-|-|
|`Users`|Array|Array of dictionaries containing information about active users.|
  

For iOS, each entry in the Users array contains the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`UserName`|String|The user name of the user.|
|`HasDataToSync`|Boolean|Whether the user has data that still needs to be synchronized to the cloud.|
|`DataQuota`|Integer|The data quota set for the user in bytes. This key is optional and may not be present if user quotas have been temporarily turned off by the system or are not enforced for the user. |
|`DataUsed`|Integer|The amount of data used by the user in bytes. This key is optional and may not be present if an error occurs while the system is trying to determine the information.|
|`IsLoggedIn`|Boolean|If `true`, the user is currently logged onto the device.|
  

For macOS 10.13 or later, each entry in the `Users` array contains the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`UserName`|String|The short name of the user.|
|`FullName`|String|The full name of the user.|
|`UID`|Integer|The user’s `UniqueID`.|
|`UserGUID`|String|The `GeneratedUID` for the user.|
|`MobileAccount`|Boolean|If `true`, the account is a mobile account.|
|`IsLoggedIn`|Boolean|If `true`, the user is currently logged onto the device.|
  

  

#### UnlockUserAccount
  

This command lets the server unlock a local user account that has been locked for too many failed password attempts. It requires the Device Lock and Passcode Removal Right and it may be sent only on the device channel.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`UnlockUserAccount`.|
|`UserName`|String|Required. The username of the local account, which may be any local account on the system (not just a user account that is managed by MDM).|
  

  

#### LogOutUser
  

This command allows the server to force the current user to log out.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`LogOutUser`.|
  

  

#### DeleteUser
  

This command allows the server to delete a user that has an active account on the device. With iOS it is available in Education Mode only; with macOS it requires DEP enrollment.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DeleteUser`.|
|`UserName`|String|Required. The user name of the user to delete.|
|`ForceDeletion`|Boolean|Optional. Whether the user should be deleted even if they have data that needs to be synced to the cloud. Defaults to false.|
  

With macOS and iOS, the status of the response to `DeleteUser` is either Acknowledged, or Error with code 12071 if the specified user does not exist, 12072 if the specified user is logged in, 12073 if the specified user has data to sync and `ForceDeletion` is false or not specified, or 12074 if the specified user could not be deleted. With macOS, 12074 is also returned if an attempt was made to delete the last admin user.  

  

### MDM Lost Mode Helps Lock and Locate Lost Devices
  

Three MDM Protocol commands—`EnableLostMode`, `DisableLostMode`, and `DeviceLocation`—let the MDM server help locate supervised devices when they are lost or stolen. A fourth command, `PlayLostModeSound`, plays a loud sound on the lost device. These commands may be used only in supervised mode. The first three commands are available in iOS 9.3 and later and the fourth in iOS 10.3.  

When a device is erased, Lost Mode is disabled. To re-enable Lost Mode on the device, the MDM server should store the device’s Lost Mode state before erasing it. If the device is enrolled again, the MDM server can then restore the correct Lost Mode state.  

When a device is in MDM Lost mode, invalid commands sent to it may return an Error with code 12078.  

  

#### EnableLostMode
  

This command allows the server to put the device in MDM lost mode, with a message, phone number, and footnote text. A message or phone number must be provided.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`EnableLostMode`.|
|`Message`|String|Required if `PhoneNumber` is not provided; otherwise optional. If provided, this message is displayed on the lock screen.|
|`PhoneNumber`|String|Required if `Message` is not provided; otherwise optional. If provided, this phone number is displayed on the lock screen.|
|`Footnote`|String|Optional. If provided, this footnote text is displayed in place of “Slide to Unlock.”|
  

The response status is either Acknowledged or it is Error with code 12066 if MDM Lost Mode could not be enabled.  

  

#### Play Lost Mode Sound
  

This command allows the server to tell the device to play a sound if it is in MDM Lost Mode. The sound will play until the device is either removed from Lost Mode or a user disables the sound at the device.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`PlayLostModeSound`.|
  

The response status is either Acknowledged, or Error with code 12067 if the device is not in MDM Lost Mode, or Error with code 12080 if the sound could not be played.  

  

#### DisableLostMode
  

This command allows the server to take the device out of MDM lost mode.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DisableLostMode`.|
  

The response status is either Acknowledged or it is Error with code 12069 if MDM Lost Mode could not be disabled.  

  

#### DeviceLocation
  

This command allows the server to ask the device to report its location if it is in MDM lost mode.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DeviceLocation`.|
  

The device replies with either an error response with code 12067 if the device is not in MDM Lost Mode, code 12068 if the location could not be determined, or the following response dictionary:  


|Key|Type|Content|
|-|-|-|
|`Latitude`|Double|The latitude of the device’s current location.|
|`Longitude`|Double|The longitude of the device’s current location.|
|`HorizontalAccuracy`|Double|The radius of uncertainty for the location, measured in meters. If negative, this value could not be determined.|
|`VerticalAccuracy`|Double|The accuracy of the altitude value in meters. If negative, this value could not be determined.|
|`Altitude`|Double|The altitude of the device’s current location. If negative, this value could not be determined.|
|`Speed`|Double|The instantaneous speed of the device in meters per second. If negative, this value could not be determined.|
|`Course`|Double|The direction in which the device is traveling. If negative, this value could not be determined.|
|`Timestamp`|String|The [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp for when this location was determined.|
  

  

### Managed Applications
  

Running iOS 5 and later, an MDM server can manage third-party applications from the App Store as well as custom in-house enterprise applications. The server can specify whether the app and its data are removed from the device when the MDM profile is removed. Additionally, the server can prevent managed app data from being backed up to iTunes and iCloud.  

In iOS 7 and later, an MDM server can provide a configuration dictionary to third-party apps and can read data from a feedback dictionary provided by third-party apps. See [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68) for details.  

On devices running iOS earlier than iOS 9, apps from the App Store cannot be installed on a user’s device if the App Store has been disabled. With iOS 9 and later, VPP apps can be installed even when the App Store is disabled (see [VPP App Assignment](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW1)).  

To install a managed app on an iOS device, the MDM server sends an installation command to the user’s device. Unless the device is supervised, the managed apps then require a user’s acceptance before they are installed.  

When a server requests the installation of a managed app from the App Store, if the app was not purchased using App Assignment (that is, if the original `InstallApplication` request’s `Options` dictionary contained a `PurchaseMethod` value of 0), the app “belongs” to the iTunes account that is used at the time the app is installed. Paid apps require the server to send in a Volume Purchasing Program (VPP) redemption code that purchases the app for the end user. For more information on VPP, go to [http://www.apple.com/business/vpp/](http://www.apple.com/business/vpp/).  

The macOS MDM client does not support managed applications. However, it does support the parts of the `InstallApplication`, `InstallMedia`, and `InviteToProgram` MDM commands related to VPP enrollment and installation.  

  

#### InstallApplication Commands Install a Third-Party Application
  

To send an `InstallApplication` command, the server sends a request containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstallApplication`.|
|`iTunesStoreID`|Number|The application’s iTunes Store ID.</br>For example, the numeric ID for Keynote is `361285480` as found in the App Store link [http://itunes.apple.com/us/app/keynote/id361285480?mt=8](http://itunes.apple.com/us/app/keynote/id361285480?mt=8).|
|`Identifier`|String|Optional. The application’s bundle identifier. Available in iOS 7 and later.|
|`Options`|Dictionary|Optional. App installation options. The available options are listed below. Available in iOS 7 and later.|
|`ManifestURL`|String|The `https` URL where the manifest of an enterprise application can be found.</br>Note: In iOS 7 and later, this URL and the URLs of any assets specified in the manifest must begin with `https`.|
|`ManagementFlags`|Integer|The bitwise OR of the following flags:</br>1: Remove app when MDM profile is removed.</br>4: Prevent backup of the app data.|
|Configuration|Dictionary|Optional. If provided, this contains the initial configuration dictionary for the managed app. For more information, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68).|
|Attributes|Dictionary|Optional. If provided, this dictionary contains the initial attributes for the app. For a list of allowed keys, see [ManagedApplicationAttributes Queries App Attributes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW69).|
|`ChangeManagementState`|String|Optional. Currently the only supported value is the following:</br>`Managed`: Take management of this app if the user has installed it already. Available in iOS 9 and later.|
  

If the application is not already installed and the `ChangeManagementState` is set to `Managed`, the app will be installed and managed.  If the application is installed unmanaged, the user will be prompted to allow management of the app on unsupervised devices and, if accepted, the application becomes managed.  

The request must contain exactly one of the following fields: `Identifier`, `iTunesStoreID`, or `ManifestURL` value.  

The options dictionary can contain the following keys:  


|Key|Type|Content|
|-|-|-|
|`NotManaged`|Boolean|If true, the app is queued for installation but is not managed. macOS app installation must set this value to `true`.|
|`PurchaseMethod`|Integer|One of the following:</br>0: Legacy Volume Purchase Program (iOS only)</br>1: Volume Purchase Program App Assignment|
  

  

##### iOS App Installation
  

Here is an example of an iOS `InstallApplication` command for a per-device VPP app that uses the `ChangeManagementState` option:  

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>ChangeManagementState</key>
   		<string>Managed</string>
   <key>ManagementFlags</key>
   		<integer>1</integer>
   <key>Options</key>
   	<dict>
   		<key>PurchaseMethod</key>
   		<integer>1</integer>
   	</dict>
   <key>RequestType</key>
   		<string>InstallApplication</string>
   <key>iTunesStoreID</key>
   		<integer>361309726</integer>
</dict>
</plist>
```  

If the request is accepted by the user, the device responds with an Acknowledged response and the following fields:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The app’s identifier (Bundle ID)|
|`State`|String|The app’s installation state. If the state is NeedsRedemption, the server needs to send a redemption code to complete the app installation. If it is PromptingForUpdate, the process is waiting for the user to approve an app update.|
  

If the app cannot be installed, the device responds with an Error status, with the following fields:  


|Key|Type|Content|
|-|-|-|
|`RejectionReason`|String|One of the following:<ul><li>`AppAlreadyInstalled`</li><li>`AppAlreadyQueued`</li><li>`NotSupported`</li><li>`CouldNotVerifyAppID`</li><li>`AppStoreDisabled`</li><li>`NotAnApp`</li><li>`PurchaseMethodNotSupported` (iOS 7 and later)</li></ul>|
  

  

##### macOS App Installation
  

macOS apps are installed through MDM as packages. Using `productbuild`, each package must be signed with an appropriate certificate (such as a TLS/SSL certificate with signing usage) and must be md5 hashed into 10 MB chunks. Only the package needs to be signed, not the app; Apple’s Gatekeeper doesn’t check apps installed through MDM.  

The command lines to install a macOS app package should look like this:  

```
$ sudo pkgbuild —component ~/Desktop/MyApp.app —install-location /Applications
 —sign myserver.myenterprise.com /tmp/myPackage.pkg
$ split -b 10485760 myPackage.pkg myPackage.pkg.
$ md5 -r myPackage.pkg.*
```  

The manifest file included in the foregoing installation should contain:  


* the (HTTP) path to the package 

* the (HTTP) path to the display icons 

* the md5 hash size (10 MB as defined by CommerceKit) 

* the md5 hash information 

* the size of the download (package) in bytes 

* a unique bundle identifier to identify the package 

* bundle identifiers describing the items inside the package 

* descriptive titles for display purposes 
  

The following lists a typical `Manifest.plist` file:  

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>items</key>
   <array>
   	<dict>
   		<key>assets</key>
   		<array>
   			<dict>
   				<key>kind</key>
   				<string>software-package</string>
   				<key>md5-size</key>
   				<integer>10485760</integer>
   				<key>md5s</key>
   				<array>
   					<string>d519a84e907a088f7e77381e8ce265e5</string>
   					<string>0c4ea856a1b18ea7e24124d41fad3cc1</string>
   					<string>5a6b17332bf258e77956ac0d7a69ff8a</string>
   				</array>
   				<key>url</key>
   				<string>http://myserver.myenterprise.com/MDM_Test/MyApp.pkg</string>
   			</dict>
   			<dict>
   				<key>kind</key>
   				<string>full-size-image</string>
   				<key>needs-shine</key>
   				<false/>
   				<key>url</key>
   				<string>http://myserver.myenterprise.com/MDM_Test/Server.png</string>
   			</dict>
   			<dict>
   				<key>kind</key>
   				<string>display-image</string>
   				<key>needs-shine</key>
   				<false/>
   				<key>url</key>
   				<string>http://myserver.myenterprise.com/MDM_Test/Server.png</string>
   			</dict>
   		</array>
   		<key>metadata</key>
   		<dict>
   			<key>bundle-identifier</key>
   			<string>com.myenterprise.MyAppPackage</string>
   			<key>bundle-version</key>
   			<string>1.0</string>
   			<key>items</key>
   			<array>
   				<dict>
   					<key>bundle-identifier</key>
   					<string>com.myenterprise.MyAppNotMAS</string>
   					<key>bundle-version</key>
   					<string>1.7.4</string>
   				</dict>
   			</array>
   			<key>kind</key>
   			<string>software</string>
   			<key>sizeInBytes</key>
   			<string>26613453</string>
   			<key>subtitle</key>
   			<string>My Enterprise</string>
   			<key>title</key>
   			<string>Example Enterprise Install</string>
   		</dict>
   	</dict>
   </array>
</dict>
</plist>
```  

  

#### ApplyRedemptionCode Commands Install Paid Applications via Redemption Code
  

If a redemption code is needed during app installation, the server can use the `ApplyRedemptionCode` command to complete the app installation:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ApplyRedemptionCode`.|
|`Identifier`|String|The App ID returned by the InstallApplication command.|
|`RedemptionCode`|String|The redemption code that applies to the app being installed.|
  

If the user accepts the request, an acknowledgement response is sent.  

> **Note:** It is an error to send a redemption for an app that doesn’t require a redemption code.  
  

  

#### ManagedApplicationList Commands Provide the Status of Managed Applications
  

The `ManageApplicationList` command allows the server to query the status of managed apps.  

> **Note:** Certain statuses are transient. Once they are reported to the server, the entries for the apps are removed from the next query.  
  

To send a `ManagedApplicationList` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ManagedApplicationList`.|
|`Identifiers`|Array|Optional. An array of app identifiers as strings. If provided, the response contains only the status of apps whose identifiers appear in this array. Available in iOS 7 and later.|
  

In response, the device sends a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`ManagedApplicationList`|Dictionary|A dictionary of managed apps.|
  

The keys of the `ManagedApplicationList` dictionary are the app identifiers for the managed apps. The corresponding values are dictionaries that contain the following keys:  


|Key|Type|Content|
|-|-|-|
|`Status`|String|The status of the managed app; see [Table 12](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW333) for possible values.|
|`ManagementFlags`|Integer|Management flags. (See InstallApplication command above for a list of flags.)|
|`UnusedRedemptionCode`|String|If the user has already purchased a paid app, the unused redemption code is reported here. This code can be used again to purchase the app for someone else. This code is reported only once.|
|HasConfiguration|Boolean|If `true`, the app has a server-provided configuration. For details, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68). Available in iOS 7 and later.|
|HasFeedback|Boolean|If `true`, the app has feedback for the server. For details, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68). Available in iOS 7 and later.|
|IsValidated|Boolean|If `true`, the app has validated as allowed to run and is able to run on the device. If an app is enterprise-distributed and is not validated, it will not run on the device until validated. Available in iOS 9.2 and later.|
  


|Value|Description|
|-|-|
|`NeedsRedemption`|The app is scheduled for installation but needs a redemption code to complete the transaction.|
|`Redeeming`|The device is redeeming the redemption code.|
|`Prompting`|The user is being prompted for app installation.|
|`PromptingForLogin`|The user is being prompted for App Store credentials.|
|`Installing`|The app is being installed.|
|`ValidatingPurchase`|An app purchase is being validated.|
|`Managed`|The app is installed and managed.|
|`ManagedButUninstalled`|The app is managed but has been removed by the user. When the app is installed again (even by the user), it will be managed once again.|
|`PromptingForUpdate`|The user is being prompted for an update.|
|`PromptingForUpdateLogin`|The user is being prompted for App Store credentials for an update.|
|`PromptingForManagement`|The user is being prompted to change an installed app to be managed.|
|`Updating`|The app is being updated.|
|`ValidatingUpdate`|An app update is being validated.|
|`Unknown`|The app state is unknown.|
|The following statuses are transient and are reported only once:|
|`UserInstalledApp`|The user has installed the app before managed app installation could take place.|
|`UserRejected`|The user rejected the offer to install the app.|
|`UpdateRejected`|The user rejected the offer to update the app.|
|`ManagementRejected`|The user rejected management of an already installed app.|
|`Failed`|The app installation has failed.|
  

  

#### RemoveApplication Commands Remove Installed Managed Applications
  

The RemoveApplication command is used to remove managed apps and their data from a device. Applications not installed by the server cannot be removed with this command. To send a `RemoveApplication` command, the server sends a dictionary containing the following commands:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RemoveApplication`.|
|`Identifier`|String|The application’s identifier.|
  

  

#### InviteToProgram Lets the Server Invite a User to Join a Volume Purchasing Program
  

In iOS 7 and later, this command allows a server to invite a user to join the Volume Purchase Program for per-user VPP app assignment. After this command issues an invitation, you can use the `iTunesStoreAccountIsActive` query to get the hash of the iTunes Store account currently logged in.  

To send an `InviteToProgram` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InviteToProgram`.|
|`ProgramID`|String|The program’s identifier. One of the following:<ul><li>`com.apple.cloudvpp`: Volume Purchase Program App Assignment</li></ul>|
|`InvitationURL`|String|An invitation URL provided by the program.|
  

In response, the device sends a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`InvitationResult`|String|One of the following:<ul><li>`Acknowledged`</li><li>`InvalidProgramID`</li><li>`InvalidInvitationURL`</li></ul>|
  

This command yields a `NotNow` status until the user exits Setup Assistant.  

  

#### ValidateApplications Verifies Application Provisioning Profiles
  

This command allows the server to force validation of the free developer and universal provisioning profiles associated with an enterprise app. **Availability:** Available in iOS 9.2 and later.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ValidateApplications`.|
|`Identifiers`|Array of Strings|Optional. An array of app identifiers. If provided, the enterprise apps whose identifiers appear in this array have their provisioning profiles validated. If not, only installed managed apps have their provisioning profiles validated.|
  

  

### Installed Books
  

Books obtained from the iBooks Store can be installed on a device. These books will be backed up, will sync to iTunes, and will remain after the MDM profile is removed. Books not obtained from the iBooks Store will not sync to iTunes and will be removed when the MDM profile is removed.  

Books obtained from the iBooks Store must be purchased using VPP Licensing. Installing a book from the iBooks Store on a device that already has that book installed causes the book to be visible to the MDM server.  

Installation of books requires the App Installation right. The App Store must be enabled for iBooks Store media installation to work. The App Store need not be enabled to install books retrieved using a URL.  

  

#### InstallMedia Installs a Book onto a Device
  

To send an `InstallMedia` command (in iOS 8 or later), the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstallMedia`.|
|`iTunesStoreID`|Integer|Optional. The media’s iTunes Store ID.|
|`MediaURL`|String|Optional; not supported in macOS. The URL from which the media will be retrieved.|
|`MediaType`|String|`Book`.|
  

The request must contain either an `iTunesStoreID` or a `MediaURL`.  

If a `MediaURL` is provided, the URL must lead to a PDF, gzipped epub, or gzipped iBooks document. The following fields are provided to define this document:  


|Key|Type|Content|
|-|-|-|
|`PersistentID`|String|Persistent ID in reverse-DNS form, e.g., `com.acme.manuals.training`.|
|`Kind`|String|Optional. The media kind. Must be one of the following:<ul><li>`pdf`: PDF file</li><li>`epub`: A gzipped epub</li><li>`ibooks`: A gzipped iBooks Author-exported book</li></ul></br>If this field is not provided, the file extension in the URL is used.|
|`Version`|String|Optional. A version string that is meaningful to the MDM server.|
|`Author`|String|Optional.|
|`Title`|String|Optional.|
  

Installing a book not from the iBooks Store with the same `PersistentID` as an existing book not from the iBooks Store replaces the old book with the new. Installing an iBooks Store book with the same `iTunesStoreID` as an existing installed book updates the book from the iBooks Store.  

The user is not prompted for book installation or update unless user interaction is needed to complete an iBooks Store transaction.  

If the request is accepted, the device responds with an Acknowledged response and the following fields:  


|Key|Type|Content|
|-|-|-|
|`iTunesStoreID`|Integer|The book’s iTunes Store ID, if it was provided in the command.|
|`MediaURL`|String|The book’s URL, if it was provided in the command.|
|`PersistentID`|String|Persistent ID, if it was provided in the command.|
|`MediaType`|String|The media type.|
|`State`|String|The installation state of this media. This value can be one of the following:<ul><li>`Queued`</li><li>`PromptingForLogin`</li><li>`Updating`</li><li>`Installing`</li><li>`Installed`</li><li>`Uninstalled`</li><li>`UserInstalled`</li><li>`Rejected`</li></ul></br>The following states are transient and are reported only once:<ul><li>`Failed`</li><li>`Unknown`</li></ul>|
  

If the book cannot be installed, an `Error` status is returned, which may contain an error chain. In addition, a `RejectionReason` field of type `String` is returned, containing one of these values:  


* `CouldNotVerifyITunesStoreID` 

* `PurchaseNotFound`: No VPP license found in the user’s history 

* `AppStoreDisabled` 

* `WrongMediaType` 

* `DownloadInvalid`: URL doesn’t lead to valid book 
  

  

#### ManagedMediaList Returns a List of Installed Media on a Device
  

To send a `ManagedMediaList` command, the server sends a dictionary containing the following key:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ManagedMediaList`.|
  

If the request is accepted, the device responds with an `Acknowledged` response and the following field:  


|Key|Type|Content|
|-|-|-|
|`Books`|Array|Array of dictionaries.|
  

Each entry in the `ManagedMedia` array is a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`iTunesStoreID`|Integer|The item’s iTunes Store ID, if the item was retrieved from the iTunes Store.|
|`State`|String|The installation state of this media. This value can be one of the following:<ul><li>`Queued`</li><li>`PromptingForLogin`</li><li>`Updating`</li><li>`Installing`</li><li>`Installed`</li><li>`Uninstalled`</li><li>`UserInstalled`</li><li>`Rejected`</li></ul>|
|`PersistentID`|String|Provided if available.|
|`Kind`|String|Provided if available.|
|`Version`|String|Provided if available.|
|`Author`|String|Provided if available.|
|`Title`|String|Provided if available.|
  

  

#### RemoveMedia Removes a Piece of Installed Media
  

This command allows an MDM server to remove installed media. This command returns `Acknowledged` if the item is not found.  

To send a `RemoveMedia` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RemoveMedia`.|
|`MediaType`|String|`Book`.|
|`iTunesStoreID`|Integer|Optional. iTunes Store ID.|
|`PersistentID`|String|
Optional. Persistent ID of the item to remove.|
  

Upon success, an `Acknowledged` status is returned. Otherwise, an error status is returned.  

  

### Managed Settings
  

In iOS 5 or later, this command allows the server to set settings on the device. These settings take effect on a one-time basis. The user may still be able to change the settings at a later time. This command requires the Apply Settings right.  

The macOS MDM client does not support managing settings.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`Settings`.|
|`Settings`|Array|Array of dictionaries. See below.|
  

Each entry in the `Settings` array must be a dictionary. The specific values in that dictionary are described in the documentation for the specific setting.  

Unless the command is invalid, the `Settings` command always returns an `Acknowledged` status. However, the response dictionary contains an additional key-value pair:  


|Key|Type|Content|
|-|-|-|
|`Settings`|Array|Array of results. See below.|
  

In the response, the `Settings` array contains a result dictionary that corresponds with each command that appeared in the original `Settings` array (in the request). These dictionaries contain the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`Status`|String|Status of the command.</br>Only `Acknowledged` and `Error` are reported.|
|`ErrorChain`|Array|Optional. An array representing the chain of errors that occurred.|
|`Identifier`|String|Optional. The app identifier to which this error applies.</br>**Availability:** Available in iOS 7 and later.|
  

Each entry in the `ErrorChain` array is a dictionary containing the same keys found in the top level `ErrorChain` dictionary of the protocol.  

  

#### VoiceRoaming Modifies the Voice Roaming Setting
  

To send a `VoiceRoaming` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`VoiceRoaming`.|
|Enabled|Boolean|If `true`, enables voice roaming.</br>If `false`, disables voice roaming.</br>The voice roaming setting is only available on certain carriers.</br>Disabling voice roaming also disables data roaming.|
  

  

#### PersonalHotspot Modifies the Personal Hotspot Setting
  

To send a `PersonalHotspot` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`PersonalHotspot`.|
|Enabled|Boolean|If `true`, enables Personal Hotspot.</br>If `false`, disables Personal Hotspot.</br>The Personal Hotspot setting is only available on certain carriers.|
  

> **Note:** This query requires the Network Information right.  
  

  

#### Wallpaper Sets the Wallpaper
  

A wallpaper change (in iOS 8 or later) is a one-time setting that can be changed by the user at will. This command is supported in supervised mode only.  

To send a `Wallpaper` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`Wallpaper`.|
|`Image`|Data|A Base64-encoded image to be used for the wallpaper. Images must be in either PNG or JPEG format.|
|`Where`|Number|Where the wallpaper should be applied.</br>1: Lock screen</br>2: Home (icon list) screen</br>3: Lock and Home screens|
  

  

#### DataRoaming Modifies the Data Roaming Setting
  

To send a `DataRoaming` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`DataRoaming`.|
|`Enabled`|Boolean|If `true`, enables data roaming.</br>If `false`, disables data roaming.</br>Enabling data roaming also enables voice roaming.|
  

  

#### ApplicationAttributes Sets or Updates the App Attributes for a Managed Application
  

To set or update the attributes for a managed application, send a `Settings` command with the following dictionary as an entry:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`ApplicationAttributes`.|
|`Identifier`|String|The app identifier.|
|`Attributes`|Dictionary|Optional. Attributes to be applied to the app. If this member is missing, any existing attributes for the app are removed.|
  

> **Note:** This setting requires the App Management right.  
  

The keys that can appear in the `Attributes` dictionary are listed below:  


|Key|Type|Content|
|-|-|-|
|`VPNUUID`|String|Per-App VPN UUID assigned to this app.|
  

  

#### DeviceName and HostName Set the Names of the Device
  

To send a `DeviceName` command (available only on supervised devices or devices running macOS v10.10 or later), the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`DeviceName`.|
|`DeviceName`|String|The requested computer name and local host name for the device.|
  

On macOS, the `DeviceName` command sets only the computer name and local host name of the device. To set the `HostName` of the device (available only on macOS 10.11 or later), the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`HostName`.|
|`HostName`|String|The requested `HostName` for the device.|
  

  

#### MDMOptions Sets Options Related to the MDM Protocol
  

To send an `MDMOptions` command (available only in iOS 7 and later), the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`MDMOptions`.|
|`MDMOptions`|Dictionary|A dictionary, as described below.|
  

The `MDMOptions` dictionary can contain the following keys:  


|Key|Type|Content|
|-|-|-|
|`ActivationLockAllowedWhileSupervised`|Boolean|Optional. If `true`, a supervised device registers itself with Activation Lock when the user enables Find My iPhone. Defaults to `false`. This setting is ignored on unsupervised devices.|
  

  

#### PasscodeLockGracePeriod Customizes the Passcode Lock on Shared iPads
  

The `PasscodeLockGracePeriod` command sets  the time the screen must be locked before needing a passcode to unlock it:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`PasscodeLockGracePeriod`.|
|`PasscodeLockGracePeriod`|Integer|The number of seconds the screen must be locked before unlock attempts will require the device passcode.|
  

This command is valid for Shared iPad only. Changing to a less restrictive value will not take effect until the user logs out. The command is available on iOS 9.3.2 and later.  

  

#### MaximumResidentUsers
  

Shared iPad Mode only. Sets the maximum number of users that can use a Shared iPad. This can be set only when the iPad is in the `AwaitingConfiguration` phase, before the `DeviceConfigured` message has been sent to the device. If `MaximumResidentUsers` is greater than the maximum possible number of users supported on the device, the device is configured with the maximum possible number of users instead.  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`MaximumResidentUsers`.|
|`MaximumResidentUsers`|Integer|The maximum number of users that can use a Shared iPad.|
  

**Availability: **Available in iOS 9.3 and later.  

  

### Managed App Configuration and Feedback
  

In iOS 7 and later, an MDM server can use configuration and feedback dictionaries to communicate with and configure third-party managed apps.  

**Important:** The managed app configuration and feedback dictionaries are stored as unencrypted files. Do not store passwords or private keys in these dictionaries.  

The configuration dictionary provides one-way communication from the MDM server to an app. An app can access its (read-only) configuration dictionary by reading the key `com.apple.configuration.managed` using the `NSUserDefaults` class. A managed app can respond to new configurations that arrive while the app is running by observing the `NSUserDefaultsDidChangeNotification` notification.  

A managed app can also store feedback information that can be queried over MDM. An app can store new values for this feedback dictionary by setting the `com.apple.feedback.managed` key using the `NSUserDefaults` class. This dictionary can be read or deleted over MDM. An app can respond to the deletion of the feedback dictionary by observing the `NSUserDefaultsDidChangeNotification` notification.  

  

#### ManagedApplicationConfiguration Retrieves Managed App Configurations
  

To send a `ManagedApplicationConfiguration` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ManagedApplicationConfiguration`.|
|`Identifiers`|Array|Array of managed bundle identifiers, as strings.|
  

> **Note:** The `ManagedApplicationConfiguration` command requires that the server have the App Management right.  
> Queries about apps that are not managed are ignored.  
  

In response, the device sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`ApplicationConfigurations`|Array|An array of dictionaries, one per app.|
  

Each member of the `ApplicationConfigurations` array is a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The application’s bundle identifier.|
|`Configuration`|Dictionary|Optional. The current configuration. If the app has no managed configuration, this key is absent.|
  

  

#### ApplicationConfiguration Sets or Updates the App Configuration for a Managed Application
  

In iOS 7 and later, to set or update the app configuration for a managed application, send a `Settings` command with the following dictionary as an entry:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`ApplicationConfiguration`.|
|`Identifier`|String|The application’s bundle identifier.|
|`Configuration`|Dictionary|Optional. Configuration dictionary to be applied to the app. If this member is missing, any existing managed configuration for the app is removed.|
  

> **Note:** This setting requires the App Management right.  
  

  

#### ManagedApplicationAttributes Queries App Attributes
  

In iOS 7 and later, attributes can be set on managed apps. These attributes can be changed over time.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ManagedApplicationAttributes`.|
|`Identifiers`|Array|Array of managed bundle identifiers, as strings.|
  

The device replies with a dictionary that contains the following keys:  


|Key|Type|Content|
|-|-|-|
|`ApplicationAttributes`|Array|Array of dictionaries.|
  

Each member of the `ApplicationAttributes` array is a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The application’s bundle identifier.|
|`Attributes`|Dictionary|Optional. The current attributes for the application.|
  

The keys that can appear in the `Attributes` dictionary are listed below:  


|Key|Type|Content|
|-|-|-|
|`VPNUUID`|String|Per-App VPN UUID assigned to this app.|
  

  

#### ManagedApplicationFeedback Retrieves Managed App Feedback
  

To send a `ManagedApplicationFeedback` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ManagedApplicationFeedback`.|
|`Identifiers`|Array|Array of managed bundle identifiers, as strings.|
|`DeleteFeedback`|Boolean|Optional. If `true`, the application’s feedback dictionary is deleted after it is read.|
  

> **Note:** The `ManagedApplicationFeedback` command requires that the server have the App Management right. Queries about apps that are not managed are ignored.  
  

In response, the device sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`ManagedApplicationFeedback`|Array|An array of dictionaries, one per app.|
  

Each member of the `ApplicationConfigurations` array is a dictionary with the following keys:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The application’s bundle identifier.|
|`Feedback`|Dictionary|Optional. The current feedback dictionary. If the app has no feedback dictionary, this key is absent.|
  

  

### AccountConfiguration
  

When a macOS (v10.11 and later) device is configured via DEP to enroll in an MDM server and the DEP profile has the `await_device_configuration` flag set to true, the `AccountConfiguration` command can be sent to the device to have it create the local administrator account (thereby skipping the page to create this account in Setup Assistant). This command can only be sent to a macOS device that is in the `AwaitingConfiguration` state.  

The `AccountConfiguration` command replaces the `SetupConfiguration` command, which is deprecated. While both commands remain supported, new software should use `AccountConfiguration`.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`AccountConfiguration`.|
|`SkipPrimarySetupAccountCreation`|Boolean|(Optional, default=false). If true, skip the UI for setting up the primary accounts. Setting this key to true requires that an entry be specified in `AutoSetupAdminAccounts`. Setting this value to true also prevents auto login after Setup Assistant completes.|
|`SetPrimarySetupAccountAsRegularUser`|Boolean|(Optional, default=false). If true, the primary accounts are created as regular users. Setting this to true requires that an entry be specified in `AutoSetupAdminAccounts`.|
|`AutoSetupAdminAccounts`|Array of Dictionaries|(Required if either of the above options are true) Describes the admin accounts to be created by Setup Assistant (see below). Currently, macOS creates only a single admin account. Array elements after the first are ignored.|
  

The `AutoSetupAdminAccounts` dictionaries contain the specifications of local administrator accounts to be created before Setup Assistant finishes:  


|Key|Type|Content|
|-|-|-|
|`shortName`|String|The short name of the user.|
|`fullName`|String|(Optional) string of full user name. This defaults to `shortName` if not specified.|
|`passwordHash`|Data|Contains the pre-created salted PBKDF2 SHA512 password hash for the account (see below).|
|`hidden`|Boolean|(Optional, default=false) If true, this sets the account attribute to make the account hidden to `loginwindow` and Users&Groups. OD attribute: `dsAttrTypeNative:IsHidden`.|
  

The `passwordHash` data objects should be created on the server using the CommonCrypto libraries or equivalent as a salted SHA512 PBKDF2 dictionary containing three items: `entropy` is the derived key from the password hash (an example is from `CCKeyDerivationPBKDF()`), `salt` is the 32 byte randomized salt (from `CCRandomCopyBytes()`), and `iterations` contains the number of iterations (from `CCCalibratePBKDF()`) using a minimum hash time of 100 milliseconds (or if not known, a number in the range 20,000 to 40,000 iterations). This dictionary of the three keys should be placed into an outer dictionary under the key `SALTED-SHA512-PBKDF2` and converted to binary data before being set into the configuration dictionary `passwordHash` key value.  

  

### Firmware (EFI) Password Management
  

Starting with macOS 10.13, two commands, `SetFirmwarePassword` and `VerifyFirmwarePassword`, let MDM manage firmware passwords.  

> **Note:** 
There is no way through software to clear an EFI password without knowing the current password. Therefore, if an EFI password is set before MDM can manage it, there is no way for MDM to change it unless the server provides a way of prompting an administrator to enter the current password.  
  

  

#### SetFirmwarePassword
  

This command changes or clears the firmware password for the device. It requires the Device Lock and Passcode Removal Right and may be sent only on the device channel.  

The request dictionary has these keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`SetFirmwarePassword`.|
|`CurrentPassword`|String|Required if the device currently has a firmware password set.|
|`NewPassword`|String|(Required) Pass an empty string to clear the firmware password|
|`AllowOroms`|Boolean|Pass `true` if option ROMs are to be enabled. Default is `false`.|
  

The response dictionary has this key:  


|Key|Type|Content|
|-|-|-|
|`PasswordChanged`|Boolean|Indicates success or failure. In case of failure, `ErrorChain` may provide additional error information.|
  

This command will force the firmware password mode to a value of `command`. It will prompt the user only if MDM is attempting to option+boot to a different volume.  

The characters in `NewPassword` must consist of low-ASCII printable characters (0x20 .. 0x7E) to ensure that all characters can be entered on the EFI login screen. This is a subset of the characters allowed in the EFI login window. However, since the exact allowed character set is not well-defined, the `SetFirmwarePassword` command is conservative in limiting the characters it allows.  

The device imust be restarted for the new firmware password to take effect. This command will fail and return an error in `ErrorChain` if the device has a firmware change pending; see `ChangePending` in [Table 11](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW423).  

This command will return an error if it is called again within 30 seconds after providing an incorrect password.  

  

#### VerifyFirmwarePassword
  

This command verifies the device’s firmware password. It may be sent only on the device channel.  

The request dictionary has these keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`VerifyFirmwarePassword`.|
|`Password`|String|(Required) The password to be verified.|
  

The response dictionary has this key:  


|Key|Type|Content|
|-|-|-|
|`PasswordVerified`|Boolean|Whether or not the provided password matches the firmware password set for the device.|
  

This command delays for 30 seconds so it won’t execute too often. If another request is received within that interval, this command will return `false` and set an error in `ErrorChain`.  

  

### SetAutoAdminPassword
  

`SetAutoAdminPassword` allows changing the password of a local admin account that was created by Setup Assistant during DEP enrollment via the `AccountConfiguration` command. It is available in macOS v10.11 and later.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`SetAutoAdminPassword`.|
|`GUID`|String|The Globally Unique Identifier of the local admin account for which the password is to be changed. If this string does not correspond to the GUID of an admin account created during DEP enrollment, the command returns an error.|
|`passwordHash`|Data|Contains the pre-created salted PBKDF2 SHA512 password hash for the account (see below).|
  

The `passwordHash` data objects should be created on the server using the CommonCrypto libraries or equivalent as a salted SHA512 PBKDF2 dictionary containing three items: `entropy` is the derived key from the password hash (an example is from `CCKeyDerivationPBKDF()`), `salt` is the 32 byte randomized salt (from `CCRandomCopyBytes()`), and `iterations` contains the number of iterations (from `CCCalibratePBKDF()`) using a minimum hash time of 100 milliseconds (or if not known, a number in the range 20,000 to 40,000 iterations). This dictionary of the three keys should be placed into an outer dictionary under the key `SALTED-SHA512-PBKDF2` and converted to binary data before being set into the configuration dictionary `passwordHash` key value.  

  

### DeviceConfigured
  

`DeviceConfigured` informs the device that it can continue past DEP enrollment. It works only on devices in DEP that have their cloud configuration set to await configuration.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`DeviceConfigured`.|
  

  

### Software Update
  

The Software Update commands allow an MDM server to perform software updates. In macOS, a variety of system software can be updated. In iOS, only OS updates are supported.  

> **Note:** 
If the device has a passcode, it must be cleared before an iOS update is performed.  
  

Only Supervised DEP-enrolled iOS devices and DEP-managed Mac computers are eligible for software update management. However, the `AvailableOSUpdates` query is available to non-DEP managed devices.  

The MDM server must have the App Installation right to perform these commands.  

  

#### ScheduleOSUpdate
  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ScheduleOSUpdate`.|
|Updates|Array|An array of dictionaries specifying the OS updates to download or install. If this entry is missing, the device applies the default behavior for all available updates.|
  

The Updates array contains dictionaries with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`ProductKey`|String|The product key of the update to be installed.|
|`InstallAction`|String|One of the following:<ul><li>`Default`: Download and/or install the software update, depending on the current device state. See the `UpdateResults` dictionary, below, to determine which `InstallAction` is scheduled.</li><li>`DownloadOnly`: Download the software update without installing it.</li><li>`InstallASAP`: Install an already downloaded software update.</li><li>`NotifyOnly`: Download the software update and notify the user via the App Store (macOS only).</li><li>`InstallLater`: Download the software update and install it at a later time (macOS only).</li></ul>|
  

The device returns the following response:  


|Key|Type|Content|
|-|-|-|
|`UpdateResults`|Array|Array of dictionaries.|
  

The `UpdateResults` dictionary contains the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`ProductKey`|String|The product key.|
|`InstallAction`|String|The install action that the device has scheduled for this update. One of the following:<ul><li>`Error`: An error occurred during scheduling.</li><li>`DownloadOnly`: Download the software update without installing it.</li><li>`InstallASAP`: Install an already downloaded software update.</li><li>`NotifyOnly`: Download the software update and notify the user via the App Store (macOS only).</li><li>`InstallLater`: Download the software update and install it at a later time (macOS only).</li></ul>|
|`Status`|String|The status of the software update. Possible values are:<ul><li>`Idle`: No action is being taken on this software update.</li><li>`Downloading`: The software update is being downloaded.</li><li>`DownloadFailed`: The download has failed.</li><li>`DownloadRequiresComputer`: The device must be connected to a computer to download this update (iOS only).</li><li>`DownloadInsufficientSpace`: There is not enough space to download the update.</li><li>`DownloadInsufficientPower`: There is not enough power to download the update.</li><li>`DownloadInsufficientNetwork`: There is insufficient network capacity to download the update.</li><li>`Installing`: The software update is being installed.</li><li>`InstallInsufficientSpace`: There is not enough space to install the update.</li><li>`InstallInsufficientPower`: There is not enough power to install the update.</li><li>`InstallPhoneCallInProgress`: Installation has been rejected because a phone call is in progress.</li><li>`InstallFailed`: Installation has failed for an unspecified reason.</li></ul>|
|`ErrorChain`|Array|Array of dictionaries describing the error that occurred.|
  

The device may return a different `InstallAction` than the one that was requested.  

> **Note:** 
In iOS versions before 10.3, responding to the `ScheduleOSUpdate` request relied on the device not being passcode-protected.  
  

Because software updates may happen immediately, the device may not have the opportunity to respond to an installation command before it restarts for installation. When this happens, the MDM server should resend the `ScheduleOSUpdate` request when the device checks in again. The device returns a status of `Idle` because the update has been installed and is no longer applicable.  

  

#### ScheduleOSUpdateScan
  

`ScheduleOSUpdateScan` requests that the device perform a background scan for OS updates.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ScheduleOSUpdateScan`.|
|`Force`|Boolean|If set to `true`, force a scan to start immediately. Otherwise, the scan occurs at a system-determined time. Defaults to `false`.|
  

The device returns the following response:  


|Key|Type|Content|
|-|-|-|
|`ScanInitiated`|Boolean|Returns true if the scan was successfully initiated (macOS only).
|
  

This command is needed by macOS only. iOS devices respond with an `Acknowledged` status on success.  

  

#### AvailableOSUpdates
  

`AvailableOSUpdates` queries the device for a list of available OS updates. In macOS, a `ScheduleOSUpdateScan` must be performed to update the results returned by this query.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`AvailableOSUpdates`.|
  

The device returns the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`AvailableOSUpdates`|Array|Array of dictionaries.|
  

Each element in the AvailableOSUpdates array contains a dictionary with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`ProductKey`|String|The product key that represents this update.|
|`HumanReadableName`|String|The human-readable name of the software update, in the current user’s current locale.|
|`ProductName`|String|The product name: e.g., iOS.|
|`Version`|String|The version of the update: e.g., 9.0.|
|`Build`|String|
The build number of the update: e.g., 13A999.|
|`DownloadSize`|Number|Storage size needed to download the software update. Floating point number of bytes.|
|`InstallSize`|Number|Storage size needed to install the software update. Floating point number of bytes.|
|`AppIdentifiersToClose`|Array|Array of strings. Each entry represents an app identifier that is closed to install this update (macOS only).|
|`IsCritical`|Boolean|Set to `true` if this update is considered critical. Defaults to `false`.|
|`IsConfigurationDataUpdate`|Boolean|Set to `true` if this is an update to a configuration file. Defaults to false (macOS only).|
|`IsFirmwareUpdate`|Boolean|Set to `true` if this is an update to firmware. Defaults to `false` (macOS only).|
|`RestartRequired`|Boolean|Set to `true` if the device restarts after this update is installed. Defaults to `false`.|
|`AllowsInstallLater`|Boolean|Set to `true` if the update is eligible for InstallLater. Defaults to `true`.|
  

A total of `DownloadSize + InstallSize` bytes is needed to successfully install a software update.  

  

#### OSUpdateStatus
  

`OSUpdateStatus` queries the device for the status of software updates.  


|Key|Type|Content|
|-|-|-|
|`RequestType 
`|String|`OSUpdateStatus`.|
  

The device responds with the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`OSUpdateStatus`.|Array|Array of dictionaries.|
  

Each entry in the `OSUpdateStatus` array is a dictionary with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`ProductKey`|String|The product key.|
|`IsDownloaded`|Boolean|Set to `true` if the update has been downloaded.|
|`DownloadPercentComplete`|Number|
Percentage of download that is complete. Floating point number (0.0 to 1.0).|
|`Status`|String|The status of this update. Possible values are:<ul><li>`Idle`: No action is being taken on this software update.</li><li>`Downloading`: The software update is being downloaded.</li><li>`Installing`: The software update is being installed. This status may not be returned if the device must reboot during installation.</li></ul>|
  

  

### Support for macOS Requests
  

The table below lists the MDM protocol request types that are available for Apple devices that run macOS. The interfaces of these requests to macOS are similar to the iOS interfaces described in the rest of this chapter.  


|Command|Min OS|User/Device|Comments|
|-|-|-|-|
|AccountConfiguration|10.11|Device|Valid only during DEP enrollment.|
|AvailableOSUpdates|10.11|Device|
|CertificateList|10.7|Both|
|DeviceConfigured|10.11|Both|Valid only during DEP enrollment.|
|DeviceInformation|10.7|Varies|See [DeviceInformation Commands Get Information About the Device](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW15).|
|DeviceLock|10.7|Device|
|EraseDevice|10.7|Device|
|InstallApplication|10.9|User|For VPP (`iTunesStoreID`, `Identifier`).|
|10.10|Device|`ManifestURL`.|
|10.11|Both|
|InstalledApplicationList|10.7|Both|
|InstallMedia|10.9|User|For VPP books only.|
|InstallProfile|10.7|Both|
|InviteToProgram|10.9|Both|
|OSUpdateStatus|10.11.5|Device|
|ProfileList|10.7|Both|
|ProvisioningProfileList|10.7|Both|Supported, but always returns empty list.|
|RemoveProfile|10.7|Both|
|RequestMirroring|10.10|Device|
|Restrictions|10.7|Both|Supported, but always returns empty list.|
|RotateFileVaultKey|10.9|Device|See [Using the RotateFileVaultKey Command](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW566).|
|ScheduleOSUpdate|10.11|Device|Requires DEP enrolled computer.|
|ScheduleOSUpdateScan|10.11|Device|
|SecurityInfo|10.7|Varies|See [SecurityInfo Commands Request Security-Related Information](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW19).|
|SetAutoAdminPassword|10.11|Device|
|Settings|10.9|varies|DeviceName (device), OrganizationInfo (device).|
|StopMirroring|10.10|Device|
  

  

#### Using the RotateFileVaultKey Command
  

Resetting a device deployment’s `FileVaultMaster.keychain` password periodically through Master Password rotation helps mitigate the risk of compromising the security of the deployed devices. For further information about this technique, see Apple’s *Best Practices for Deploying FileVault 2*, page 36, at [training.apple.com/pdf/WP_FileVault2.pdf](http://training.apple.com/pdf/WP_FileVault2.pdf).  

The `RotateFileVaultKey` command requires the access right “Device Lock and Passcode Removal” and is processed only if sent to the device channel. To send a `RotateFileVaultKey` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`RotateFileVaultKey`.|
|`KeyType`|String|Either `'personal'` or `'institutional'` (see below).|
|`FileVaultUnlock`|Dictionary|See below.|
|`NewCertificate`|Data|Required if `KeyType` is set to `institutional`. A DER-encoded certificate to be used in creating a new institutional recovery key. The certificate must have a common name containing “FileVault Recovery Key” and meet other requirements specified in Apple’s *Best Practices for Deploying FileVault 2* ([training.apple.com/pdf/WP_FileVault2.pdf](http://training.apple.com/pdf/WP_FileVault2.pdf)).|
|`ReplyEncryptionCertificate`|Data|Required if `KeyType` is set to `personal`. A DER-encoded certificate to be used in encrypting the new personal recovery key into a wrapper conforming to the IETF Cryptographic Message Syntax (CMS) standard.|
  

To unlock a device by means of a password, `KeyType` must be set to `personal` and the `FileVaultUnlock` dictionary must contain this key:  


|Key|Type|Content|
|-|-|-|
|`Password`|String|The current Personal Recovery Key (PRK) or a FileVault user’s password.|
  

To unlock a device using the institutional recovery key, `KeyType` must be set to `institutional` and the `FileVaultUnlock` dictionary must contain the following keys:  


|Key|Type|Content|
|-|-|-|
|`PrivateKeyExport`|Data|The data for a .p12 export of the private key for the current institutional recovery key.|
|`PrivateKeyExportPassword`|String|The password for the `PrivateKeyExport`.p12 data (see above).|
  

If the device is unlocked by means of a personal password, the response sent back to MDM server will be embedded within a `RotateResult` dictionary containing the following key:  


|Key|Type|Content|
|-|-|-|
|`EncryptedNewRecoveryKey`|Data|A new PRK that is encrypted using a `ReplyEncryptionCertificate` as a CMS-compliant envelope.|
  

If the device is unlocked using the institutional recovery key, no response will be needed and no dictionary will be sent.  
  

## Error Codes
  

The following sections list the error codes currently returned by iOS and macOS devices. Your software should *not* depend on these values, because they may change in future operating system releases. They are provided solely for informational purposes.  

  

### MCProfileErrorDomain 
  


| Code | Meaning |
|-|-|
| 1000 | Malformed profile |
| 1001 | Unsupported profile version |
| 1002 | Missing required field |
| 1003 | Bad data type in field |
| 1004 | Bad signature |
| 1005 | Empty profile |
| 1006 | Cannot decrypt |
| 1007 | Non-unique UUIDs |
| 1008 | Non-unique payload identifiers |
| 1009 | Profile installation failure |
| 1010 | Unsupported field value |
  

  

### MCPayloadErrorDomain 
  


| Code | Meaning |
|-|-|
| 2000 | Malformed payload |
| 2001 | Unsupported payload version |
| 2002 | Missing required field |
| 2003 | Bad data type in field |
| 2004 | Unsupported field value |
| 2005 | Internal Error |
  

  

### MCRestrictionsErrorDomain 
  


| Code | Meaning |
|-|-|
| 3000 | Inconsistent restriction sense (internal error) |
| 3001 | Inconsistent value comparison sense (internal error) |
  

  

### MCInstallationErrorDomain 
  


| Code | Meaning |
|-|-|
| 4000 | Cannot parse profile |
| 4001 | Installation failure |
| 4002 | Duplicate UUID |
| 4003 | Profile not queued for installation |
| 4004 | User cancelled installation |
| 4005 | Passcode does not comply |
| 4006 | Profile removal date is in the past |
| 4007 | Unrecognized file format |
| 4008 | Mismatched certificates |
| 4009 | Device locked |
| 4010 | Updated profile does not have the same identifier |
| 4011 | Final profile is not a configuration profile |
| 4012 | Profile is not updatable |
| 4013 | Update failed |
| 4014 | No device identity available |
| 4015 | Replacement profile does not contain an MDM payload |
| 4016 | Internal error |
| 4017 | Multiple global HTTPProxy payloads |
| 4018 | Multiple APN or Cellular payloads |
| 4019 | Multiple App Lock payloads
|
| 4020 | UI installation prohibited |
| 4021 | Profile must be installed non-interactively |
| 4022 | Profile must be installed using MDM |
| 4023 | Unacceptable payload |
| 4024 | Profile not found |
| 4025 | Invalid supervision
|
| 4026 | Removal date in the past |
| 4027 | Profile requires passcode change |
| 4028 | Multiple home screen layout payloads |
| 4029 | Multiple notification settings layout payloads |
| 4030 | Unacceptable payload in Shared iPad |
| 4031 | Payload contains sensitive user information |
  

  

### MCPasscodeErrorDomain 
  


| Code | Meaning |
|-|-|
| 5000 | Passcode too short |
| 5001 | Too few unique characters |
| 5002 | Too few complex characters |
| 5003 | Passcode has repeating characters |
| 5004 | Passcode has ascending descending characters |
| 5005 | Passcode requires number |
| 5006 | Passcode requires alpha characters |
| 5007 | Passcode expired |
| 5008 | Passcode too recent |
| 5009 | (unused) |
| 5010 | Device locked |
| 5011 | Wrong passcode |
| 5012 | (unused) |
| 5013 | Cannot clear passcode |
| 5014 | Cannot set passcode |
| 5015 | Cannot set grace period |
| 5016 | Cannot set fingerprint unlock |
| 5017 | Cannot set fingerprint purchase |
| 5018 | Cannot set maximum failed passcode attempts |
  

  

### MCKeychainErrorDomain 
  


| Code | Meaning |
|-|-|
| 6000 | Keychain system error |
| 6001 | Empty string |
| 6002 | Cannot create query |
  

  

### MCEmailErrorDomain 
  


| Code | Meaning |
|-|-|
| 7000 | Host unreachable |
| 7001 | Invalid credentials |
| 7002 | Unknown error occurred during validation |
| 7003 | SMIME certificate not found |
| 7004 | SMIME certificate is bad |
| 7005 | IMAP account is misconfigured |
| 7006 | POP account is misconfigured |
| 7007 | SMTP account is misconfigured |
  

  

### MCWebClipErrorDomain 
  


| Code | Meaning |
|-|-|
| 8000 | Cannot install Web Clip |
  

  

### MCCertificateErrorDomain 
  


| Code | Meaning |
|-|-|
| 9000 | Invalid password |
| 9001 | Too many certificates in a payload |
| 9002 | Cannot store certificate |
| 9003 | Cannot store WAPI data |
| 9004 | Cannot store root certificate |
| 9005 | Certificate is malformed |
| 9006 | Certificate is not an identity |
  

  

### MCDefaultsErrorDomain 
  


| Code | Meaning |
|-|-|
| 10000 | Cannot install defaults |
| 10001 | Invalid signer |
  

  

### MCAPNErrorDomain 
  


| Code | Meaning |
|-|-|
| 11000 | Cannot install APN |
| 11000 | Custom APN already installed |
  

  

### MCMDMErrorDomain 
  


| Code | Meaning |
|-|-|
| 12000 | Invalid access rights |
| 12001 | Multiple MDM instances |
| 12002 | Cannot check in |
| 12003 | Invalid challenge response |
| 12004 | Invalid push certificate |
| 12005 | Cannot find certificate |
| 12006 | Redirect refused |
| 12007 | Not authorized |
| 12008 | Malformed request |
| 12009 | Invalid replacement profile |
| 12010 | Internal inconsistency error |
| 12011 | Invalid MDM configuration |
| 12012 | MDM replacement mismatch |
| 12013 | Profile not managed |
| 12014 | Provisioning profile not managed |
| 12015 | Cannot get push token |
| 12016 | Missing identity |
| 12017 | Cannot create escrow keybag |
| 12018 | Cannot copy escrow keybag data |
| 12019 | Cannot copy escrow secret |
| 12020 | Unauthorized by server |
| 12021 | Invalid request type |
| 12022 | Invalid topic |
| 12023 | The iTunes Store ID of the application could not be validated |
| 12024 | Could not validate app manifest |
| 12025 | App already installed |
| 12026 | License for app “<app bundle ID>” could not be found |
| 12027 | Not an app |
| 12028 | Not waiting for redemption |
| 12029 | App not managed |
| 12030 | Invalid URL |
| 12031 | App installation disabled |
| 12032 | Too many apps in manifest |
| 12033 | Invalid manifest |
| 12034 | URL is not HTTPS |
| 12035 | App cannot be purchased |
| 12036 | Cannot remove app in current state |
| 12037 | Invalid redemption code |
| 12038 | App not managed |
| 12039 | (unused) |
| 12040 | iTunes Store login required |
| 12041 | Unknown language code |
| 12042 | Unknown locale code |
| 12043 | Media download failure |
| 12044 | Invalid media type |
| 12045 | Invalid media replacement type |
| 12046 | Cannot validate media ID |
| 12047 | Cannot find VPP assignment |
| 12048 | No update available |
| 12049 | Device passcode must be cleared |
| 12050 | Update scan failed |
| 12051 | Update download in progress |
| 12052 | Update download complete |
| 12053 | Update download requires computer |
| 12054 | Insufficient space for update download |
| 12055 | Insufficient power for update download |
| 12056 | Insufficient network for update download |
| 12057 | Update download failed |
| 12058 | Update install in progress |
| 12059 | Update install requires download |
| 12060 | Insufficient space for update install |
| 12061 | Insufficient power for update install |
| 12062 | Update install failed |
| 12063 | User rejected |
| 12064 | License not found |
| 12065 | System app |
| 12066 | Could not enable MDM lost mode |
| 12067 | Device not in MDM lost mode |
| 12068 | Could not determine device location |
| 12069 | Could not disable MDM lost mode |
| 12070 | Cannot list users |
| 12071 | Specified user does not exist |
| 12072 | Specified user is logged in |
| 12073 | Specified user has data to sync |
| 12074 | Could not delete user |
| 12075 | Specified profile not installed |
| 12076 | Per-user connections not supported |
| 12077 | System update not permitted with logged-in user |
| 12078 | Invalid request type in MDM Lost mode |
| 12079 | No MDM instance |
| 12080 | Could not play Lost Mode sound |
| 12081 | Not netwok tethered |
  

  

### MCWiFiErrorDomain 
  


| Code | Meaning |
|-|-|
| 13000 | Cannot install |
| 13001 | Username required |
| 13002 | Password required |
| 13003 | Cannot create Wi-Fi configuration |
| 13004 | Cannot set up EAP |
| 13005 | Cannot set up proxy |
  

  

### MCTunnelErrorDomain 
  


| Code | Meaning |
|-|-|
| 14000 | Invalid field |
| 14001 | Device locked |
| 14002 | Cloud configuration already exists |
  

  

### MCVPNErrorDomain 
  


| Code | Meaning |
|-|-|
| 15000 | Cannot install VPN |
| 15001 | Cannot remove VPN |
| 15002 | Cannot lock network configuration |
| 15003 | Invalid certificate |
| 15004 | Internal error |
| 15005 | Cannot parse VPN payload |
  

  

### MCSubCalErrorDomain 
  


| Code | Meaning |
|-|-|
| 16000 | Cannot create subscription |
| 16001 | No host name |
| 16002 | Account not unique |
  

  

### MCCalDAVErrorDomain 
  


| Code | Meaning |
|-|-|
| 17000 | Cannot create account |
| 17001 | No host name |
| 17002 | Account not unique |
  

  

### MCDAErrorDomain 
  


| Code | Meaning |
|-|-|
| 18000 | Unknown error |
| 18001 | Host unreachable |
| 18002 | Invalid credentials |
  

  

### MCLDAPErrorDomain 
  


| Code | Meaning |
|-|-|
| 19000 | Cannot create account |
| 19001 | No host name |
| 19002 | Account not unique |
  

  

### MCCardDAVErrorDomain 
  


| Code | Meaning |
|-|-|
| 20000 | Cannot create account |
| 20001 | No host name |
| 20002 | Account not unique |
  

  

### MCEASErrorDomain 
  


| Code | Meaning |
|-|-|
| 21000 | Cannot get policy from server |
| 21001 | Cannot comply with policy from server |
| 21002 | Cannot comply with encryption policy from server |
| 21003 | No host name |
| 21004 | Cannot create account |
| 21005 | Account not unique |
| 21006 | Cannot decrypt certificate |
| 21007 | Cannot verify account |
  

  

### MCSCEPErrorDomain 
  


| Code | Meaning |
|-|-|
| 22000 | Invalid key usage |
| 22001 | Cannot generate key pair |
| 22002 | Invalid CAResponse |
| 22003 | Invalid RAResponse |
| 22004 | Unsupported certificate configuration |
| 22005 | Network error |
| 22006 | Insufficient CACaps |
| 22007 | Invalid signed certificate |
| 22008 | Cannot create identity |
| 22009 | Cannot create temporary identity |
| 22010 | Cannot store temporary identity |
| 22011 | Cannot generate CSR |
| 22012 | Cannot store CACertificate |
| 22013 | Invalid PKIOperation response |
  

  

### MCHTTPTransactionErrorDomain 
  


| Code | Meaning |
|-|-|
| 23000 | Bad identity |
| 23001 | Bad server response |
| 23002 | Invalid server certificate |
  

  

### MCOTAProfilesErrorDomain 
  


| Code | Meaning |
|-|-|
| 24000 | Cannot create attribute dictionary |
| 24001 | Cannot sign attribute dictionary |
| 24002 | Bad identity payload |
| 24003 | Bad final profile |
  

  

### MCProvisioningProfileErrorDomain 
  


| Code | Meaning |
|-|-|
| 25000 | Bad profile |
| 25001 | Cannot install |
| 25002 | Cannot remove |
  

  

### MCDeviceCapabilitiesErrorDomain 
  


| Code | Meaning |
|-|-|
| 26000 | Block level encryption unsupported |
| 26001 | File level encryption unsupported |
  

  

### MCSettingsErrorDomain 
  


| Code | Meaning |
|-|-|
| 28000 | Unknown item |
| 28001 | Bad wallpaper image |
| 28002 | Cannot set wallpaper |
  

  

### MCChaperoneErrorDomain 
  


| Code | Meaning |
|-|-|
| 29000 | Device not supervised |
| 29003 | Bad certificate data |
  

  

### MCStoreErrorDomain 
  


| Code | Meaning |
|-|-|
| 30000 | Authentication failed |
| 30001 | Timed out |
  

  

### MCGlobalHTTPProxyErrorDomain 
  


| Code | Meaning |
|-|-|
| 31000 | Cannot apply credential |
| 31001 | Cannot apply settings |
  

  

### MCSingleAppErrorDomain 
  


| Code | Meaning |
|-|-|
| 32000 | Too many apps |
  

  

### MCSSOErrorDomain 
  


| Code | Meaning |
|-|-|
| 34000 | Invalid app identifier match pattern |
| 34001 | Invalid URL match pattern |
| 34002 | Kerberos principal name missing |
| 34003 | Kerberos principal name invalid |
| 34004 | Kerberos identity certificate cannot be found |
  

  

### MCFontErrorDomain 
  


| Code | Meaning |
|-|-|
| 35000 | Invalid font data |
| 35001 | Failed font installation |
| 35002 | Multiple fonts in a single payload |
  

  

### MCCellularErrorDomain 
  


| Code | Meaning |
|-|-|
| 36000 | Cellular already configured |
| 36001 | Internal error |
  

  

### MCKeybagErrorDomain 
  


| Code | Meaning |
|-|-|
| 37000 | Internal error |
| 37001 | Internal error |
  

  

### MCDomainsErrorDomain 
  


| Code | Meaning |
|-|-|
| 38000 | Invalid domain matching pattern |
  

  

### MCWebContentFilterErrorDomain 
  


| Code | Meaning |
|-|-|
| 40000 | Internal error |
| 40001 | Invalid certificate |
  

  

### MCNetworkUsageRulesErrorDomain
  


| Code | Meaning |
|-|-|
| 41000 | Internal error |
| 41001 | Invalid configuration |
| 41002 | Internal error |
  

  

### MCOSXServerErrorDomain
  


| Code | Meaning |
|-|-|
| 42000 | Cannot create account |
| 42001 | No hostname |
| 42002 | Account not unique |
  

  

### MCHomeScreenLayoutErrorDomain
  


| Code | Meaning |
|-|-|
| 43000 | Multiple Home screen layouts |
  

  

### MCNotificationSettingsErrorDomain
  


| Code | Meaning |
|-|-|
| 44000 | Multiple notification settings |
  

  

### MCEDUClassroomErrorDomain
  


| Code | Meaning |
|-|-|
| 45000 | Cannot install |
| 45001 | Student already installed |
| 45002 | Cannot find certificate |
| 45003 | Bad identity certificate |
  

  

### MCSharedDeviceConfigurationErrorDomain
  


| Code | Meaning |
|-|-|
| 46000 | Multiple shared device configurations |
  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/2-MDM_Check_In_Protocol/MDM_Check_In_Protocol..html)

  



