from fabric import api


def deploy():
    "predeploy, uploadeggs, uploadbuildout, buildout and then postdeploy"

    hostout = api.env['hostout']
    hostout.predeploy()
    hostout.uploadbuildout()
    hostout.buildout()
    hostout.postdeploy()


def predeploy():
    """Perform any initial plugin tasks. Call bootstrap if needed"""
    hostout = api.env['hostout']
    f = open(hostout.options['versionsfile'], "w")
    f.write("[versions]\n")
    f.close()

    api.env.superfun()
