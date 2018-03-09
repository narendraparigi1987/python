#!/usr/bin/python2.7

import git
import os
import time
import sys

# OTHER WAY
git_repo = Repo('/var/lib/jenkins/jobs/Test-Yellow-Python-diff/workspace/')
git_repo.git.status()
git_repo.git.add('/var/lib/jenkins/jobs/Test-Yellow-Python-diff/workspace/Diff_DDL.sql')
git_repo.git.config('--global', "mitra502", "Saikat Mitra")
#git_repo.git.config('--global', "saikat.mitra@kpn.com", "user@domain.com")
git_repo.git.status()
git_repo.git.commit(m=' Diff SQL')
git_repo.git.push('--set-upstream', 'origin', 'master')