# MDM Command Payloads

 [Configuration Profile Reference - MDM Command Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW4)  
  

## MDM Command Payloads
  

A host may send a command to the device by sending a plist-encoded dictionary that contains the following required keys:  


|Key|Type|Content|
|-|-|-|
|`CommandUUID`|String|UUID of the command.|
|`Command`|Dictionary|The command dictionary.|
  

The content of the `Command` dictionary must include the following required key, as well as other keys defined by each command.  


|Key|Type|Content|
|-|-|-|
|`RequestType`|String|Request type. See each command’s description.|
