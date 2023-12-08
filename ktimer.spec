#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ktimer
Version  : 23.08.3
Release  : 60
URL      : https://download.kde.org/stable/release-service/23.08.3/src/ktimer-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/ktimer-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/ktimer-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: ktimer-bin = %{version}-%{release}
Requires: ktimer-data = %{version}-%{release}
Requires: ktimer-license = %{version}-%{release}
Requires: ktimer-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n ktimer-23.08.3
cd %{_builddir}/ktimer-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702007880
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702007880
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktimer
cp %{_builddir}/ktimer-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ktimer/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ktimer-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ktimer/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/ktimer-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktimer/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang ktimer
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ktimer
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
/usr/share/doc/HTML/fr/ktimer/index.cache.bz2
/usr/share/doc/HTML/fr/ktimer/index.docbook
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
/usr/share/doc/HTML/ru/ktimer/index.cache.bz2
/usr/share/doc/HTML/ru/ktimer/index.docbook
/usr/share/doc/HTML/sr/ktimer/index.cache.bz2
/usr/share/doc/HTML/sr/ktimer/index.docbook
/usr/share/doc/HTML/sr@latin/ktimer/index.cache.bz2
/usr/share/doc/HTML/sr@latin/ktimer/index.docbook
/usr/share/doc/HTML/sv/ktimer/index.cache.bz2
/usr/share/doc/HTML/sv/ktimer/index.docbook
/usr/share/doc/HTML/tr/ktimer/first.png
/usr/share/doc/HTML/tr/ktimer/index.cache.bz2
/usr/share/doc/HTML/tr/ktimer/index.docbook
/usr/share/doc/HTML/tr/ktimer/main.png
/usr/share/doc/HTML/tr/ktimer/running.png
/usr/share/doc/HTML/tr/ktimer/two_at_once.png
/usr/share/doc/HTML/uk/ktimer/first.png
/usr/share/doc/HTML/uk/ktimer/index.cache.bz2
/usr/share/doc/HTML/uk/ktimer/index.docbook
/usr/share/doc/HTML/uk/ktimer/main.png
/usr/share/doc/HTML/uk/ktimer/running.png
/usr/share/doc/HTML/uk/ktimer/two_at_once.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktimer/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ktimer/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/ktimer/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f ktimer.lang
%defattr(-,root,root,-)

