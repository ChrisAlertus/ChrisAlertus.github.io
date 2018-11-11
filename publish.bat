git add --all
git commit -a -m %1
git push -u origin pelican-src
pelican content -o output -s pelicanconf.py
ghp-import output -r origin2 -b master
git push -u origin master
git checkout pelican-src
