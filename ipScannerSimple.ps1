cls

Function StringVersions {
param([string]$inputString)
$obj = New-Object PSObject
$obj | Add-Member NoteProperty STATUS($array[1])
$obj | Add-Member NoteProperty HostName($array[2])
$obj | Add-Member NoteProperty IPAddress($array[3])
$obj | Add-Member NoteProperty MACAddress($array[4])
#$obj | Add-Member NoteProperty Comments($array[5])
  Write-Output $obj
}

$netAddress = ipconfig | Select-String ipv4
$na = $netAddress[0] -replace "   IPv4 Address. . . . . . . . . . . :", ""   
write-host $na  
    foreach($i in 1..15)
        {
            $array = @("", "", "", "", "", "") 
 
            $ip = "192.168.1.$i"
            if(test-Connection $ip -Count 1 -quiet){
                try
                {
                    if($ip -eq $na){
                        $array = @("black", "FOUND", "", "", "", "THIS DEVICE")
                        }
                        
                    else{
                        $hostName = [System.Net.Dns]::GetHostByAddress($ip).HostName
                        $macLine = arp -a $ip 
                        $macFormat = $macLine[3] -replace $ip + "       ", ""
                        $macAdd = $macFormat -replace "     dynamic", " "
            
                        $array = @("green", "FOUND", $HostName, $ip, $macAdd, "")
                    
                        
                        }
                    
                }
                
                catch
                {
                    if($ip -eq $na){
                        $array = @("black", "FOUND", "", "", "", "THIS DEVICE")
                        }
                        
                    else{
                        $macLine = arp -a $ip 
                        $macFormat = $macLine[3] -replace $ip+ "       ", ""
                        $macAdd = $macFormat -replace "     dynamic", " "
                
                        $array = @("blue", "FOUND", "", $ip, $macAdd, "Cannot Resolve Host Name")
                        }
                    
                        continue
                }
                
            
            }
            
            else{ $array = @("darkred", "NOT FOUND", "Cannot find Hostname", "", "Cannot find MAC address", "Cannot find Hostname or MAC address") }
            
            
            StringVersions $item
            
           

                
                
        }
        


