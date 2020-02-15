Name:           playerctl
Version:        2.1.1
Release:        2%{?dist}
Summary:        Command-line MPRIS-compatible Media Player Controller

License:        LGPLv3+
URL:            https://github.com/acrisci/playerctl
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

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
Requires:       %{name} = %{version}-%{release}
BuildRequires:  gtk-doc

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
%meson -Dbash-completions=true
%meson_build

%install
%meson_install

%check
%meson_test


%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_datadir}/bash-completion/completions/playerctl.bash
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.playerctld.service
%{_datadir}/man/man1/%{name}.*


%files devel
%license COPYING
%{_datadir}/gir-1.0/Playerctl-2.0.gir
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files docs
%license COPYING
%{_datadir}/gtk-doc/


%files libs
%license COPYING
%{_libdir}/girepository-1.0/
%{_libdir}/lib%{name}.so.2*


%files static
%license COPYING
%{_libdir}/lib%{name}.a


%changelog
* Sat Feb 15 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.1.1-2
- Install Bash completions provided by upstream

* Thu Feb 06 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.1.1-1
- Update to latest upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.2-2
- Add gcc as BuildRequires
- Remove pkgconfig(gobject-introspection-1.0) from devel sub-package
- Fix ownership of girepository-1.0 directory

* Tue Apr 09 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.0.2-1
- Update to latest upstream release
- Fix ownership of directories created by package
- Move gtk-doc dependency to docs sub-package
- Docs sub-package no longer depends on arch-specific main package
- Other minor improvements from fedora-review tool

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
