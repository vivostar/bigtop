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

%define azkaban_name azkaban
%define lib_azkaban /usr/lib/%{azkaban_name}
%define var_lib_azkaban /var/lib/%{azkaban_name}
%define var_run_azkaban /var/run/%{azkaban_name}
%define var_log_azkaban /var/log/%{azkaban_name}
%define bin_azkaban /usr/lib/%{azkaban_name}/bin
%define etc_azkaban /etc/%{azkaban_name}
# %define config_azkaban %{etc_azkaban}/conf
%define bin /usr/bin
%define man_dir /usr/share/man
%define azkaban_services solo-server web-server exec-server
# %define lib_hadoop_client /usr/lib/hadoop/client
# %define lib_hadoop_yarn /usr/lib/hadoop-yarn/

%if  %{?suse_version:1}0
%define doc_azkaban %{_docdir}/azkaban
%define alternatives_cmd update-alternatives
%else
%define doc_azkaban %{_docdir}/azkaban-%{azkaban_version}
%define alternatives_cmd alternatives
%endif

# disable repacking jars
%define __os_install_post %{nil}

Name: azkaban
Version: %{azkaban_version}
Release: %{azkaban_release}
Summary: Lightning-Fast Cluster Computing
URL: http://azkaban.apache.org/
Group: Development/Libraries
BuildArch: noarch
License: ASL 2.0
Source0: %{azkaban_name}-%{azkaban_version}.tar.gz
Source1: do-component-build 
Source2: install_%{azkaban_name}.sh
Source3: bigtop.bom
#BIGTOP_PATCH_FILES
Requires: bigtop-utils >= 0.7 
Requires(preun): /sbin/service

%global initd_dir %{_sysconfdir}/init.d

%if  %{?suse_version:1}0
# Required for init scripts
Requires: insserv
%global initd_dir %{_sysconfdir}/rc.d

%else
# Required for init scripts
Requires: /lib/lsb/init-functions

%global initd_dir %{_sysconfdir}/rc.d/init.d

%endif

%description 
Azkaban

%package -n azkaban-solo-server
Summary: Azkaban Solo Server
Group: Development/Libraries
%description -n azkaban-solo-server
Azkaban Solo Server

%package -n azkaban-web-server
Summary: Azkaban Web Server
Group: Development/Libraries
%description -n azkaban-web-server
Azkaban Web Server

%package -n azkaban-exec-server
Summary: Azkaban Exec Server
Group: Development/Libraries
%description -n azkaban-exec-server
Azkaban Exec Server

%prep
%setup -n %{azkaban_name}-%{azkaban_base_version}

#BIGTOP_PATCH_COMMANDS

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT

bash $RPM_SOURCE_DIR/%{SOURCE2} \
          --build-dir=`pwd`         \
          --source-dir=$RPM_SOURCE_DIR \
          --prefix=$RPM_BUILD_ROOT  

%pre
getent group azkaban >/dev/null || groupadd -r azkaban
# getent passwd azkaban >/dev/null || useradd -c "Azkaban" -s /sbin/nologin -g azkaban -r -d %{var_lib_azkaban} azkaban 2> /dev/null || :

# %post

# %preun

#######################
#### FILES SECTION ####
#######################
%files -n azkaban-solo-server
%defattr(-,root,root,755)
%{lib_azkaban}/solo-server

%files -n azkaban-web-server
%defattr(-,root,root,755)
%{lib_azkaban}/web-server

%files -n azkaban-solo-server
%defattr(-,root,root,755)
%{lib_azkaban}/exec-server