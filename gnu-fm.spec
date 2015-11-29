Name:		gnu-fm	
Version:	git5784e50a
Release:	1%{?dist}
Summary:	Music community platform in PHP (a la Last.fm)

Group:		Applications/Multimedia
License:	AGPLv3+
URL:		https://gnu.io/fm/
Source0:	https://git.gnu.io/gnu/gnu-fm/repository/archive.tar.gz

BuildArch:	noarch
BuildRequires:	
Requires:	php,php-adodb,php-Smarty,php-php-gettext

%description
A music community platform in PHP. GNU FM provides a web platform for users to
record their plays and view statistics about their music listening. Powers the
website https://libre.fm.

%prep
%setup -q


%build
%configure


%install
%make_install


%files
%doc AUTHORS contributing COPYING fixed-git-repo gnufm_install.txt README.md



%changelog
* Sun Nov 29 2015 Justin W. Flory <jflory7@fedoraproject.org> - git5784e50a-1
- Initial build for gnu-fm
