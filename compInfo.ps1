cls 
#Gets Domain
write-host "Domain: $env:userdomain" 
#Gets User Name
write-host "User Name: $env:username" 
#Gets Computer Name
write-host "Computer: $env:computername"
#Gets current IP address being used
$netAddress = ipconfig | Select-String ipv4
$na = $netAddress[0] -replace "   IPv4 Address. . . . . . . . . . . :", "IP Address:" 
Write-host $na
#Gets the Model of the Computer
$strModel = (gwmi win32_computerSystem).model
write-host "Model:"$strModel
#Gets Serial Number of the Computer
$Serial = (gwmi win32_bios).SerialNumber
write-host "Serial Number:"$Serial