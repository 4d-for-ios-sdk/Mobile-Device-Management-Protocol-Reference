# Error Handling

 [Configuration Profile Reference - Error Handling](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW34)  
  

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