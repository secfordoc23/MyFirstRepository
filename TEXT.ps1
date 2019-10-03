Add-Type -AssemblyName System.Speech
 
Write-host "Speech to Text"
$input = read-host "Enter Text to be spoken(q to Quit)"
while($input -ne 'q')
{
 
                $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
                $synth.Speak($input)
                Write-host "Speech to Text"
                $input = read-host "Enter Text to be spoken(q to Quit)"
}