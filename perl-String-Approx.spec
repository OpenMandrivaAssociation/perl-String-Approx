%define upstream_name    String-Approx
%define upstream_version 3.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl extension for approximate matching (fuzzy matching)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
String::Approx lets you match and substitute strings approximately. With this
you can emulate errors: typing errorrs, speling errors, closely related
vocabularies (colour color), genetic mutations (GAG ACT), abbreviations
(McScot, MacScot).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Artistic BUGS COPYRIGHT COPYRIGHT.agrep ChangeLog LGPL PROBLEMS README README.apse
%{perl_vendorarch}/auto/String
%{perl_vendorarch}/String
%{_mandir}/*/*
