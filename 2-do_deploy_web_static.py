#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""

import os
from fabric.api import *
from datetime import datetime

env.hosts = ['100.25.212.192', '54.236.51.221']
env.user = 'ubuntu'


def do_pack():
    """Return the archive path if correctly generated
    Otherwise, return None"""
    local("mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(path))
    if result.succeeded:
        return path
    else:
        return None

def do_deploy(archive_path):
    """Deploy archive to web server"""
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}'.format(releases_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('sudo rm -rf {}/web_static'.format(releases_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except Exception:
        return False
