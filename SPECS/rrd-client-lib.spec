%define debug_package %{nil}

Name:           rrd-client-lib
Version:        1.1.0
Release:        1%{?dist}
Summary:        C library for writing RRDD plugins
License:        MIT
Group:          Development/Other
URL:            https://github.com/xapi-project/rrd-client-lib/
Source0:        https://github.com/xapi-project/rrd-client-lib/archive/v%{version}/rrd-client-lib-%{version}.tar.gz
BuildRequires:  zlib
BuildRequires:  ocaml-rrd-transport-devel

%description
Library for writing RRDD plugins in C. This package contains just the
dynamic library but no header files or static libraries.

%package devel
Group:          Development/Libraries
Summary:        Libraries and header files for rrd development
Requires:       rrd-client-lib = %{version}-%{release}

%description devel
C library for writing RRDD plugins - including header files

%prep
%autosetup

%build
make 

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install librrd.so  %{buildroot}%{_libdir}
install librrd.h   %{buildroot}%{_includedir}
install librrd.a   %{buildroot}%{_libdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE parson/README.md
%{_libdir}/librrd.so

%files devel
%{_includedir}/librrd.h
%{_libdir}/librrd.a

%changelog
* Thu Sep 01 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- New upstream release, compatible with xcp-rrdd plugin mechanism
* Mon Aug 15 2016 Christian Lindig <christian.lindig@citrix.com> - 1.0.1
- New upstream release that adds more tests
* Wed Aug 10 2016 Christian Lindig <christian.lindig@citrix.com> - 1.0.0
- Initial package
