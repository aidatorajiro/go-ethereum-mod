import subprocess
import os.path
import os

class Mod:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        ## TODO: do some metadata processing

    def apply_mod(self, ethereum_dir):
        pass


def rollback_ethereum(ethereum_dir):
    p = subprocess.Popen(['git', 'reset', '--hard'], cwd=ethereum_dir)
    p.wait()
    p = subprocess.Popen(['git', 'clean', '-fd'], cwd=ethereum_dir)
    p.wait()

