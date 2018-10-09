Name:           brightlight
Version:        7
Release:        1%{?dist}
Summary:        CLI tool to change screen back-light brightness

License:        ISC
URL:            https://github.com/multiplexd/brightlight
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         add-license-file.patch

BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  make


%description
brightlight gets and sets the screen back-light brightness on Linux systems
using the kernel sysfs interface.


%prep
%global _hardened_build 1
%autosetup

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE.txt
%{_bindir}/%{name}
%attr(4755, root, root) %{_bindir}/%{name}


%changelog
* Mon Oct 08 2018 Justin W. Flory <jwf@fedoraproject.org> - 7-1
- Upgrade to upstream major release
* Thu Nov 09 2017 Justin W. Flory <jwf@fedoraproject.org> - 5-2
- setuid to root to change back-light brightness as non-privileged user
* Tue Oct 31 2017 Justin W. Flory <jwf@fedoraproject.org> - 5-1
- Tweak to the Makefile, contributed by Igor Gnatenko
* Sat Oct 21 2017 Justin W. Flory <jwf@fedoraproject.org> - 4-1
- First brightlight package
