Name:           xcp-networkd
Version:        0.9.6
Release:        2%{?dist}
Summary:        Simple host network management service for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-networkd
Source0:        https://github.com/xapi-project/xcp-networkd/archive/v%{version}/xcp-networkd-%{version}.tar.gz
Source1:        xcp-networkd.service
Source2:        xcp-networkd-sysconfig
Source3:        xcp-networkd-conf
Source4:        xcp-networkd-network-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  ocaml-netlink-devel
BuildRequires:  libffi-devel
BuildRequires:  systemd-devel

Requires:       ethtool
Requires:       libnl3

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Simple host networking management service for the xapi toolstack.

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xcp-networkd.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/xcp-networkd
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/xcp-networkd.conf
%{__install} -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/xensource/network.conf

%files
%doc README.markdown LICENSE MAINTAINERS
%{_sbindir}/xcp-networkd
%{_bindir}/networkd_db
%{_unitdir}/xcp-networkd.service
%{_mandir}/man1/xcp-networkd.1.gz
%config(noreplace) %{_sysconfdir}/sysconfig/xcp-networkd
%config(noreplace) %{_sysconfdir}/xcp-networkd.conf
%config(noreplace) %{_sysconfdir}/xensource/network.conf

%post
%systemd_post xcp-networkd.service

%preun
%systemd_preun xcp-networkd.service

%postun
%systemd_postun_with_restart xcp-networkd.service

%changelog
* Thu Mar 3 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.9.6-2
- Package for systemd

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.4-1
- Update to 0.9.4
- Add networkd_db CLI

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Wed Aug 28 2013 David Scott <dave.scott@eu.citrix.com>
- When loading the bridge module, prevent guest traffic being
  processed by the domain 0 firewall

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Fri Jun  7 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

