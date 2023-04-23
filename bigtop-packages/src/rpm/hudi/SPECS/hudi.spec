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
Requires: %{hadoop_pkg_name} %{hadoop_pkg_name}-hdfs %{hadoop_pkg_name}-yarn %{hadoop_pkg_name}-mapreduce

%description
Apache Hudi is the next generation streaming data lake platform. 
Apache Hudi brings core warehouse and database functionality directly 
to a data lake. Hudi provides tables, transactions, efficient upserts and deletes,
advanced indexes, streaming ingestion services, data clustering/compaction 
optimizations, and concurrency all while keeping your data in open source file 
formats.

%define package_macro() \
%package %1 \
Summary: apache hudi %1 bundle \
Group: System/Daemons \
%description %1 \
apache hudi %1 bundle 

%package_macro spark
%package_macro flink
%package_macro datahub-sync
%package_macro timeline-server
%package_macro kafka-connect
%package_macro trino
%package_macro utilities
%package_macro utilities-slim
%package_macro aws
%package_macro gcp
%package_macro hadoop-mr
%package_macro presto
%package_macro cli
%package_macro hive-sync

%prep
%setup -q -n %{hudi_name}-%{hudi_base_version}

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

LIB_DIR=${LIB_DIR:-/usr/lib/hudi}
install -d -m 0755 $RPM_BUILD_ROOT/$LIB_DIR/lib

for comp in spark utilities utilities-slim cli        
do 
cp ./packaging/hudi-${comp}-bundle/target/hudi-${comp}-bundle_2.11-%{hudi_version}.jar $RPM_BUILD_ROOT/$LIB_DIR/lib
done

for comp in datahub-sync timeline-server kafka-connect trino gcp \
            aws hadoop-mr presto hive-sync          
do 
cp ./packaging/hudi-${comp}-bundle/target/hudi-${comp}-bundle-%{hudi_version}.jar $RPM_BUILD_ROOT/$LIB_DIR/lib
done

cp ./packaging/hudi-flink-bundle/target/hudi-flink1.16-bundle-%{hudi_version}.jar $RPM_BUILD_ROOT/$LIB_DIR/lib

%pre

# Manage configuration symlink
%post

%preun


#######################
#### FILES SECTION ####
#######################
# Scala Jar file management RPMs
%define jar_scala_macro() \
%files %1 \
%defattr(-,root,root) \
%{usr_lib_hudi}/lib/hudi-%1-bundle_2.11-%{hudi_version}.jar

# Java Jar file management RPMs
%define jar_macro() \
%files %1 \
%defattr(-,root,root) \
%{usr_lib_hudi}/lib/hudi-%1-bundle-%{hudi_version}.jar

%jar_scala_macro spark
%jar_macro datahub-sync
%jar_macro timeline-server
%jar_macro kafka-connect
%jar_macro trino
%jar_scala_macro utilities
%jar_scala_macro utilities-slim
%jar_macro aws
%jar_macro gcp
%jar_macro hadoop-mr
%jar_macro presto
%jar_scala_macro cli
%jar_macro hive-sync

%files flink
%defattr(-,root,root) 
%{usr_lib_hudi}/lib/hudi-flink1.16-bundle-%{hudi_version}.jar