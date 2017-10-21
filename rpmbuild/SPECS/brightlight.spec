%global debug_package %{nil}

Name:           brightlight
Version:        4
Release:        1%{?dist}
Summary:        CLI tool to change screen back light brightness

License:        GPLv2+
URL:            https://github.com/multiplexd/%{name}
Source0:        https://github.com/multiplexd/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libbsd
BuildRequires:  libbsd-devel
BuildRequires:  make


%description
brightlight is a program that can get and set the screen back light brightness
on Linux systems using the kernel sysfs interface.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{_bindir}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Sat Oct 21 2017 Justin W. Flory <jwf@fedoraproject.org> - 4-1
- First brightlight package
