%define debug_package %{nil}

Name:           ocaml-mirage-profile
Version:        0.6.1
Release:        1%{?dist}
Summary:        Library for collecting trace data
License:        BSD-2-clause
URL:            https://github.com/mirage/mirage-profile/
Source0:        https://github.com/mirage/mirage-profile/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-types-devel

%description
Library for collecting trace data

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-profile-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%{_libdir}/ocaml/mirage-profile
%exclude %{_libdir}/ocaml/mirage-profile/*.a
%exclude %{_libdir}/ocaml/mirage-profile/*.cmxa
%exclude %{_libdir}/ocaml/mirage-profile/*.cmx
%exclude %{_libdir}/ocaml/mirage-profile/*.mli

%files devel
%{_libdir}/ocaml/mirage-profile/*.a
%{_libdir}/ocaml/mirage-profile/*.cmx
%{_libdir}/ocaml/mirage-profile/*.cmxa
%{_libdir}/ocaml/mirage-profile/*.mli

%changelog
* Thu Jan 28 2016 Andrew Cooper <andrew.cooper3@citrix.com> - 0.6.1-1
- Initial package
