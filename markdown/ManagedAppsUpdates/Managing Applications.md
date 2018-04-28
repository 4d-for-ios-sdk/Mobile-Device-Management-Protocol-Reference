# Managing Applications

 [Configuration Profile Reference - Managing Applications](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/ManagedAppsUpdates/ManagedAppsUpdates.html#//apple_ref/doc/uid/TP40017387-CH10-SW25)  
  

## Managing Applications
  

MDM is the recommended way to manage applications for your enterprise. You can use MDM to help users install enterprise apps, and in iOS 5.0 and later, you can also install App Store apps purchased using the Volume Purchase Program (VPP). The way that you manage these applications depends on the version of iOS that a device is running.  

  

### iOS 9.0 and Later
  

In iOS 9.0 and later, you can use MDM’s app assignment feature to assign app licenses to device serial numbers. MDM can then be used to push a VPP app to a device regardless of whether an iTunes account is signed in. You can later remove those licenses and use them with other devices.  

  

### iOS 7.0 and Later
  

In iOS 7.0 and later, you can use MDM’s app assignment feature to assign app licenses to iTunes accounts. MDM can then be used to push a VPP app to a device that is signed in to that iTunes account. You can later remove those licenses and use them with other iTunes accounts.  

Also, in iOS 7.0 and later, an MDM server can provide configuration dictionaries to managed apps and can read response dictionaries from those apps. Apps can take advantage of this functionality to preconfigure themselves in a supervised environment, such as a classroom setting.  

  

### iOS 5.0 and Later
  

In iOS 5.0 and later, using MDM to manage apps gives you several advantages:  


* You can purchase apps for users without manually distributing redemption codes. 

* You can notify the user that an app is available for installation. (The user must agree to installation before the app is installed.) 

* A managed app can be excluded from the user’s backup. This prevents the app’s data from leaving the device during a backup. 

* The app can be configured so that the app and its data are automatically removed when the MDM profile is removed. This prevents the app’s data from persisting on a device unless it is managed. 
  

An app purchased from the App Store and installed on a user’s device is “owned” by the iTunes account used at the time of installation. This means that the user may install the app (not its data) on unmanaged devices.  

An app internally developed by an enterprise is not backed up. A user cannot install such an app on an unmanaged device.  

In order to support this behavior, your internally hosted enterprise app catalog must use the `InstallApplication` command instead of providing a direct link to the app (with a manifest URL or iTunes Store URL). This allows you to mark the app as managed during installation.  

  

### iOS 4.x and Later
  

To disable enterprise apps, you can remove the provisioning profile that they depend on. However, as mentioned in [Provisioning Profiles Can Be Installed Using MDM](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW8), *do not* rely solely on that mechanism for limiting access to your enterprise applications for two reasons:  


* Removing a provisioning profile does not prevent the app from launching until the device is rebooted. 

* The provisioning profile is likely to have been synced to a computer, and thus will probably be reinstalled during the next sync. 
  

To limit access to your enterprise application, follow these recommendations:  


* Have an online method of authenticating users when they launch your app. Use either a password or identity certificate to authenticate the user. 

* Store local app data in your application’s Caches folder to prevent the data from being backed up. 

* When you decide that the user should no longer have access to the application’s data, mark the user’s account on the server inactive in some way. 

* When your app detects that the user is no longer eligible to access the app, if the data is particularly sensitive, it should erase the local app data. 

* If your application has an offline mode, limit the amount of time users can access the data before reauthenticating online. Ensure that this timeout is enforced across multiple application launches. 

* If desired, you can also limit the number of launches to prevent time server forging attacks. 

* Be sure to store any information about the last successful authentication in your Caches folder (or in the keychain with appropriate flags) so that it does not get backed up. If you do not, the user could potentially modify the time stamp in a backup file, resync the device, and continue using the application. 
  

These guidelines assume that all the application’s data is replicated on your server. If you have data that resides only on the device (including offline edits), preserve a copy of the user’s changes on the server. Be sure to do so in a way that protects the integrity of the server’s data against disgruntled former users.