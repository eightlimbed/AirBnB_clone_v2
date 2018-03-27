#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
import os


def make_timestamp(year, *args):
    '''Generates a timestamp for .tgz files'''
    timestamp = str(year)
    for arg in args:
        timestamp += str(arg).zfill(2)
    return timestamp


def do_pack():
    '''Generates a .tgz archive from the contents of `web_static`.'''
    now = datetime.utcnow()
    y, m, d, h, s = now.year, now.month, now.day, now.hour, now.second
    timestamp = make_timestamp(y, m, d, h, s)
    filename = 'web_static_{}.tgz'.format(timestamp)
    if not os.path.exists('versions'):
        local('mkdir versions')
    else:
        pass
    result = local('tar -cvzf versions/{} web_static'.format(filename))
    if result.failed:
        return None
    return 'versions/{}'.format(filename)
