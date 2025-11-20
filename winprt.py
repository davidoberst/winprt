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

#---------CREATE FIREWALL RULE------------------
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

#---------POWERSHELL SCRIPTS AND RESULTS------------------

 CheckIfIsAdmin = (  #CHECK IF THE USER IS ADMIN BEFORE OPEN THE PORT
    '([Security.Principal.WindowsPrincipal] '
    '[Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole('
    '[Security.Principal.WindowsBuiltInRole]::Administrator)'
)
 #FIREWALL RULE, EXECUTE POWERSHELL SCRIPT AND SAVE THE RESULT
 firewallRuleCreationOutput = subprocess.run(
        ["powershell", "-Command", createFirewallRuleComand],
        capture_output=True,  
        text=True
    )
 #CHECK IF IS ADMIN RESULT
 CheckIfIsAdminResult = subprocess.run(
    ["powershell", "-Command", CheckIfIsAdmin],
    capture_output=True,
    text=True
)
 a = firewallRuleCreationOutput.returncode #SAVE THE OUTPUT OF THE PS SCRIPT 

 #CHECK IF THE USER IS ADMIN CALLING 
 if CheckIfIsAdminResult.stdout.strip() == "True" and a == 0: 
  print("")
  print(f"Firewall rule was created succesfully!")
  time.sleep(1)
  print("")
  print("Opening the Port...")
  time.sleep(1)
 else:
  print("")
  print("Error creating the firewall rule, in order to use the tool you need to have root priviliges.")
  
#USER ENTRY
port = input("Wich port do you want to open? -->  ")
time.sleep(1)
CreateFirewallRule()

