from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project

import logging
logging.basicConfig()

env.user = 'cydev'
env.base_dir = '/blog.cydev'
env.use_ssh_config = True
env.hosts = ['cydev.ru']


def deploy(branch='master', restart='yes'):
    with cd(env.base_dir):
        rsync_project(local_dir="public", remote_dir=env.base_dir, exclude='.git')
