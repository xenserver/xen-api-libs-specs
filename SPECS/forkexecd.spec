Version:        1.0.0
Release:        2%{?dist}
Name:           forkexecd
Summary:        A subprocess management service
License:        LGPL
URL:            https://github.com/xapi-project/forkexecd
Source0:        https://github.com/xapi-project/forkexecd/archive/%{version}/forkexecd-%{version}.tar.gz
Source1:        forkexecd-init
BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-oclock-devel
#Requires:  redhat-lsb-core

Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
A service which starts and manages subprocesses, avoiding the need to manually
fork() and exec() in a multithreaded program.

%prep
%setup -q
cp %{SOURCE1} forkexecd-init

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install fe_main.native %{buildroot}/%{_sbindir}/forkexecd
install fe_cli.native %{buildroot}/%{_sbindir}/forkexecd-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 forkexecd-init %{buildroot}%{_sysconfdir}/init.d/forkexecd


%files
%{_sbindir}/forkexecd
%{_sbindir}/forkexecd-cli
%{_sysconfdir}/init.d/forkexecd

%post
case $1 in
  1) # install
    /sbin/chkconfig --add forkexecd
    ;;
  2) # upgrade
    /sbin/chkconfig --del forkexecd
    /sbin/chkconfig --add forkexecd
    ;;
esac

%preun
case $1 in
  0) # uninstall
    /sbin/service forkexecd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del forkexecd
    ;;
  1) # upgrade
    ;;
esac

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
* Mon May 16 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-2
- Re-run chkconfig on upgrade

* Wed Apr 13 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Update to 1.0.0
- Add build dependency on oasis

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.2-1
- Update to 0.9.2

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

