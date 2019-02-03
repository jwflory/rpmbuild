Name:           playerctl
Version:        2.0.1
Release:        2%{?dist}
Summary:        Command-line MPRIS-compatible Media Player Controller

License:        LGPLv3+
URL:            https://github.com/acrisci/playerctl
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc


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
%{_datadir}/gir-1.0/Playerctl-2.0.gir
%{_libdir}/girepository-1.0/Playerctl-2.0.typelib
%{_libdir}/lib%{name}.*
%doc %{_datadir}/gtk-doc/html/%{name}/*
%doc %{_datadir}/man/man1/%{name}.*


%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-2
- Improvements suggested by Dridi Boukelmoune in RH Bugzilla bug 1671571

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-1
- First release: playerctl
