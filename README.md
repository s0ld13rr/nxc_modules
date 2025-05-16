# List of custom NetExec modules

## Telegram enumerator

Enumerates existence of Telegram Desktop `tdata` folders across user profiles via SMB, useful for identifying potential session data without triggering excessive noise.

Usage: 

```
cp telegram.py ~/.nxc/modules/telegram.py
nxc smb 10.0.0.0/8 -u 'user' -p 'password' -M telegram
```
