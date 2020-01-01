%define	major 1
%define libname	%mklibname srtp2 %{major}
%define develname %mklibname -d srtp2
%define _disable_rebuild_configure 1

Summary:	Secure Real-time Transport Protocol (SRTP)
Name:		libsrtp
Version:	2.3.0
Release:	1
License:	GPL
Group:		System/Libraries
URL:		https://github.com/cisco/libsrtp/
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig(libpcap)

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
%autosetup -p1

%build

%configure \
	--enable-syslog \
	--enable-generic-aesicm

%make_build shared_library

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc CHANGES
%{_includedir}/srtp2
%{_libdir}/*.so
%{_libdir}/pkgconfig/libsrtp2.pc
