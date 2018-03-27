#!/usr/bin/python3

from fabric.api import env, put, run
import os


# Define the servers and user info
env.hosts = ['54.172.87.188', '34.227.61.41']
env.user = 'ubuntu'


def do_deploy(archive_path):
    '''Distributes an archive to two web servers'''
    if os.path.exists(archive_path):

        # Upload the archive to /tmp/ on the server
        put(archive_path, '/tmp/')

        # Create directory to uncompress tgz file
        rel_archive_path = archive_path[9:]
        # looks like: web_static_201803271315.tgz

        dest = '/data/web_static/releases/{}/'.format(rel_archive_path)[0:-5]
        # looks like: /data/web_static/releases/web_static_201803271315

        run('mkdir -p {}'.format(dest))

        # Uncompress the archive
        run('tar -xzf /tmp/{} -C {}'.format(rel_archive_path, dest))

        # Delete the archive
        run('rm /tmp/{}'.format(rel_archive_path))

        # Move the files out of dest/web_static into dest
        run('mv -n {}/web_static/* {}'.format(dest, dest))

        # Remove that dir, which should be empty
        run('rm -rf {}/web_static'.format(dest))

        # Remove the symlink on the server
        run('rm -rf /data/web_static/current')

        # Create a new symlink on the server pointing to `dest`
        run('ln -s {} /data/web_static/current'.format(dest))

        print('New version deployed successfully!')
        return True

    return False
