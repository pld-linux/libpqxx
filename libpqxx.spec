Summary:	C++ interface to PostgreSQL
Summary(pl):	Interfejs C++ do PostgreSQL
Name:		libpqxx
Version:	2.4.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://gborg.postgresql.org/pub/libpqxx/stable/%{name}-%{version}.tar.gz
# Source0-md5:	d7368eec9e8e929a2d106cde1d9b6a22
URL:		http://gborg.postgresql.org/project/libpqxx/projdisplay.php
BuildRequires:	libstdc++-devel
BuildRequires:	postgresql-devel >= 7.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for C++ interface to PostgreSQL.

%description -l pl
Pakiet ten zawiera biblioteki dla interfejsu C++ do PostgreSQL.

%package devel
Summary:	C++ interface to PostgreSQL - development part
Summary(pl):	Interfejs C++ do PostgreSQL - czê¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	postgresql-devel

%description devel
This package includes header files for C++ interface.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe dla interfejsu C++.

%package static
Summary:	C++ interface to PostgreSQL - static libraries
Summary(pl):	Interfejs C++ do PostgreSQL - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes static library for interface C++.

%description static -l pl
Pakiet ten zawiera biblioteki statyczne dla interfejsu C++.

%package examples
Summary:	C++ interface to PostgreSQL - examples
Summary(pl):	Interfejs C++ do PostgreSQL - przyk³adowe programy
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package includes examples for C++ interface.

%description examples -l pl
Pakiet ten zawiera przyk³adowe programy dla interfejsu C++.

%package doc
Summary:	C++ interface to PostgreSQL - documentation
Summary(pl):	Interfejs C++ do PostgreSQL - dokumentacja
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description doc
This package includes documentation for C++ interface.

%description doc -l pl
Pakiet ten zawiera dokumentacjê dla interfejsu C++.

%prep
%setup -q

%build
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

./libtool --mode=install install tools/rmlo $RPM_BUILD_ROOT%{_bindir}

cp -a test/test* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc
cp -arv doc/html/{Reference,Tutorial} $RPM_BUILD_ROOT%{_docdir}/%{name}-doc


%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/rmlo
%attr(755,root,root) %{_libdir}/libpqxx-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pqxx-config
%attr(755,root,root) %{_libdir}/libpqxx.so
%{_libdir}/libpqxx.*la
%{_includedir}/pqxx
%{_pkgconfigdir}/*.pc

%files doc
%defattr(644,root,root,755)
%docdir %{_docdir}/%{name}-doc
%{_docdir}/%{name}-doc/Tutorial/*
%{_docdir}/%{name}-doc/Reference/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpqxx.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
