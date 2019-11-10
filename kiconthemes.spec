#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kiconthemes
Version  : 5.64.0
Release  : 22
URL      : https://download.kde.org/stable/frameworks/5.64/kiconthemes-5.64.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.64/kiconthemes-5.64.0.tar.xz
Source1 : https://download.kde.org/stable/frameworks/5.64/kiconthemes-5.64.0.tar.xz.sig
Summary  : Support for icon themes
Group    : Development/Tools
License  : LGPL-2.1
Requires: kiconthemes-bin = %{version}-%{release}
Requires: kiconthemes-data = %{version}-%{release}
Requires: kiconthemes-lib = %{version}-%{release}
Requires: kiconthemes-license = %{version}-%{release}
Requires: kiconthemes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kiconthemes-5.64.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573401297
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
export SOURCE_DATE_EPOCH=1573401297
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiconthemes
cp %{_builddir}/kiconthemes-5.64.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kiconthemes/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/lib64/libKF5IconThemes.so.5.64.0
/usr/lib64/qt5/plugins/designer/kiconthemes5widgets.so
/usr/lib64/qt5/plugins/iconengines/KIconEnginePlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiconthemes/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f kiconthemes5.lang
%defattr(-,root,root,-)

