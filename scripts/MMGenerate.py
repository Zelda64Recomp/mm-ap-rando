import ModuleUpdate
import worlds
from worlds.AutoWorld import AutoWorldRegister
from worlds.mm_recomp import MMRWorld
from Generate import main as generate_main

# register the Majora's Mask Recompiled world type
# we do this to not rely on AutoWorldRegister's auto-discovery
AutoWorldRegister.world_types = { "Majora's Mask Recompiled":  MMRWorld }

# monkey patch the data package to include our world
worlds.network_data_package = DataPackage = {
    "games": {world_name: world.get_data_package_data() for world_name, world in { "Majora's Mask Recompiled":  MMRWorld }.items()},
}

def main():
  generate_main()
