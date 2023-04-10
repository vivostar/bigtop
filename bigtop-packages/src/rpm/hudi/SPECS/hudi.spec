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

%define hudi_name hudi
%define hudi_pkg_name hudi%{pkg_name_suffix}
%define hadoop_pkg_name hadoop%{pkg_name_suffix}
%define __os_install_post %{nil}

%define usr_lib_hudi %{parent_dir}/usr/lib/%{hudi_name}
%define etc_hudi %{parent_dir}/etc/%{hudi_name}

Name: %{hudi_pkg_name}
Version: %{hudi_version}
Release: %{hudi_release}
Summary:Apache Hudi is the next generation streaming data lake platform.
URL: http://hudi.apache.org
Group: Development/Libraries
Buildroot: %{_topdir}/INSTALL/%{name}-%{version}
License: Apache License v2.0
Source0: %{hudi_name}-%{hudi_base_version}-src.tar.gz
Source1: do-component-build
#BIGTOP_PATCH_FILES
BuildArch: noarch
Requires: %{hadoop_pkg_name} %{hadoop_pkg_name}-hdfs %{hadoop_pkg_name}-yarn %{hadoop_pkg_name}-mapreduce spark

%description
Apache Hudi is the next generation streaming data lake platform. 
Apache Hudi brings core warehouse and database functionality directly 
to a data lake. Hudi provides tables, transactions, efficient upserts and deletes,
advanced indexes, streaming ingestion services, data clustering/compaction 
optimizations, and concurrency all while keeping your data in open source file 
formats.

%package spark
Summary: Apache Hudi Spark Bundle
Group: System/Daemons
Requires:%{hadoop_pkg_name} %{hadoop_pkg_name}-hdfs %{hadoop_pkg_name}-yarn %{hadoop_pkg_name}-mapreduce spark

%description spark
Apache Hudi Spark Bundle

%prep
%setup -q -n %{hudi_name}-%{hudi_base_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

LIB_DIR=${LIB_DIR:-/usr/lib/hudi}
install -d -m 0755 $RPM_BUILD_ROOT/$LIB_DIR/lib
cp ./packaging/hudi-spark-bundle/target/hudi-spark-bundle_2.11-%{hudi_version}.jar $RPM_BUILD_ROOT/$LIB_DIR/lib

%pre

# Manage configuration symlink
%post

%preun


#######################
#### FILES SECTION ####
#######################
%files spark
%defattr(-,root,root)
/usr/lib/hudi/lib/hudi-spark-bundle_2.11-%{hudi_version}.jar