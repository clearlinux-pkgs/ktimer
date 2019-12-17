#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktimer
Version  : 19.12.0
Release  : 15
URL      : https://download.kde.org/stable/release-service/19.12.0/src/ktimer-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/ktimer-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/ktimer-19.12.0.tar.xz.sig
Summary  : Countdown Launcher
Group    : Development/Tools
License  : GPL-2.0
Requires: ktimer-bin = %{version}-%{release}
Requires: ktimer-data = %{version}-%{release}
Requires: ktimer-license = %{version}-%{release}
Requires: ktimer-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

%package bin
Summary: bin components for the ktimer package.
Group: Binaries
Requires: ktimer-data = %{version}-%{release}
Requires: ktimer-license = %{version}-%{release}

%description bin
bin components for the ktimer package.


%package data
Summary: data components for the ktimer package.
Group: Data

%description data
data components for the ktimer package.


%package doc
Summary: doc components for the ktimer package.
Group: Documentation

%description doc
doc components for the ktimer package.


%package license
Summary: license components for the ktimer package.
Group: Default

%description license
license components for the ktimer package.


%package locales
Summary: locales components for the ktimer package.
Group: Default

%description locales
locales components for the ktimer package.


%prep
%setup -q -n ktimer-19.12.0
cd %{_builddir}/ktimer-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576566019
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576566019
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktimer
cp %{_builddir}/ktimer-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/ktimer/7c203dee3a03037da436df03c4b25b659c073976
pushd clr-build
%make_install
popd
%find_lang ktimer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ktimer

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ktimer.desktop
/usr/share/icons/hicolor/128x128/apps/ktimer.png
/usr/share/icons/hicolor/16x16/apps/ktimer.png
/usr/share/icons/hicolor/32x32/apps/ktimer.png
/usr/share/icons/hicolor/48x48/apps/ktimer.png
/usr/share/metainfo/org.kde.ktimer.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ktimer/index.cache.bz2
/usr/share/doc/HTML/ca/ktimer/index.docbook
/usr/share/doc/HTML/cs/ktimer/index.cache.bz2
/usr/share/doc/HTML/cs/ktimer/index.docbook
/usr/share/doc/HTML/de/ktimer/first.png
/usr/share/doc/HTML/de/ktimer/index.cache.bz2
/usr/share/doc/HTML/de/ktimer/index.docbook
/usr/share/doc/HTML/de/ktimer/main.png
/usr/share/doc/HTML/de/ktimer/running.png
/usr/share/doc/HTML/de/ktimer/two_at_once.png
/usr/share/doc/HTML/en/ktimer/first.png
/usr/share/doc/HTML/en/ktimer/index.cache.bz2
/usr/share/doc/HTML/en/ktimer/index.docbook
/usr/share/doc/HTML/en/ktimer/main.png
/usr/share/doc/HTML/en/ktimer/running.png
/usr/share/doc/HTML/en/ktimer/two_at_once.png
/usr/share/doc/HTML/es/ktimer/index.cache.bz2
/usr/share/doc/HTML/es/ktimer/index.docbook
/usr/share/doc/HTML/et/ktimer/index.cache.bz2
/usr/share/doc/HTML/et/ktimer/index.docbook
/usr/share/doc/HTML/it/ktimer/index.cache.bz2
/usr/share/doc/HTML/it/ktimer/index.docbook
/usr/share/doc/HTML/nl/ktimer/index.cache.bz2
/usr/share/doc/HTML/nl/ktimer/index.docbook
/usr/share/doc/HTML/pt/ktimer/index.cache.bz2
/usr/share/doc/HTML/pt/ktimer/index.docbook
/usr/share/doc/HTML/pt_BR/ktimer/first.png
/usr/share/doc/HTML/pt_BR/ktimer/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ktimer/index.docbook
/usr/share/doc/HTML/pt_BR/ktimer/main.png
/usr/share/doc/HTML/pt_BR/ktimer/running.png
/usr/share/doc/HTML/pt_BR/ktimer/two_at_once.png
/usr/share/doc/HTML/sr/ktimer/index.cache.bz2
/usr/share/doc/HTML/sr/ktimer/index.docbook
/usr/share/doc/HTML/sv/ktimer/index.cache.bz2
/usr/share/doc/HTML/sv/ktimer/index.docbook
/usr/share/doc/HTML/uk/ktimer/first.png
/usr/share/doc/HTML/uk/ktimer/index.cache.bz2
/usr/share/doc/HTML/uk/ktimer/index.docbook
/usr/share/doc/HTML/uk/ktimer/main.png
/usr/share/doc/HTML/uk/ktimer/running.png
/usr/share/doc/HTML/uk/ktimer/two_at_once.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktimer/7c203dee3a03037da436df03c4b25b659c073976

%files locales -f ktimer.lang
%defattr(-,root,root,-)

