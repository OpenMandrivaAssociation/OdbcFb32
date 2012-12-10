Summary:	ODBC driver for Firebird
Name:		OdbcFb32
Version:	2.0.0142
Release:	7
License:	IDPL
URL:		http://www.firebirdsql.org/
Group:		System/Libraries
Source:		OdbcFb32-beta-%{version}-src.tar.bz2
Patch:		OdbcFb32-libname.diff
ExclusiveArch:	i586
BuildRequires:	firebird-devel
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	gcc-c++
BuildRequires:	unixODBC-devel

%description
An ODBC driver for Firebird, for use with unixODBC.

%package manual
Summary:	Manual for %{name}
Group:		System/Libraries

%description manual
Documentation for %{name}

%prep
%setup -q -n ODBC_V2-0-BETA
%patch0 -p0

%build
cd ./OdbcJdbc/Builds/Gcc.lin
make -f makefile.linux
cd ../..

%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}

install -m0755 ./OdbcJdbc/Builds/Gcc.lin/Release/libOdbcFb32.so %{buildroot}%{_libdir}/libOdbcFb32.so 
install -m0644 ./OdbcJdbc/Builds/Gcc.lin/readme.linux %{buildroot}%{_docdir}/%{name}
install -m0644 ./OdbcJdbc/Install/IDPLicense.txt %{buildroot}%{_docdir}/%{name}
install -m0644 ./OdbcJdbc/Install/Linux/*.ini %{buildroot}%{_docdir}/%{name}

%files
%defattr(0644,root,root,0755)
%{_libdir}/libOdbcFb32.so

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}/*




%changelog
* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0142-6mdv2009.0
+ Revision: 254388
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0.0142-4mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 22 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0142-4mdv2007.0
+ Revision: 86088
- Really forces i586 arch.
- Bumped release.
- This package won't build on x86_64 for now. FB Community is working on this.
- Bump release.
- Avoid arch confusion in BuildRequires.
- Updated BuildRequires.
- General cleanup.
- Do not include the whole libdir, otherwise it will include debug libs.
- Import OdbcFb32

