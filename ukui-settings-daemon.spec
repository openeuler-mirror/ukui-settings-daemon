%define debug_package %{nil}
Name:           ukui-settings-daemon
Version:        3.0.1
Release:        1
Summary:        daemon handling the UKUI session settings
License:        GPL-2.0, GPL-2+, GPL-2.1, LGPL-2.1+, GPL-3+, LGPL-2+, MIT~OldStyleWithDisclaimer+RedHat, MIT~OldStyle+RedHat
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

patch0:  0001-fix-dependency-issue.patch

BuildRequires: intltool libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel libnotify-devel nss-devel polkit-devel pulseaudio-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel mate-desktop-libs xorg-x11-server-utils libusb-devel
#x11proto-kb-devel
BuildRequires:mate-desktop-devel >= 1.18
BuildRequires:libmatekbd-devel >= 1.18 
BuildRequires:libmatemixer-devel >= 1.18
BuildRequires:mate-common >= 1.18
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
Requires: intltool libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel libnotify-devel nss-devel polkit-devel pulseaudio-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel mate-desktop-libs xorg-x11-server-utils mate-desktop-devel libmatekbd-devel libmatemixer-devel mate-common

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


%package devel
Summary:	daemon handling the UKUI session settings (development files)
Requires: intltool libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel libnotify-devel nss-devel polkit-devel pulseaudio-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel mate-desktop-libs xorg-x11-server-utils mate-desktop-devel libmatekbd-devel libmatemixer-devel mate-common
Requires: ukui-settings-daemon

%description devel
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
 This package contains the development files for building
 ukui-settings-daemon plugins.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 --sysconfdir=/etc
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/

%files
%{_sysconfdir}/*
%{_prefix}/%{_lib}/ukui-settings-daemon/
%{_libexecdir}/ukui-settings-daemon
%{_libexecdir}/usd-datetime-mechanism
%{_libexecdir}/usd-locate-pointer
%{_libexecdir}/usd-usb-monitor
%{_datadir}/dbus-1/*
%{_datadir}/polkit-1/

%files common
%doc debian/changelog debian/copyright
%{_datadir}/glib-2.0/
%{_datadir}/icons/
%{_datadir}/locale/
%{_datadir}/man/
%{_datadir}/ukui-settings-daemon/

%files devel
%{_prefix}/include/ukui-settings-daemon/
%{_prefix}/%{_lib}/pkgconfig/


%changelog
* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1026

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.1-1
- Init package for openEuler
