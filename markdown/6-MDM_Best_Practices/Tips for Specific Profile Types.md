# Tips for Specific Profile Types

 [Configuration Profile Reference - Tips for Specific Profile Types](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW3)  
  

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