Name:           ocaml-sexplib
Version:        109.20.00
Release:        0
Summary:        Convert values to and from s-expressions in OCaml

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            https://ocaml.janestreet.com/ocaml-core/109.20.00/individual/sexplib-109.20.00.tar.gz
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/sexplib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 4.00.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-type-conv

%description
Convert values to and from s-expressions in OCaml.

%prep
%setup -q -n sexplib-%{version}

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES.txt COPYRIGHT.txt INRIA-DISCLAIMER.txt INSTALL.txt LICENSE-Tywith.txt LICENSE.txt README.md THIRD-PARTY.txt
%{_libdir}/ocaml/sexplib

%changelog
* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

