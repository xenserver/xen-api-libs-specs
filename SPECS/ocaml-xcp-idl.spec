%global debug_package %{nil}

Name:           ocaml-xcp-idl
Version:        1.11.0
Release:        1%{?dist}
Summary:        Common interface definitions for XCP services
License:        LGPL
URL:            https://github.com/xapi-project/xcp-idl
Source0:        https://github.com/xapi-project/xcp-idl/archive/v%{version}/xcp-idl-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib
BuildRequires:  message-switch-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-xcp-inventory-devel

%description
Common interface definitions for XCP services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       message-switch-devel%{?_isa}
Requires:       ocaml-uri-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-cohttp-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}
Requires:       ocaml-fd-send-recv-devel%{?_isa}
Requires:       ocaml-xmlm-devel%{?_isa}
Requires:       ocaml-sexplib-devel%{?_isa}
Requires:       ocaml-xcp-inventory-devel%{?_isa}
Requires:       ocaml-xcp-rrd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n xcp-idl-%{version}

%build
oasis setup
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export OCAMLFIND_LDCONF=ignore
make install

%files
%doc CHANGES
%doc LICENSE 
%doc MAINTAINERS
%doc README.md 
%{_libdir}/ocaml/xcp
%exclude %{_libdir}/ocaml/xcp/*.a
%exclude %{_libdir}/ocaml/xcp/*.cmxa
%exclude %{_libdir}/ocaml/xcp/*.cmx
%exclude %{_libdir}/ocaml/xcp/*.mli

%files devel
%{_libdir}/ocaml/xcp/*.a
%{_libdir}/ocaml/xcp/*.cmx
%{_libdir}/ocaml/xcp/*.cmxa
%{_libdir}/ocaml/xcp/*.mli

%changelog
* Wed Jan 25 2017 Gabor Igloi <gabor.igloi@citrix.com> - 1.11.0-1
- Automatically generate build files with OASIS at build-time

* Mon Dec 12 2016 Gabor Igloi <gabor.igloi@citrix.com> - 1.10.0-1
- Fix OCaml compiler warnings
- Remove outdated INSTALL file; add INSTALL.md with generic build instructions

* Thu Oct 13 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.5.0-1
- New version - adds v6 interface

* Wed Sep 14 2016 Euan Harris <euan.harris@citrix.com> - 1.4.0-1
- Add force option to VM.start
- Add device information in VIF.state

* Wed Aug 17 2016 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- Update to 1.3.0; the interface to xenopsd changed

* Mon Jul 25 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.0-1
- Update to 1.2.0

* Mon Jul 4 2016 Euan Harris <euan.harris@citrix.com> - 1.1.0-1
- Update to 1.1.0

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 9 2015 David Scott <dave.scott@citrix.com> - 0.14.0-1
- Update to 0.14.0

* Fri Aug 14 2015 David Scott <dave.scott@citrix.com> - 0.13.0-1
- Update to 0.13.0

* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.11.1-1
- Update to 0.11.1
- Update to message-switch.0.11.0 API

* Sat Apr  4 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Fri Apr  3 2015 David Scott <dave.scott@citrix.com> - 0.9.21-2
- Update to cohttp.0.15.2

* Wed Jan 21 2015 David Scott <dave.scott@citrix.com> - 0.9.21-1
- Update to 0.9.21

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.9.20-1
- Update to 0.9.20

* Wed Aug 20 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.18-1
- Update to 0.9.18

* Fri Jun 06 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.17-1
- Update to 0.9.17

* Mon Jun 02 2014 Euan Harris <euan.harris@citrix.com> - 0.9.16-2
- Split files correctly between base and devel packages

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.16-1
- Update to 0.9.16, with RRD fixes

* Fri Apr 25 2014 David Scott <dave.scott@eu.citrix.com> - 0.9.15-1
- Update to 0.9.15, now with vGPU and SR.probe

* Thu Sep 26 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.14-1
- Support searching for executables on the XCP_PATH as well as the PATH

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Logging, channel passing and interface updates

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.12-1
- Allow domain 0 memory policy to be queried

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

