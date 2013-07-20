# NOTE: it's totally different than libmimedir used in gnome-pim
#       (http://me.in-berlin.de/~jroger/gnome-pim/ up to 0.2.1 version)
Summary:	RFC 2425 implementation
Summary(pl.UTF-8):	Implementacja RFC 2425
Name:		libmimedir-vlm
Version:	0.4
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/libmimedir-%{version}.tar.gz
# Source0-md5:	156e1eb69377d9ae9180a09e38148ec6
Patch0:		%{name}-shared.patch
URL:		http://libmimedir.sourceforge.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) written by Lev
Walkin.

%description -l pl.UTF-8
Implementacja RFC 2425 (MIME Directory Profile). Autorem tej wersji
jest Lev Walkin.

%package devel
Summary:	Header file for libmimedir library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libmimedir
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libmimedir library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libmimedir.

%package static
Summary:	Static libmimedir library
Summary(pl.UTF-8):	Statyczna biblioteka libmimedir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmimedir library.

%description static -l pl.UTF-8
Statyczna biblioteka libmimedir.

%prep
%setup -q -n libmimedir-%{version}
%patch0 -p1

%build
%configure
%{__make}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmimedir-vlm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmimedir-vlm.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimedir-vlm.so
%{_libdir}/libmimedir-vlm.la
%{_includedir}/libmimedir.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmimedir-vlm.a
