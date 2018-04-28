# Managing OS Software Updates

 [Configuration Profile Reference - Managing OS Software Updates](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/ManagedAppsUpdates/ManagedAppsUpdates.html#//apple_ref/doc/uid/TP40017387-CH10-SW41)  
  

## Managing OS Software Updates
  

MDM commands can restrict updates or initiate updates of the operating system on managed devices. The Apple Software Lookup Service provides a list of available OS versions across platforms to help determine which OS to use.  

  

### Restricting Updates
  

Administrators can delay the availability of OS updates on the device via the [Restrictions Payload](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW13). Use the `forceDelayedSoftwareUpdates` key to enable the feature and the `enforcedSoftwareUpdateDelay` to define how many days the update should be delayed.  

  

### Software Updates
  

Send [Software Update](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW302) commands to the device to update to a specific OS version on the device. Administrators can also control when the device should be updated.  

  

### Apple Software Lookup Service
  

Use the service at [https://gdmf.apple.com/v2/pmv](https://gdmf.apple.com/v2/pmv) to obtain a list of available updates.  

The JSON repsonse contains two lists of available software releases. The `AssetSets` list contains all the releases available for MDMs to push to their supervised devices. The other list, `PublicAssetSets` contains the latest releases available to the general public (non-supervised devices) if they try to upgrade. The `PublicAssetSets` is a subset of the `AssetSets` list.   

Each element in the list contains the product version number of the OS, the posting date, the expiration date, and a list of supported devices for that release. The expiration date is typically set to 90 days after the posting date and if an expiration date is in the past, then that release should be ignored. The device list will match the `ProductName` values from the device, which is returned in the initial `Authenticate` request or the `DeviceInformation` response.  

This is a sample response:    

```
{
  "PublicAssetSets": {
    "iOS": [
      {
        “ProductVersion": "10.0.2",
        "PostingDate": "2017-11-29",
        "ExpirationDate": "2018-02-27",
        "SupportedDevices": ["iPad3,4", "iPad3,5", "iPhone5,1", "iPhone5,2", "iPod7,1"]
      },
      {
        "ProductVersion": "7.0.1",
        "PostingDate": "2017-11-29",
        "ExpirationDate": "2018-02-27",
        "SupportedDevices": ["AppleTV2,1"]
      }
    ]
  },
  "AssetSets": {
    "iOS": [
      {
        "ProductVersion": "10.0.2",
        "PostingDate": "2017-11-29",
        "ExpirationDate": "2018-02-27",
        "SupportedDevices": ["iPad3,4", "iPad3,5", "iPhone5,1", "iPhone5,2", "iPod7,1"]
      },
      {
        "ProductVersion": "7.0.1",
        "PostingDate": "2017-11-29",
        "ExpirationDate": "2018-02-27",
        "SupportedDevices": ["AppleTV2,1"]
      },
      {
        "ProductVersion": "10.0.1",
        "PostingDate": "2017-11-10",
        "ExpirationDate": "2018-02-08",
        "SupportedDevices": ["iPad3,4", "iPad3,5", "iPhone5,1", "iPhone5,2", "iPod7,1"]
      }
    ]
  }
}

```  

Use the product version list to determine which versions are greater than the device’s current OS version. Provide that list of versions to the administrator as potential OS update candidates.  

The assets are grouped by OS platform. Currently, all the assets are under iOS, including tvOS and watchOS.