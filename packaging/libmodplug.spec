Summary: MOD music file playing library
Name: libmodplug
Version: 0.8.8.5
Release: 1
License: Public Domain
Group: System/Libraries
URL: http://modplug-xmms.sourceforge.net/

Source: %{name}-%{version}.tar.gz

%description
Libmodplug is the library behind Modplug-XMMS, a fully featured, complete
input plugin for XMMS which plays mod-like music formats

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libmodplug.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmodplug/
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc
%exclude %{_libdir}/libmodplug.la

