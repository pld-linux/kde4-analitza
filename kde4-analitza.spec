#
# Conditional build:
#
%define         orgname     analitza
%define         _state      stable
%define         qtver       4.8.0
#
Summary:	Mathematical features library
Summary(pl.UTF-8):	analitza
Name:		kde4-analitza
Version:	4.14.3
Release:	2
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	725a6692b626e673b2a93e7848fd9a98
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The analitza library will let you add mathematical features to your
program.

%package devel
Summary:	analitza header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla analitza
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains analitza header files.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe dla analitza.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calgebra
%attr(755,root,root) %ghost %{_libdir}/libanalitza.so.?
%attr(755,root,root) %{_libdir}/libanalitza.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanalitzagui.so.?
%attr(755,root,root) %{_libdir}/libanalitzagui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanalitzaplot.so.?
%attr(755,root,root) %{_libdir}/libanalitzaplot.so.*.*.*
%{_datadir}/apps/libanalitza

%files devel
%defattr(644,root,root,755)
%{_includedir}/analitza
%attr(755,root,root) %{_libdir}/libanalitza.so
%attr(755,root,root) %{_libdir}/libanalitzagui.so
%attr(755,root,root) %{_libdir}/libanalitzaplot.so
%{_includedir}/analitzagui
%{_includedir}/analitzaplot
%{_libdir}/cmake/analitza
