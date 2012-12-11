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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.260.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 3.260.0-1mdv2010.0
+ Revision: 404414
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 3.26-7mdv2009.0
+ Revision: 258388
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.26-6mdv2009.0
+ Revision: 246472
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 3.26-4mdv2008.1
+ Revision: 152303
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-3mdv2008.0
+ Revision: 86921
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-2mdv2007.0
- Rebuild

* Tue Apr 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-1mdk
- New release 3.26
- better source URL
- correct optimisations
- %%mkrel

* Wed Jun 01 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.25-1mdk
- New release 3.25
- spec cleanup
- make test in %%check

* Wed Jan 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.24-1mdk
- 3.24
- Add tests, fix URL, trim verbose description

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 3.23-4mdk
- Rebuild for new perl

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.23-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.23-2mdk
- fixed dir ownership (distlint)

* Mon Dec 15 2003 Guillaume Rousse <guillomovitch@mandrake.org> 3.23-1mdk
- first mdk release

