#!/usr/bin/python3

from fabric.api import env, put, run, local, cd
from datetime import datetime
import os

# Define the servers and user info
env.hosts = ['54.172.87.188', '34.227.61.41']
env.user = 'ubuntu'


def do_clean(number=0):
    '''Deletes out-of-date archives. `number` is the number of archives,
    including the most recent, to keep. If number is 1 or 0, only the most
    recent version will be kept. If the number is 2, only the 2 most recent
    versions will be kept, etc.'''

    # Make a list of all the versions (in web_static/versions)
    # This script should run from the AirBnB_clone directory
    versions = sorted([f for f in os.listdir('versions')])
    trash, keep = versions[:int(number)], versions[int(number):]

    # Delete all the old versions on local machine
    for file in trash:
        local('rm versions/{}'.format(file))

    # Delete all the old versions on the servers
    with cd('/data/web_static/releases'):
        for file in trash:
            run('rm -f {}'.format(file))