import subprocess
import os.path
import os
from const import *

print("======== DOWNLOADING ETHEREUM ========")

# download go-ethereum
if not os.path.exists(os.path.join(base_dir, 'go-ethereum')):
    p = subprocess.Popen(['git', 'clone', 'https://github.com/ethereum/go-ethereum'],
                      cwd=base_dir)
    p.wait()

print("======== BUILDING GETH ========")

# Install prerequisite and make geth. Requires go and C compiler.
p = subprocess.Popen(['make', 'geth'],
                      cwd=ethereum_dir)
p.wait()

print("======== FINISHED ========")