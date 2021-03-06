
$lineNumber = 1
$netview = (net.exe view)

$lines = $netview.count

$computers = $netview[3..($lines - 3)]

$computers | ForEach-Object {New-Object psObject -Property @{'Num'=$lineNumber;'Computers'= $_};$lineNumber++} | format-table 'Num', 'Computers' -autosize

$selection = read-host 'Enter the number of the Computer you want to look up: '

$comp = $computers[$selection - 1]

Invoke-Command {get-Process} -ComputerName $comp 
