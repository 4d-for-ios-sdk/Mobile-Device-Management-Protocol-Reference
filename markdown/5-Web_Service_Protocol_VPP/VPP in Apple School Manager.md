# VPP in Apple School Manager

 [Configuration Profile Reference - VPP in Apple School Manager](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-DontLinkElementID_6)  
  

## VPP in Apple School Manager
  

In the fall of 2017, VPP was added into Apple School Manager. Apple School Manager is a single destination for schools to manage devices and content for their users. Moving VPP into the Apps and Books section of the Apple School Manager enables program facilitators (also referred to as content managers) to purchase content in the same place that they manage Apple IDs and devices for students and teachers. The purchases made in VPP in Apple School Manager are location based, making it much easier for content managers to move licenses between locations as needed.   

To support location based assets, VPP in Apple School Manager uses location tokens. The location tokens are used by content managers the same way as the legacy VPP tokens are used. Content managers download the location token from the settings page in Apple School Manager and upload it into their MDM. The MDM then has access to the licenses available at that location. Allocating the licenses within the MDM uses the same workflow for both types of licenses.  

  

### Supporting VPP in Apple School Manager 
  

Migrating to VPP in Apple School Manager is recommended, but optional. Licenses assigned when using the legacy token must be managed by the content manager’s legacy token, until they are transfered to a location. Therefore, MDMs will need to support both models of licensing at the same time. Failure to support the legacy and location based models of tokens will create discrepancies between user experiences in Apple School Manager and their MDM.  

To update your MDM to support location based tokens, these steps must be taken:  


* Update API calls to handle the location information being returned for the new VPP in Apple School Manager features. Licenses assigned with the legacy token will not have a location. All of the assets purchased with VPP in Apple School Manager will have additional location information in their API responses. Specifically, these API have been updated to return location information: [getVPPAssetsSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW302), [VPPClientConfigSrv](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/5-Web_Service_Protocol_VPP/webservice.html#//apple_ref/doc/uid/TP40017387-CH8-SW14). 

* Update the MDM UI to show location names for the tokens and assets. Location names are not unique (many schools may have the same name) but location UIDs are unique to a specific location. Displaying the location name to the user is particularly important when location token is about to expire. 

* Refresh license status at appropriate times to maintain an accurate UI. Since licenses can be reallocated in the Apple School Manager, license counts will change outside of the MDM. Refreshing on each page load is recommended.  

* Handle when duplicate tokens are uploaded by different content managers. There is just one location token that needs to be stored, instead of a token per VPP account.  

* Handle new error codes for the location based tokens. 
