%define debug_package %{nil}
Name:           ukui-settings-daemon
Version:        3.1.2
Release:        2
Summary:        daemon handling the UKUI session settings
License:        GPL-2.0-or-later and GPL-3.0-or-later and LGPL-2.0-or-later 
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-modify-compile-error-of-ukui-settings-daemon.patch

BuildRequires: pkgconf-pkg-config 
BuildRequires: intltool 
BuildRequires: qtchooser
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtsensors-devel 
BuildRequires: kf5-kconfig-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libxklavier-devel
BuildRequires: libXtst-devel
BuildRequires: mate-desktop-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: libmatemixer-devel
BuildRequires: libmatekbd-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libwnck3-devel
BuildRequires: libcanberra-devel
BuildRequires: libwayland-client
BuildRequires: libnotify-devel
BuildRequires: geoclue2-devel
BuildRequires: colord-devel
BuildRequires: lcms2-devel
BuildRequires: imlib2-devel 
BuildRequires: xorg-x11-server-devel
BuildRequires: libgudev-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: libX11-devel 
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: libxkbcommon-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: qt5-qtx11extras-devel 
BuildRequires: ukui-interface


Requires: mate-desktop-libs ukui-settings-daemon-common colord imwheel ukui-polkit xorg-x11-server-utils xorg-x11-drv-synaptics-legacy glib2-devel
%description
 This package contains the daemon which is responsible for setting the
 various parameters of a UKUI session and the applications that run
 under it. It handles the following kinds of settings:
 .
  * Keyboard: layout, accessibility options, shortcuts, media keys
  * Clipboard management
  * Theming: background, icons, GTK+ applications
  * Cleanup of unused files
  * Mouse: cursors, speed, accessibility options
  * Startup of other daemons: screensaver, sound daemon
  * Typing break
 .
 It also sets various application settings through X resources and
 freedesktop.org XSETTINGS.
 
%package common
Summary:	daemon handling the UKUI session settings (common files)

%description common
 This package contains the daemon which is responsible for setting the
 various parameters of a UKUI session and the applications that run
 under it. It handles the following kinds of settings:
 .
  * Keyboard: layout, accessibility options, shortcuts, media keys
  * Clipboard management
  * Theming: background, icons, GTK+ applications
  * Cleanup of unused files
  * Mouse: cursors, speed, accessibility options
  * Startup of other daemons: screensaver, sound daemon
  * Typing break
 .
 It also sets various application settings through X resources and
 freedesktop.org XSETTINGS.
 .
 This package contains the architecture independent files.

%prep
%setup -q
%patch1 -p1

%build
qmake-qt5
make -j32

%install
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}/usr/share/man/man1
mkdir -p %{buildroot}/usr/share/man/man2

gzip -c %{_builddir}/%{name}-%{version}/man/touchpad-state.1       > %{buildroot}/usr/share/man/man1/touchpad-state.1.gz
gzip -c %{_builddir}/%{name}-%{version}/man/ukui-settings-daemon.1       > %{buildroot}/usr/share/man/man1/ukui-settings-daemon.1.gz
gzip -c %{_builddir}/%{name}-%{version}/man/usd-locate-pointer.1         > %{buildroot}/usr/share/man/man1/usd-locate-pointer.1.gz


%clean
rm -rf $RPM_BUILD_ROOT

%post
set -e &> /dev/null || :
glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null || :

%files
%doc debian/changelog debian/copyright
%{_sysconfdir}/*
%{_prefix}/%{_lib}/ukui-settings-daemon/
%{_datadir}/dbus-1/*
/lib/udev/rules.d/01-touchpad-state-onmouse.rules
/usr/bin/authoritydbus
/usr/bin/touchpad-state
/usr/bin/ukui-settings-daemon
/usr/bin/ukydisplayswitch
/usr/bin/usd-locate-pointer


%files common
%doc debian/changelog debian/copyright
%{_datadir}/glib-2.0/
%{_datadir}/locale/
%{_datadir}/ukui-settings-daemon/
%{_datadir}/man/*



%changelog
* Tue Dec 6 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-2
- modify install error

* Mon Dec 5 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-1
- update version to 3.1.2

* Mon Aug 08 2022 tanyulong<tanyulong@kylinos.cn> - 3.0.1-7
- update Copyright and Authors information

* Thu Aug 04 2022 tanyulong<tanyulong@kylinos.cn> - 3.0.1-6
- remove depend xserver xorg input synaptics on s390x

* Tue May 24 2022 tanyulong<tanyulong@kylinos.cn> - 3.0.1-5
- Improve the project according to the requirements of compliance improvement

* Tue Apr 19 2022 douyan <douyan@kylimos.cn> - 3.0.1-4
- fix first install post script issue

* Wed Apr 06 2022 tanyulong <tanyulong@kylinos.cn> - 3.0.1-3
- add yaml file

* Thu Dec 16 2021 peijiankang <peijiankang@kylinos.cn> - 3.0.1-2
- Modify the shortcut key prompt

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1026

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.1-1
- Init package for openEuler
