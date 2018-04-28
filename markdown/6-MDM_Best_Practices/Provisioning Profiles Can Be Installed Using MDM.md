# Provisioning Profiles Can Be Installed Using MDM

 [Configuration Profile Reference - Provisioning Profiles Can Be Installed Using MDM](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW8)  
  

## Provisioning Profiles Can Be Installed Using MDM
  

Third-party enterprise applications require provisioning profiles in order to run them. You can use MDM to deliver up-to-date versions of these profiles so that users do not have to manually install these profiles, replace profiles as they expire, and so on.  

To do this, deliver the provisioning profiles through MDM instead of distributing them through your corporate web portal or bundled with the application.  

> **Security Note:** Although an MDM server can remove provisioning profiles, you should not depend on this mechanism to revoke access to your enterprise applications for two reasons:  
> 
* An application continues to be usable until the next device reboot even if you remove the provisioning profile. 

* Provisioning profiles are synchronized with iTunes. Thus, they may get reinstalled the next time the user syncs the device. 
  
> An application continues to be usable until the next device reboot even if you remove the provisioning profile.  
> Provisioning profiles are synchronized with iTunes. Thus, they may get reinstalled the next time the user syncs the device.  
