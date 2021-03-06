mode con: cols=75 lines=70
Import-module ActiveDirectory

# Function to Display ATS with date centered
Function logo
{
    cls
    $currentDate = get-date -format F
    write-host
    write-host "            ZZZZZZ   7ZZZZZZZZZZZZZZZZZ   ZZZZZZZZZZZZZ  "
    write-host "           ZZZZZZZZ  ZZZZZZZZZZZZZZZZZZ  ZZZZZZZZZZZZZZZ "
    write-host "          ZZZZZZZZZ        ZZZZZZ       ZZZZZZ     ZZZZZZ"
    write-host "         ZZZZ ZZZZZ       ZZZZZZZ       ZZZZZZZZZ        "
    write-host "        ZZZZ  ZZZZZZ      ZZZZZZ        ZZZZZZZZZZZZZZ   "
    write-host "       ZZZZ   ZZZZZZ      ZZZZZZ         ZZZZZZZZZZZZZZ  "
    write-host "      ZZZZ    ZZZZZZ     ZZZZZZZ             ZZZZZZZZZZZ "
    write-host "     ZZZZZZZZZZZZZZZ7    ZZZZZZ       ZZZZZZ     ZZZZZZZ "
    write-host "    ZZZZZZZZZZZZZZZZZ    ZZZZZZ       ZZZZZZZ    ZZZZZZ  "
    write-host "   ZZZZZZZZZZZZZZZZZZ    ZZZZZZ        ZZZZZZZZZZZZZZZ   "
    write-host "  ZZZZZZ       ZZZZZZ   ZZZZZZ         ZZZZZZZZZZZZ      "
    write-host "----------------------------------------------------------"
    write-host "`t" $currentDate
    write-host
    
}

Function accountExpireDate
{
    $expire = ""
    $userName = $input
    
    #(([datetime]::FromFileTime((get-aduser $user -properties "msDS-UserPasswordExpiryTimeComputed")."msDS-UserPasswordExpiryTimeComputed"))-(get-date)).days
    if($userName.passwordneverexpires -eq $true)
    {
        $expire = "never"    
    }
    else
    {
        $expire = (([datetime]::FromFileTime((get-aduser -identity $userName -properties "msDS-UserPasswordExpiryTimeComputed")."msDS-UserPasswordExpiryTimeComputed"))-(get-date)).days
    }
    
    return $expire
}

Function userSearch
{
    #Variable declaration
    $name = "*"
    $name += $input
    $name += "*" 
    $lineNumber = 1
    
    #Searches for user accounts that are "like" the user's input
    $user = Get-aduser -SearchBase "DC=atsdom,DC=advancedtech,DC=com" -ldapfilter "(|(samaccountname=$name)(displayname=$name))"
    #$user = Get-ADUser -SearchBase "DC=atsdom,DC=advancedtech,DC=com" -Filter {(displayname -like $name) -or (samaccountname -like $name)} -properties *, "msDS-UserPasswordExpiryTimeComputed"
    if($user.count -le '0')
    {
        logo
        write-host "There was no user accounts found"
    }
   
    elseif($user.count -ge '1')
    {
        logo
        #Formats found users to a numbered table displaying number, username, Displayname, and account locked status
        $user | ForEach-Object {New-Object psObject -Property @{'Num'=$lineNumber;'Display Name'= $_.displayname; 'Username' = $_.samaccountname; 'LockedOut' = $_.lockedout; 'Expired' = $_.passwordexpired; 'Expire Date' = ($_ | accountExpireDate)};$lineNumber++} | format-table 'Num', 'Username', 'Display Name', 'LockedOut', 'Expired', 'Expire Date' -autosize
        
        
        $selection = read-host 'Enter the number of which user you want to look up: '

        $username = $user[$selection - 1].samaccountname

        logo
    
        net user $username /domain
    }
    else
    {
        logo
        write-host "There was no user accounts found"
    }
    <#
    logo
    
    #Formats found users to a numbered table displaying number, username, Displayname, and account locked status
    $user | ForEach-Object {New-Object psObject -Property @{'Num'=$lineNumber;'Display Name'= $_.displayname; 'Username' = $_.samaccountname; 'LockedOut' = $_.lockedout};$lineNumber++} | format-table 'Num', 'Username', 'Display Name', 'LockedOut' -autosize
    
    $selection = read-host 'Enter the number of which user you want to look up: '

    $username = $user[$selection - 1].samaccountname

    logo
    
    net user $username /domain
    #>
    
    #Code to unlock a User account if it is locked out only and prompts for credentials for elevated rights
    <#
    if(($user[$selection - 1].lockedout) -eq $true)
    {
        unlock-adaccount -identity $username -confirm -credential PSCredential
        
    }
    #>
    $user = ""
    $username = ""
    $lineNumber = ""
    
}

logo

write-host "----------------------------------"
write-host "Enter q (case sensitive) to quit"
write-host "----------------------------------"
$name = read-host 'Enter Name'


While ($name -ne "q"){

#Calls the userSearch function and pipes in user input
$name | userSearch 

$name = ""

write-host "----------------------------------"
write-host "Enter q (case sensitive) to quit"
write-host "----------------------------------"
$name = read-host 'Enter Name'
}

