#!/usr/bin/env python3

import rtoml
import os
from pathlib import Path

def get_env():
    util_version = os.getenv("UTIL_VERSION")
    if util_version is None:
        raise Exception("need set environment variable for UTIL_VERSION")
    proto_version = os.getenv("PROTO_VERSION")
    if proto_version is None:
        raise Exception("need set environment variable for PROTO_VERSION")

    return util_version, proto_version

if __name__ == '__main__':
    util_version, proto_version = get_env()

    cargo_path = Path('Cargo.toml')

    project = rtoml.load(cargo_path)
    # print(project)

    try:
        if project['package']['version']:
            project['package']['version'] = proto_version
    except (KeyError):
        pass

    try:
        if project['dependencies']['cloud-util']:
            project['dependencies']['cloud-util'] = "=" + util_version
    except (KeyError):
        pass
    
    try:
        if project['dependencies']['cita_cloud_proto']:
            project['dependencies']['cita_cloud_proto'] = "=" + proto_version
    except (KeyError):
        pass
    
    try:
        if project['dependencies']['crypto_sm']:
            project['dependencies']['crypto_sm']["branch"] = "v" + proto_version
    except (KeyError):
        pass

    try:
        if project['dependencies']['crypto_eth']:
            project['dependencies']['crypto_eth']["branch"] = "v" + proto_version
    except (KeyError):
        pass

    
    rtoml.dump(project, cargo_path, pretty=True)
