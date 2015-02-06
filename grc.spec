Summary:	Generic Colouriser
Name:		grc
Version:	1.5
Release:	2
License:	GPLv2+
Group:		Text tools
Url:		http://kassiopeia.juls.savba.sk/~garabik/software/grc.html
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/grc/%{name}_%{version}.tar.gz
Patch0:		grc-1.4-ipv6.patch
Patch1:		grc-1.4-support-more-files.patch
Requires:	python
BuildArch:	noarch

%description
Generic Colouriser is yet another colouriser for beautifying
your logfiles or output of commands.

%files
%doc CHANGES CREDITS README Regexp.txt TODO
%{_bindir}/%{name}
%{_bindir}/%{name}at
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/conf.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}*.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# fix symlinked doc file
rm -f CHANGES
cp debian/changelog CHANGES

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name}{,at} %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 conf.* %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -m 644 %{name}.conf %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 %{name}{,at}.1 %{buildroot}%{_mandir}/man1


