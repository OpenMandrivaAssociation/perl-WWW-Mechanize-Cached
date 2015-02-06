%define upstream_name       WWW-Mechanize-Cached
%define upstream_version 1.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Cache response to be polite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-Cached-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::Cache)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(Devel::SimpleTrace)
BuildRequires:	perl(Find::Lib)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(WWW::Mechanize)

BuildArch:	noarch

%description
Uses the Cache::Cache hierarchy to implement a caching Mech. This
lets one perform repeated requests without hammering a server
impolitely.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Cached.pm
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 596699
- update to 1.40

* Thu Sep 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.370.0-1mdv2011.0
+ Revision: 575426
- adding missing buildrequires:
- update to 1.37

* Sat Nov 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.350.0-1mdv2011.0
+ Revision: 467879
- update to 1.35

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1mdv2010.0
+ Revision: 396297
- new version

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.32-7mdv2009.0
+ Revision: 290441
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.32-4mdv2008.0
+ Revision: 25462
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.32-3mdv2008.0
+ Revision: 23571
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.32-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.32-1mdk
- initial Mandriva package


