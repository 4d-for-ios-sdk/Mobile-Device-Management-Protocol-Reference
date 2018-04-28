# Request Types

 [Configuration Profile Reference - Request Types](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW6)  
  

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
|`Identifiers`|Array|Optional. An array of app identifiers as strings. If provided, the response contains only the status of apps whose identifiers appear in this array. </br>**Availability:** Available in iOS 7 and later.|
|`ManagedAppsOnly`|Boolean|Optional. If `true`, only managed app identifiers are returned. </br>**Availability:** Available in iOS 7 and later.|
  

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
|`ExternalVersionIdentifier`|String|The application’s external version ID. It can be used for comparison in the iTunes Search API to decide if the application needs to be updated.</br>**Availability:** Available in iOS 11 and later.|
|`AppStoreVendable`|Boolean|If `true`, the app came from the store and can participate in store features.</br>**Availability:** Available in iOS 11.3 and later.|
|`DeviceBasedVPP`|Boolean|If `true`, the app is distributed to the device without requiring an Apple ID.</br>**Availability:** Available in iOS 11.3 and later.|
|`BetaApp`|Boolean|If true, the app is part of the Beta program.</br>**Availability:** Available in iOS 11.3 and later.|
|`AdHocCodeSigned`|Boolean|If true, the app is ad-hoc code signed.</br>**Availability:** Available in iOS 11.3 and later.|
|`HasUpdateAvailable`|Boolean|If true, the app has an update available. This key will only be present for App Store apps. On macOS, this key will only be present for VPP apps.</br>**Availability:** Available in iOS 11.3 and later and in macOS 10.13.4 and later.|
  

  

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
|`PreviousScanResult`|Integer|
|`PerformPeriodicCheck`|Boolean|
|`AutomaticCheckEnabled`|Boolean|
|`BackgroundDownloadEnabled`|Boolean|
|`AutomaticAppInstallationEnabled`|Boolean|
|`AutomaticOSInstallationEnabled`|Boolean|
|`AutomaticSecurityUpdatesEnabled`|Boolean|
  

  

#### Network Information Queries Provide Hardware Addresses, Phone Number, and SIM Card and Cellular Network Info
  

The queries in  are available if the MDM host has a Network Information access right.  

> **Note:** Not all devices understand all queries. For example, queries specific to GSM (IMEI, SIM card queries, and so on) are ignored if the device is not GSM-capable. The macOS MDM client responds only to `BluetoothMAC`, `WiFiMAC`, and `EthernetMAC`.  
  


|Query|Reply Type|Comment|
|-|-|-|
|`ICCID`|String|The ICC identifier for the installed SIM card.|
|`BluetoothMAC`|String|Bluetooth MAC address.|
|`WiFiMAC`|String|Wi-Fi MAC address.|
|`EthernetMACs`|Array of strings|Ethernet MAC addresses.</br>**Availability:** Available in iOS 7 and later.|
|`EthernetMAC`|String|Primary Ethernet MAC address.</br>**Availability:** Available in macOS v10.7 and later.|
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
  

The `SecurityInfo` dictionary contains the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`HardwareEncryptionCaps`|Integer|Bitfield. Describes the underlying hardware encryption capabilities of the device. Values are described in [Table 10](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW23).</br>**Availability:** Available in iOS only.|
|`PasscodePresent`|Boolean|Set to `true` if the device is protected by a passcode.</br>**Availability:** Available in iOS only.|
|`PasscodeCompliant`|Boolean|Set to `true` if the user’s passcode is compliant with all requirements on the device, including Exchange and other accounts.</br>**Availability:** Available in iOS only.|
|`PasscodeCompliantWithProfiles`|Boolean|Set to `true` if the user’s passcode is compliant with requirements from profiles.</br>**Availability:** Available in iOS only.|
|`PasscodeLockGracePeriodEnforced`|Integer|The current enforced value for the amount of time in seconds the device must be locked before unlock will require the device passcode.</br>**Availability:** Available in iOS only.|
|`FDE_Enabled`|Boolean|Device channel only. Whether Full Disk Encryption (FDE) is enabled or not.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_HasPersonalRecoveryKey`|Boolean|Device channel only. If FDE has been enabled, returns whether a personal recovery key has been set.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_HasInstitutionalRecoveryKey`|Boolean|Device channel only. If FDE has been enabled, returns whether an institutional recovery key has been set.</br>**Availability:** Available in macOS 10.9 and later.|
|`FDE_PersonalRecoveryKeyCMS`|Data|If FileVault Personal Recovery Key (PRK) escrow is enabled and a recovery key has been set up, this key will contain the PRK encrypted with the certificate from the `com.apple.security.FDERecoveryKeyEscrow` payload and wrapped as a CMS blob.</br>**Availability:** Available in macOS 10.13 and later.|
|`FDE_PersonalRecoveryKeyDeviceKey`|String|If FileVault PRK escrow is enabled and a recovery key has been set up, this key contains a short string that is displayed to the user in the EFI login window as part of the help message if the user enters an incorrect password three times. The server can use this string as an index when saving the device PRK. Currently, this string is the device serial number, which replaces the `recordNumber` that was returned by the server in the earlier escrow mechanism.</br>**Availability:** Available in macOS 10.13 and later.|
|`FirewallSettings`|Dictionary|The current Firewall settings. This information will be returned only when the command is sent to the device channel. The response is a dictionary with the following keys:<ul><li>`FirewallEnabled` (Boolean): Set to `true` if firewall is on.</li><li>`BlockAllIncoming` (Boolean): Set to `true` if all incoming connections are blocked.</li><li>`StealthMode` (Boolean): Set to `true` if stealth mode is enabled.</li><li>`Applications` (Array of Dictionaries): Blocking status for specific applications. Each dictionary contains these keys:</li><li></br><ul>   <li>`BundleID` (String) : Identifies the application</li>   <li>`Allowed` (Boolean) : Set to `true` if incoming connections are allowed</li>   <li>`Name` (String) : descriptive name of the application for display purposes only (may be missing if no corresponding app is found on the client computer).</li></ul></li></ul></br>**Availability:** Available in macOS 10.12 and later.|
|`SystemIntegrityProtectionEnabled`|Boolean|Device channel only. Set to `true` if System Integrity Protection is enabled on the device. In macOS 10.11 or later, this information may also be retrieved using a `DeviceInformation` query.</br>**Availability:** Available in macOS 10.12 and later.|
|`FirmwarePasswordStatus`|Dictionary|State of EFI firmware password; see .</br>**Availability:** Available in macOS 10.13 and later.|
|`ManagementStatus`|Dictionary|Provides information about the client’s MDM enrollment. The dictionary contains these keys:<ul><li>`EnrolledViaDEP` (Boolean): Set to `true` if the device was entrolled in MDM during DEP.</li><li>`UserApprovedEnrollment` (Boolean): Set to `true` if the enrollment was “user approved”. If `false`, the client may reject certain security-sensitive payloads or commands.</li></ul></br>**Availability:** Available in macOS 10.13.2 and later.|
  

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
|`Message`|String|Optional. If provided, this message is displayed on the lock screen and should contain the words “lost iPad.” Ignored on Shared iPads.</br>**Availability:** Available in iOS 7 and later.|
|`PhoneNumber`|String|Optional. If provided, this phone number is displayed on the lock screen. Ignored on Shared iPads. </br>**Availability:** Available in iOS 7 and later.|
  

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
|`UnlockToken`|Data|The `UnlockToken` value that the device provided in its [TokenUpdate Message](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/2-MDM_Check_In_Protocol/MDM_Check_In_Protocol..html#//apple_ref/doc/uid/TP40017387-CH4-SW1) check-in message.|
  

> **Security Note:** This command requires both Device Lock and Passcode Removal access rights.  
  

> **Note:** The macOS MDM client generates an `Error` response to the server.  
  

  

### EraseDevice Commands Remotely Erase a Device
  

Upon receiving this command, the device immediately erases itself. No warning is given to the user. This command is performed immediately even if the device is locked.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`EraseDevice`|
|`PIN`|String|The Find My Mac PIN. Must be 6 characters long.</br>**Availability:** Available in macOS 10.8 and later.|
|`PreserveDataPlan`|Boolean|Optional. If `true`, and a data plan exists on the device, it will be preserved. Defaults to `false`.</br>**Availability:** Available in iOS 11 and later.|
|`DisallowProximitySetup`|Boolean|Optional. If `true`, on the next reboot Proximity Setup is not allowed and the pane in Setup Assistant will be skipped. Defaults to `false`.</br>**Availability:** Available in iOS 11.3 and later.|
  

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
|`ScanTime`|Integer|Optional. Number of seconds to spend searching for the destination. The default is 30 seconds. This value must be in the range 10–300.|
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

  

#### InstallApplication Commands Install an Application
  

To send an `InstallApplication` command, the server sends a request containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`InstallApplication`.|
|`iTunesStoreID`|Number|The application’s iTunes Store ID.</br>For example, the numeric ID for Keynote is `361285480` as found in the App Store link [http://itunes.apple.com/us/app/keynote/id361285480?mt=8](http://itunes.apple.com/us/app/keynote/id361285480?mt=8).|
|`Identifier`|String|Optional. The application’s bundle identifier. </br>Available in iOS 7 and later. </br>In iOS 11.3 and later, this can be used to reinstall a system app. System apps installed in this manner will not be considered managed apps.|
|`Options`|Dictionary|Optional. App installation options. The available options are listed below. Available in iOS 7 and later.|
|`ManifestURL`|String|The `https` URL where the manifest of an enterprise application can be found. For more information about the manifest file, see [Install in-house apps wirelessly](https://help.apple.com/deployment/ios/#/apda0e3426d7).</br>Note: In iOS 7 and later, this URL and the URLs of any assets specified in the manifest must begin with `https`.|
|`ManagementFlags`|Integer|The bitwise OR of the following flags:</br>1: Remove app when MDM profile is removed.</br>4: Prevent backup of the app data.|
|Configuration|Dictionary|Optional. If provided, this contains the initial configuration dictionary for the managed app. For more information, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68).|
|Attributes|Dictionary|Optional. If provided, this dictionary contains the initial attributes for the app. For a list of allowed keys, see [ManagedApplicationAttributes Queries App Attributes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW69).|
|`ChangeManagementState`|String|Optional. Currently the only supported value is the following:</br>`Managed`: Take management of this app if the user has installed it already. Available in iOS 9 and later.|
  

If the application is not already installed and the `ChangeManagementState` is set to `Managed`, the app will be installed and managed.  If the application is installed unmanaged, the user will be prompted to allow management of the app on unsupervised devices and, if accepted, the application becomes managed.   

The request must contain exactly one of the following fields: `Identifier`, `iTunesStoreID`, or `ManifestURL` value.  

The options dictionary can contain the following keys:  


|Key|Type|Content|
|-|-|-|
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
|`Identifiers`|Array|Optional. An array of app identifiers as strings. If provided, the response contains only the status of apps whose identifiers appear in this array. </br>**Availability: **Available in iOS 7 and later.|
  

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
|HasConfiguration|Boolean|If `true`, the app has a server-provided configuration. For details, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68). </br>**Availability:** Available in iOS 7 and later.|
|HasFeedback|Boolean|If `true`, the app has feedback for the server. For details, see [Managed App Configuration and Feedback](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW68). </br>**Availability:** Available in iOS 7 and later.|
|IsValidated|Boolean|If `true`, the app has validated as allowed to run and is able to run on the device. If an app is enterprise-distributed and is not validated, it will not run on the device until validated. </br>**Availability:** Available in iOS 9.2 and later.|
|ExternalVersionIdentifier|String|The application’s external version ID. It can be used for comparison in the iTunes Search API to decide if the application needs to be updated. </br>**Availability:** Available in iOS 11 and later.|
  


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
  

Installing a book not from the iBooks Storewith the same `PersistentID` as an existing book not from the iBooks Store replaces the old book with the new. Installing an iBooks Store book with the same `iTunesStoreID` as an existing installed book updates the book from the iBooks Store.  

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
  

  

#### Bluetooth Modifies the Bluetooth Setting
  

To send a `Bluetooth` command, the server sends a dictionary containing the following keys:  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`Bluetooth`.</br>**Availability:** Available in iOS 11.3 and later for supervised devices and in macOS 10.13.4 and later.|
|`Enabled`|Boolean|If `true`, enables Bluetooth.</br>If `false`, disables Bluetooth.</br>**Availability:** Available in iOS 11.3 and later for supervised devices and in macOS 10.13.4 and later.|
  

  

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
  

Shared iPad Mode only. The `PasscodeLockGracePeriod` command sets the time the screen must be locked before needing a passcode to unlock it. Changing to a less restrictive value will not take effect until the user logs out.  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`PasscodeLockGracePeriod`.|
|`PasscodeLockGracePeriod`|Integer|The number of seconds the screen must be locked before unlock attempts will require the device passcode.|
  

**Availability:** Available in iOS 9.3.2 and later.  

  

#### MaximumResidentUsers Sets Maximum Number of Users for a Shared iPad
  

Shared iPad Mode only. Sets the maximum number of users that can use a Shared iPad. This can be set only when the iPad is in the `AwaitingConfiguration` phase, before the `DeviceConfigured` message has been sent to the device. If `MaximumResidentUsers` is greater than the maximum possible number of users supported on the device, the device is configured with the maximum possible number of users instead.  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`MaximumResidentUsers`.|
|`MaximumResidentUsers`|Integer|The maximum number of users that can use a Shared iPad.|
  

**Availability: **Available in iOS 9.3 and later.  

  

#### DiagnosticSubmission Enables Submission of Diagnostics
  

Shared iPad Mode only. Sets the user preference of diagnostic submission.  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`DiagnosticSubmission`.|
|`Enabled`|Boolean|If `true`, enables diagnostic submission. </br>If `false`, disables diagnostic submission.|
  

**Availability: **Available in iOS 9.3 and later.  

  

#### AppAnalytics Enables Sharing Analytics with App Developers
  

Shared iPad Mode only. Sets the user preference of sharing analytics with app developers.  


|Key|Type|Content|
|-|-|-|
|`Item`|String|`AppAnalytics`.|
|`Enabled`|Boolean|If `true`, enables app analytics. </br>If `false`, disables app analytics.|
  

**Availability: **Available in iOS 9.3.2 and later.  

  

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

On macOS, all supported Software Update commands except the `AvailableOSUpdates` query require DEP enrollment.  

On iOS 10.3 and later, supported Software Update commands require supervision but not DEP enrollment. If there is a passcode on the device, a user must enter it to start a software update. Prior to iOS 10.3, the supervised devices need to be DEP-enrolled and have no passcode.  

The MDM server must have the App Installation right to perform these commands.  

  

#### ScheduleOSUpdate
  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ScheduleOSUpdate`.|
|`Updates`|Array|An array of dictionaries specifying the OS updates to download or install. If this entry is missing, the device applies the default behavior for all available updates.|
  

The Updates array contains dictionaries with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`ProductKey`|String|The product key of the update to be installed.|
|`ProductVersion`|String|Optional. Defines the version to install. If the `ProductVersion` is specified, the `ProductKey` field is optional.</br>If a matching update is not available, the result of the operation will be “update not available”, even if there are other valid and available updates for the device.</br>The `Version` key from the `AvailableOSUpdates` command can be used. The version format is the user facing version, like “11.2.5” or “11.3”.</br>**Availability:** Available in iOS 11.3 and later.|
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
|`IsConfigurationDataUpdate`|Boolean|Set to `true` if this is an update to a configuration file. Defaults to `false` (macOS only).|
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
  

  

### Extension Management
  

These commands support the management of extensions on macOS.  

  

#### ActiveNSExtensions
  

`ActiveNSExtensions` returns information about the active NSExtensions for a particular user. NSExtensions are installed and enabled at the user level; there is no concept of “device” NSExtensions.  

Requires access rights to inspect installed apps. Supported only on the user channel.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`ActiveNSExtensions`.|
|`FilterExtensionPoints`|Array|Optional. Array of extension points, that limit the results to the extensions belonging to the specified extension points.|
  

The response will be an array of dictionaries with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The identifier of the extension.|
|`ExtensionPoint`|String|The `NSExtensionPointIdentifier` for the extension.|
|`DisplayName`|String|The display name.|
|`ContainerDisplayName`|String|The display name of the container app (if any).|
|`ContainerIdentifier`|String|The identifier of the container (if any).|
|`Path`|String|The path to the extension.|
|`Version`|String|The version of the extension.|
|`UserElection`|String|The user’s enable/disable state of the extension, set through the preferences pane. Will be one of: “Default”, “Use”, or “Ignore”.|
  

Extensions that have been restricted from executing (via the `com.apple.NSExtension` configuration profile payload or Application Launch Restrictions) will not appear in the response list.  

  

#### NSExtensionMappings
  

`NSExtensionMappings` returns information about the installed extensions for a user. This command is useful when building the set of extension identifiers and extension points for the `com.apple.NSExtension` profile payloads.  

Requires access rights to inspect installed apps. Supported only on the user channel.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|`NSExtensionMappings`.|
  

The response will be an array of dictionaries with the following keys and values:  


|Key|Type|Content|
|-|-|-|
|`Identifier`|String|The identifier of the extension.|
|`ExtensionPoint`|String|The `NSExtensionPointIdentifier` for the extension.|
|`DisplayName`|String|The display name.|
  

The returned list will be a superset of the list returned by the `ActiveNSExtensions` command. This list may contain extensions that will never be enabled on the system due to various restrictions.  

  

### Support for macOS Requests
  

The table below lists the MDM protocol request types that are available for Apple devices that run macOS. The interfaces of these requests to macOS are similar to the iOS interfaces described in the rest of this chapter.  


|Command|Min OS|User/Device|Comments|
|-|-|-|-|
|AccountConfiguration|10.11|Device|Valid only during DEP enrollment.|
|ActiveNSExtensions|10.13|User|
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
|NSExtensionMappings|10.13|User|
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
|`Password`|String|A FileVault user’s password, or if using a CoreStorage volume, the current Personal Recovery Key (PRK).|
  

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