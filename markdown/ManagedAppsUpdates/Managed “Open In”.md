# Managed “Open In”

 [Configuration Profile Reference - Managed “Open In”](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/ManagedAppsUpdates/ManagedAppsUpdates.html#//apple_ref/doc/uid/TP40017387-CH10-SW30)  
  

## Managed “Open In”
  

In iOS 7.0 and later, an MDM server can prevent accidental movement of data in and out of managed accounts and apps on a user’s device by installing a profile with a Restrictions payload that specifies the restrictions `allowOpenFromManagedToUnmanaged` and `allowOpenFromUnmanagedToManaged`.  

When the `allowOpenFromManagedToUnmanaged` restriction is specified, an Open In sheet started from within a managed app or account shows only other managed apps and accounts. When the `allowOpenFromUnmanagedToManaged` restriction is specified, an Open In sheet started from within an unmanaged app or account shows only other unmanaged apps and accounts.  

The Open In sheet shown by Safari and AirDrop continues to show all apps and accounts even when these restrictions are specified.  

It is a best practice to use these restrictions to manage data and attachments on a user’s device.