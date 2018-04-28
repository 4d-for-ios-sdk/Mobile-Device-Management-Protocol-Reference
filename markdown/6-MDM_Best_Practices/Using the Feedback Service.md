# Using the Feedback Service

 [Configuration Profile Reference - Using the Feedback Service](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW19)  
  

## Using the Feedback Service
  

Your server should regularly poll the Apple Push Notification Feedback Service to detect if a device’s push token has become invalid. When a device token is reported invalid, your server should consider the device to be no longer managed and should stop sending push notifications or commands to the device. If needed, you may also take appropriate action to restrict the device’s access to your organization’s resources.  

The Feedback service should be considered unreliable for detecting device inactivity, because you may not receive feedback in certain cases. Your server should use timeouts as the primary means of determining device management status.