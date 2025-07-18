#!/usr/bin/env python3
import subprocess
import shlex
import logging

class RCC:
   def __init__(self, command: str, suppress_output: bool = False):
      """
      Runs given command and waits for it to finish
      std_out and std_err are guaranteed to be strings, and are kept for the lifetime of the object twice (once as raw, once formatted)
      self.std_out and self.std_err contain the raw output
      """
      self.command = command
      command_tokens = shlex.split(command.replace("\n", " ").replace("\t", " ").strip())
      if not suppress_output:
         logging.debug(f"RUNCMD: \"{command}\"")
      
      t = subprocess.run(command_tokens,
         check = False,
         stdout = subprocess.PIPE,
         stderr = subprocess.PIPE,
         universal_newlines = True)
      
      self.return_code = t.returncode
      self.std_out = str(t.stdout)
      self.std_err = str(t.stderr)
      
      self.std_out_formatted = '\n'.join( [f"   [std::out] > {s}" for s in self.std_out.split("\n")] )
      self.std_err_formatted = '\n'.join( [f"   [std::err] > {s}" for s in self.std_err.split("\n")] )
      
      if (not suppress_output):
         logging.debug(f"Command finished:")
         logging.debug(f"   CMD: (RET {self.return_code}) {self.command}")
         if len(self.std_out) > 0:
            logging.debug(self.std_out_formatted)
         if len(self.std_err) > 0:
            logging.debug(self.std_err_formatted)
      #endregion
   
   def Check(self):
      """
      if self.return_code != 0: throws an exception
      Returns self
      """
      if self.return_code != 0:
         logging.debug(f"   CMD: (RET {self.return_code}) {self.command}")
         if len(self.std_out) > 0:
            logging.debug(self.std_out_formatted)
         if len(self.std_err) > 0:
            logging.debug(self.std_err_formatted)

         raise Exception(f"Exit code not 0: {self.return_code}; "
            + f"STDERR: {self.std_err}; "
            + f"STDOUT: {self.std_out}")
      return self
