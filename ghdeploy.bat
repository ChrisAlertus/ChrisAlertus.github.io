call pelpub.bat
git checkout -b source
git add -A
git commit -m "Deploying changes"
git push origin2 source
pushd output
git checkout -b master
git add -A
git commit -m "Deploying changes"
git push origin2 master --force
popd
