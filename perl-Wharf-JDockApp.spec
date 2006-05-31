#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Wharf
%define		pnam	JDockApp
Summary:	Wharf::JDockApp - Perl extension for doing Wharf or Window Maker dockapps
Name:		perl-Wharf-JDockApp
Version:	1.2.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JE/JETTERO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ec183b4b08f8b2faaa2aaa35ad7366f

BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wharf::JDockApp - Perl extension for doing Wharf or Window Maker
dockapps.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/%{pdir}/%{pnam}/
%{perl_vendorarch}/%{pdir}/%{pnam}/*.pm
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*
%{_mandir}/man3/*
