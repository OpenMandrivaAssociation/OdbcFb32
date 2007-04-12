%define	name OdbcFb32
%define version 2.0.0142
%define release %mkrel 4

Summary:	ODBC driver for Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	IDPL
URL:		http://www.firebirdsql.org/
Group:		System/Libraries
Source:		OdbcFb32-beta-%{version}-src.tar.bz2
Patch:		OdbcFb32-libname.diff
ExclusiveArch:	i586
BuildRequires:	firebird-devel
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	libstdc++6-devel
BuildRequires:	unixODBC-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
An ODBC driver for Firebird, for use with unixODBC.

%package manual
Summary:	Manual for %{name}
Group:		System/Libraries

%description manual
Documentation for %{name}

%prep
%setup -q -n ODBC_V2-0-BETA
%patch0 

%build
cd ./OdbcJdbc/Builds/Gcc.lin
make -f makefile.linux
cd ../..

%install
rm -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}

install -m0755 ./OdbcJdbc/Builds/Gcc.lin/Release/libOdbcFb32.so %{buildroot}%{_libdir}/libOdbcFb32.so 
install -m0644 ./OdbcJdbc/Builds/Gcc.lin/readme.linux %{buildroot}%{_docdir}/%{name}
install -m0644 ./OdbcJdbc/Install/IDPLicense.txt %{buildroot}%{_docdir}/%{name}
install -m0644 ./OdbcJdbc/Install/Linux/*.ini %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_libdir}/libOdbcFb32.so

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}/*


