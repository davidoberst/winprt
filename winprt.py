import subprocess
import time
from pyfiglet import figlet_format
import sys
print(figlet_format("winprt", font="small"))
print("v.0.0.1","by davidoberst","https://github.com/davidoberst",sep=" | ")
print("-"*58)
print("[1] Open a Port")
print("[1] Close a Port")

def openPortTCP():
 time.sleep(1)
 port = (input("PORT --> "))
 
 comand = (
        f'New-NetFirewallRule '
        f'-DisplayName "OPENPORT" '
        f'-Direction Inbound '
        f'-Protocol TCP '
        f'-LocalPort {port} '
        f'-Action Allow '
        f'-Profile Any'
    )

 CheckIfIsAdmin = ( 
    '([Security.Principal.WindowsPrincipal] '
    '[Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole('
    '[Security.Principal.WindowsBuiltInRole]::Administrator)'
)

 result = subprocess.run(
        ["powershell", "-Command", comand],
        capture_output=True,  
        text=True
    )
 CheckIfIsAdminResult = subprocess.run(["powershell", "-Command",CheckIfIsAdmin])
 
 if CheckIfIsAdminResult == "True":
  print(f"Output {result.returncode}")
  print(result.stdout) 
  print(result.stderr)
 else:
  print("You need to be Admin to run this tool.")
  sys.exit()

option = int(input("--> "))
if option == 1:
 time.sleep(1)
 openPortTCP()