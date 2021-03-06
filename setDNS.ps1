function Set-IPAddress { 
        param(    [string]$networkinterface = "Local Area Connection", 
            [string]$ip , 
            [string]$mask ="255.255.255.0", 
            #$(read-host "Enter the subnet mask (ie 255.255.0.0)"), 
            [string]$gateway ="17.24.16.254" , 
            #$(read-host "Enter the default gateway (ie 10.215.1.250"), 
            [string]$dns1 = "8.8.8.8", 
            [string]$dns2 = "8.8.4.4", 
            [string]$registerDns = "TRUE" 
     )    
.... 
function Get-IPAddress { 
     param(    [string]$networkinterface = "Local Area Connection"  ) 
....