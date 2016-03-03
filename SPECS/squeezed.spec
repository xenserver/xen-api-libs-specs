Name:           squeezed
Version:        0.11.0
Release:        2%{?dist}
Summary:        Memory ballooning daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/squeezed
Source0:        https://github.com/xapi-project/squeezed/archive/v%{version}/squeezed-%{version}.tar.gz
Source1:        squeezed.service
Source2:        squeezed-sysconfig
Source3:        squeezed-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-dom0-libs
BuildRequires:  xen-libs-devel
BuildRequires:  xen-libs
BuildRequires:  systemd-devel
Requires:       message-switch

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Memory ballooning daemon for the xapi toolstack.

%prep
%setup -q

%build
./configure --prefix %{_prefix} --destdir %{buildroot}
make

%install
%{__install} -D -m 0755 squeezed.native %{buildroot}%{_sbindir}/squeezed
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/squeezed.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/squeezed
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/squeezed.conf

%files
%doc README.md 
%doc LICENSE 
%doc MAINTAINERS
%{_sbindir}/squeezed
%{_unitdir}/squeezed.service
%config(noreplace) %{_sysconfdir}/sysconfig/squeezed
%config(noreplace) %{_sysconfdir}/squeezed.conf

%post
%systemd_post squeezed.service

%preun
%systemd_preun squeezed.service

%postun
%systemd_postun_with_restart squeezed.service

%changelog
* Thu Mar 3 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.11.0-2
- Package for systemd

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-2
- Remove dependency on xen-missing-headers

* Fri Jun  6 2014 Jonathan Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-1
- Update to 0.10.6

* Fri Apr 11 2014 Euan Harris <euan.harris@citrix.com> - 0.10.5-1
- Switch build from obuild to oasis

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.4-1
- Update to 0.10.4

* Fri Sep 20 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.3-1
- Update to allow minimal operation without xen

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.2-1
- Update to new xenstore interface in v1.2.3

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.1-1
- Add get_domain_zero_palicy call required for domain 0 ballooning

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.0-1
- Update to 0.10.0, with support for domain 0 ballooning

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

