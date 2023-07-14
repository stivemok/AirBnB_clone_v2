#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""
import os
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ['100.25.212.192', '54.236.51.221']
env.user = 'ubuntu'


def deploy():
    """Deploy archive files"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)


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
