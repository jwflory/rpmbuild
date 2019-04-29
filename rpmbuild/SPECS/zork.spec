Name:           zork
Version:        1.0.2
Release:        1%{?dist}
Summary:        Public Domain source code to the original DUNGEON game (Zork I)

License:        Public Domain
URL:            https://github.com/devshane/zork
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         zork-tweak-makefile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel


%description
Public Domain source code to the original DUNGEON game (Zork I). Released to
the PD by Infocom. Includes source files, headers, and information.

This version of Dungeon was modified from FORTRAN to C. The original was
written in DEC FORTRAN, translated from MDL. It was then translated to f77 for
UN*X systems, from which it was translated to C. The C translation was done
with the help of f2c, the FORTRAN to C translator written by David Gay (AT&T
Bell Labs), Stu Feldman (Bellcore), Mark Maimone (Carnegie-Mellon University),
and Norm Schryer (AT&T Bell Labs).


%prep
%global _hardened_build 1
%autosetup

%build
export CFLAGS="%{optflags}"
export DATADIR="%{_datadir}/%{name}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
export BINDIR="%{buildroot}%{_bindir}"
export DATADIR="%{buildroot}%{_datadir}/%{name}/"
export LIBDIR="%{buildroot}%{_datadir}"
export MANDIR="%{buildroot}%{_mandir}"
%make_install


%files
%license readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/dtextc.dat
%{_mandir}/man6/dungeon.6.gz


%changelog
* Mon Apr 29 2019 Justin W. Flory <jflory7@fedoraproject.org> - 1.0.2-1
- First zork package
