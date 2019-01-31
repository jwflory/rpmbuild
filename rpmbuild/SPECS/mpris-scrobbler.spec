Name:           mpris-scrobbler
Version:        0.3.1
Release:        1%{?dist}
Summary:        User daemon to submit currently playing song to LastFM, LibreFM, ListenBrainz

License:        MIT
URL:            https://github.com/mariusor/mpris-scrobbler
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  /usr/bin/m4

%if 0%{?rhel} && 0%{?rhel} < 8 || 0%{?fedora} <= 29
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%if ! 0%{?rhel}
BuildRequires: /usr/bin/scdoc
%endif

Requires:       /usr/bin/xdg-open


%description
mpris-scrobbler is a minimalist user daemon that submits the currently playing
song to LastFM, LibreFM, ListenBrainz, and compatible services. To retrieve
song information, it uses the MPRIS DBus interface, so it works with any media
player that exposes this interface.


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
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-signon
%{_userunitdir}/%{name}.service

%if ! 0%{?rhel}
%{_mandir}/man1/mpris-scrobbler{,-signon}.1*
%{_mandir}/man5/mpris-scrobbler-credentials.5*
%endif


%changelog
* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-1
- First release: mpris-scrobbler
- With guidance and help from  Igor Gnatenko
