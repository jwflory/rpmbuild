Name:           mpris-scrobbler
Version:        0.3.1
Release:        1%{?dist}
Summary:        User daemon to submit currently playing song to LastFM, LibreFM, ListenBrainz

License:        MIT
URL:            https://github.com/mariusor/mpris-scrobbler
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  dbus dbus-devel
BuildRequires:  expat expat-devel
BuildRequires:  gcc
BuildRequires:  json-c json-c-devel
BuildRequires:  libcurl libcurl-devel
BuildRequires:  libevent libevent-devel
BuildRequires:  m4 make
BuildRequires:  meson ninja-build
BuildRequires:  openssl openssl-devel
BuildRequires:  scdoc

Requires:       xdg-utils


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
%doc %{_mandir}/man1/mpris-scrobbler.1.gz
%doc %{_mandir}/man5/mpris-scrobbler-credentials.5.gz
%doc %{_mandir}/man1/mpris-scrobbler-signon.1.gz
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-signon
/usr/lib/systemd/user/%{name}.service


%changelog
* Thu Jan 31 2019 Justin W. Flory <jflory7@fedoraproject.org> - 0.3.1-1
- First release: mpris-scrobbler
