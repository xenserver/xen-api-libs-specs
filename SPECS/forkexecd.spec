Version:        0.9.2
Release:        2%{?dist}

Name:           forkexecd
Summary:        A subprocess management service
License:        LGPL
URL:            https://github.com/xapi-project/forkexecd
Source0:        https://github.com/xapi-project/forkexecd/archive/%{version}/forkexecd-%{version}.tar.gz
Source1:        forkexecd.service
Source2:        forkexecd-sysconfig
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  systemd-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
A service which starts and manages subprocesses, avoiding the need to manually
fork() and exec() in a multithreaded program.

%prep
%setup -q

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
%{__install} -D -m 0755 fe_main.native %{buildroot}%{_sbindir}/forkexecd
%{__install} -D -m 0755 fe_cli.native %{buildroot}%{_sbindir}/forkexecd-cli
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/forkexecd.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/forkexecd

%files
%{_sbindir}/forkexecd
%{_sbindir}/forkexecd-cli
%{_unitdir}/forkexecd.service
%config(noreplace) %{_sysconfdir}/sysconfig/forkexecd

%post
%systemd_post forkexecd.service

%preun
%systemd_preun forkexecd.service

%postun
%systemd_postun_with_restart forkexecd.service

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-fd-send-recv-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}
Requires:       ocaml-xcp-idl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/forkexec/*

%changelog
* Thu Mar 3 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.9.2-2
- Package for systemd

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.2-1
- Update to 0.9.2

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

