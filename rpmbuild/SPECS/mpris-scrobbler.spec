Name:           mpris-scrobbler
Version:        0.3.2
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
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif

%if 0%{?fedora} >= 28
BuildRequires:  /usr/bin/scdoc
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

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-signon
%{_userunitdir}/%{name}.service

%if 0%{?fedora} >= 28
%{_mandir}/man1/mpris-scrobbler{,-signon}.1*
%{_mandir}/man5/mpris-scrobbler-credentials.5*
%endif


%changelog
* Mon Apr 08 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.2-1
- Update package to latest upstream release

* Sat Feb 16 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-2
- Add systemd scriptlets

* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-1
- First release: mpris-scrobbler
- With guidance and help from  Igor Gnatenko
