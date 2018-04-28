# Handling a NotNow Response

 [Configuration Profile Reference - Handling a NotNow Response](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW406)  
  

## Handling a NotNow Response
  

If the device’s response to the previous command sent has a status of `NotNow`, your server has two response choices:  


* It may immediately stop sending commands to the device. In this case the device automatically polls your server when conditions change and it is able to process the last requested command. The server does not need to send another push notification in response to this status. However, the server may send another push notification to the device to have it poll the server immediately. The device does not cache the command that was refused. If the server wants the device to retry the command, it must send the command again when the device polls the server. 

* It may send another command on the same connection, but if this new command returns anything other than a `NotNow` response, the device will *not* automatically poll the server as it would have with the first response choice. The server must send a push notification at a later time to make the device reconnect. The device polls the server in response to a `NotNow` status only if that is the last status sent by the device to the server. 
  

The three example flowcharts below illustrate the foregoing choices.  

**Example 1:** The final command results in the server receiving a `NotNow` response. The device will poll the server later, when the `InstallApplication` command might succeed.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow1_2x.png" height="400" width="407">  

**Example 2:** The final command results in the server receiving something other than a `NotNow` response. The device will not poll the server later, because the last response was not `NotNow`.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow2_2x.png" height="322" width="407">  

**Example 3:** The connection to the device is unexpectedly interrupted. Because the last status the server received was not `NotNow`, the server should send a push notification to the device to retry the `InstallApplication` command. The server must not assume that the device will automatically poll the server later.  

<img src="https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/blob/master/assets//NotNow3_2x.png" height="357" width="454">