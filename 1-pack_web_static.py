#!/usr/bin/env python3
"""Distributes an archive to your web servers using the do_deploy function"""

from fabric.api import *
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/ssh/key'

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    directory_name = filename.split('.')[0]
    remote_path = "/tmp/{}".format(filename)
    remote_directory = "/data/web_static/releases/{}".format(directory_name)

    put(archive_path, remote_path)
    run("mkdir -p {}".format(remote_directory))
    run("tar -xzf {} -C {}".format(remote_path, remote_directory))
    run("rm {}".format(remote_path))
    run("mv {}/web_static/* {}".format(remote_directory, remote_directory))
    run("rm -rf {}/web_static".format(remote_directory))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(remote_directory))

    return True
