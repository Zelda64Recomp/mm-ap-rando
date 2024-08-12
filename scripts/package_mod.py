import zipfile
import sys

site_packages = sys.path[-1]

with zipfile.PyZipFile("build/MMRecompRando.zip", mode="w") as zip_module:
  zip_module.write("lib/archipelago/BaseClasses.py", "BaseClasses.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Generate.py", "Generate.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Fill.py", "Fill.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Main.py", "Main.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/ModuleUpdate.py", "ModuleUpdate.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/MultiServer.py", "MultiServer.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/NetUtils.py", "NetUtils.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Options.py", "Options.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Utils.py", "Utils.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/settings.py", "settings.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/requirements.txt", "requirements.txt", zipfile.ZIP_DEFLATED)

  zip_module.write("lib/archipelago/worlds/__init__.py", "worlds/__init__.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/AutoSNIClient.py", "worlds/AutoSNIClient.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/AutoWorld.py", "worlds/AutoWorld.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/Files.py", "worlds/Files.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/LauncherComponents.py", "worlds/LauncherComponents.py", zipfile.ZIP_DEFLATED)

  # write necessary dependencies
  zip_module.writepy(site_packages + "/requests", "deps")
  zip_module.writepy(site_packages + "/urllib3", "deps")

