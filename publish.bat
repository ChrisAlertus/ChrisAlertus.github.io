git add --all
git commit -a -m %1
git push -u origin2 source
pelican content -o output -s pelicanconf.py
ghp-import output -r origin2 -b master
git push origin master --force
git checkout source
