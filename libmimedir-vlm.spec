# NOTE: it's totally different than libmimedir used in gnome-pim
#       (http://me.in-berlin.de/~jroger/gnome-pim/ up to 0.2.1 version)
Summary:	RFC 2425 implementation
Summary(pl):	Implementacja RFC 2425
Name:		libmimedir-vlm
Version:	0.3
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/synce/libmimedir-0.3.tar.gz
# Source0-md5:	bb967f6f8931d4efdc34d3729b7f819b
Patch0:		libmimedir-destdir.patch
URL:		http://libmimedir.sourceforge.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of RFC 2425 (MIME Directory Profile) written by Lev
Walkin.

%description -l pl
Implementacja RFC 2425 (MIME Directory Profile). Autorem tej wersji
jest Lev Walkin.

%prep
%setup -q -n libmimedir-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libmimedir{,-vlm}.a

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmimedir-vlm.a
%{_includedir}/libmimedir.h
