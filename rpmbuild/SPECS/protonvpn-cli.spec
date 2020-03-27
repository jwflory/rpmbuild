%global         github_name protonvpn-cli-ng
%global         srcname protonvpn_cli

Name:           protonvpn-cli
Version:        2.2.2
Release:        7%{?dist}
Summary:        Linux command-line client for ProtonVPN written in Python

License:        GPLv3
URL:            https://github.com/ProtonVPN/%{github_name}
Source:         %{url}/archive/v%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       openvpn
%if 0%{?fedora} || 0%{?.el8}
Recommends:     dialog
Recommends:     NetworkManager-openvpn
Suggests:       NetworkManager-openvpn-gnome
%else
Requires:       dialog
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
%autosetup -n %{github_name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/protonvpn


%changelog
* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-7
- Approved package for official Fedora repositories
- Remove Requires handled by Python dependency generator (BZ #1809814)

* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-6
- Remove python3-dialog as dependency (already Required automatically)

* Mon Mar 16 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-5
- Remove tags not used in Fedora packages
- Add missing dependencies tracked in upstream requirements.txt

* Tue Mar 03 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-4
- Adhere to Fedora Packaging Guidelines via fedora-review

* Wed Feb 26 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-1
- Update to latest upstream

* Mon Feb 3 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.1-1
- Update to latest upstream

* Wed Dec 25 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.0-1
- First protonvpn-cli package
