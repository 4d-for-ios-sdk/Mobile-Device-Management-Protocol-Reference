# Device Management Workflow

 [Configuration Profile Reference - Device Management Workflow](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW50)  
  

## Device Management Workflow
  

A typical MDM device management workflow contains the following steps:  


1. Set up an account for your MDM server if you have not already done so. 

2. Use the Fetch Devices endpoint to obtain devices associated with the MDM server’s account. 

   > **Note:** Your server should periodically use the Sync Devices endpoint to obtain updated information about existing devices and new devices.  
 

3. Assign a profile to the device. You can do this in one of the following ways: 

 

   * Use the Define Profile endpoint to create a new MDM server profile and associate it with one or more devices. 

   * Use the Assign Profile endpoint to associate an existing MDM server profile with one or more devices. 
 

4. Remove the profile from the device when appropriate by using the Remove Profile endpoint. 
