Name:           xapi-test-utils
Version:        1.0.2
Release:        1%{?dist}
Summary:        An OCaml package with modules for easy unit testing
License:        LGPL+linking exception
URL:            https://github.com/xapi-project/%{name}
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit
BuildRequires:  oasis
BuildRequires:  ocaml-stdext-devel

%description
Helper modules to assist in writing unit tests.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
make install DESTDIR=%{buildroot}%{_libdir}/ocaml

%files
%doc README.md
%{_libdir}/ocaml/%{name}
%exclude %{_libdir}/ocaml/%{name}/*.a
%exclude %{_libdir}/ocaml/%{name}/*.cmxa
%exclude %{_libdir}/ocaml/%{name}/*.cmx

%files devel
%{_libdir}/ocaml/%{name}/*.a
%{_libdir}/ocaml/%{name}/*.cmx
%{_libdir}/ocaml/%{name}/*.cmxa

%changelog
* Wed Jun 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.2-1
- Update to 1.0.2

* Sun May 15 2016 Rob Hoes <rob.hoes@citrix.com> - 1.0.1-1
- Fix (un)installation

* Fri May 13 2016 Rob Hoes <rob.hoes@citrix.com> - 1.0.0-1
- Initial package
