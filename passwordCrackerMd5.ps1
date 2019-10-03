cls
Function Get-StringHash
{
    param([String] $string, $algorithm = "MD5")
    $StringBuilder = New-Object System.Text.StringBuilder
    [System.Security.Cryptography.HashAlgorithm]::Create($algorithm).ComputeHash([System.Text.Encoding]::UTF8.GetBytes($String))|%{[Void]$StringBuilder.Append($_.ToString("x2"))}
    return $StringBuilder.ToString()
}

Function passwordListDate
{
    param([String]$beginningOfPassword, $dateFormat, [int]$numberOfPasswords)
    $passwordList = New-Object System.Collections.ArrayList
    for($i=$numberOfPasswords; $i -ge 0; $i--)
    {
        $password = $beginningOfPassword + (get-date).AddDays(-$i).ToString($dateFormat)
        $passwordList.Add($password) | Out-Null
    }
    return $passwordList
}

[String]$inputHash = read-host "Enter in the MD5 Hash"
$beginning = read-host "Enter First part of password"
$dateFormat = read-host "Enter date format"
[int]$numPass = read-host "Enter the number of Passwords to Generate"

$listOfPasswords = passwordListDate -beginningOfPassword $beginning -dateFormat $dateFormat -numberOfPasswords $numPass

foreach($password in $listOfPasswords)
{
    [String]$passHash = Get-StringHash -string $password

    if($passHash.Equals($inputHash))
    {
        Write-host "Password Found: $password" -ForegroundColor Green
        break;
    }
    else
    {
        Write-Host "Bad Hash: $password" -ForegroundColor Red
    }
}

