#!/bin/bash
set -e
workdir=$(dirname $0)
pushd $workdir
mkdir gpg
git clone https://src.fedoraproject.org/rpms/epel-release.git
pushd epel-release
set +e
for branch in $(git branch -rl origin/epel*); do
  git checkout -f $branch RPM-GPG-KEY-EPEL-\*
done
set -e
mv RPM-GPG-KEY-EPEL-* ../gpg/
popd
rm -rf epel-release

git clone https://src.fedoraproject.org/rpms/fedora-repos.git --depth 1
mv fedora-repos/RPM-GPG-KEY-* gpg/
rm -rf fedora-repos

python3 gen_gpg.py -d gpg ../content/security.yml ../public/fedora.gpg 
ls -al ../public/fedora.gpg
gpg --with-fingerprint --show-keys --keyid-format long ../public/fedora.gpg
rm -Rf gpg
popd

