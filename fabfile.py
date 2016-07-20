from fabric.api import task, run, put, cd, sudo, settings

homefolder = 'webportal'
PORT = 7000   # Keep it the same with portal.PORT


@task
def deploy():
    run('rm -rf %s && mkdir %s' % (homefolder, homefolder))
    sudo('apt install -y virtualenv')
    with cd(homefolder):
        put('portal.py', '.')
        put('dserver.py', '.')
        put('requirements.txt', '.')
        run('virtualenv -p /usr/bin/python3 venv')
        run('. venv/bin/activate && pip install -r requirements.txt')
        cnt = 0
        retry = 5
        while cnt < retry:
            cnt = cnt + 1
            with settings(warn_only=True):
                run('. venv/bin/activate && python dserver.py && sleep 5')
                result = run('curl -i -X GET http://localhost:%s' % PORT)
                if result.succeeded:
                    break
