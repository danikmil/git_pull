#update all module

import os
from git import Repo

root_dir = '.' 
directories = [ name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name)) ]

for module_dir in directories:
    try:
        print "name of module -->>", module_dir
        current_dir = os.getcwd()
        target_dir = current_dir + '/' + module_dir
        os.chdir(target_dir)
        branch = Repo(target_dir).active_branch
        branch_name = branch.name
        os.system('git pull origin %s' % (branch_name, ))
        print "Module %s is successfully loading" % module_dir
        os.chdir(current_dir)
    except Exception, e:
        print "ERROR -->> %s" % e

print 'Well Done'

