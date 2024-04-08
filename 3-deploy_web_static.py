#!/usr/bin/python3
"""
    Creates archive and deploys it
"""
from fabric.api import local, run, put, env
from os.path import exists, isdir
from datetime import datetime
from os import stat

env.hosts = ['52.87.255.243', '100.26.155.240']


date = datetime.now()


def do_pack():
    """generates a .tgx archive from web_static"""
    path = "versions/web_static_{}.tgz".format(
            date.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    print("Packing web_static to {}".format(path))
    pack = local("tar -cvzf " + path + " ./web_static")
    file_size = stat(path).st_size
    print("web_static packed: {} -> {} Bytes".format(path, file_size))
    if pack.succeeded:
        return path
    return None
