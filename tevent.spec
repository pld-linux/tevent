Summary:	An event system library
Summary(pl.UTF-8):	Biblioteka systemu zdarzeń
Name:		tevent
Version:	0.14.1
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://www.samba.org/ftp/tevent/%{name}-%{version}.tar.gz
# Source0-md5:	ac12f248559e21410b036f4bfe6b8987
URL:		https://tevent.samba.org/
BuildRequires:	cmocka-devel >= 1.1.3
BuildRequires:	libbsd-devel
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-talloc-devel >= 2:2.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.704
BuildRequires:	talloc-devel >= 2:2.4.0
# tevent 0.10+ dropped python2 support
Obsoletes:	python-tevent < 0.10
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
Requires:	talloc-devel >= 2:2.4.0

%description devel
Header files for tevent library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tevent.

%package -n python3-tevent
Summary:	Python 3 bindings for tevent
Summary(pl.UTF-8):	Interfejs Pythona 3 do tevent
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-talloc >= 2:2.4.0

%description -n python3-tevent
Python 3 bindings for tevent.

%description -n python3-tevent -l pl.UTF-8
Interfejs Pythona 3 do tevent.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./configure \
    --jobs=1 \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --disable-rpath

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

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

%files -n python3-tevent
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_tevent.cpython-*.so
%{py3_sitedir}/tevent.py
%{py3_sitedir}/__pycache__/tevent.cpython-*.py[co]
