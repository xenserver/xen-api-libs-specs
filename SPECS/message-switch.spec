Name:           message-switch
Version:        0.12.0
Release:        2%{?dist}
Summary:        A store and forward message switch
License:        FreeBSD
URL:            https://github.com/djs55/message-switch
Source0:        https://github.com/djs55/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        message-switch.service
Source2:        message-switch-sysconfig
Source3:        message-switch-conf
Source4:        message-switch-bugtool1.xml
Source5:        message-switch-bugtool2.xml
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires: ocaml-cohttp-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: ocaml-async-devel
BuildRequires: ocaml-shared-block-ring-devel
BuildRequires: ocaml-mtime-devel
BuildRequires: ocaml-pa-structural-sexp-devel

BuildRequires: oasis
BuildRequires: systemd-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
A store and forward message switch for OCaml.

%prep
%setup -q

%build
sed -i s/,\ bisect// _oasis
oasis setup
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
%{__install} -D -m 0755 switch_main.native %{buildroot}%{_sbindir}/message-switch
%{__install} -D -m 0755 main.native %{buildroot}/%{_sbindir}/message-cli
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/message-switch.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/message-switch
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/message-switch.conf
%{__install} -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/xensource/bugtool/message-switch.xml
%{__install} -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/xensource/bugtool/message-switch/stuff.xml

%files
%{_sbindir}/message-switch
%{_sbindir}/message-cli
%{_unitdir}/message-switch.service
%{_sysconfdir}/xensource/bugtool/message-switch.xml
%{_sysconfdir}/xensource/bugtool/message-switch/stuff.xml
%config(noreplace) %{_sysconfdir}/sysconfig/message-switch
%config(noreplace) %{_sysconfdir}/message-switch.conf

%post
%systemd_post message-switch.service

%preun
%systemd_preun message-switch.service

%postun
%systemd_postun_with_restart message-switch.service

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cohttp-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README.md CHANGES
%{_libdir}/ocaml/message_switch/*

%changelog
* Fri Mar  4 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.12.0-2
- Package for systemd

* Thu Jul 16 2015 David Scott <dave.scott@citrix.com> - 0.12.0-1
- Add bugtool collection
- Several bugfixes

* Mon Jun 15 2015 David Scott <dave.scott@citrix.com> - 0.11.0-3
- Add blocking fix.

* Fri Jun 12 2015 David Scott <dave.scott@citrix.com> - 0.11.0-2
- Add tail-recursion fix

* Thu Apr 23 2015 David Scott <dave.scott@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Sun Apr 19 2015 David Scott <dave.scott@citrix.com> - 0.10.5.1-2
- Fix for bug exposed by cohttp upgrade

* Thu Apr  2 2015 David Scott <dave.scott@citrix.com> - 0.10.5.1-1
- Update to 0.10.5.1

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.10.4-1
- Update to 0.10.4, enable core/async

* Thu Jun 19 2014 David Scott <dave.scott@citrix.com> - 0.10.3-1
- Update to 0.10.3

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.2-1
- Update to 0.10.2

* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.1-1
- Update to 0.10.1 which is more tolerant of startup orderings

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

