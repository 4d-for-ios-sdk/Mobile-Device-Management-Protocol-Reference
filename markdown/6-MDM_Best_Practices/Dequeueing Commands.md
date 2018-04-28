# Dequeueing Commands

 [Configuration Profile Reference - Dequeueing Commands](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW20)  
  

## Dequeueing Commands
  

Your server should not consider a command accepted and executed by the device until you receive the `Acknowledged` or `Error` status with the command UUID in the message. In other words, your server should leave the last command on the queue until you receive the status for that command.  

It is possible for the device to send the same status twice. You should examine the `CommandUUID` field in the device’s status message to determine which command it applies to.