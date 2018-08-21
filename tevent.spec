Summary:	An event system library
Summary(pl.UTF-8):	Biblioteka systemu zdarzeń
Name:		tevent
Version:	0.9.37
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://www.samba.org/ftp/tevent/%{name}-%{version}.tar.gz
# Source0-md5:	6859cd4081fdb2a76b1cb4bf1c803a59
URL:		http://tevent.samba.org/
BuildRequires:	talloc-devel >= 2:2.1.13
BuildRequires:	python-devel >= 1:2.4.2
BuildRequires:	python-talloc-devel >= 2:2.1.13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tevent is an event system based on the talloc memory management
library. It is the core event system used in Samba.

The low level tevent has support for many event types, including
timers, signals, and the classic file descriptor events.

Tevent also provide helpers to deal with asynchronous code providing
the tevent_req (tevent request) functions.

%description -l pl.UTF-8
Tevent to system zdarzeń oparty na bibliotece zarządzającej pamięcią
talloc. Jest to główny system zdarzeń używany w Sambie.

Niskopoziomowo tevent obsługuje wiele rodzajów zdarzeń, w tym
zegary, sygnały i zdarzenia związane z klasycznymi deskryptorami
plików.

Tevent udostępnia także funkcje pomocnicze tevent_req (żądanie tevent)
dla kodu asynchronicznego.

%package devel
Summary:	Header files for tevent library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tevent
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	talloc-devel >= 2:2.1.13

%description devel
Header files for tevent library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tevent.

%package -n python-tevent
Summary:	Python bindings for tevent
Summary(pl.UTF-8):	Pythonowy interfejs do tevent
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-talloc >= 2:2.1.13
%pyrequires_eq  python-libs

%description -n python-tevent
Python bindings for tevent.

%description -n python-tevent -l pl.UTF-8
Pythonowy interfejs do tevent.

%prep
%setup -q

%build
# note: configure in fact is waf call
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
PYTHONDIR=%{py_sitedir} \
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtevent.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtevent.so
%{_includedir}/tevent.h
%{_pkgconfigdir}/tevent.pc

%files -n python-tevent
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_tevent.so
%{py_sitedir}/tevent.py[co]
