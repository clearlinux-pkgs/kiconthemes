#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kiconthemes
Version  : 5.50.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.50/kiconthemes-5.50.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.50/kiconthemes-5.50.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.50/kiconthemes-5.50.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kiconthemes-bin
Requires: kiconthemes-lib
Requires: kiconthemes-license
Requires: kiconthemes-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : karchive-dev
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kitemviews-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# KIconThemes
Icon GUI utilities
## Introduction
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks. Provided are:

%package bin
Summary: bin components for the kiconthemes package.
Group: Binaries
Requires: kiconthemes-license

%description bin
bin components for the kiconthemes package.


%package dev
Summary: dev components for the kiconthemes package.
Group: Development
Requires: kiconthemes-lib
Requires: kiconthemes-bin
Provides: kiconthemes-devel

%description dev
dev components for the kiconthemes package.


%package lib
Summary: lib components for the kiconthemes package.
Group: Libraries
Requires: kiconthemes-license

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
%setup -q -n kiconthemes-5.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536424311
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536424311
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kiconthemes
cp COPYING.LIB %{buildroot}/usr/share/doc/kiconthemes/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kiconthemes5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kiconfinder5

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
/usr/lib64/libKF5IconThemes.so.5.50.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kiconthemes/COPYING.LIB

%files locales -f kiconthemes5.lang
%defattr(-,root,root,-)

