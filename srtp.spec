%define	major 0
%define libname	%mklibname srtp %{major}
%define develname %mklibname -d srtp

Summary:	Secure Real-time Transport Protocol (SRTP)
Name:		srtp
Version:	1.4.4
Release:	12
License:	GPL
Group:		System/Libraries
URL:		http://srtp.sourceforge.net/
Source0:	http://srtp.sourceforge.net/%{name}-%{version}.tgz
Patch0:		srtp-shared.diff
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

%setup -q -n %{name}
%patch0 -p1

# lib64 fix
#find -name "Makefile" | xargs perl -pi -e 's|\$\(INSTALL_BASE\)/lib|\$\(INSTALL_BASE\)/%{_lib}|g'

%build
autoreconf -fi

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export CC=gcc
export CXX=g++
%configure \
	--enable-pic \
	--enable-syslog \
	--enable-generic-aesicm

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc CHANGES README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc CHANGES README
%{_includedir}/%{name}/*
%{_libdir}/*.so


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

