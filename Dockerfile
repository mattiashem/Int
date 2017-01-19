from fareoffice/base
#
# Setup and use for seting up servers on openstack for int.
# 1. Creates a new server in openstack
# 2. Setup Loadbalanser teafik
# 3. Clean out INT Env
# 
#
#Setup python and openstack client
RUN yum install epel-release -y
RUN yum -y install python-pip gcc make python-devel openssl-devel
RUN pip install --upgrade pip
RUN pip install python-openstackclient fabric


RUN mkdir /code
ADD code/ /code
COPY code/ac.sh /ac.sh

WORKDIR /code

CMD fab show
