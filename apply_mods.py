import subprocess
import os.path
import os
from const import *
from mod import Mod, rollback_ethereum

rollback_ethereum()

# generate mod list
mods_list = []

for dir in os.listdir(mods_dir):
    mod_base_dir = os.path.join(mods_dir, dir)
    if os.path.isdir(mod_base_dir):
        mods_list.append(Mod(mod_base_dir))

for mod in mods_list:
    mod.apply_mod(ethereum_dir)

