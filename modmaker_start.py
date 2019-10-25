# A tool for creating a mod
# Usage:
#   1. python ./modmaker_start.py
#   2. Modify contents under go-ethereum-modmaker
#   3. python ./modmaker_end.py
#   4. A modfile will be generated

import subprocess
import os.path
import os
from const import *
import shutil
from mod import rollback_ethereum

maker_dir = os.path.join(base_dir, 'go-ethereum-modmaker')

print("======== DELETING EXISTING MODMAKER DIRECTORY ========")

if os.path.exists(maker_dir):
    shutil.rmtree(maker_dir)

print("======== COPYING ETHEREUM ========")

shutil.copytree(ethereum_dir, maker_dir, symlinks=True)

rollback_ethereum(maker_dir)

