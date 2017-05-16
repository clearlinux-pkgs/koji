#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : koji
Version  : 1.10.0
Release  : 20
URL      : https://github.com/koji-project/koji/archive/koji-1.10.0.tar.gz
Source0  : https://github.com/koji-project/koji/archive/koji-1.10.0.tar.gz
Summary  : Build system tools
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0 LGPL-2.1
Requires: koji-bin
Requires: koji-python
Requires: koji-data
Requires: koji-config
BuildRequires : pkgconfig(systemd)
BuildRequires : python-dev
BuildRequires : systemd-dev

%description
Koji is a system for building and tracking RPMS.  The base package
contains shared libraries and the command-line interface.

%package bin
Summary: bin components for the koji package.
Group: Binaries
Requires: koji-data
Requires: koji-config

%description bin
bin components for the koji package.


%package config
Summary: config components for the koji package.
Group: Default

%description config
config components for the koji package.


%package data
Summary: data components for the koji package.
Group: Data

%description data
data components for the koji package.


%package python
Summary: python components for the koji package.
Group: Default

%description python
python components for the koji package.


%prep
%setup -q -n koji-koji-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494960216
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1494960216
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/koji-hub-plugins/echo.py
/usr/lib/koji-hub-plugins/echo.pyc
/usr/lib/koji-hub-plugins/echo.pyo
/usr/lib/koji-hub-plugins/messagebus.py
/usr/lib/koji-hub-plugins/messagebus.pyc
/usr/lib/koji-hub-plugins/messagebus.pyo
/usr/lib/koji-hub-plugins/rpm2maven.py
/usr/lib/koji-hub-plugins/rpm2maven.pyc
/usr/lib/koji-hub-plugins/rpm2maven.pyo
/usr/lib/koji-hub-plugins/runroot.py
/usr/lib/koji-hub-plugins/runroot.pyc
/usr/lib/koji-hub-plugins/runroot.pyo
/usr/lib/koji-hub-plugins/runroot_hub.py
/usr/lib/koji-hub-plugins/runroot_hub.pyc
/usr/lib/koji-hub-plugins/runroot_hub.pyo

%files bin
%defattr(-,root,root,-)
/usr/bin/koji
/usr/bin/koji-gc
/usr/bin/koji-shadow
/usr/bin/kojid
/usr/bin/kojira
/usr/bin/kojivmd
/usr/libexec/koji-hub/rpmdiff
/usr/libexec/kojid/mergerepos

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/kojid.service
/usr/lib/systemd/system/kojira.service
/usr/lib/systemd/system/kojivmd.service

%files data
%defattr(-,root,root,-)
%exclude /usr/share/koji-hub/kojihub.py
%exclude /usr/share/koji-hub/kojihub.pyc
%exclude /usr/share/koji-hub/kojihub.pyo
%exclude /usr/share/koji-hub/kojixmlrpc.py
%exclude /usr/share/koji-hub/kojixmlrpc.pyc
%exclude /usr/share/koji-hub/kojixmlrpc.pyo
%exclude /usr/share/koji-web/lib/kojiweb/__init__.py
%exclude /usr/share/koji-web/lib/kojiweb/__init__.pyc
%exclude /usr/share/koji-web/lib/kojiweb/__init__.pyo
%exclude /usr/share/koji-web/lib/kojiweb/util.py
%exclude /usr/share/koji-web/lib/kojiweb/util.pyc
%exclude /usr/share/koji-web/lib/kojiweb/util.pyo
%exclude /usr/share/koji-web/scripts/archiveinfo.chtml
%exclude /usr/share/koji-web/scripts/archivelist.chtml
%exclude /usr/share/koji-web/scripts/buildinfo.chtml
%exclude /usr/share/koji-web/scripts/buildrootinfo.chtml
%exclude /usr/share/koji-web/scripts/builds.chtml
%exclude /usr/share/koji-web/scripts/buildsbystatus.chtml
%exclude /usr/share/koji-web/scripts/buildsbytarget.chtml
%exclude /usr/share/koji-web/scripts/buildsbyuser.chtml
%exclude /usr/share/koji-web/scripts/buildtargetedit.chtml
%exclude /usr/share/koji-web/scripts/buildtargetinfo.chtml
%exclude /usr/share/koji-web/scripts/buildtargets.chtml
%exclude /usr/share/koji-web/scripts/channelinfo.chtml
%exclude /usr/share/koji-web/scripts/error.chtml
%exclude /usr/share/koji-web/scripts/externalrepoinfo.chtml
%exclude /usr/share/koji-web/scripts/fileinfo.chtml
%exclude /usr/share/koji-web/scripts/hostedit.chtml
%exclude /usr/share/koji-web/scripts/hostinfo.chtml
%exclude /usr/share/koji-web/scripts/hosts.chtml
%exclude /usr/share/koji-web/scripts/imageinfo.chtml
%exclude /usr/share/koji-web/scripts/includes/footer.chtml
%exclude /usr/share/koji-web/scripts/includes/header.chtml
%exclude /usr/share/koji-web/scripts/index.chtml
%exclude /usr/share/koji-web/scripts/index.py
%exclude /usr/share/koji-web/scripts/index.pyc
%exclude /usr/share/koji-web/scripts/index.pyo
%exclude /usr/share/koji-web/scripts/notificationedit.chtml
%exclude /usr/share/koji-web/scripts/packageinfo.chtml
%exclude /usr/share/koji-web/scripts/packages.chtml
%exclude /usr/share/koji-web/scripts/packagesbyuser.chtml
%exclude /usr/share/koji-web/scripts/recentbuilds.chtml
%exclude /usr/share/koji-web/scripts/reports.chtml
%exclude /usr/share/koji-web/scripts/rpminfo.chtml
%exclude /usr/share/koji-web/scripts/rpmlist.chtml
%exclude /usr/share/koji-web/scripts/rpmsbyhost.chtml
%exclude /usr/share/koji-web/scripts/search.chtml
%exclude /usr/share/koji-web/scripts/searchresults.chtml
%exclude /usr/share/koji-web/scripts/tagedit.chtml
%exclude /usr/share/koji-web/scripts/taginfo.chtml
%exclude /usr/share/koji-web/scripts/tagparent.chtml
%exclude /usr/share/koji-web/scripts/tags.chtml
%exclude /usr/share/koji-web/scripts/taskinfo.chtml
%exclude /usr/share/koji-web/scripts/tasks.chtml
%exclude /usr/share/koji-web/scripts/tasksbyhost.chtml
%exclude /usr/share/koji-web/scripts/tasksbyuser.chtml
%exclude /usr/share/koji-web/scripts/userinfo.chtml
%exclude /usr/share/koji-web/scripts/users.chtml
%exclude /usr/share/koji-web/scripts/wsgi_publisher.py
%exclude /usr/share/koji-web/scripts/wsgi_publisher.pyc
%exclude /usr/share/koji-web/scripts/wsgi_publisher.pyo
%exclude /usr/share/koji-web/static/debug.css
%exclude /usr/share/koji-web/static/errors/unauthorized.html
%exclude /usr/share/koji-web/static/images/1px.gif
%exclude /usr/share/koji-web/static/images/assigned.png
%exclude /usr/share/koji-web/static/images/bkgrnd_greydots.png
%exclude /usr/share/koji-web/static/images/building.png
%exclude /usr/share/koji-web/static/images/canceled.png
%exclude /usr/share/koji-web/static/images/closed.png
%exclude /usr/share/koji-web/static/images/complete.png
%exclude /usr/share/koji-web/static/images/deleted.png
%exclude /usr/share/koji-web/static/images/expired.png
%exclude /usr/share/koji-web/static/images/failed.png
%exclude /usr/share/koji-web/static/images/free.png
%exclude /usr/share/koji-web/static/images/gray-triangle-down.gif
%exclude /usr/share/koji-web/static/images/gray-triangle-up.gif
%exclude /usr/share/koji-web/static/images/init.png
%exclude /usr/share/koji-web/static/images/initializing.png
%exclude /usr/share/koji-web/static/images/koji.ico
%exclude /usr/share/koji-web/static/images/koji.png
%exclude /usr/share/koji-web/static/images/no.png
%exclude /usr/share/koji-web/static/images/open.png
%exclude /usr/share/koji-web/static/images/powered-by-koji.png
%exclude /usr/share/koji-web/static/images/ready.png
%exclude /usr/share/koji-web/static/images/unknown.png
%exclude /usr/share/koji-web/static/images/waiting.png
%exclude /usr/share/koji-web/static/images/yes.png
%exclude /usr/share/koji-web/static/js/watchlogs.js
%exclude /usr/share/koji-web/static/koji.css
%exclude /usr/share/koji-web/static/themes/README
%exclude /usr/share/kojivmd/kojikamid

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
