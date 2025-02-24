#!/usr/bin/env python3
import subprocess
import shlex
import os
import pwd
import grp
import shutil

def chk_usr_exists(usr_name: str) -> bool:
   try:
      pwd.getpwnam(usr_name)
      return True
   except KeyError:
      return False
   
def chk_grp_exists(grp_name: str) -> bool:
   try:
      grp.getgrnam(grp_name)
      return True
   except KeyError:
      return False
