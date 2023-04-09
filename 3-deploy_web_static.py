#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""
import os
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'

def do_pack():
    """Create a tgz archive of web_static folder"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except:
        return None

def do_deploy(archive_path):
    """Distribute archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(file_name))
        folder_name = file_name.split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, folder_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(folder_name, folder_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(folder_name))
        return True
    except:
        return False

def deploy():
    """Pack and distribute an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
