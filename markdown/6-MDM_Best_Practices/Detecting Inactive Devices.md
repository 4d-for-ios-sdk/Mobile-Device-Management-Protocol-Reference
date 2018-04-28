# Detecting Inactive Devices

 [Configuration Profile Reference - Detecting Inactive Devices](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW18)  
  

## Detecting Inactive Devices
  

To be notified when a device becomes inactive, set the `CheckOutWhenRemoved` key to `true` in the MDM payload. Doing so causes the device to contact your server when it ceases to be managed. However, because a managed device makes only a single attempt to deliver this message, you should also employ a timeout to detect devices that fail to check out due to network conditions.  

To do this, your server should send a push notification periodically to ensure that managed devices are still listening to your push notifications. If the device fails to respond to push notifications after some time, the device can be considered inactive. A device can become inactive for several reasons:  


* The MDM profile is no longer installed. 

* The device has been erased. 

* The device has been disconnected from the network. 

* The device has been turned off. 
  

> **Note:** 
Your security report on each managed device should specify whether or not MDM is set to be non-removable. This information is returned by the profile query, as described in [Define Profile](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW30).  
  

The time that your server should wait before deciding that a device is inactive can be varied according to your IT policy, but a time period of several days to a week is recommended. While it’s harmless to send push notifications once a day or so to make sure the device is responding, it is not necessary. Apple’s push notification servers cache your last push notification and deliver it to the device when it comes back on the network.  

When a device becomes inactive, your server may take appropriate action, such as limiting the device’s access to your organization’s resources until the device starts responding to push notifications once more.