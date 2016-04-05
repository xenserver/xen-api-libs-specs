Summary: Xapi storage script plugin server
Name:    xapi-storage-script
Version: 0.12.1
Release: 1%{?dist}
License: LGPL+linking exception
URL:     https://github.com/xapi-project/xapi-storage-script
Source0: https://github.com/xapi-project/xapi-storage-script/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: xapi-storage-script.service
Source2: xapi-storage-script-sysconfig
Source3: xapi-storage-script-conf.in
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-xcp-idl-devel
BuildRequires: ocaml-async-inotify-devel
BuildRequires: message-switch-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: xapi-storage-ocaml-plugin-devel
BuildRequires: ocaml-xcp-rrd-devel
BuildRequires: systemd-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Allows script-based Xapi storage adapters.

%prep 
%setup -q -n %{name}-%{version}

%build
make
mv main.native xapi-storage-script
./xapi-storage-script --help=groff > xapi-storage-script.8 && gzip xapi-storage-script.8
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE3} > xapi-storage-script.conf

%install
mkdir -p %{buildroot}%{_libexecdir}/xapi-storage-script
mkdir -p %{buildroot}%{_libexecdir}/xapi-storage-script/volume
mkdir -p %{buildroot}%{_libexecdir}/xapi-storage-script/datapath
%{__install} -D -m 0755 xapi-storage-script %{buildroot}%{_sbindir}/xapi-storage-script
%{__install} -D -m 0644 xapi-storage-script.conf %{buildroot}%{_sysconfdir}/xapi-storage-script.conf
%{__install} -D -m 0644 xapi-storage-script.8.gz %{buildroot}%{_mandir}/man8/xapi-storage-script.8.gz
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xapi-storage-script.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/xapi-storage-script

%post
%systemd_post xapi-storage-script.service

%preun
%systemd_preun xapi-storage-script.service

%postun
%systemd_postun_with_restart xapi-storage-script.service

%files
%{_libexecdir}/xapi-storage-script
%{_libexecdir}/xapi-storage-script/volume
%{_libexecdir}/xapi-storage-script/datapath
%{_sbindir}/xapi-storage-script
%{_mandir}/man8/xapi-storage-script.8.gz
%{_unitdir}/xapi-storage-script.service
%config(noreplace) %{_sysconfdir}/sysconfig/xapi-storage-script
%config(noreplace) %{_sysconfdir}/xapi-storage-script.conf

%changelog
* Thu Mar  8 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.12.1-2
- Package for systemd

* Wed Feb 03 2016 Euan Harris <euan.harris@citrix.com> - 0.12.1-1
- Update to 0.12.1

* Tue Sep 15 2015 David Scott <dave.scott@citrix.com> - 0.12.0-3
- Bump release

* Wed Sep  9 2015 David Scott <dave.scott@citrix.com> - 0.12.0-1
- Update to 0.12.0

* Fri Aug  7 2015 David Scott <dave.scott@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Tue Aug  4 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Mon Jul 20 2015 David Scott <dave.scott@citrix.com> - 0.9.0-2
- Backport robustness patch

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.9.0-1
- Update to 0.9.0

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.8.0-2
- Backport clone-on-boot fix

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 9 2015 David Scott <dave.scott@citrix.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jul 8 2015 David Scott <dave.scott@citrix.com> - 0.6.0-1
- Update to 0.6.0

* Tue Jul 7 2015 David Scott <dave.scott@citrix.com> - 0.5.0-1
- Update to 0.5.0

* Tue Apr 28 2015 David Scott <dave.scott@citrix.com> - 0.4.0-1
- Update to 0.4.0

* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.3.0-1
- Update to 0.3.0

* Sat Apr  4 2015 David Scott <dave.scott@citrix.com> - 0.2.0-1
- Update to 0.2.0

* Sun Oct 19 2014 David Scott <dave.scott@citrix.com> - 0.1.2-1
- Write the pidfile properly
- VDI.epoch_{begin,end} are no-ops

* Fri Oct 17 2014 David Scott <dave.scott@citrix.com> - 0.1.1-1
- Add the /volume and /datapath subdirectories to the package
- Fix daemonization
- Use syslog

* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
