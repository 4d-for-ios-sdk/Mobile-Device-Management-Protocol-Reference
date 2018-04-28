# MDM Protocol Extensions

 [Configuration Profile Reference - MDM Protocol Extensions](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW62)  
  

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