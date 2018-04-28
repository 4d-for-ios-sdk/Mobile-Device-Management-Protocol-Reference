# Dealing with Restores

 [Configuration Profile Reference - Dealing with Restores](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW23)  
  

## Dealing with Restores
  

A user can restore his or her device from a backup. If the backup contains an MDM payload, MDM service is reinstated and the device is automatically scheduled to deliver a `TokenUpdate` check-in message. MDM service is reinstated only if the backup is restored to the same device. It is not reinstated if the user restores a backup to a new device.  

Your server can either accept the device by replying with a `200` status or reject the device with a `401` status. If your server replies with a `401` status, the device removes the profile that contains the MDM payload.  

It is good practice to respond with a `401` status to any device that the server is not actively managing.