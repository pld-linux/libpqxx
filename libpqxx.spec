Summary:	C++ interface to PostgreSQL
Summary(pl):	Interfejs C++ do PostgreSQL
Name:		libpqxx
Version:	1.4.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://gborg.postgresql.org/pub/libpqxx/stable/%{name}-%{version}.tar.gz
URL:		http://gborg.postgresql.org/project/libpqxx/projdisplay.php
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for C++ interface to PostgreSQL.

%description -l pl
Pakiet ten zawiera biblioteki dla interfejsu C++ do PostgreSQL.

%package devel
Summary:	C++ interface to PostgreSQL - development part
Summary(pl):	Interfejs C++ do PostgreSQL - czePae programistyczna
Requires:	%{name} = %{version}
Requires:	postgresql-devel
Group:		Development/Libraries

%description devel
This package includes library and header files for C++ interface.

%description devel -l pl
Pakiet ten zawiera biblioteki i pliki nag³ówkowe dla interfejsu C++.

%package static
Summary:	C++ interface to PostgreSQL - static libraries
Summary(pl):	Interfejs C++ do PostgreSQL - biblioteki statyczne
Requires:	%{name}-devel = %{version}
Group:		Development/Libraries

%description static
This package includes static library for interface C++.

%description static -l pl
Pakiet ten zawiera biblioteki statyczne dla interfejsu C++.

%package examples
Summary:	C++ interface to PostgreSQL - examples
Summary(pl):	Interfejs C++ do PostgreSQL - przyk³adowe programy
Requires:	%{name}-devel = %{version}
Group:		Documentation

%description examples
This package includes examples for interface C++.

%description examples -l pl
Pakiet ten zawiera przyk³adowe programy dla interfejsu C++.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a test/test* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/pqxx

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
