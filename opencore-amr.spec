#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	OpenCORE Framework implementation of Adaptive Multi Rate Narrowband and Wideband speech codec
Summary(pl.UTF-8):	Szkielet OpenCORE kodeków mowy Adaptive Multi Rate Narrowband i Wideband
Name:		opencore-amr
Version:	0.1.6
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	03de025060a4f16c4c44218f65e13e95
URL:		http://opencore-amr.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec and an
implementation for the 3GPP TS 26.173 specification for the Adaptive
Multi-Rate - Wideband (AMR-WB) speech decoder. The implementation is
derived from the OpenCORE framework, part of the Google Android
project.

%description -l pl.UTF-8
Biblioteka ta zawiera implementację specyfikacji 3GPP TS 26.073 kodeka
mowy Adaptive Multi Rate (AMR) oraz implementację specyfikacji 3GPP TS
26.173 dekodera mowy Adaptive Multi-Rate - Wideband (AMR-WB).
Implementacja pochodzi ze szkieletu OpenCORE, części projektu Google
Android.

%package devel
Summary:	Header files for opencore-amr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki opencore-amr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for opencore-amr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opencore-amr.

%package static
Summary:	Static opencore-amr library
Summary(pl.UTF-8):	Statyczna biblioteka opencore-amr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opencore-amr library.

%description static -l pl.UTF-8
Statyczna biblioteka opencore-amr.

%prep
%setup -q

%{__rm} m4/libtool.m4 m4/lt*.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable static_libs static}
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
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libopencore-amrnb.so.*.*.*
%attr(755,root,root) %{_libdir}/libopencore-amrwb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencore-amrnb.so.0
%attr(755,root,root) %ghost %{_libdir}/libopencore-amrwb.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencore-amrnb.so
%attr(755,root,root) %{_libdir}/libopencore-amrwb.so
%{_libdir}/libopencore-amrnb.la
%{_libdir}/libopencore-amrwb.la
%{_includedir}/opencore-amrnb
%{_includedir}/opencore-amrwb
%{_pkgconfigdir}/opencore-amrnb.pc
%{_pkgconfigdir}/opencore-amrwb.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopencore-amrnb.a
%{_libdir}/libopencore-amrwb.a
%endif
