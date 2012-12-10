Summary:	Generic Colouriser
Name:		grc
Version:	1.4
Release:	%mkrel 1
Source0:	http://korpus.juls.savba.sk/~garabik/software/grc/%{name}_%{version}.tar.gz
License:	GPLv2
Url:		http://melkor.dnp.fmph.uniba.sk/~garabik/grc.html
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python

%description
Generic Colouriser is yet another colouriser for beautifying
your logfiles or output of commands.

%prep
%setup -q

%build
# fix symlinked doc file
rm -f CHANGES
cp debian/changelog CHANGES

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name}{,at} $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 conf.* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{name}{,at}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES CREDITS INSTALL README Regexp.txt TODO
%{_bindir}/%{name}
%{_bindir}/%{name}at
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/conf.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}*.1*



%changelog
* Thu Oct 06 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.4-1mdv2012.0
+ Revision: 703337
- bump new version

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdv2011.0
+ Revision: 610983
- rebuild

* Thu Mar 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3-1mdv2010.1
+ Revision: 514233
- update to 1.3

* Wed Jun 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2-1mdv2010.0
+ Revision: 382524
- Update to new version 1.2
- Fix source URL

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.6-6mdv2009.0
+ Revision: 246634
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.6-4mdv2008.1
+ Revision: 126285
- kill re-definition of %%buildroot on Pixel's request
- import grc


* Thu Feb  9 2006 Olivier Blin <oblin@mandriva.com> 1.0.6-4mdk
- double-birthay rebuild

* Tue Feb 10 2004 Olivier Blin <blino@mandrake.org> 1.0.6-3mdk
- fix DIRM

* Sat Dec 27 2003 Olivier Blin <blino@mandrake.org> 1.0.6-2mdk
- use %%config for config files

* Mon Dec 22 2003 Olivier Blin <blino@mandrake.org> 1.0.6-1mdk
- initial Mandrake release, based on spec file in tarball
