from fabric import api
import tempfile
from collective.hostout.hostout import buildoutuser

def deploy():
    "predeploy, uploadeggs, uploadbuildout, buildout and then postdeploy"

    hostout = api.env['hostout']
    hostout.predeploy()
    hostout.uploadeggs()
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

@buildoutuser
def uploadeggs():
    """Release developer eggs and send to host """

    hostout = api.env['hostout']

    # Ensure there is no local pinned.cfg so we don't clobber it
    # Now upload pinned.cfg.
    pinned = "[buildout]\ndevelop=\n[versions]\n"
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(pinned)
    tmp.flush()
    api.put(tmp.name, api.env.path+'/pinned.cfg')
    tmp.close()