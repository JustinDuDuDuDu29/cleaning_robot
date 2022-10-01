from git import Repo
import distutils.dir_util as dUtil

def getUpdateDefault():
    # todo chang to env
    Repo.clone_from("https://github.com/JustinDuDuDuDu29/cleaning_robot.git", "./tmp/Update")

def override():
    dUtil.copy_tree("./tmp/Update", ".")

# getUpdateDefault()
override()
# NMSL