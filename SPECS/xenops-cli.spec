Name:           xenops-cli
Version:        1.0.2
Release:        1%{?dist}
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
URL:            https://github.com/xapi-project/xenops-cli
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  oasis

%description
Command-line interface for xenopsd, the xapi toolstack domain manager.

%prep
%autosetup

%build
make
./main.native --help=groff > xenops-cli.1 && gzip xenops-cli.1

%install
%{__install} -D -m 0755 main.native %{buildroot}%{_sbindir}/xenops-cli
%{__install} -D -m 0644 xenops-cli.1.gz %{buildroot}%{_mandir}/man1/xenops-cli.1.gz

%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xenops-cli
%{_mandir}/man1/xenops-cli.1.gz

%changelog
* Mon Sep 12 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.2-1
- Update to 1.0.2

* Thu May 12 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.1-1
- Update to 1.0.1
- New build dependency on oasis
- Install man page

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 9 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.0-2
- Bump release

* Thu Aug 20 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

