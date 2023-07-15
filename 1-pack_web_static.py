#!/usr/bin/python3
"""Fabric script that generates .tgz archive
from web_static folder of AirBnB Clone repo"""
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """Return the archive path if correctly generated
    Otherwise, return None"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(path))
    if result.succeeded:
        size = os.stat(path).st_size
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    else:
        return None
