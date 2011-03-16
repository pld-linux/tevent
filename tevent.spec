Summary:	An event system library
Summary(pl.UTF-8):	Biblioteka systemu zdarzeń
Name:		tevent
Version:	0.9.11
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://samba.org/ftp/tevent/%{name}-%{version}.tar.gz
# Source0-md5:	407b2bedeb95d1d6d1c0acdc2a4dd4f6
URL:		http://tevent.samba.org/
BuildRequires:	libtalloc-devel >= 2:2.0.5
BuildRequires:	python-devel >= 1:2.4.2
BuildRequires:	python-talloc-devel >= 2:2.0.5
BuildRequires:	rpm-pythonprov
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
Requires:	libtalloc-devel >= 2:2.0.5

%description devel
Header files for tevent library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tevent.

%package -n python-tevent
Summary:	Python bindings for tevent
Summary(pl.UTF-8):	Pythonowy interfejs do tevent
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-talloc >= 2:2.0.5
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
	--libdir=%{_libdir}

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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