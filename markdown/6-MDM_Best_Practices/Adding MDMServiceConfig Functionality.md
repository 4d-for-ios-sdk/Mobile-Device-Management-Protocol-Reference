# Adding MDMServiceConfig Functionality

 [Configuration Profile Reference - Adding MDMServiceConfig Functionality](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/6-MDM_Best_Practices/MDM_Best_Practices.html#//apple_ref/doc/uid/TP40017387-CH5-SW101)  
  

## Adding MDMServiceConfig Functionality
  

To simplify administration using Apple Configurator (or other tools in the future) you can add an unauthenticated HTTPS request entry point to your server, labeled with the Uniform Resource Identifier `/MDMServiceConfig`. The resulting URL would have the form  `https://mdm.example.com/MDMServiceConfig`. The server code should return in the body of its response a UTF-8 JSON-encoded hash (Content-Type: application/json; charset=UTF8) with some or all of the following keys, the values of which should be fully-functional URLs.  


|Key|Value|
|-|-|
|`dep_enrollment_url`|This is the URL the device should contact to begin MDM enrollment with the MDM server. It should have the same value the server would send for the `url` key when defining a DEP profile via `https://mdmenrollment.apple.com/profile`, as described in [Define Profile](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW30).|
|`dep_anchor_certs_url`|This is the URL that a client can use to obtain the certificates required to trust the URL specified by the `dep_enrollment_url` key. It is the exact same format as the `anchor_certs` value in the DEP profile, except the body needs to be UTF-8 JSON-encoded for transfer. The decoded body of the response from this URL should be usable in a DEP profile under the `anchor_certs` key without any modification. If the MDM server is using a trusted SSL certificate (so no additional certs are required), this URL should still be provided but the body of the response to the URL should either be empty (Content-Length: 0) or the JSON string for an empty array (`'[]'`).|
|`trust_profile_url`|This is the URL a client can use to obtain a Trust Profile for the MDM server. This should be a fully formed `.mobileconfig` profile with only payloads of type `com.apple.security.root`. If the server is using trusted certificates (so no Trust Profile is required), this key should be omitted from the response. Do not return a URL that would generate an empty profile.|
  

> **Note:** 
Although the foregoing keys are individually optional, it is recommended that `dep_enrollment_url` and `dep_anchor_certs_url` be implemented or not as a pair.  
  

  

### Examples
  

Below are examples of code that implements `/MDMServiceConfig`.  

  

#### The MDMServiceConfig Request
  

  

##### Request Format
  

```
GET https://mdm.example.com/MDMServiceConfig
```  

  

##### Response Body
  

```
{
    "dep_enrollment_url": "https://mdm.example.com/devicemanagement/mdm/dep_mdm_enroll",
    "dep_anchor_certs_url": "https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs",
    "trust_profile_url": "https://certs.example.com/mdm/trust_profile"
}
```  

It is not required that the URLs refer to the same host as the `/MDMServiceConfig` request, as illustrated by the example for `trust_profile_url`.  

  

#### The dep_anchor_certs_url Key
  

  

##### Request Format
  

```
GET https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs
```  

  

##### Response Body (truncated for clarity)
  

```
["MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIGA1UEAwwbU3ly
\nYWggQ2VydGlmaWNhd...SVVTo9ll1Lv3OJGqBkxPl9TCC\nfYYnArwzlk4qm1tP\n"]
```  

  

#### The trust_profile_url Key
  

  

##### Request Format
  

```
GET https://certs.example.com/mdm/trust_profile
```  

  

##### Response Body (truncated for clarity)
  

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>PayloadContent</key>
   <array>
   	<dict>
   		<key>PayloadContent</key>
   		<data>
   		MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIG
   		...
   		9TCCfYYnArwzlk4qm1tP
   		</data>
   		<key>PayloadDescription</key>
   		<string>Installs the Root certificate for Example Corp.</string>
   		<key>PayloadDisplayName</key>
   		<string>Root certificate for Example Corp</string>
   		<key>PayloadIdentifier</key>
   		<string>com.apple.ssl.certificate</string>
   		<key>PayloadOrganization</key>
   		<string>Example Corp</string>
   		<key>PayloadType</key>
   		<string>com.apple.security.root</string>
   		<key>PayloadUUID</key>
   		<string>B90FA650-5A7D-496A-8C84-0D81C9EBCE6E</string>
   		<key>PayloadVersion</key>
   		<integer>1</integer>
   	</dict>
   </array>
   <key>PayloadDescription</key>
   <string>Configures your device to trust the MDM server.</string>
   <key>PayloadDisplayName</key>
   <string>Trust Profile for Example Corp</string>
   <key>PayloadIdentifier</key>
   <string>com.apple.config.mdm.example.com.ssl</string>
   <key>PayloadScope</key>
   <string>System</string>
   <key>PayloadType</key>
   <string>Configuration</string>
   <key>PayloadUUID</key>
   <string>94cdf5c0-bde0-0131-1ed5-005056831d08</string>
   <key>PayloadVersion</key>
   <integer>1</integer>
</dict>
</plist>
```