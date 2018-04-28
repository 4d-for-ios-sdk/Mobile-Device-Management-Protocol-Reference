# Structure of MDM Messages

 [Configuration Profile Reference - Structure of MDM Messages](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW3)  
  

## Structure of MDM Messages
  

Once the MDM payload is installed, the device listens for a push notification. The topic that MDM listens to corresponds to the contents of the `User ID` parameter in the Subject field of the push notification client certificate.  

To cause the device to poll the MDM server for commands, the MDM server sends a notification through the APNS gateway to the device. The message sent with the push notification is JSON-formatted and must contain the `PushMagic` string as the value of the `mdm` key. For example:  

```
{"mdm":"PushMagicValue"}
```  

In place of `PushMagicValue` above, substitute the actual `PushMagic` string that the device sends to the MDM server in the `TokenUpdate` message. That should be the whole message. There should not be an `aps` key. (The `aps` key is used only for third-party app push notifications.)  

The device responds to this push notification by contacting the MDM server using HTTP PUT over TLS (SSL). This message may contain an `Idle` status or may contain the result of a previous operation. If the connection is severed while the device is performing a task, the device will try to report its result again once networking is restored.  

 shows an example of an MDM request payload.  

**Listing 1**  MDM request payload example  

```
PUT /your/url HTTP/1.1
Host: www.yourhostname.com
Content-Length: 1234
Content-Type: application/x-apple-aspen-mdm; charset=UTF-8
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>UDID</key>
    <string>...</string>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Status</key>
    <string>Acknowledged</string>
  </dict>
</plist>
 
```  

The server responds by sending the next command that the device should perform by enclosing it in the HTTP reply.  

 shows an example of the server’s response payload.  

**Listing 2**  MDM response payload example  

```
HTTP/1.1 200 OK
Content-Length: 1234
Content-Type: application/xml; charset=UTF-8
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Command</key>
    <dict>
      ...
    </dict>
  </dict>
</plist>
 
```  

The device performs the command and sends its reply in another HTTP PUT request to the MDM server. The MDM server can then reply with the next command or end the connection by sending a `200` status (OK) with an empty response body.  

> **Note:** An empty response body must be zero bytes in length, not an empty property list.  
  

If the connection is broken while the device is performing a command, the device caches the result of the command and re-attempts connection to the server until the status is delivered.  

It is safe to send several push notifications to the device. APNS coalesces multiple notifications and delivers only the last one to the device.  

You can monitor the MDM activity in the device console using Xcode or [Apple Configurator 2](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12). A healthy (but empty) push activity should look like this:  

```
Wed Sep 29 02:09:05 unknown mdmd[1810] <Warning>: MDM|mdmd starting...
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Network reachability has changed.
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Polling MDM server https://10.0.1.4:2001/mdm for commands
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Transaction completed. Status: 200
Wed Sep 29 02:09:06 unknown mdmd[1810] <Warning>: MDM|Server has no commands for this device.
Wed Sep 29 02:09:08 unknown mdmd[1810] <Warning>: MDM|mdmd stopping...
```