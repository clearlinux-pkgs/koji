#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : koji
Version  : 1.14.0
Release  : 52
URL      : https://github.com/koji-project/koji/archive/koji-1.14.0.tar.gz
Source0  : https://github.com/koji-project/koji/archive/koji-1.14.0.tar.gz
Summary  : Build system tools
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0 LGPL-2.1
Requires: koji-bin
Requires: koji-legacypython
Requires: koji-python3
Requires: koji-config
Requires: koji-doc
Requires: koji-data
Requires: koji-python
Requires: Babel
Requires: Babel-legacypython
Requires: Cheetah
Requires: Cheetah-legacypython
Requires: Jinja2
Requires: Jinja2-legacypython
Requires: Markdown
Requires: Markdown-legacypython
Requires: MarkupSafe
Requires: MarkupSafe-legacypython
Requires: Pygments
Requires: Pygments-legacypython
Requires: Sphinx
Requires: Sphinx-legacypython
Requires: Whoosh
Requires: Whoosh-legacypython
Requires: alabaster
Requires: alabaster-legacypython
Requires: argparse
Requires: argparse-legacypython
Requires: asn1crypto
Requires: asn1crypto-legacypython
Requires: attrs
Requires: attrs-legacypython
Requires: certifi
Requires: certifi-legacypython
Requires: cffi
Requires: cffi-legacypython
Requires: chardet
Requires: chardet-legacypython
Requires: colorama
Requires: colorama-legacypython
Requires: coverage
Requires: coverage-legacypython
Requires: cryptography
Requires: cryptography-legacypython
Requires: docutils
Requires: docutils-legacypython
Requires: funcsigs
Requires: funcsigs-legacypython
Requires: git
Requires: html5lib
Requires: html5lib-legacypython
Requires: idna
Requires: idna-legacypython
Requires: imagesize
Requires: imagesize-legacypython
Requires: ipaddress
Requires: ipaddress-legacypython
Requires: libcomps
Requires: linecache2
Requires: linecache2-legacypython
Requires: nose
Requires: nose-legacypython
Requires: ordereddict
Requires: ordereddict-legacypython
Requires: pbr
Requires: pbr-legacypython
Requires: pluggy
Requires: pluggy-legacypython
Requires: psycopg2
Requires: psycopg2-legacypython
Requires: py
Requires: py-legacypython
Requires: pyOpenSSL
Requires: pyOpenSSL-legacypython
Requires: pycparser
Requires: pycparser-legacypython
Requires: pytest
Requires: pytest-legacypython
Requires: python-dateutil
Requires: python-dateutil-legacypython
Requires: python-mock
Requires: python-mock-legacypython
Requires: python-multilib
Requires: python-multilib-legacypython
Requires: python-rpm
Requires: pytz
Requires: pytz-legacypython
Requires: requests
Requires: requests-legacypython
Requires: rpm
Requires: setuptools
Requires: setuptools-legacypython
Requires: simplejson
Requires: simplejson-legacypython
Requires: six
Requires: six-legacypython
Requires: snowballstemmer
Requires: snowballstemmer-legacypython
Requires: sphinx_rtd_theme
Requires: sphinx_rtd_theme-legacypython
Requires: sphinxcontrib-websupport
Requires: sphinxcontrib-websupport-legacypython
Requires: traceback2
Requires: traceback2-legacypython
Requires: typing
Requires: typing-legacypython
Requires: unittest2
Requires: unittest2-legacypython
Requires: urllib3
Requires: urllib3-legacypython
Requires: zope.testing
Requires: zope.testing-legacypython
Requires: zope.testrunner
Requires: zope.testrunner-legacypython
BuildRequires : pkgconfig(systemd)
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : systemd-dev
Patch1: 0001-builder-use-sudo-to-call-mock.patch
Patch2: 0002-Use-old-version-of-NSS-forking-behavior.patch
Patch3: 0003-Change-install-dir-to-usr-bin.patch
Patch4: 0004-Force-usr-bin-python2.patch
Patch5: 0005-Do-not-build-kojivm.patch
Patch6: 0006-Do-not-build-kojihub-plugins.patch

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


%package legacypython
Summary: legacypython components for the koji package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the koji package.


%package python
Summary: python components for the koji package.
Group: Default
Requires: koji-python3

%description python
python components for the koji package.


%package python3
Summary: python3 components for the koji package.
Group: Default
Requires: python3-core

%description python3
python3 components for the koji package.


%prep
%setup -q -n koji-koji-1.14.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519770003
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1519770003
rm -rf %{buildroot}
%make_install
## make_install_append content
/usr/bin/make DESTDIR=%{buildroot} PYTHON=python2 install
mkdir -p %{buildroot}/usr/share/doc/koji/
mv %{buildroot}/etc %{buildroot}/usr/share/doc/koji/
cp -a docs  %{buildroot}/usr/share/doc/koji/
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/koji-builder-plugins/__pycache__/runroot.cpython-36.pyc
/usr/lib/koji-builder-plugins/__pycache__/save_failed_tree.cpython-36.pyc
/usr/lib/koji-builder-plugins/runroot.py
/usr/lib/koji-builder-plugins/runroot.pyc
/usr/lib/koji-builder-plugins/save_failed_tree.py
/usr/lib/koji-builder-plugins/save_failed_tree.pyc

%files bin
%defattr(-,root,root,-)
/usr/bin/koji
/usr/bin/koji-gc
/usr/bin/koji-shadow
/usr/bin/kojid
/usr/bin/kojira
/usr/libexec/koji-hub/rpmdiff
/usr/libexec/kojid/mergerepos

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/kojid.service
/usr/lib/systemd/system/kojira.service

%files data
%defattr(-,root,root,-)
%exclude /usr/share/koji-hub/kojihub.py
%exclude /usr/share/koji-hub/kojihub.pyc
%exclude /usr/share/koji-hub/kojixmlrpc.py
%exclude /usr/share/koji-hub/kojixmlrpc.pyc
%exclude /usr/share/koji-web/lib/kojiweb/__init__.py
%exclude /usr/share/koji-web/lib/kojiweb/__init__.pyc
%exclude /usr/share/koji-web/lib/kojiweb/util.py
%exclude /usr/share/koji-web/lib/kojiweb/util.pyc
%exclude /usr/share/koji-web/scripts/archiveinfo.chtml
%exclude /usr/share/koji-web/scripts/archivelist.chtml
%exclude /usr/share/koji-web/scripts/buildinfo.chtml
%exclude /usr/share/koji-web/scripts/buildrootinfo.chtml
%exclude /usr/share/koji-web/scripts/buildrootinfo_cg.chtml
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
/usr/share/koji-hub/__init__.py
/usr/share/koji-hub/__init__.pyc
/usr/share/koji-hub/__pycache__/__init__.cpython-36.pyc
/usr/share/koji-web/lib/kojiweb/__pycache__/__init__.cpython-36.pyc
/usr/share/koji-web/lib/kojiweb/__pycache__/util.cpython-36.pyc
/usr/share/koji-web/scripts/__pycache__/index.cpython-36.pyc
/usr/share/koji-web/scripts/__pycache__/wsgi_publisher.cpython-36.pyc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/koji/*

%files extras
%defattr(-,root,root,-)
/usr/share/koji-hub/kojihub.py
/usr/share/koji-hub/kojihub.pyc
/usr/share/koji-hub/kojixmlrpc.py
/usr/share/koji-hub/kojixmlrpc.pyc
/usr/share/koji-web/lib/kojiweb/__init__.py
/usr/share/koji-web/lib/kojiweb/__init__.pyc
/usr/share/koji-web/lib/kojiweb/util.py
/usr/share/koji-web/lib/kojiweb/util.pyc
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
/usr/share/koji-web/scripts/searchresults.chtml
/usr/share/koji-web/scripts/tagedit.chtml
/usr/share/koji-web/scripts/taginfo.chtml
/usr/share/koji-web/scripts/tagparent.chtml
/usr/share/koji-web/scripts/tags.chtml
/usr/share/koji-web/scripts/taskinfo.chtml
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

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
