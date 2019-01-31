Name:           playerctl
Version:        2.0.1
Release:        1%{?dist}
Summary:        MPRIS command-line controller and library for spotify, vlc, audacious, bmp, cmus, and others

License:        LGPLv3
URL:            https://github.com/acrisci/playerctl
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc

Requires:       glib


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


%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}


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
%doc %{_datadir}/gtk-doc/html/%{name}/*
%doc %{_datadir}/man/man1/%{name}.*


%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/girepository-1.0/Playerctl-2.0.typelib
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.1-1
- First release: playerctl
