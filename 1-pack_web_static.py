#!/usr/bin/python3
"""Fabric script that generates .tgz archive
from web_static folder of AirBnB Clone repo"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Return the archive path if correctly generated
    Otherwise, return None"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(path))
        return path
    except Exception:
        return None
