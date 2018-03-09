import os
from git import *
from git import Repo
from git import Git

git_ssh_identity_file = os.path.expanduser('~/.ssh/id_rsa')
git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file

git_url='ssh://git@git.kpn.org:7999/ter/td-test.git'
repo_dir='temp1'

with Git.custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
   #Repo.clone_from('git@git.kpn.org:7999', '/ter/td-test.git', branch='master')
   Repo.clone_from(git_url, repo_dir)
   print("Done")