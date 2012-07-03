%define major 1
%define libname %mklibname cli %major
%define develname %mklibname -d cli



Name:		libcli
Version:	1.9.5
Release:	1
Summary:	A shared library for a Cisco-like cli
Group:		System/Libraries
License:	LGPLv2+
URL:		http://sites.dparrish.com/libcli
Source0:	https://github.com/downloads/dparrish/libcli/libcli-%{version}.tar.gz

%description
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 


%package -n	%libname
Summary:	A shared library for a Cisco-like cl
Group:		System/Libraries

%description -n %libname

Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

%package -n	%develname
Summary:	Development files for libcli
Provides:	cli-devel = %{version}-%{release}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %develname
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

These are the development files.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 libcli*.h %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 libcli.so.1.9.5 %{buildroot}%{_libdir}/
ln -s %{_libdir}/libcli.so.1.9.5 %{buildroot}%{_libdir}/libcli.so.1.9
ln -s %{_libdir}/libcli.so.1.9 %{buildroot}%{_libdir}/libcli.so


%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.*

%files -n %develname
%doc README
%{_libdir}/*.so
%{_includedir}/*.h
