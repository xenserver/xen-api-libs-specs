Name:           xcp-rrdd
Version:        1.1.0
Release:        1%{?dist}
Summary:        Statistics gathering daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-rrdd
Source0:        https://github.com/xapi-project/xcp-rrdd/archive/v%{version}/xcp-rrdd-%{version}.tar.gz
Source1:        xcp-rrdd.service
Source2:        xcp-rrdd-sysconfig
Source3:        xcp-rrdd-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-rrd-transport-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  forkexecd-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-libs-devel
BuildRequires:  blktap-devel
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-inotify-devel >= 2.3
#Requires:       redhat-lsb-core
BuildRequires:  ocaml-systemd-devel

%{?systemd_requires}

%description
Statistics gathering daemon for the xapi toolstack.

%prep
%autosetup

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir}
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xcp-rrdd.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/xcp-rrdd
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/xcp-rrdd.conf

%files
%doc README.markdown LICENSE
%{_sbindir}/xcp-rrdd
%{_unitdir}/xcp-rrdd.service
%config(noreplace) %{_sysconfdir}/sysconfig/xcp-rrdd
%config(noreplace) %{_sysconfdir}/xcp-rrdd.conf

%post
%systemd_post xcp-rrdd.service

%preun
%systemd_preun xcp-rrdd.service

%postun
%systemd_postun_with_restart xcp-rrdd.service

%changelog
* Mon Aug 22 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- update to 1.1.0
- xcp-rrdd implements a new mechanism to discover plugins
- new build requirement: ocaml-inotify-devel

* Mon Aug 22 2016 Rafal Mielniczuk <rafal.mielniczuk@citrix.com> - 1.0.1-2
- Package for systemd

* Mon Jul 25 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- Update to 1.0.1

* Mon May 16 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-2
- Re-run chkconfig on upgrade

* Wed Apr 27 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-2
- Remove xen-missing-headers dependency 

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-1
- Update to 0.9.7
- Create new subpackage for the devel libraries now installed

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5, now will start without xen

* Sat Apr 26 2014 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.4, now depends on rrdd-transport

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

