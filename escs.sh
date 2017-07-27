##############################################################################
# clone, libdict, github.
cd ~/projects
git clone git@github.com:iogf/libdict.git libdict-code
##############################################################################
# push, github, libdict.
cd ~/projects/libdict-code
git status
git add *
git commit -a
git push
##############################################################################
# create, development, branch, libdict. 
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# switch, master, branch, change, libdict.
cd ~/projects/libdict-code
git checkout master
##############################################################################
# switch, development, branch, change, libdict.
cd ~/projects/libdict-code
git checkout development
##############################################################################
# undo, changes, libdict, github.
cd ~/projects/libdict-code
git checkout *
##############################################################################
# merge, development, into master, libdict.
cd ~/projects/libdict-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# merge, master, into, development, libdict.
cd ~/projects/libdict-code
git checkout development
git merge master
git push
git checkout development
##############################################################################
# install, libdict.
cd ~/projects/libdict-code
sudo bash -i
python setup.py install
rm -fr build
exit
##############################################################################
# remove, delete, .git, libdict.
find . -name .git -print -exec rm -fr {} \;
##############################################################################
# create, start, run, initialize, ameliarc, libdict.
amelia --init
amelia --run
##############################################################################
# uninstall, delete, remove, libdict, global, package, installation.
rm -fr ~/.amelia
sudo bash -i
rm -fr /usr/local~/projects/python2.7/dist-packages/libdict
exit
##############################################################################
## build, make, a tarball, disutils, libdict.
cd ~/projects/libdict-code
python2 setup.py sdist 
rm -fr dist
rm MANIFEST
##############################################################################
# libdict, pip.
cd ~/projects/libdict-code
python setup.py sdist register upload
rm -fr dist
##############################################################################
# py2 to py3.

cd ~/projects/libdict-code

# Apply them.
2to3  -w .

find . -name "*.bak" -exec rm -f {} \;



