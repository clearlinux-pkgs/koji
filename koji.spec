#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : koji
Version  : 1.21.1
Release  : 134
URL      : https://pagure.io/koji/archive/koji-1.21.1/koji-koji-1.21.1.tar.gz
Source0  : https://pagure.io/koji/archive/koji-1.21.1/koji-koji-1.21.1.tar.gz
Summary  : Build system tools
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0 LGPL-2.1
Requires: koji-bin = %{version}-%{release}
Requires: koji-license = %{version}-%{release}
Requires: koji-python = %{version}-%{release}
Requires: koji-python3 = %{version}-%{release}
Requires: koji-services = %{version}-%{release}
Requires: Cheetah3
Requires: git
Requires: koji-doc
Requires: libcomps
Requires: librepo
Requires: psycopg2
Requires: pyOpenSSL
Requires: python-dateutil
Requires: python-multilib
Requires: requests
Requires: requests-kerberos
Requires: rpm
Requires: six
BuildRequires : Cheetah3
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : git
BuildRequires : libcomps
BuildRequires : librepo
BuildRequires : nose
BuildRequires : pkgconfig(systemd)
BuildRequires : psycopg2
BuildRequires : pyOpenSSL
BuildRequires : python-dateutil
BuildRequires : python-mock
BuildRequires : python-multilib
BuildRequires : requests
BuildRequires : requests-kerberos
BuildRequires : requests-mock
BuildRequires : rpm
BuildRequires : six
BuildRequires : systemd-dev
Patch1: 0001-Change-install-dir-to-usr-bin.patch
Patch2: 0002-Do-not-build-kojivm.patch
Patch3: 0003-builder-use-sudo-to-call-mock.patch
Patch4: 0004-Use-old-version-of-NSS-forking-behavior.patch
Patch5: 0005-Close-koji-db-connections.patch
Patch6: 0006-Force-python3-for-executables.patch
Patch7: 0007-Remove-check-for-existence-of-config-file.patch

%description
Koji is a system for building and tracking RPMS.  The base package
contains shared libraries and the command-line interface.

%package bin
Summary: bin components for the koji package.
Group: Binaries
Requires: koji-license = %{version}-%{release}
Requires: koji-services = %{version}-%{release}

%description bin
bin components for the koji package.


%package doc
Summary: doc components for the koji package.
Group: Documentation

%description doc
doc components for the koji package.


%package extras
Summary: extras components for the koji package.
Group: Default

%description extras
extras components for the koji package.


%package license
Summary: license components for the koji package.
Group: Default

%description license
license components for the koji package.


%package python
Summary: python components for the koji package.
Group: Default
Requires: koji-python3 = %{version}-%{release}

%description python
python components for the koji package.


%package python3
Summary: python3 components for the koji package.
Group: Default
Requires: python3-core

%description python3
python3 components for the koji package.


%package services
Summary: services components for the koji package.
Group: Systemd services

%description services
services components for the koji package.


%prep
%setup -q -n koji-koji-1.21.1
cd %{_builddir}/koji-koji-1.21.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591734954
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags}


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test3 PYTHON=python3 || :

%install
export SOURCE_DATE_EPOCH=1591734954
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/koji
cp %{_builddir}/koji-koji-1.21.1/COPYING %{buildroot}/usr/share/package-licenses/koji/c4b884eb09c7b65e2a469c7dbaf2f927e2af8e9f
%make_install KOJI_MINIMAL=1 PYTHON=/usr/bin/python3
## Remove excluded files
rm -f %{buildroot}/usr/libexec/kojid/mergerepos
## install_append content
mkdir -p %{buildroot}/usr/share/doc/koji/
mv %{buildroot}/etc %{buildroot}/usr/share/doc/koji/
cp -a docs  %{buildroot}/usr/share/doc/koji/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/koji
/usr/bin/koji-gc
/usr/bin/koji-shadow
/usr/bin/koji-sidetag-cleanup
/usr/bin/koji-sweep-db
/usr/bin/kojid
/usr/bin/kojira

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/koji/*

%files extras
%defattr(-,root,root,-)
/usr/share/koji-hub/__init__.py
/usr/share/koji-hub/kojihub.py
/usr/share/koji-hub/kojixmlrpc.py
/usr/share/koji-web/lib/kojiweb/__init__.py
/usr/share/koji-web/lib/kojiweb/util.py
/usr/share/koji-web/scripts/api.chtml
/usr/share/koji-web/scripts/archiveinfo.chtml
/usr/share/koji-web/scripts/archivelist.chtml
/usr/share/koji-web/scripts/buildinfo.chtml
/usr/share/koji-web/scripts/buildrootinfo.chtml
/usr/share/koji-web/scripts/buildrootinfo_cg.chtml
/usr/share/koji-web/scripts/builds.chtml
/usr/share/koji-web/scripts/buildsbystatus.chtml
/usr/share/koji-web/scripts/buildsbytarget.chtml
/usr/share/koji-web/scripts/buildsbyuser.chtml
/usr/share/koji-web/scripts/buildtargetedit.chtml
/usr/share/koji-web/scripts/buildtargetinfo.chtml
/usr/share/koji-web/scripts/buildtargets.chtml
/usr/share/koji-web/scripts/channelinfo.chtml
/usr/share/koji-web/scripts/clusterhealth.chtml
/usr/share/koji-web/scripts/error.chtml
/usr/share/koji-web/scripts/externalrepoinfo.chtml
/usr/share/koji-web/scripts/fileinfo.chtml
/usr/share/koji-web/scripts/hostedit.chtml
/usr/share/koji-web/scripts/hostinfo.chtml
/usr/share/koji-web/scripts/hosts.chtml
/usr/share/koji-web/scripts/imageinfo.chtml
/usr/share/koji-web/scripts/includes/footer.chtml
/usr/share/koji-web/scripts/includes/header.chtml
/usr/share/koji-web/scripts/index.chtml
/usr/share/koji-web/scripts/index.py
/usr/share/koji-web/scripts/notificationedit.chtml
/usr/share/koji-web/scripts/packageinfo.chtml
/usr/share/koji-web/scripts/packages.chtml
/usr/share/koji-web/scripts/packagesbyuser.chtml
/usr/share/koji-web/scripts/recentbuilds.chtml
/usr/share/koji-web/scripts/reports.chtml
/usr/share/koji-web/scripts/rpminfo.chtml
/usr/share/koji-web/scripts/rpmlist.chtml
/usr/share/koji-web/scripts/rpmsbyhost.chtml
/usr/share/koji-web/scripts/search.chtml
/usr/share/koji-web/scripts/tagedit.chtml
/usr/share/koji-web/scripts/taginfo.chtml
/usr/share/koji-web/scripts/tagparent.chtml
/usr/share/koji-web/scripts/tags.chtml
/usr/share/koji-web/scripts/taskinfo.chtml
/usr/share/koji-web/scripts/taskinfo_params.chtml
/usr/share/koji-web/scripts/tasks.chtml
/usr/share/koji-web/scripts/tasksbyhost.chtml
/usr/share/koji-web/scripts/tasksbyuser.chtml
/usr/share/koji-web/scripts/userinfo.chtml
/usr/share/koji-web/scripts/users.chtml
/usr/share/koji-web/scripts/wsgi_publisher.py
/usr/share/koji-web/static/debug.css
/usr/share/koji-web/static/errors/unauthorized.html
/usr/share/koji-web/static/images/1px.gif
/usr/share/koji-web/static/images/assigned.png
/usr/share/koji-web/static/images/bkgrnd_greydots.png
/usr/share/koji-web/static/images/building.png
/usr/share/koji-web/static/images/canceled.png
/usr/share/koji-web/static/images/closed.png
/usr/share/koji-web/static/images/complete.png
/usr/share/koji-web/static/images/deleted.png
/usr/share/koji-web/static/images/expired.png
/usr/share/koji-web/static/images/failed.png
/usr/share/koji-web/static/images/free.png
/usr/share/koji-web/static/images/gray-triangle-down.gif
/usr/share/koji-web/static/images/gray-triangle-up.gif
/usr/share/koji-web/static/images/init.png
/usr/share/koji-web/static/images/initializing.png
/usr/share/koji-web/static/images/koji.ico
/usr/share/koji-web/static/images/koji.png
/usr/share/koji-web/static/images/no.png
/usr/share/koji-web/static/images/open.png
/usr/share/koji-web/static/images/powered-by-koji.png
/usr/share/koji-web/static/images/ready.png
/usr/share/koji-web/static/images/unknown.png
/usr/share/koji-web/static/images/waiting.png
/usr/share/koji-web/static/images/yes.png
/usr/share/koji-web/static/js/watchlogs.js
/usr/share/koji-web/static/koji.css
/usr/share/koji-web/static/themes/README

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/koji/c4b884eb09c7b65e2a469c7dbaf2f927e2af8e9f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/koji-sweep-db.service
/usr/lib/systemd/system/koji-sweep-db.timer
/usr/lib/systemd/system/kojid.service
/usr/lib/systemd/system/kojira.service
