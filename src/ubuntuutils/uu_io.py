#!/usr/bin/env python3
import os
import shutil
import logging

def file_read(path: str) -> str:
   """
   Reads the file using the open() function
   """
   if not os.path.exists(path):
      raise Exception(f"File not found: \"{path}\"")
   with open(path, "r") as f:
      return f.read()
   
def file_write_utf8(path: str, contents: str, permission_bits: int | None = None):
   """
   Writes the given contents to the file, overrides the file contents
   Writes the data as utf-8
   """
   if os.path.exists(path):
      if not os.path.isfile(path):
         raise Exception(f"Not a file: {path}")
      with open(path, "r+", encoding="utf-8") as f:
         f.seek(0)
         f.write(contents)
         f.truncate()
   else:
      with open(path, "w", encoding="utf-8") as f:
         f.write(contents)
   if isinstance(permission_bits, int):
      logging.debug(f"<{oct(permission_bits)}> \"{path}\"")
      os.chmod(path, permission_bits)

def clear_directory(directory: str):
   """
   Removes all contents of a directory.
   Use carefully
   """
   if not os.path.isdir(directory):
      raise Exception(f"Not a directory: \"{directory}\"")
   
   for filename in os.listdir(directory):
      file_path = os.path.join(directory, filename)
      try:
         if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
         elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
      except Exception as e:
         logging.error(f'Failed to delete {file_path}. Reason: {e}')
