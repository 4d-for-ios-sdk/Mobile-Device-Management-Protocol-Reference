# Securing the ClearPasscode Command

 [Configuration Profile Reference - Securing the ClearPasscode Command](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW24)  
  

## Securing the ClearPasscode Command
  

Though this may sound obvious, clearing the passcode on a managed device compromises its security. Not only does it allow access to the device without a passcode, it also disables Data Protection.  

If your MDM payload specifies the Device Lock correctly, the device includes an `UnlockToken` data blob in the `TokenUpdate` message that it sends your server after installing the profile. This data blob contains a cryptographic package that allows the device to be unlocked. Treat this data as the equivalent of a “master passcode” for the device. Your IT policy should specify how this data is stored, who has access to it, and how the `ClearPasscode` command can be issued and accounted for.  

Do not send the `ClearPasscode` command until you have verified that the device’s owner has physical ownership of the device. You should *never* send the command to a lost device.