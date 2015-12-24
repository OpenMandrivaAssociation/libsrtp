%define	major 1
%define libname	%mklibname srtp %{major}
%define develname %mklibname -d srtp
%define _disable_rebuild_configure 1

Summary:	Secure Real-time Transport Protocol (SRTP)
Name:		libsrtp
Version:	1.5.3
Release:	1
License:	GPL
Group:		System/Libraries
URL:		https://github.com/cisco/libsrtp/
Source0:	https://github.com/cisco/libsrtp/releases/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake libtool

%description
SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified
in RFC 3711.

%package -n	%{libname}
Summary:	Secure Real-time Transport Protocol (SRTP) library
Group:          System/Libraries

%description -n	%{libname}
SRTP is a security profile for RTP that adds confidentiality, message 
authentication, and replay protection to that protocol. It is specified 
in RFC 3711.

%package -n	%{develname}
Summary:	Development files for the SRTP library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	srtp-devel = %{version}-%{release}

%description -n	%{develname}
SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified 
in RFC 3711.

This package contains the development files for the Secure Real-time Transport
Protocol (SRTP) library

%prep

%setup -q
%apply_patches

%build

%configure \
	--enable-syslog \
	--enable-generic-aesicm

%make libsrtp.so.%{major}

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc CHANGES README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc CHANGES README
%{_includedir}/srtp/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libsrtp.pc


%changelog
* Tue Apr 03 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-4mdv2012.0
+ Revision: 788942
- bump release
- libify the thing

* Sat Dec 18 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.4-2mdv2011.0
+ Revision: 622766
- Add -fPIC to CFLAGS

* Wed Nov 24 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.4-1mdv2011.0
+ Revision: 600451
- 1.4.4

* Wed Nov 24 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.2-1mdv2011.0
+ Revision: 600442
- 1.4.2
  initial version
- create srtp

