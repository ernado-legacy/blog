from fabric.api import run, local, env, cd


env.hosts = ['root@msk1.cydev.ru:122']
root = '/src/cydev/'


def update():
    ver = local('git rev-parse HEAD', capture=True)
    with cd(root):
        remote_ver = run('git rev-parse HEAD')
        run('git reset --hard')
        run('git pull origin master')
        run('docker build -t cydev/cydev .')
        run('docker run --rm -v /src/cydev/public:/public cydev/cydev')
