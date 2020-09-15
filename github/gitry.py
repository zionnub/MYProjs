from github import Github

from git import Repo

repo = Repo(pk_repo_path)
o = self.repo.remotes.origin
o.pull()[0]
print(repo.untracked_files)
# First create a Github instance:

# or using an access token
g = Github("")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    #print(repo.name)
    if(repo.name=='MYProjs'):
        # print(dir(repo))
        print(repo.commits_url)
        print(repo.blobs_url)
        r=repo.clone_url
        repo.get_commits




from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare



import pygit
pygit.repos()
pygit.update()

yaml.load()

import GitPython


import git

git.Git(https://github.com/zionnub/MYProjs.git)



import git

g = git.cmd.Git("/Users/sdas/Documents/catalog-content")
g.pull()


repo = git.Repo.init('/Users/sdas/Documents/MYProjs')
with repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))


import os
import re

path = "/Users/sdas/Documents/catalog-content"
path ="/Users/sdas/Documents/catalog-content/noon/pages/desktop"
files = os.listdir(path)

for f in files:
	print(f)

files = os.walk(path)
y=0
for root, directories, files in os.walk(path):
    for name in files:
        x=re.findall("yml$",name)
        if x:
            print(os.path.join(root, name))
            # print(name)
            y=y+1
             # print("Matched'")
print(y)


for root, directories, files in os.walk(path):
	for name in files:
		print(os.path.join(root, name))
        print(name)
        x=re.findall("py$",name)
        if x:
            print("Matched'")
        else:
          print("No match")



for root, directories, files in os.walk(path):
	for name in files:
		print(os.path.join(root, name))
	for name in directories:
		print(os.path.join(root, name))
