Summary:	C++ interface to PostgreSQL
Summary(pl.UTF-8):	Interfejs C++ do PostgreSQL
Name:		libpqxx
Version:	7.0.6
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/jtv/libpqxx/releases
Source0:	https://github.com/jtv/libpqxx/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d89df9f71643519ec3bfa54505330e24
URL:		http://pqxx.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	postgresql-devel >= 9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for C++ interface to PostgreSQL.

%description -l pl.UTF-8
Pakiet ten zawiera biblioteki dla interfejsu C++ do PostgreSQL.

%package devel
Summary:	C++ interface to PostgreSQL - development part
Summary(pl.UTF-8):	Interfejs C++ do PostgreSQL - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7
Requires:	postgresql-devel >= 9.1

%description devel
This package includes header files for C++ interface.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe dla interfejsu C++.

%package static
Summary:	C++ interface to PostgreSQL - static libraries
Summary(pl.UTF-8):	Interfejs C++ do PostgreSQL - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes static library for interface C++.

%description static -l pl.UTF-8
Pakiet ten zawiera biblioteki statyczne dla interfejsu C++.

%package examples
Summary:	C++ interface to PostgreSQL - examples
Summary(pl.UTF-8):	Interfejs C++ do PostgreSQL - przykładowe programy
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package includes examples for C++ interface.

%description examples -l pl.UTF-8
Pakiet ten zawiera przykładowe programy dla interfejsu C++.

%package doc
Summary:	C++ interface to PostgreSQL - documentation
Summary(pl.UTF-8):	Interfejs C++ do PostgreSQL - dokumentacja
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description doc
This package includes documentation for C++ interface.

%description doc -l pl.UTF-8
Pakiet ten zawiera dokumentację dla interfejsu C++.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

./libtool --mode=install install tools/rmlo $RPM_BUILD_ROOT%{_bindir}

cp -a test/test* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpqxx.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README*
%attr(755,root,root) %{_bindir}/rmlo
%attr(755,root,root) %{_libdir}/libpqxx-7.0.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpqxx.so
%{_includedir}/pqxx
%{_pkgconfigdir}/libpqxx.pc

%files doc
%defattr(644,root,root,755)
%doc doc/html/{Reference,Tutorial}

%files static
%defattr(644,root,root,755)
%{_libdir}/libpqxx.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
