# MDM Result Payloads

 [Configuration Profile Reference - MDM Result Payloads](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW5)  
  

## MDM Result Payloads
  

The device replies to the host by sending a plist-encoded dictionary containing the following keys, as well as other keys returned by each command.  


|Key|Type|Content|
|-|-|-|
|`Status`|String|Status. Legal values are described in [Table 1](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW31).|
|`UDID`|String|UDID of the device.|
|`CommandUUID`|String|UUID of the command that this response is for (if any).|
|`ErrorChain`|Array|Optional. Array of dictionaries representing the chain of errors that occurred. The content of these dictionaries is described in [Table 2](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW33).|
  

The `Status` key contains one of the following strings:  


|Status value|Description|
|-|-|
|`Acknowledged`|Everything went well.|
|`Error`|An error has occurred. See the `ErrorChain` array for details.|
|`CommandFormatError`|A protocol error has occurred. The command may be malformed.|
|`Idle`|The device is idle (there is no status).|
|`NotNow`|The device received the command, but cannot perform it at this time. It will poll the server again in the future. For details, see [Error Handling](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW34).|
  

The `ErrorChain` key contains an array. The first item is the top-level error. Subsequent items in the array are the underlying errors that led up to that top-level error.  

Each entry in the `ErrorChain` array contains the following dictionary:  


|Key|Type|Content|
|-|-|-|
|`LocalizedDescription`|String|Description of the error in the device’s localized language.|
|`USEnglishDescription`|String|Optional. Description of the error in US English.|
|`ErrorDomain`|String|The error domain.|
|`ErrorCode`|Number|The error code.|
  

The `ErrorDomain` and `ErrorCode` keys contain internal codes used by Apple that may be useful for diagnostics. Your host should not rely on these values, as they may change between software releases. However, for reference, the current codes are listed in [Error Codes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW77).