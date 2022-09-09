#!/bin/sh

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e

usage() {
  echo "
usage: $0 <options>
  Required not-so-options:
     --build-dir=DIR             path to azkaban dist.dir
     --prefix=PREFIX             path to install into
     --component=azkabanComponentName  Azkaban component name [solo-server|web-server|exec-server]
  Optional options:
     --comp-dir=DIR               path to install azkaban comp [/usr/lib/azkaban-solo-server]
  "
  exit 1
}

OPTS=$(getopt \
  -n $0 \
  -o '' \
  -l 'build-dir:' \
  -l 'prefix:' \
  -l 'doc-dir:' \
  -l 'comp-dir:' \
  -l 'component:' \
  -- "$@")

if [ $? != 0 ] ; then
    usage
fi

eval set -- "$OPTS"
while true ; do
    case "$1" in
        --build-dir)
        BUILD_DIR=$2 ; shift 2
        ;;
        --prefix)
        PREFIX=$2 ; shift 2
        ;;
        --component)
        COMPONENT=$2 ; shift 2
        ;;
        --doc-dir)
        DOC_DIR=$2 ; shift 2
        ;;
        --comp-dir)
        COMP_DIR=$2 ; shift 2
        ;;
        --solo-server-dir)
        SOLO_SERVER_DIR=$2 ; shift 2
        ;;
        --web-server-dir)
        WEB_SERVER_DIR=$2 ; shift 2
        ;;
        --exec-server-dir)
        EXEC_SERVER_DIR=$2 ; shift 2
        ;;
        --)
        shift ; break
        ;;
        *)
        echo "Unknown option: $1"
        usage
        exit 1
        ;;
    esac
done

for var in PREFIX BUILD_DIR COMPONENT ; do
  if [ -z "$(eval "echo \$$var")" ]; then
    echo Missing param: $var
    usage
  fi
done

SOLO_SERVER_DIR=${SOLO_SERVER_DIR:-/usr/lib/azkaban-solo-server}
WEB_SERVER_DIR=${WEB_SERVER_DIR:-/usr/lib/azkaban-web-server}
EXEC_SERVER_DIR=${EXEC_SERVER_DIR:-/usr/lib/azkaban-exec-server}

if [ "${COMP_DIR}" == "" ]
then
	COMP_DIR=azkaban/${COMPONENT}
fi

# Create the required directories.
install -d -m 0755 ${PREFIX}/usr/lib/$COMP_DIR
# install -d -m 0755 ${PREFIX}/$ETC_DIR/{admin,usersync,kms,tagsync}
# install -d -m 0755 ${PREFIX}/var/{log,run}/ranger/{admin,usersync,kms,tagsync}
# Copy artifacts to the appropriate Linux locations.
cp -r ${BUILD_DIR}/azkaban-${COMPONENT}*/* ${PREFIX}/usr/lib/${COMP_DIR}/
