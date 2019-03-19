Name:           playerctl
Version:        2.0.1
Release:        8%{?dist}
Summary:        Command-line MPRIS-compatible Media Player Controller

License:        LGPLv3+
URL:            https://github.com/acrisci/playerctl
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%description
Playerctl is a command-line utility and library for controlling media players
that implement the MPRIS D-Bus Interface Specification. Playerctl makes it easy
to bind player actions, such as play and pause, to media keys. You can also get
metadata about the playing track such as the artist and title for integration
into statusline generators or other command-line tools.

For more advanced users, Playerctl provides an introspectable library available
in your favorite scripting language that allows more detailed control like the
ability to subscribe to media player events or get metadata such as artist and
title for the playing track.

Examples of players implementing the MPRIS D-Bus Interface Specification include
spotify, vlc, audacious, bmp, cmus, and others.


%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%package docs
Summary:        Documentation related to %{name}
BuildArch:      noarch
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description docs
%{summary}.


%package libs
Summary:        Libraries and shared code for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
%{summary}.


%package static
Summary:        Static libraries for %{name} development
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
%{summary}.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test


%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.*


%files devel
%license COPYING
%{_datadir}/gir-1.0/Playerctl-2.0.gir
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files docs
%license COPYING
%{_datadir}/gtk-doc/html/%{name}/*


%files libs
%license COPYING
%{_libdir}/girepository-1.0/Playerctl-2.0.typelib
%{_libdir}/lib%{name}.so.2*


%files static
%license COPYING
%{_libdir}/lib%{name}.a


%changelog
* Tue Mar 19 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-8
- Fix sub-package description strings

* Sun Mar 03 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-7
- Add license to all sub-packages
- Add period after all sub-package summary macros

* Thu Feb 07 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-6
- Split out into -libs subpackage (BZ # 1671571)

* Wed Feb 06 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-5
- Change static package name and dependency on -devel package

* Mon Feb 04 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-4
- Build separate package for static development libraries

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-3
- Additional improvements by Dridi Boukelmoune and Fabio Valentini in RH Bugzilla bug 1671571

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-2
- Improvements suggested by Dridi Boukelmoune in RH Bugzilla bug 1671571

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-1
- First release: playerctl
