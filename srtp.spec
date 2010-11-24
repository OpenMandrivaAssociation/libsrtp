Summary:	Secure Real-time Transport Protocol (SRTP)
Name:		srtp
Version:	1.4.4
Release:	%mkrel 1
License:	GPL
Group:		System/Libraries
URL:		http://srtp.sourceforge.net/
Source0:	http://srtp.sourceforge.net/%{name}-%{version}.tgz
Provides:	srtp-devel = %{version}-%{release}
Provides:	srtp-static-devel = %{version}-%{release}
Obsoletes:	srtp-devel, srtp-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
SRTP is a security profile for RTP that adds confidentiality, message 
authentication, and replay protection to that protocol. It is specified 
in RFC 3711.

%prep

%setup -q -n %{name}

# lib64 fix
#find -name "Makefile" | xargs perl -pi -e 's|\$\(INSTALL_BASE\)/lib|\$\(INSTALL_BASE\)/%{_lib}|g'

%build

%configure \
	--enable-pic \
	--enable-syslog \
	--enable-generic-aesicm

%make 
%make libsrtp.a

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_includedir}/%{name}/*
%{_libdir}/*.a
