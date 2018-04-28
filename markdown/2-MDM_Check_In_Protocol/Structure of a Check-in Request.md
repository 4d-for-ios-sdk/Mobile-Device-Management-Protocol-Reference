# Structure of a Check-in Request

 [Configuration Profile Reference - Structure of a Check-in Request](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/2-MDM_Check_In_Protocol/MDM_Check_In_Protocol.html#//apple_ref/doc/uid/TP40017387-CH4-SW3)  
  

## Structure of a Check-in Request
  

When the MDM payload is installed, the device initiates communication with the check-in server. The device validates the TLS certificate of the server, then uses the identity specified in its MDM payload as the client authentication certificate for the connection.  

After successfully negotiating this secure connection, the device sends an HTTP PUT request in this format:  

```
PUT /your/url HTTP/1.1
Host: www.yourhostname.com
Content-Length: 1234
Content-Type: application/x-apple-aspen-mdm-checkin
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>MessageType</key>
    <string>Authenticate</string>
    <key>Topic</key>
    <string>...</string>
    <key>UDID</key>
    <string>...</string>
  </dict>
</plist>
 
```  

The server must send a `200 (OK)` status code to indicate success or a `401 (Unauthorized)` status code to indicate failure. The body of the reply is ignored.