%define upstream_name       WWW-Mechanize-Cached
%define upstream_version 1.37

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Cache response to be polite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Uses the Cache::Cache hierarchy to implement a caching Mech. This
lets one perform repeated requests without hammering a server
impolitely.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
