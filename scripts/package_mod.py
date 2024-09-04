import zipfile
import sys
import os

site_packages = sys.path[-1]
output_path = sys.argv[1]
print(f"Packaging MMRecompRando to {output_path}/MMRecompRando.zip")

with zipfile.PyZipFile(f"{output_path}/MMRecompRando.zip", mode="w") as zip_module:
  zip_module.write("lib/archipelago/BaseClasses.py", "BaseClasses.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Generate.py", "Generate.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Fill.py", "Fill.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Main.py", "Main.py", zipfile.ZIP_DEFLATED)
  zip_module.write("scripts/DummyModuleUpdate.py", "ModuleUpdate.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/MultiServer.py", "MultiServer.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/NetUtils.py", "NetUtils.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Options.py", "Options.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/Utils.py", "Utils.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/settings.py", "settings.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/requirements.txt", "requirements.txt", zipfile.ZIP_DEFLATED)
  zip_module.write("scripts/MMGenerate.py", "MMGenerate.py", zipfile.ZIP_DEFLATED)

  zip_module.write("scripts/worlds_init.py", "worlds/__init__.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/AutoSNIClient.py", "worlds/AutoSNIClient.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/AutoWorld.py", "worlds/AutoWorld.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/Files.py", "worlds/Files.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/LauncherComponents.py", "worlds/LauncherComponents.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/alttp/EntranceRandomizer.py", "worlds/alttp/EntranceRandomizer.py", zipfile.ZIP_DEFLATED)
  zip_module.write("lib/archipelago/worlds/alttp/Text.py", "worlds/alttp/Text.py", zipfile.ZIP_DEFLATED)
  zip_module.write("scripts/__init__.py", "worlds/alttp/__init__.py", zipfile.ZIP_DEFLATED)

  # write necessary worlds to zip
  for world in ["generic", "mm_recomp"]:
    world_root = "lib/archipelago/worlds/" + world
    for root, dirs, files in os.walk(world_root):
        for file in files:
          full_path = os.path.join(root, file)
          rel_path = os.path.relpath(full_path, world_root)
          if rel_path.startswith("docs/") or rel_path.startswith("test/"):
            continue

          zip_path = os.path.join("worlds", world, rel_path)
          zip_module.write(full_path, zip_path, zipfile.ZIP_DEFLATED)

  # write necessary dependencies to deps folder in zip
  for package in ["typing_extensions.py", "yaml", "schema.py", "websockets"]:
    package_root = site_packages + "/" + package
    if package.endswith(".py"):
        zip_module.write(package_root, "deps/" + package, zipfile.ZIP_DEFLATED)
    else:
      for root, dirs, files in os.walk(package_root):
          for file in files:
              if not file.endswith(".pyc"):
                  full_path = os.path.join(root, file)
                  rel_path = os.path.relpath(full_path, package_root)
                  zip_path = os.path.join("deps", package, rel_path)
                  zip_module.write(full_path, zip_path, zipfile.ZIP_DEFLATED)
