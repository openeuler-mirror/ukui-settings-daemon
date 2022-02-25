%define debug_package %{nil}
Name:           ukui-settings-daemon
Version:        3.0.1
Release:        3
Summary:        daemon handling the UKUI session settings
License:        GPL-2.0, GPL-2+, GPL-2.1, LGPL-2.1+, GPL-3+, LGPL-2+, MIT~OldStyleWithDisclaimer+RedHat, MIT~OldStyle+RedHat
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: intltool 
BuildRequires: libcanberra-devel 
BuildRequires: dbus-glib-devel 
BuildRequires: dconf-devel 
BuildRequires: fontconfig-devel 
BuildRequires: glib2-devel 
BuildRequires: gtk3-devel 
BuildRequires: libnotify-devel 
BuildRequires: nss-devel 
BuildRequires: polkit-devel 
BuildRequires: pulseaudio-libs-devel 
BuildRequires: startup-notification-devel 
BuildRequires: libX11-devel 
BuildRequires: libXext-devel 
BuildRequires: libXi-devel 
BuildRequires: libxklavier-devel 
BuildRequires: libXrandr-devel 
BuildRequires: libXt-devel 
BuildRequires: mate-desktop-libs 
BuildRequires: xorg-x11-server-utils 
BuildRequires: libusb-devel
BuildRequires: mate-desktop-devel >= 1.18
BuildRequires: libmatekbd-devel >= 1.18 
BuildRequires: libmatemixer-devel >= 1.18
BuildRequires: mate-common >= 1.18

#x11proto-kb-devel

BuildRequires: pkgconf-pkg-config 
BuildRequires: qt5-qtbase
BuildRequires: qtchooser
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtsensors-devel 
BuildRequires: kf5-kconfig-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libxklavier-devel
BuildRequires: libXtst-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libwnck3-devel
BuildRequires: libcanberra-devel
BuildRequires: libwayland-client
BuildRequires: geoclue2-devel
BuildRequires: lcms2-devel
BuildRequires: imlib2-devel 
BuildRequires: xorg-x11-server-devel
BuildRequires: libgudev-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: libxkbcommon-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: qt5-qtx11extras-devel 
#BuildRequires: ukui-common-devel
BuildRequires: colord
BuildRequires: glib2
BuildRequires: ukui-interface
BuildRequires: colord-gtk-devel
BuildRequires: gsettings-qt-devel

Requires: mate-desktop-libs ukui-polkit ukui-settings-daemon-common imwheel xorg-x11-drv-synaptics-legacy

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
Requires: intltool libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel libnotify-devel nss-devel polkit-devel pulseaudio-libs-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel mate-desktop-libs xorg-x11-server-utils mate-desktop-devel libmatekbd-devel libmatemixer-devel mate-common

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

%build
qmake-qt5
make -j24

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
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/

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
* Tue Feb  22 2022 huayadong <huayadong@kylinos.cn> - 3.0.1-3
- update to upstream version 3.0.1-3

* Thu Dec 16 2021 peijiankang <peijiankang@kylinos.cn> - 3.0.1-2
- Modify the shortcut key prompt

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1026

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.1-1
- Init package for openEuler
