import re
import ubuntuutils.uu_run_command_container as run_command_container

def check_package_installed(package_name: str) -> bool:
   """
   Checks if the package with the given name is installed using dpkg
   """
   if re.fullmatch(r"^[a-zA-Z0-9\.\-]+$", package_name) is None:
      raise ValueError(f"Invalid package name: {package_name}")
   pkg_chk = run_command_container.RCC(f"dpkg -l {package_name}", False)
   return pkg_chk.return_code == 0