Summary:	Generic Colouriser
Name:		grc
Version:	1.0.6
Release:	%mkrel 4
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
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

