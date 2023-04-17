# manifest
Manifests to release CITACloud automated with git repo tool

# usage

## install repo
```bash
curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o repo
chmod +x repo
sudo mv repo /usr/local/bin/
# add next line to ~/.bashrc
export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo'
```

## release
For example, release version is `6.6.5`.

### repo init
```bash
repo init -u git@github.com:cita-cloud/manifest.git -b main -m default.xml
repo sync
```

### tag cita_cloud_proto
Create a tag `6.6.5` for repo cita_cloud_proto.

### publish cloud-common-rs

Create a branch `v6.6.5` for repo cloud-common-rs.

Publish creates cloud-util `0.6.2` and cita_cloud_proto `6.6.5`.

### release micro services

install deps

```bash
pip install rtoml
```

```bash
repo start v6.6.5 --all
export PROTO_VERSION=6.6.5
export UTIL_VERSION=0.6.2
# copy update-deps.py to current dir
repo forall -p -v -c python3 `pwd`/update-deps.py

repo forall -p -v -c git add .
repo forall -p -v -c git commit -m "release v6.6.5"

repo forall -p -v -c git push origin HEAD
```


