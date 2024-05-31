#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kiconthemes
Version  : 6.2.0
Release  : 81
URL      : https://download.kde.org/stable/frameworks/6.2/kiconthemes-6.2.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.2/kiconthemes-6.2.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.2/kiconthemes-6.2.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Support for icon themes
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kiconthemes-bin = %{version}-%{release}
Requires: kiconthemes-data = %{version}-%{release}
Requires: kiconthemes-lib = %{version}-%{release}
Requires: kiconthemes-license = %{version}-%{release}
Requires: kiconthemes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : karchive-dev
BuildRequires : kauth
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kitemviews-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KIconThemes
Icon GUI utilities
## Introduction
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks. Provided are:

%package bin
Summary: bin components for the kiconthemes package.
Group: Binaries
Requires: kiconthemes-data = %{version}-%{release}
Requires: kiconthemes-license = %{version}-%{release}

%description bin
bin components for the kiconthemes package.


%package data
Summary: data components for the kiconthemes package.
Group: Data

%description data
data components for the kiconthemes package.


%package dev
Summary: dev components for the kiconthemes package.
Group: Development
Requires: kiconthemes-lib = %{version}-%{release}
Requires: kiconthemes-bin = %{version}-%{release}
Requires: kiconthemes-data = %{version}-%{release}
Provides: kiconthemes-devel = %{version}-%{release}
Requires: kiconthemes = %{version}-%{release}

%description dev
dev components for the kiconthemes package.


%package lib
Summary: lib components for the kiconthemes package.
Group: Libraries
Requires: kiconthemes-data = %{version}-%{release}
Requires: kiconthemes-license = %{version}-%{release}

%description lib
lib components for the kiconthemes package.


%package license
Summary: license components for the kiconthemes package.
Group: Default

%description license
license components for the kiconthemes package.


%package locales
Summary: locales components for the kiconthemes package.
Group: Default

%description locales
locales components for the kiconthemes package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kiconthemes-6.2.0
cd %{_builddir}/kiconthemes-6.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715636100
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
export GOAMD64=v2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
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
export SOURCE_DATE_EPOCH=1715636100
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiconthemes
cp %{_builddir}/kiconthemes-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kiconthemes/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kiconthemes-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kiconthemes6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kiconfinder6
/usr/bin/kiconfinder6

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kiconthemes.categories
/usr/share/qlogging-categories6/kiconthemes.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KIconThemes/KIconColors
/usr/include/KF6/KIconThemes/KIconEffect
/usr/include/KF6/KIconThemes/KIconEngine
/usr/include/KF6/KIconThemes/KIconLoader
/usr/include/KF6/KIconThemes/KIconTheme
/usr/include/KF6/KIconThemes/KQuickIconProvider
/usr/include/KF6/KIconThemes/kiconcolors.h
/usr/include/KF6/KIconThemes/kiconeffect.h
/usr/include/KF6/KIconThemes/kiconengine.h
/usr/include/KF6/KIconThemes/kiconloader.h
/usr/include/KF6/KIconThemes/kicontheme.h
/usr/include/KF6/KIconThemes/kiconthemes_export.h
/usr/include/KF6/KIconThemes/kiconthemes_version.h
/usr/include/KF6/KIconThemes/kquickiconprovider.h
/usr/include/KF6/KIconWidgets/KIconButton
/usr/include/KF6/KIconWidgets/KIconDialog
/usr/include/KF6/KIconWidgets/KPixmapSequenceLoader
/usr/include/KF6/KIconWidgets/kiconbutton.h
/usr/include/KF6/KIconWidgets/kicondialog.h
/usr/include/KF6/KIconWidgets/kiconwidgets_export.h
/usr/include/KF6/KIconWidgets/kpixmapsequenceloader.h
/usr/lib64/cmake/KF6IconThemes/KF6IconThemesConfig.cmake
/usr/lib64/cmake/KF6IconThemes/KF6IconThemesConfigVersion.cmake
/usr/lib64/cmake/KF6IconThemes/KF6IconThemesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6IconThemes/KF6IconThemesTargets.cmake
/usr/lib64/libKF6IconThemes.so
/usr/lib64/libKF6IconWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6IconThemes.so.6.2.0
/V3/usr/lib64/libKF6IconWidgets.so.6.2.0
/V3/usr/lib64/qt6/plugins/designer/kiconthemes6widgets.so
/V3/usr/lib64/qt6/plugins/iconengines/KIconEnginePlugin.so
/V3/usr/lib64/qt6/qml/org/kde/iconthemes/libiconthemesplugin.so
/usr/lib64/libKF6IconThemes.so.6
/usr/lib64/libKF6IconThemes.so.6.2.0
/usr/lib64/libKF6IconWidgets.so.6
/usr/lib64/libKF6IconWidgets.so.6.2.0
/usr/lib64/qt6/plugins/designer/kiconthemes6widgets.so
/usr/lib64/qt6/plugins/iconengines/KIconEnginePlugin.so
/usr/lib64/qt6/qml/org/kde/iconthemes/iconthemesplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/iconthemes/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/iconthemes/libiconthemesplugin.so
/usr/lib64/qt6/qml/org/kde/iconthemes/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kiconthemes/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kiconthemes/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kiconthemes/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kiconthemes/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kiconthemes/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kiconthemes6.lang
%defattr(-,root,root,-)

