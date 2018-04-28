# Updating Expired Profiles

 [Configuration Profile Reference - Updating Expired Profiles](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW12)  
  

## Updating Expired Profiles
  

In iOS 7 and later, an MDM server can replace profiles that have expired signing certificates with new profiles that have current certificates. This includes the MDM profile itself.  

To replace an installed profile, install a new profile that has the same top-level `PayloadIdentifier` as an installed profile.  

Replacing an MDM profile with a new profile restarts the check-in process. If an SCEP payload is included, a new client identity is created. If the update fails, the old configuration is restored.