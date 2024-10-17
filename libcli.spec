%define major 1
%define libname %mklibname cli
%define develname %mklibname -d cli

Name:		libcli
Version:	1.10.7
Release:	1
Summary:	A shared library for a Cisco-like cli
Group:		System/Libraries
License:	LGPLv2+
URL:		https://sites.dparrish.com/libcli
Source0:	https://github.com/dparrish/libcli/archive/refs/tags/V%{version}.tar.gz

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
%autosetup -p1
%if "%{_lib}" != "lib"
sed -i -e "s,/lib$,/%{_lib},g;s,/lib ,/%{_lib} ,g" Makefile
%endif

%build
%make_build STATIC_LIB=0 PREFIX=%{_prefix}

%install
%make_install STATIC_LIB=0 PREFIX=%{_prefix}

%files -n %{libname}
%{_libdir}/*.so
%{_libdir}/*.so.*

%files -n %develname
%{_includedir}/*.h
