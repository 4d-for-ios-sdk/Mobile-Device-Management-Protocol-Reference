# MDM Best Practices

 [Configuration Profile Reference - MDM Best Practices](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html)  
  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html)
  
Although there are many ways to deploy mobile device management, the techniques and policies described in this chapter make it easier to deploy MDM in a sensible and secure fashion.  
  

## Tips for Specific Profile Types
  

Although you can include any amount of information in your initial profile, it is easier to manage profiles if your base profile provides little beyond the MDM payload. You can always add additional restrictions and capabilities in separate payloads.  

  

### Initial Profiles Should Contain Only the Basics
  

The initial profile deployed to a device should contain only the following payloads:  


* Any root certificates needed to establish SSL trust. 

* Any intermediate certificates needed to establish SSL trust. 

* A client identity certificate for use by the MDM payload (either a PKCS#12 container, or an SCEP payload). An SCEP payload is recommended. 

* The MDM payload. 
  

Once the initial profile is installed, your server can push additional managed profiles to the device.  

In a single-user environment in macOS, installing an MDM profile causes the device to be managed by MDM (via device profiles) and the user that installed the profile (via user profiles), but any other local user logging into that machine will not be managed (other than via device profiles).  

Multiple network users bound to Open Directory servers can also have their devices managed, assuming the MDM server is configured to recognize them.  

  

### Managed Profiles Should Pair Restrictions with Capabilities
  

Configure each managed profile with a related pair of restrictions and capabilities (the proverbial carrots and sticks) so that the user gets specific benefits (access to an account, for instance) in exchange for accepting the associated restrictions.  

For example, your IT policy may require a device to have a 6-character passcode (stick) in order to access your corporate VPN service (carrot). You can do this in two ways:  


* Deliver a single managed profile with both a passcode restriction payload and a VPN payload. 

* Deliver a locked profile with a passcode restriction, optionally poll the device until it indicates compliance, and then deliver the VPN payload. 
  

Either technique ensures that the user cannot remove the passcode length restriction without losing access to the VPN service.  

  

### Each Managed Profile Should Be Tied to a Single Account
  

Do not group multiple accounts together into a single profile. Having a separate profile for each account makes it easier to replace and repair each account’s settings independently, add and delete accounts as access needs change, and so on.  

This advantage becomes more apparent when your organization uses certificate-based account credentials. As client certificates expire, you can replace those credentials one account at a time. Because each profile contains a single account, you can replace the credentials for that account without needing to replace the credentials for every account.  

Similarly, if a user requests a password change on an account, your servers could update the password on the device. If multiple accounts are grouped together, this would not be possible unless the servers keep an unencrypted copy of all of the user’s other account passwords (which is dangerous).  
  

## Provisioning Profiles Can Be Installed Using MDM
  

Third-party enterprise applications require provisioning profiles in order to run them. You can use MDM to deliver up-to-date versions of these profiles so that users do not have to manually install these profiles, replace profiles as they expire, and so on.  

To do this, deliver the provisioning profiles through MDM instead of distributing them through your corporate web portal or bundled with the application.  

> **Security Note:** Although an MDM server can remove provisioning profiles, you should not depend on this mechanism to revoke access to your enterprise applications for two reasons:  
> 
* An application continues to be usable until the next device reboot even if you remove the provisioning profile. 

* Provisioning profiles are synchronized with iTunes. Thus, they may get reinstalled the next time the user syncs the device. 
  
> An application continues to be usable until the next device reboot even if you remove the provisioning profile.  
> Provisioning profiles are synchronized with iTunes. Thus, they may get reinstalled the next time the user syncs the device.  
  
  

## Passcode Policy Compliance
  

Because an MDM server may push a profile containing a passcode policy without user interaction, it is possible that a user’s passcode must be changed to comply with a more stringent policy. When this situation arises, a 60-minute countdown begins. During this grace period, the user is prompted to change the passcode when returning to the Home screen, but can dismiss the prompt and continue working. After the 60-minute grace period, the user must change the passcode in order to launch any application on the device, including built-in applications.  

An MDM server can check to see if a user has complied with all passcode restrictions using the `SecurityInfo` command. An MDM server can wait until the user has complied with passcode restrictions before pushing other profiles to the device.  
  

## Deployment Scenarios
  

There are several ways to deploy an MDM payload. Which scenario is best depends on the size of your organization, whether an existing device management system is in place, and what your IT policies are.  

Here are some general best practices:  


* It is best practice to register VPP users and assign apps/books to those users before sending invitations to the users. This makes each assignment faster because it does not need to put the item in the user’s purchases at the time of assignment. Also, because an invitation acceptance will likely occur well before an MDM InstallApplication command is issued, the odds are higher that all licenses will have long since propagated to the user’s iTunes Store purchase history on the user’s clients, which is a necessary step for the `InstallApplication` command to succeed. 

* It is best practice to invite an individual user to each VPP organization only once. By checking the `itsIdHash`, MDM servers can detect when a single Apple ID accepts multiple invitations. Attempting to assign licenses for the same item to multiple VPP users with the same `itsIdHash` results in an “Already Assigned” error (code 9616). 

* It is best practice to provide a helpful error message when receiving error 403, T_C_NOT_SIGNED, such as “Terms and Conditions must be accepted. Please log into the Device Enrollment Program to accept the new Terms and Conditions on behalf of your organization.” 
  

  

### OTA Profile Enrollment
  

You may use over-the air enrollment (described in [Over-the-Air Profile Delivery and Configuration](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505)) to deliver a profile to a device. This option allows your servers to validate a user’s login, query for more information about the device, and validate the device’s built-in certificate before delivering a profile containing an MDM payload.  

When a profile is installed through over-the air enrollment, it is also eligible for updates. In iOS 7 and later, profiles can be updated even after expiration, as described in [Updating Expired Profiles](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW12). In older versions of iOS, when a certificate in the profile is about to expire, an “Update” button appears that allows the user to fetch a more recent copy of the profile using his or her existing credentials.  

This approach is recommended for most organizations because it is scalable.  

  

### Device Enrollment Program
  

The Device Enrollment Program, when combined with an MDM server, makes it easier to deploy configuration profiles over the air to devices that you own. When performed at the time of purchase, devices enrolled in this program can prompt the user to begin the MDM enrollment process as soon as the device is first activated, removing the need for preconfiguring each device.  

The Device Enrollment Program allows devices to be supervised during activation. Supervised devices allow an MDM server to apply additional restrictions and to send certain configuration commands that you otherwise cannot send, such as setting the device’s language and locale, starting and stopping AirPlay Mirroring, and so on. Also, MDM profiles delivered using the Device Enrollment Program cannot be removed by the user.  

MDM vendors can take advantage of web services provided by the Device Enrollment Program, integrating its features with their services.  

  

### Vendor-Specific Installation
  

Third-party vendors may install the MDM profile in a variety of other ways that are integrated with their management systems.  
  

## SSL Certificate Trust
  

MDM only connects to servers that have valid SSL certificates. If your server’s SSL certificate is rooted in your organization’s root certificate, the device must trust the root certificate before MDM will connect to your server.  

You may include the root certificate and any intermediate certificates in the same profile that contains the MDM payload. Certificate payloads are installed before the MDM payload.  

You can also install a `trust_profile_url`, as described in [Adding MDMServiceConfig Functionality](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW101).  

Your MDM server should replace the profile that contains the MDM payload well before any of the certificates in that profile expire. Remember: If any certificate in the SSL trust chain expires, the device cannot connect to the server to receive its commands. When this occurs, you lose the ability to manage the device.  
  

## Distributing Client Identities
  

Each device must have a unique client identity certificate. You may deliver these certificates as PKCS#12 containers or via SCEP. Using SCEP is recommended because the protocol ensures that the private key for the identity exists only on the device.  

Consult your organization’s Public Key Infrastructure policy to determine which method is appropriate for your installation.  
  

## Identifying Devices
  

An MDM server should identify a connecting device by examining the device’s client identity certificate. The server should then cross-check the UDID reported in the message to ensure that the UDID is associated with the certificate.  

The device’s client identity certificate is used to establish the SSL/TLS connection to the MDM server. If your server sits behind a proxy that strips away (or does not ask for) the client certificate, read [Passing the Client Identity Through Proxies](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW1).  
  

## Passing the Client Identity Through Proxies
  

If your MDM server is behind an HTTPS proxy that does not convey client certificates, MDM provides a way to tunnel the client identity in an additional HTTP header.  

If the value of the `SignMessage` field in the MDM payload is set to true, each message coming from the device carries an additional HTTP header named `Mdm-Signature`. This header contains a BASE64-encoded CMS Detached Signature of the message.  

Your server can validate the body with the detached signature in the `SignMessage` header. If the validation is successful, your server can assume that the message came from the signer, whose certificate is stored in the signature.  

Keep in mind that this option consumes a lot of data relative to the typical message body size. The signature is sent with every message, adding almost 2 KB of data to each outgoing message from the device. Use this option only if necessary.  
  

## Detecting Inactive Devices
  

To be notified when a device becomes inactive, set the `CheckOutWhenRemoved` key to `true` in the MDM payload. Doing so causes the device to contact your server when it ceases to be managed. However, because a managed device makes only a single attempt to deliver this message, you should also employ a timeout to detect devices that fail to check out due to network conditions.  

To do this, your server should send a push notification periodically to ensure that managed devices are still listening to your push notifications. If the device fails to respond to push notifications after some time, the device can be considered inactive. A device can become inactive for several reasons:  


* The MDM profile is no longer installed. 

* The device has been erased. 

* The device has been disconnected from the network. 

* The device has been turned off. 
  

> **Note:** 
Your security report on each managed device should specify whether or not MDM is set to be non-removable. This information is returned by the profile query, as described in [Define Profile](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW30).  
  

The time that your server should wait before deciding that a device is inactive can be varied according to your IT policy, but a time period of several days to a week is recommended. While it’s harmless to send push notifications once a day or so to make sure the device is responding, it is not necessary. Apple’s push notification servers cache your last push notification and deliver it to the device when it comes back on the network.  

When a device becomes inactive, your server may take appropriate action, such as limiting the device’s access to your organization’s resources until the device starts responding to push notifications once more.  
  

## Using the Feedback Service
  

Your server should regularly poll the Apple Push Notification Feedback Service to detect if a device’s push token has become invalid. When a device token is reported invalid, your server should consider the device to be no longer managed and should stop sending push notifications or commands to the device. If needed, you may also take appropriate action to restrict the device’s access to your organization’s resources.  

The Feedback service should be considered unreliable for detecting device inactivity, because you may not receive feedback in certain cases. Your server should use timeouts as the primary means of determining device management status.  
  

## Dequeueing Commands
  

Your server should not consider a command accepted and executed by the device until you receive the `Acknowledged` or `Error` status with the command UUID in the message. In other words, your server should leave the last command on the queue until you receive the status for that command.  

It is possible for the device to send the same status twice. You should examine the `CommandUUID` field in the device’s status message to determine which command it applies to.  
  

## Terminating a Management Relationship
  

You can terminate a management relationship with a device by performing one of these actions:  


* Remove the profile that contains the MDM payload. An MDM server can always remove this profile, even if it does not have the access rights to add or remove configuration profiles. 

* Respond to any device request with a `401 Unauthorized` HTTP status. The device automatically removes the profile containing the MDM payload upon receiving a `401` status code. 
  
  

## Updating Expired Profiles
  

In iOS 7 and later, an MDM server can replace profiles that have expired signing certificates with new profiles that have current certificates. This includes the MDM profile itself.  

To replace an installed profile, install a new profile that has the same top-level `PayloadIdentifier` as an installed profile.  

Replacing an MDM profile with a new profile restarts the check-in process. If an SCEP payload is included, a new client identity is created. If the update fails, the old configuration is restored.  
  

## Dealing with Restores
  

A user can restore his or her device from a backup. If the backup contains an MDM payload, MDM service is reinstated and the device is automatically scheduled to deliver a `TokenUpdate` check-in message. MDM service is reinstated only if the backup is restored to the same device. It is not reinstated if the user restores a backup to a new device.  

Your server can either accept the device by replying with a `200` status or reject the device with a `401` status. If your server replies with a `401` status, the device removes the profile that contains the MDM payload.  

It is good practice to respond with a `401` status to any device that the server is not actively managing.  
  

## Securing the ClearPasscode Command
  

Though this may sound obvious, clearing the passcode on a managed device compromises its security. Not only does it allow access to the device without a passcode, it also disables Data Protection.  

If your MDM payload specifies the Device Lock correctly, the device includes an `UnlockToken` data blob in the `TokenUpdate` message that it sends your server after installing the profile. This data blob contains a cryptographic package that allows the device to be unlocked. Treat this data as the equivalent of a “master passcode” for the device. Your IT policy should specify how this data is stored, who has access to it, and how the `ClearPasscode` command can be issued and accounted for.  

Do not send the `ClearPasscode` command until you have verified that the device’s owner has physical ownership of the device. You should *never* send the command to a lost device.  
  

## Adding MDMServiceConfig Functionality
  

To simplify administration using Apple Configurator (or other tools in the future) you can add an unauthenticated HTTPS request entry point to your server, labeled with the Uniform Resource Identifier `/MDMServiceConfig`. The resulting URL would have the form  `https://mdm.example.com/MDMServiceConfig`. The server code should return in the body of its response a UTF-8 JSON-encoded hash (Content-Type: application/json; charset=UTF8) with some or all of the following keys, the values of which should be fully-functional URLs.  


|Key|Value|
|-|-|
|`dep_enrollment_url`|This is the URL the device should contact to begin MDM enrollment with the MDM server. It should have the same value the server would send for the `url` key when defining a DEP profile via `https://mdmenrollment.apple.com/profile`, as described in [Define Profile](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW30).|
|`dep_anchor_certs_url`|This is the URL that a client can use to obtain the certificates required to trust the URL specified by the `dep_enrollment_url` key. It is the exact same format as the `anchor_certs` value in the DEP profile, except the body needs to be UTF-8 JSON-encoded for transfer. The decoded body of the response from this URL should be usable in a DEP profile under the `anchor_certs` key without any modification. If the MDM server is using a trusted SSL certificate (so no additional certs are required), this URL should still be provided but the body of the response to the URL should either be empty (Content-Length: 0) or the JSON string for an empty array (`'[]'`).|
|`trust_profile_url`|This is the URL a client can use to obtain a Trust Profile for the MDM server. This should be a fully formed `.mobileconfig` profile with only payloads of type `com.apple.security.root`. If the server is using trusted certificates (so no Trust Profile is required), this key should be omitted from the response. Do not return a URL that would generate an empty profile.|
  

> **Note:** 
Although the foregoing keys are individually optional, it is recommended that `dep_enrollment_url` and `dep_anchor_certs_url` be implemented or not as a pair.  
  

  

### Examples
  

Below are examples of code that implements `/MDMServiceConfig`.  

  

#### The MDMServiceConfig Request
  

  

##### Request Format
  

```
GET https://mdm.example.com/MDMServiceConfig
```  

  

##### Response Body
  

```
{
    "dep_enrollment_url": "https://mdm.example.com/devicemanagement/mdm/dep_mdm_enroll",
    "dep_anchor_certs_url": "https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs",
    "trust_profile_url": "https://certs.example.com/mdm/trust_profile"
}
```  

It is not required that the URLs refer to the same host as the `/MDMServiceConfig` request, as illustrated by the example for `trust_profile_url`.  

  

#### The dep_anchor_certs_url Key
  

  

##### Request Format
  

```
GET https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs
```  

  

##### Response Body (truncated for clarity)
  

```
["MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIGA1UEAwwbU3ly
\nYWggQ2VydGlmaWNhd...SVVTo9ll1Lv3OJGqBkxPl9TCC\nfYYnArwzlk4qm1tP\n"]
```  

  

#### The trust_profile_url Key
  

  

##### Request Format
  

```
GET https://certs.example.com/mdm/trust_profile
```  

  

##### Response Body (truncated for clarity)
  

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>PayloadContent</key>
   <array>
   	<dict>
   		<key>PayloadContent</key>
   		<data>
   		MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIG
   		...
   		9TCCfYYnArwzlk4qm1tP
   		</data>
   		<key>PayloadDescription</key>
   		<string>Installs the Root certificate for Example Corp.</string>
   		<key>PayloadDisplayName</key>
   		<string>Root certificate for Example Corp</string>
   		<key>PayloadIdentifier</key>
   		<string>com.apple.ssl.certificate</string>
   		<key>PayloadOrganization</key>
   		<string>Example Corp</string>
   		<key>PayloadType</key>
   		<string>com.apple.security.root</string>
   		<key>PayloadUUID</key>
   		<string>B90FA650-5A7D-496A-8C84-0D81C9EBCE6E</string>
   		<key>PayloadVersion</key>
   		<integer>1</integer>
   	</dict>
   </array>
   <key>PayloadDescription</key>
   <string>Configures your device to trust the MDM server.</string>
   <key>PayloadDisplayName</key>
   <string>Trust Profile for Example Corp</string>
   <key>PayloadIdentifier</key>
   <string>com.apple.config.mdm.example.com.ssl</string>
   <key>PayloadScope</key>
   <string>System</string>
   <key>PayloadType</key>
   <string>Configuration</string>
   <key>PayloadUUID</key>
   <string>94cdf5c0-bde0-0131-1ed5-005056831d08</string>
   <key>PayloadVersion</key>
   <integer>1</integer>
</dict>
</plist>
```  

[Next](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/7-MDMVendorCSRSigningOverview/MDMVendorCSRSigningOverview.html)[Previous](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6.5-MDM_Rosters/MDM_Rosters.html)

  



