
import subprocess
import time
from pyfiglet import figlet_format
import sys

#BANNER  
logo = figlet_format("winprt", font="larry3d")
print("\033[31m" + logo + "\033[0m")
print("\033[33m" + "v.0.0.1 | by davidoberst | https://github.com/davidoberst" + "\033[0m")
print("\033[32m" + "-"*64 + "\033[0m")
print("\033[32m" + "[::] 3389     [::] 139      [::] 389     [::] 539      [::] 53" + "\033[0m")
print("\033[32m" + "[::] 445      [::] 135      [::] 636     [::] 3268     [::] 88" + "\033[0m")
print("\033[32m" + "-"*64 + "\033[0m")

def conditions():
    if port == "3389":
        openPort3389()
    elif port == "139":
        openPort139()
    elif port == "135":
        openPort135()
    elif port == "389":
        openPort389()
    elif port == "539":
        openPort539()
    elif port == "3268":
        openPort3268()
    elif port == "53":
        openPort53()
    elif port == "88":
        openPort88()

#---------CREATE FIREWALL RULE FUNCTION------------------

def CreateFirewallRule():
 print("")
 print("Creating firewall rule...")
 createFirewallRuleComand = (
        f'New-NetFirewallRule '
        f'-DisplayName "OPENPORT" '
        f'-Direction Inbound '
        f'-Protocol TCP '
        f'-LocalPort {port} '
        f'-Action Allow '
        f'-Profile Any'
    )
  #FIREWALL RULE, EXECUTE POWERSHELL SCRIPT AND SAVE THE RESULT
 firewallRuleCreationOutput = subprocess.run(
        ["powershell", "-Command", createFirewallRuleComand],
        capture_output=True,  
        text=True
    )
 CheckIfIsAdmin = (  #CHECK IF THE USER IS ADMIN BEFORE OPEN THE PORT
    '([Security.Principal.WindowsPrincipal] '
    '[Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole('
    '[Security.Principal.WindowsBuiltInRole]::Administrator)'
  )
 
  #CHECK IF IS ADMIN RESULT
 CheckIfIsAdminResult = subprocess.run(
    ["powershell", "-Command", CheckIfIsAdmin],
    capture_output=True,
    text=True
)
 a = firewallRuleCreationOutput.returncode #SAVE THE OUTPUT OF THE PS SCRIPT 

 if CheckIfIsAdminResult.stdout.strip() == "True" and a == 0: 
  print("")
  print(f"Firewall rule was created succesfully!")
  time.sleep(1)
  print("")
  print("Opening the Port...")
  time.sleep(1)
  conditions()
  
 else:
  print("")
  print("Error creating the firewall rule, in order to use the tool you need to have root privileges.") 
#---------END CREATE FIREWALL RULE FUNCTION------------------


#---------OPEN PORTS FUNCTIONS--------------------
def openPort3389(): #ACTIVATE REMOTE DESKTOP IN WINDOWS 
 openPort3389 = r'& { Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 0; Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "UserAuthentication" -Value 1; Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "SecurityLayer" -Value 1; Set-Service -Name TermService -StartupType Automatic; Start-Service -Name TermService; Enable-NetFirewallRule -DisplayGroup "Remote Desktop" }'

 op3389Result = subprocess.run(
    ["powershell", "-Command",openPort3389],
    capture_output=True,
    text=True
 )

 if op3389Result.returncode == 0:
  time.sleep(1)
  print("")
  print("[::] RDP (Remote Desktop) service is now enabled and ready for connections.")
  print("")
 else:
  print(f"Error opening port {port}")


def openPort445():
 openPort445 = ('New-NetFirewallRule -DisplayName "Open Port 445 SMB" -Direction Inbound -Protocol TCP -LocalPort 445 -Action Allow') 
 openPort445Result = subprocess.run (["powershell","-Command",openPort445],capture_output=True,text=True)
 if openPort445Result.returncode == 0:
   time.sleep(1)
   print("[::] SMB (Server Message Block) service is now enabled and ready for connections. ")
 else:
   time.sleep(1)
   print(f"Error opening port {port}")


def openPort139():
 
 openPort139 = (
 'Start-Service lanmanserver;Start-Service lmhosts'
 )
 openPort139Result = subprocess.run(["powershell","-Command",openPort139],capture_output=True,text=True)
 if openPort139Result == 0:
   time.sleep(1)
   print("[::] SMB (Server Message Block) service is now enabled and ready for connections. ")
 else:
   time.sleep(1)
   print(f"Error opening port {port}")

#Start-Service RPCSS


def openPort135():
 openPort135 = (
 'Start-Service RpcEptMapper;Start-Service RPCSS'
 )
 openPort135Result = subprocess.run(["powershell","-Command",openPort135],capture_output=True,text=True)
 if openPort135Result == 0:
   print("[::] RPC Endpoint Mapper (Remote Procedure Call) service is now enabled and ready for connections. ")
 else:
   print(f"Error opening port {port}")
   
   

def openPort389():
 openPort389 = (
  
 )

def openPort539():
 openPort389 = (
  
 )

def openPort3268():
 openPort3268 = (
  
 )

def openPort53():
  openPort53 = (
  
 )


def openPort88():
  openPort388 = (
  
 )

#USER ENTRY
port = input("\033[34m[::] Wich port do you want to open? :  \033[0m")

time.sleep(1)
CreateFirewallRule()

