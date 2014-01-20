%define debug_package %{nil}

Name:           ocaml-mirage-types
Version:        1.0.0
Release:        1
Summary:        MirageOS interfaces
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/mirage-types
Source0:        http://github.com/mirage/mirage-types/archive/v%{version}/mirage-types-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-cstruct-devel ocaml-ounit-devel
Requires:       ocaml ocaml-findlib

%description
This library contains interfaces to build applications that are compatible with the Mirage operating system. It defines only interfaces, and no concrete modules.

See http://openmirage.org for more information.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mirage-types-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/ocaml/mirage-types/META
%{_libdir}/ocaml/mirage-types/v1.cmi

%files devel
%defattr(-,root,root)
%doc CHANGES README.md
#%{_libdir}/ocaml/mirage-types/v1.mli
%{_libdir}/ocaml/mirage-types/v1.cmti

%changelog
* Mon Jan 20 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
