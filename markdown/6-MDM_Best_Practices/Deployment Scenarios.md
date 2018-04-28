# Deployment Scenarios

 [Configuration Profile Reference - Deployment Scenarios](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW11)  
  

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