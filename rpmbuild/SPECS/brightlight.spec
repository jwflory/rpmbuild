Name:           brightlight
Version:        5
Release:        1%{?dist}
Summary:        CLI tool to change screen backlight brightness

License:        GPLv2+
URL:            https://github.com/multiplexd/brightlight
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  make


%description
brightlight is a program that can get and set the screen backlight brightness
on Linux systems using the kernel sysfs interface.


%prep
%autosetup


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Sat Oct 21 2017 Justin W. Flory <jwf@fedoraproject.org> - 4-1
- First brightlight package
