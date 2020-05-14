%global build_dir   cmd/Desktop-Bridge/deploy/linux/
%global commit      409abba995e7add59ab8e0391dbe1f4132695fc0
%global golicenses  LICENSE
%global goipath     github.com/ProtonMail/proton-bridge
Version:            1.2.6

%gometa

%global common_description %{expand:
ProtonMail Bridge for e-mail clients.

When launched, Bridge will initialize local IMAP/SMTP servers and render its
GUI.

To configure an e-mail client, firstly log in using your ProtonMail
credentials. Open your e-mail client and add a new account using the settings
which are located in the Bridge GUI. The client will only be able to sync with
your ProtonMail account when the Bridge is running, thus the option to start
Bridge on startup is enabled by default.

When the main window is closed, Bridge will continue to run in the background.

More details on the public website: https://protonmail.com/bridge}

Name:           protonmail-bridge
Release:        1%{?dist}
Summary:        ProtonMail Bridge for email clients
License:        GPLv3
URL:            %{forgeurl}
Source0:        %{gosource}

BuildRequires:  libglvnd-devel
BuildRequires:  libsecret-devel



%description
%{common_description}

%gopkg

%prep
%goprep

%build
make build

%install
install -m 0755 --verbose --directory %{buildroot}%{_bindir}
install -m 0755 --verbose --directory %{buildroot}%{_libdir}
install -m 0755 --verbose --preserve-timestamps %{build_dir}proton-bridge %{buildroot}%{_bindir}/
install -m 0755 --verbose --preserve-timestamps %{build_dir}lib/* %{buildroot}%{_libdir}
install -m 0755 --verbose --preserve-timestamps %{build_dir}plugins/* %{buildroot}%{_libdir}
install -m 0755 --verbose --preserve-timestamps %{build_dir}qml/* %{buildroot}%{_libdir}

%check
make test

%files
%doc Changelog.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/lib/*
%{_libdir}/plugins/*
%{_libdir}/qml/*



%changelog
* Tue May 5 2020 Justin W. Flory <jflory7@fedoraproject.org> - 1.2.6-1
- First package
