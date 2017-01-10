Name:           message-switch
Version:        1.0.1
Release:        1%{?dist}
Summary:        A store and forward message switch
License:        FreeBSD
URL:            https://github.com/xapi-project/message-switch
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        message-switch-init
Source2:        message-switch-conf
Source3:        message-switch-bugtool1.xml
Source4:        message-switch-bugtool2.xml
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
# Not available in the build chroot
#Requires:      redhat-lsb-core

Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
A store and forward message switch for OCaml.

%prep
%autosetup
cp %{SOURCE1} message-switch-init
cp %{SOURCE2} message-switch-conf
cp %{SOURCE3} message-switch.xml
cp %{SOURCE4} stuff.xml

%build
sed -i s/,\ bisect// _oasis
oasis setup
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install switch_main.native %{buildroot}/%{_sbindir}/message-switch
install main.native %{buildroot}/%{_sbindir}/message-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 message-switch-init %{buildroot}%{_sysconfdir}/init.d/message-switch
install -m 0644 message-switch-conf %{buildroot}/etc/message-switch.conf
mkdir -p %{buildroot}/etc/xensource/bugtool/message-switch
install -m 0644 message-switch.xml %{buildroot}/etc/xensource/bugtool/message-switch.xml
install -m 0644 stuff.xml %{buildroot}/etc/xensource/bugtool/message-switch/stuff.xml

%files
%{_sbindir}/message-switch
%{_sbindir}/message-cli
%{_sysconfdir}/init.d/message-switch
%config(noreplace) /etc/message-switch.conf
/etc/xensource/bugtool/message-switch/stuff.xml
/etc/xensource/bugtool/message-switch.xml

%post
case $1 in
  1) # install
    /sbin/chkconfig --add message-switch
    ;;
  2) # upgrade
    /sbin/chkconfig --del message-switch
    /sbin/chkconfig --add message-switch
    ;;
esac

%preun
case $1 in
  0) # uninstall
    /sbin/service message-switch stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del message-switch
    ;;
  1) # upgrade
    ;;
esac

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
* Tue Jan 10 2017 Rob Hoes <rob.hoes@citrix.com> - 1.0.1-1
- git: Add metadata to the result of `git archive`

* Mon May 16 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-2
- Re-run chkconfig on upgrade

* Wed Apr 13 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Update to 1.0.0

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

