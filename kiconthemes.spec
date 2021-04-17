#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kiconthemes
Version  : 5.81.0
Release  : 36
URL      : https://download.kde.org/stable/frameworks/5.81/kiconthemes-5.81.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.81/kiconthemes-5.81.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.81/kiconthemes-5.81.0.tar.xz.sig
Summary  : Support for icon themes
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kiconthemes-bin = %{version}-%{release}
Requires: kiconthemes-data = %{version}-%{release}
Requires: kiconthemes-lib = %{version}-%{release}
Requires: kiconthemes-license = %{version}-%{release}
Requires: kiconthemes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
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
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsvg-dev

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
%setup -q -n kiconthemes-5.81.0
cd %{_builddir}/kiconthemes-5.81.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618620836
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1618620836
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiconthemes
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kiconthemes/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kiconthemes-5.81.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang kiconthemes5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kiconfinder5

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kiconthemes.categories
/usr/share/qlogging-categories5/kiconthemes.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIconThemes/KIconButton
/usr/include/KF5/KIconThemes/KIconDialog
/usr/include/KF5/KIconThemes/KIconEffect
/usr/include/KF5/KIconThemes/KIconEngine
/usr/include/KF5/KIconThemes/KIconLoader
/usr/include/KF5/KIconThemes/KIconTheme
/usr/include/KF5/KIconThemes/kiconbutton.h
/usr/include/KF5/KIconThemes/kicondialog.h
/usr/include/KF5/KIconThemes/kiconeffect.h
/usr/include/KF5/KIconThemes/kiconengine.h
/usr/include/KF5/KIconThemes/kiconloader.h
/usr/include/KF5/KIconThemes/kicontheme.h
/usr/include/KF5/KIconThemes/kiconthemes_export.h
/usr/include/KF5/kiconthemes_version.h
/usr/lib64/cmake/KF5IconThemes/KF5IconThemesConfig.cmake
/usr/lib64/cmake/KF5IconThemes/KF5IconThemesConfigVersion.cmake
/usr/lib64/cmake/KF5IconThemes/KF5IconThemesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IconThemes/KF5IconThemesTargets.cmake
/usr/lib64/libKF5IconThemes.so
/usr/lib64/qt5/mkspecs/modules/qt_KIconThemes.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5IconThemes.so.5
/usr/lib64/libKF5IconThemes.so.5.81.0
/usr/lib64/qt5/plugins/designer/kiconthemes5widgets.so
/usr/lib64/qt5/plugins/iconengines/KIconEnginePlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiconthemes/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kiconthemes/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kiconthemes/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kiconthemes/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kiconthemes/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kiconthemes/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kiconthemes/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kiconthemes5.lang
%defattr(-,root,root,-)

