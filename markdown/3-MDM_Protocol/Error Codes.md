# Error Codes

 [Configuration Profile Reference - Error Codes](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW77)  
  

## Error Codes
  

The following sections list the error codes currently returned by iOS and OS X devices. Your software should *not* depend on these values, because they may change in future operating system releases. They are provided solely for informational purposes.  

  

### MCProfileErrorDomain 
  


| Code | Meaning |
|-|-|
| 1000 | Malformed profile |
| 1001 | Unsupported profile version |
| 1002 | Missing required field |
| 1003 | Bad data type in field |
| 1004 | Bad signature |
| 1005 | Empty profile |
| 1006 | Cannot decrypt |
| 1007 | Non-unique UUIDs |
| 1008 | Non-unique payload identifiers |
| 1009 | Profile installation failure |
| 1010 | Unsupported field value |
  

  

### MCPayloadErrorDomain 
  


| Code | Meaning |
|-|-|
| 2000 | Malformed payload |
| 2001 | Unsupported payload version |
| 2002 | Missing required field |
| 2003 | Bad data type in field |
| 2004 | Unsupported field value |
| 2005 | Internal Error |
  

  

### MCRestrictionsErrorDomain 
  


| Code | Meaning |
|-|-|
| 3000 | Inconsistent restriction sense (internal error) |
| 3001 | Inconsistent value comparison sense (internal error) |
  

  

### MCInstallationErrorDomain 
  


| Code | Meaning |
|-|-|
| 4000 | Cannot parse profile |
| 4001 | Installation failure |
| 4002 | Duplicate UUID |
| 4003 | Profile not queued for installation |
| 4004 | User cancelled installation |
| 4005 | Passcode does not comply |
| 4006 | Profile removal date is in the past |
| 4007 | Unrecognized file format |
| 4008 | Mismatched certificates |
| 4009 | Device locked |
| 4010 | Updated profile does not have the same identifier |
| 4011 | Final profile is not a configuration profile |
| 4012 | Profile is not updatable |
| 4013 | Update failed |
| 4014 | No device identity available |
| 4015 | Replacement profile does not contain an MDM payload |
| 4016 | Internal error |
| 4017 | Multiple global HTTPProxy payloads |
| 4018 | Multiple APN or Cellular payloads |
| 4019 | Multiple App Lock payloads
|
| 4020 | UI installation prohibited |
| 4021 | Profile must be installed non-interactively |
| 4022 | Profile must be installed using MDM |
| 4023 | Unacceptable payload |
| 4024 | Profile not found |
| 4025 | Invalid supervision
|
| 4026 | Removal date in the past |
| 4027 | Profile requires passcode change |
| 4028 | Multiple home screen layout payloads |
| 4029 | Multiple notification settings layout payloads |
| 4030 | Unacceptable payload in ephemeral multi-user |
| 4031 | Payload contains sensitive user information |
  

  

### MCPasscodeErrorDomain 
  


| Code | Meaning |
|-|-|
| 5000 | Passcode too short |
| 5001 | Too few unique characters |
| 5002 | Too few complex characters |
| 5003 | Passcode has repeating characters |
| 5004 | Passcode has ascending descending characters |
| 5005 | Passcode requires number |
| 5006 | Passcode requires alpha characters |
| 5007 | Passcode expired |
| 5008 | Passcode too recent |
| 5009 | (unused) |
| 5010 | Device locked |
| 5011 | Wrong passcode |
| 5012 | (unused) |
| 5013 | Cannot clear passcode |
| 5014 | Cannot set passcode |
| 5015 | Cannot set grace period |
| 5016 | Cannot set fingerprint unlock |
| 5017 | Cannot set fingerprint purchase |
| 5018 | Cannot set maximum failed passcode attempts |
  

  

### MCKeychainErrorDomain 
  


| Code | Meaning |
|-|-|
| 6000 | Keychain system error |
| 6001 | Empty string |
| 6002 | Cannot create query |
  

  

### MCEmailErrorDomain 
  


| Code | Meaning |
|-|-|
| 7000 | Host unreachable |
| 7001 | Invalid credentials |
| 7002 | Unknown error occurred during validation |
| 7003 | SMIME certificate not found |
| 7004 | SMIME certificate is bad |
| 7005 | IMAP account is misconfigured |
| 7006 | POP account is misconfigured |
| 7007 | SMTP account is misconfigured |
  

  

### MCWebClipErrorDomain 
  


| Code | Meaning |
|-|-|
| 8000 | Cannot install Web Clip |
  

  

### MCCertificateErrorDomain 
  


| Code | Meaning |
|-|-|
| 9000 | Invalid password |
| 9001 | Too many certificates in a payload |
| 9002 | Cannot store certificate |
| 9003 | Cannot store WAPI data |
| 9004 | Cannot store root certificate |
| 9005 | Certificate is malformed |
| 9006 | Certificate is not an identity |
  

  

### MCDefaultsErrorDomain 
  


| Code | Meaning |
|-|-|
| 10000 | Cannot install defaults |
| 10001 | Invalid signer |
  

  

### MCAPNErrorDomain 
  


| Code | Meaning |
|-|-|
| 11000 | Cannot install APN |
| 11000 | Custom APN already installed |
  

  

### MCMDMErrorDomain 
  


| Code | Meaning |
|-|-|
| 12000 | Invalid access rights |
| 12001 | Multiple MDM instances |
| 12002 | Cannot check in |
| 12003 | Invalid challenge response |
| 12004 | Invalid push certificate |
| 12005 | Cannot find certificate |
| 12006 | Redirect refused |
| 12007 | Not authorized |
| 12008 | Malformed request |
| 12009 | Invalid replacement profile |
| 12010 | Internal inconsistency error |
| 12011 | Invalid MDM configuration |
| 12012 | MDM replacement mismatch |
| 12013 | Profile not managed |
| 12014 | Provisioning profile not managed |
| 12015 | Cannot get push token |
| 12016 | Missing identity |
| 12017 | Cannot create escrow keybag |
| 12018 | Cannot copy escrow keybag data |
| 12019 | Cannot copy escrow secret |
| 12020 | Unauthorized by server |
| 12021 | Invalid request type |
| 12022 | Invalid topic |
| 12023 | The iTunes Store ID of the application could not be validated |
| 12024 | Could not validate app manifest |
| 12025 | App already installed |
| 12026 | License for app “<app bundle ID>” could not be found |
| 12027 | Not an app |
| 12028 | Not waiting for redemption |
| 12029 | App not managed |
| 12030 | Invalid URL |
| 12031 | App installation disabled |
| 12032 | Too many apps in manifest |
| 12033 | Invalid manifest |
| 12034 | URL is not HTTPS |
| 12035 | App cannot be purchased |
| 12036 | Cannot remove app in current state |
| 12037 | Invalid redemption code |
| 12038 | App not managed |
| 12039 | (unused) |
| 12040 | iTunes Store login required |
| 12041 | Unknown language code |
| 12042 | Unknown locale code |
| 12043 | Media download failure |
| 12044 | Invalid media type |
| 12045 | Invalid media replacement type |
| 12046 | Cannot validate media ID |
| 12047 | Cannot find VPP assignment |
| 12048 | No update available |
| 12049 | Device passcode must be cleared |
| 12050 | Update scan failed |
| 12051 | Update download in progress |
| 12052 | Update download complete |
| 12053 | Update download requires computer |
| 12054 | Insufficient space for update download |
| 12055 | Insufficient power for update download |
| 12056 | Insufficient network for update download |
| 12057 | Update download failed |
| 12058 | Update install in progress |
| 12059 | Update install requires download |
| 12060 | Insufficient space for update install |
| 12061 | Insufficient power for update install |
| 12062 | Update install failed |
| 12063 | User rejected |
| 12064 | License not found |
| 12065 | System app |
| 12066 | Could not enable MDM lost mode |
| 12067 | Device not in MDM lost mode |
| 12068 | Could not determine device location |
| 12069 | Could not disable MDM lost mode |
| 12070 | Cannot list users |
| 12071 | Specified user does not exist |
| 12072 | Specified user is logged in |
| 12073 | Specified user has data to sync |
| 12074 | Could not delete user |
| 12075 | Specified profile not installed |
| 12076 | Per-user connections not supported |
  

  

### MCWiFiErrorDomain 
  


| Code | Meaning |
|-|-|
| 13000 | Cannot install |
| 13001 | Username required |
| 13002 | Password required |
| 13003 | Cannot create Wi-Fi configuration |
| 13004 | Cannot set up EAP |
| 13005 | Cannot set up proxy |
  

  

### MCTunnelErrorDomain 
  


| Code | Meaning |
|-|-|
| 14000 | Invalid field |
| 14001 | Device locked |
| 14002 | Cloud configuration already exists |
  

  

### MCVPNErrorDomain 
  


| Code | Meaning |
|-|-|
| 15000 | Cannot install VPN |
| 15001 | Cannot remove VPN |
| 15002 | Cannot lock network configuration |
| 15003 | Invalid certificate |
| 15004 | Internal error |
| 15005 | Cannot parse VPN payload |
  

  

### MCSubCalErrorDomain 
  


| Code | Meaning |
|-|-|
| 16000 | Cannot create subscription |
| 16001 | No host name |
| 16002 | Account not unique |
  

  

### MCCalDAVErrorDomain 
  


| Code | Meaning |
|-|-|
| 17000 | Cannot create account |
| 17001 | No host name |
| 17002 | Account not unique |
  

  

### MCDAErrorDomain 
  


| Code | Meaning |
|-|-|
| 18000 | Unknown error |
| 18001 | Host unreachable |
| 18002 | Invalid credentials |
  

  

### MCLDAPErrorDomain 
  


| Code | Meaning |
|-|-|
| 19000 | Cannot create account |
| 19001 | No host name |
| 19002 | Account not unique |
  

  

### MCCardDAVErrorDomain 
  


| Code | Meaning |
|-|-|
| 20000 | Cannot create account |
| 20001 | No host name |
| 20002 | Account not unique |
  

  

### MCEASErrorDomain 
  


| Code | Meaning |
|-|-|
| 21000 | Cannot get policy from server |
| 21001 | Cannot comply with policy from server |
| 21002 | Cannot comply with encryption policy from server |
| 21003 | No host name |
| 21004 | Cannot create account |
| 21005 | Account not unique |
| 21006 | Cannot decrypt certificate |
| 21007 | Cannot verify account |
  

  

### MCSCEPErrorDomain 
  


| Code | Meaning |
|-|-|
| 22000 | Invalid key usage |
| 22001 | Cannot generate key pair |
| 22002 | Invalid CAResponse |
| 22003 | Invalid RAResponse |
| 22004 | Unsupported certificate configuration |
| 22005 | Network error |
| 22006 | Insufficient CACaps |
| 22007 | Invalid signed certificate |
| 22008 | Cannot create identity |
| 22009 | Cannot create temporary identity |
| 22010 | Cannot store temporary identity |
| 22011 | Cannot generate CSR |
| 22012 | Cannot store CACertificate |
| 22013 | Invalid PKIOperation response |
  

  

### MCHTTPTransactionErrorDomain 
  


| Code | Meaning |
|-|-|
| 23000 | Bad identity |
| 23001 | Bad server response |
| 23002 | Invalid server certificate |
  

  

### MCOTAProfilesErrorDomain 
  


| Code | Meaning |
|-|-|
| 24000 | Cannot create attribute dictionary |
| 24001 | Cannot sign attribute dictionary |
| 24002 | Bad identity payload |
| 24003 | Bad final profile |
  

  

### MCProvisioningProfileErrorDomain 
  


| Code | Meaning |
|-|-|
| 25000 | Bad profile |
| 25001 | Cannot install |
| 25002 | Cannot remove |
  

  

### MCDeviceCapabilitiesErrorDomain 
  


| Code | Meaning |
|-|-|
| 26000 | Block level encryption unsupported |
| 26001 | File level encryption unsupported |
  

  

### MCSettingsErrorDomain 
  


| Code | Meaning |
|-|-|
| 28000 | Unknown item |
| 28001 | Bad wallpaper image |
| 28002 | Cannot set wallpaper |
  

  

### MCChaperoneErrorDomain 
  


| Code | Meaning |
|-|-|
| 29000 | Device not supervised |
| 29003 | Bad certificate data |
  

  

### MCStoreErrorDomain 
  


| Code | Meaning |
|-|-|
| 30000 | Authentication failed |
| 30001 | Timed out |
  

  

### MCGlobalHTTPProxyErrorDomain 
  


| Code | Meaning |
|-|-|
| 31000 | Cannot apply credential |
| 31001 | Cannot apply settings |
  

  

### MCSingleAppErrorDomain 
  


| Code | Meaning |
|-|-|
| 32000 | Too many apps |
  

  

### MCSSOErrorDomain 
  


| Code | Meaning |
|-|-|
| 34000 | Invalid app identifier match pattern |
| 34001 | Invalid URL match pattern |
| 34002 | Kerberos principal name missing |
| 34003 | Kerberos principal name invalid |
| 34004 | Kerberos identity certificate cannot be found |
  

  

### MCFontErrorDomain 
  


| Code | Meaning |
|-|-|
| 35000 | Invalid font data |
| 35001 | Failed font installation |
| 35002 | Multiple fonts in a single payload |
  

  

### MCCellularErrorDomain 
  


| Code | Meaning |
|-|-|
| 36000 | Cellular already configured |
| 36001 | Internal error |
  

  

### MCKeybagErrorDomain 
  


| Code | Meaning |
|-|-|
| 37000 | Internal error |
| 37001 | Internal error |
  

  

### MCDomainsErrorDomain 
  


| Code | Meaning |
|-|-|
| 38000 | Invalid domain matching pattern |
  

  

### MCWebContentFilterErrorDomain 
  


| Code | Meaning |
|-|-|
| 40000 | Internal error |
| 40001 | Invalid certificate |
  

  

### MCNetworkUsageRulesErrorDomain
  


| Code | Meaning |
|-|-|
| 41000 | Internal error |
| 41001 | Invalid configuration |
| 41002 | Internal error |
  

  

### MCOSXServerErrorDomain
  


| Code | Meaning |
|-|-|
| 42000 | Cannot create account |
| 42001 | No hostname |
| 42002 | Account not unique |
  

  

### MCHomeScreenLayoutErrorDomain
  


| Code | Meaning |
|-|-|
| 43000 | Multiple Home screen layouts |
  

  

### MCNotificationSettingsErrorDomain
  


| Code | Meaning |
|-|-|
| 44000 | Multiple notification settings |
  

  

### MCEDUClassroomErrorDomain
  


| Code | Meaning |
|-|-|
| 45000 | Cannot install |
| 45001 | Student already installed |
| 45002 | Cannot find certificate |
| 45003 | Bad identity certificate |
  

  

### MCSharedDeviceConfigurationErrorDomain
  


| Code | Meaning |
|-|-|
| 46000 | Multiple shared device configurations |
