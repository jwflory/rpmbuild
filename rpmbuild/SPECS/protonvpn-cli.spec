%define         github_name protonvpn-cli-ng

Name:           protonvpn-cli
Version:        2.2.2
Release:        1%{?dist}
Summary:        Linux command-line client for ProtonVPN written in Python

License:        GPLv3
Vendor:         Proton Technologies AG <contact@protonvpn.com>
URL:            https://github.com/ProtonVPN/protonvpn-cli-ng
Source:         %{url}/archive/v%{version}/%{github_name}-%{version}.tar.gz

Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:         %{_prefix}

BuildArch:      noarch
BuildRequires:  python3
%if 0%{?mageia}
BuildRequires:  lib64python3-devel
%else
BuildRequires:  python3-devel
%endif

Requires:       openvpn
Requires:       python3
%if 0%{?fedora} || 0%{?.el8}
Recommends:     dialog
Recommends:     python3-dialog
Recommends:     NetworkManager-openvpn
Suggests:       NetworkManager-openvpn-gnome
%else
Requires:       dialog
Requires:       python3-dialog
%endif

%description
The official Linux CLI for ProtonVPN.

ProtonVPN-CLI is a full rewrite of the bash protonvpn-cli in Python, which adds
more features and functionality with the purpose of improving readability,
speed and reliability.

ProtonVPN-CLI features a DNS Leak Protection feature, which makes sure that
your online traffic uses ProtonVPN's DNS Servers. This prevents third parties
(like your ISP) from being able to see your DNS queries (and, therefore, your
browsing history).

For further information and a usage guide, please view the project page:

https://github.com/ProtonVPN/protonvpn-cli-ng


%prep
%setup -q -n %{github_name}-%{version} -n %{github_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


%changelog
* Wed Feb 26 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-1
- Update to latest upstream

* Mon Feb 3 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.1-1
- Update to latest upstream

* Wed Dec 25 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.0-1
- First protonvpn-cli package
