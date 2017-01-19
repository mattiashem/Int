from fabric.api import run, env, local
from fabric.context_managers import cd
from fabric.operations import put, sudo
from fabric.contrib.project import rsync_project


def setupInt():
    print("Setup Servers")
    print("Get access to Openstack")
    local("source /ac.sh")
    with open('serverList.txt') as f:
      for line in f:
        host = "{0}.fareonline.net".format(line.replace('\n',''))

        print "Setup Int Server {0} in Openstack".format(host)
        local("nova boot --flavor IntServer --image foCentos --nic net-id=fa344cab-61bf-4ec5-b4a8-52b8017b84c7 \
  --security-group default --key-name Int {0}".format(host))



        print "Setup loadbalanser {0} in treafik".format(host)
        print "trefik config"




def delInt():
    local("source /ac.sh")
    with open('serverList.txt') as f:
      for line in f:
        host = "{0}.fareonline.net".format(line.replace('\n',''))
        print "Delete Int Server {0} in Openstack".format(host)
        local("nova delete {0}".format(host))