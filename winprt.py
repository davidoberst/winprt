import subprocess
import time
from pyfiglet import figlet_format
import sys
print(figlet_format("winprt", font="small"))
print("v.0.0.1","by davidoberst","https://github.com/davidoberst",sep=" | ")
print("-"*64)
print("[::] 3389     [::] 139      [::] 389     [::] 539      [::] 53")
print("[::] 445      [::] 135      [::] 636     [::] 3268     [::] 88")
print("-"*64)

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
 openPort3389 = (r'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 0') 
 op3389Result = subprocess.run(
    ["powershell", "-Command",openPort3389],
    capture_output=True,
    text=True
 )
 if op3389Result.returncode == 0:
  time.sleep(1)
  print("")
  print(f"Port {port} was openned succesfully! ")
 else:
  print(f"Error opening port {port}")


def openPort445():
 openPort445 = ('Set-Service -Name "LanmanServer" -StartupType Automatic; Start-Service -Name "LanmanServer"') 

def openPort139():
 openPort139 = (
  
 )

def openPort135():
 openPort135 = (
  
 )

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
port = input("Wich port do you want to open? -->  ")
time.sleep(1)
CreateFirewallRule()

