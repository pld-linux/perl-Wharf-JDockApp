#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Wharf
%define		pnam	JDockApp
%include	/usr/lib/rpm/macros.perl
Summary:	Wharf::JDockApp - Perl extension for doing Wharf or Window Maker dockapps
Summary(pl.UTF-8):	Wharf::JDockApp - rozszerzenie Perla do tworzenia aplikacji dokowalnych
Name:		perl-Wharf-JDockApp
Version:	1.2.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JE/JETTERO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ec183b4b08f8b2faaa2aaa35ad7366f
URL:		http://search.cpan.org/dist/Wharf-JDockApp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wharf::JDockApp - Perl extension for doing Wharf or Window Maker
dockapps.

%description -l pl.UTF-8
Wharf::JDockApp - rozszerzenie Perla do tworzenia aplikacji
dokowalnych (dockapp) Wharfa lub Window Makera.

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
%dir %{perl_vendorarch}/Wharf
%{perl_vendorarch}/Wharf/*.pm
%dir %{perl_vendorarch}/Wharf/JDockApp
%{perl_vendorarch}/Wharf/JDockApp/*.pm
%dir %{perl_vendorarch}/auto/Wharf
%dir %{perl_vendorarch}/auto/Wharf/JDockApp
%{perl_vendorarch}/auto/Wharf/JDockApp/*
%{_mandir}/man3/*
