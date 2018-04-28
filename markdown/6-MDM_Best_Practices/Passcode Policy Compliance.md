# Passcode Policy Compliance

 [Configuration Profile Reference - Passcode Policy Compliance](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW10)  
  

## Passcode Policy Compliance
  

Because an MDM server may push a profile containing a passcode policy without user interaction, it is possible that a user’s passcode must be changed to comply with a more stringent policy. When this situation arises, a 60-minute countdown begins. During this grace period, the user is prompted to change the passcode when returning to the Home screen, but can dismiss the prompt and continue working. After the 60-minute grace period, the user must change the passcode in order to launch any application on the device, including built-in applications.  

An MDM server can check to see if a user has complied with all passcode restrictions using the `SecurityInfo` command. An MDM server can wait until the user has complied with passcode restrictions before pushing other profiles to the device.