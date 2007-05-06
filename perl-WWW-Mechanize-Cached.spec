%define real_name WWW-Mechanize-Cached

Summary:	WWW::Mechanize::Cached - Cache response to be polite 
Name:		perl-%{real_name}
Version:	1.32
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{real_name}-%{version}.tar.bz2
Patch0:		WWW-Mechanize-Cached-1.32-use_perl-Test-Warn.diff
BuildRequires:	perl-devel
BuildRequires:	perl(WWW::Mechanize)
BuildRequires:	perl(Cache::Cache)
BuildRequires:	perl-Test-Warn >= 0.08-5mdk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Uses the Cache::Cache hierarchy to implement a caching Mech. This
lets one perform repeated requests without hammering a server
impolitely.

%prep
%setup -q -n %{real_name}-%{version} 
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Cached.pm
%{_mandir}/*/*

