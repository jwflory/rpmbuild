%define debug_package %{nil}
#
# automatically generate requires and provides from package.json
#
%{?nodejs_find_provides_and_requires}

#
# filter out any false provides created due to dependencies with native components
#
%{?nodejs_default_filter}

Summary:        Desktop chat client for Google Hangouts
Name:           yakyak
Group:          Applications/Communications
Version:        1.3.1
Release:        1%{?dist}

License:        MIT
URL:            https://github.com/yakyak/yakyak
Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  systemd
BuildRequires:  npm
AutoProv:       no
AutoReq:        no


%description
yakyak is a desktop chat client for Google Hangouts. It can send and receive
chat messages, create and change conversations, leave and delete conversations,
receive notifications, show in-line images, send typing notifications, and
more.


%prep
%setup -q -n %{name}-%{version}


%build

%{__rm} -f .gitignore
#
# Fedora guidlines do not allow bundled modules
# use nodejs_symlink_deps in the install section to generate
# links based on package.json contents
#
#%{__rm} -rf node_modules

%install
rm -rf $RPM_BUILD_ROOT

#
# copy in the module source
#
%{__install} -d  $RPM_BUILD_ROOT%{nodejs_sitelib}
%{__cp} -r $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_ROOT%{nodejs_sitelib}/%{name}
#
# link the daemon binaries into sbindir
#
%{__install} -d  $RPM_BUILD_ROOT%{_sbindir}
%{__ln_s} %{nodejs_sitelib}/%{name}/bin/yakyak $RPM_BUILD_ROOT%{_sbindir}/yakyak

#
# link in any dependent nodejs modules referenced in package.json
#
#%nodejs_symlink_deps

#
# npm will bundle in all dependent modules from the npm registry
# (bundling is OK for private packages but not for EPEL packages)
#
npm -g -q --production --prefix="${RPM_BUILD_ROOT}%{_prefix}" install

#
# documents will be handled by doc, so remove them from buildroot
#
%{__rm} -rf $RPM_BUILD_ROOT%{nodejs_sitelib}/%{name}{LICENSE,README.md,err.txt}

#
# Create a systemd unit file
#
mkdir -p $RPM_BUILD_ROOT%{_unitdir}/
touch $RPM_BUILD_ROOT%{_unitdir}/yakyak.service
cat << __EOF > $RPM_BUILD_ROOT%{_unitdir}/yakyak.service
[Unit]
Description=a desktop chat client for Google Hangouts

[Service]
Type=simple
ExecStart=/usr/sbin/yakyak

[Install]
WantedBy=multi-user.target
__EOF

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{name}
%{_sbindir}/yakyak
%{_unitdir}/yakyak.service



%changelog
* Tue Jun 21 2016 Justin W. Flory <jflory7@fedoraproject.org> - 1.3.1-1
- Initial spec file of yakyak
