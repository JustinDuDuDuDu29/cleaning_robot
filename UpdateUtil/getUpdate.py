from git import Repo
import distutils.dir_util as dUtil
from shutil import copytree, ignore_patterns
import os
import stat
import shutil
from os import path


def getUpdateDefault():
    # todo chang to env
    Repo.clone_from("https://github.com/JustinDuDuDuDu29/cleaning_robot.git", "./tmp/Update")


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)



def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def override():
    for root, dirs, files in os.walk("./tmp/Update"):  
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    shutil.rmtree('./tmp/Update/.git', onerror=del_rw)
    dUtil.copy_tree("./tmp/Update", ".")




def rmTmp():
    shutil.rmtree('./tmp/Update', onerror=del_rw)
