#
# TODO:
#	- add libvhdi bcond and support
#	- add libvmdk bcond and support
#
# Conditional build:
%bcond_without	aff		# Without Advanced Forensic Format (aff) support
%bcond_with	java		# Build Java bindings and jar file
#
Summary:	The Sleuth Kit - an forensic toolkit for analyzing file systems and disks
Summary(pl.UTF-8):	The Sleuth Kit - zestaw narzędzi wspomagających analizę systemów plików
Name:		sleuthkit
Version:	4.10.1
Release:	1
License:	IBM Public License/Common Public License
Group:		Applications
Source0:	https://github.com/sleuthkit/sleuthkit/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c37bb35897a471c52ec18e0cbb807e9e
Patch0:		libewf.patch
URL:		http://www.sleuthkit.org/sleuthkit/
%{?with_aff:BuildRequires:	afflib-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cppunit-devel >= 1.12.1
BuildRequires:	libewf-devel
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtool
#BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	zlib-devel
Requires:	coreutils
Requires:	file
Requires:	perl-Date-Manip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sleuth Kit is an open source forensic toolkit for analyzing
Microsoft and UNIX file systems and disks. The Sleuth Kit enables
investigators to identify and recover evidence from images acquired
during incident response or from live systems. The Sleuth Kit is open
source, which allows investigators to verify the actions of the tool
or customize it to specific needs.

It is recommended that these command line tools can be used with the
Autopsy Forensic Browser. Autopsy,
(<http://www.sleuthkit.org/autopsy/>), is a graphical interface to the
tools of The Sleuth Kit and automates many of the procedures and
provides features such as image searching and MD5 image integrity
checks.

As with any investigation tool, any results found with The Sleuth Kit
should be be recreated with a second tool to verify the data.

%description -l pl.UTF-8
The Sleuth Kit to mający otwarte źródła zestaw narzędzi do analizy
systemów plików i dysków z systemami Microsoftu i uniksowymi. The
Sleuth Kit umożliwia badającym zidentyfikować i odtworzyć dowody
uzyskane podczas reakcji na incydent lub z żywych systemów. The Sleuth
Kit ma otwarte źródła, co pozwala badającym zweryfikować działania
narzędzia lub przystosować je do określonych potrzeb.

Zalecane jest używanie tych narzędzi działających z linii poleceń wraz
z przeglądarką Autopsy (<http://www.sleuthkit.org/autopsy/>), będącą
graficznym interfejsem do narzędzi z The Sleuth Kit i automatyzującą
wiele procedur oraz udostępniającą możliwości takie jak przeszukiwanie
obrazów i sprawdzanie integralności obrazów za pomocą sum MD5.

Podobnie jak przy dowolnym narzędziu badawczym wszelkie wyniki
uzyskane przy użyciu tego zestawu powinny być odtworzone przy użyciu
drugiego narzędzia dla zweryfikowania wiarygodności.

%package libs
Summary:	Sleuthkit shared library
Summary(pl.UTF-8):	Biblioteka współdzielona Sleuthkita
Group:		Libraries

%description libs
Sleuthkit shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona Sleuthkita.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%package java
Summary:	Java bindings for sleuthkit
Summary(pl.UTF-8):	Dowiązania Javy do sleuthkit
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
Java bindings for sleuthkit.

%description java -l pl.UTF-8
Dowiązania Javy do sleuthkit.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's/-static//' {samples,tests,tools/*tools}/Makefile.in

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_aff:--without-afflib} \
	%{!?with_java:--disable-java}

%{__sed} -i -e 's/^\(LIBS = -lewf\)/\1 -ldl -lpthread/' {tools/autotools,tsk}/Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
     DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc API-CHANGES.txt ChangeLog.txt NEWS.txt README.md licenses/*
%attr(755,root,root) %{_bindir}/blkcalc
%attr(755,root,root) %{_bindir}/blkcat
%attr(755,root,root) %{_bindir}/blkls
%attr(755,root,root) %{_bindir}/blkstat
%attr(755,root,root) %{_bindir}/fcat
%attr(755,root,root) %{_bindir}/ffind
%attr(755,root,root) %{_bindir}/fiwalk
%attr(755,root,root) %{_bindir}/fls
%attr(755,root,root) %{_bindir}/fsstat
%attr(755,root,root) %{_bindir}/hfind
%attr(755,root,root) %{_bindir}/icat
%attr(755,root,root) %{_bindir}/ifind
%attr(755,root,root) %{_bindir}/ils
%attr(755,root,root) %{_bindir}/img_cat
%attr(755,root,root) %{_bindir}/img_stat
%attr(755,root,root) %{_bindir}/istat
%attr(755,root,root) %{_bindir}/jcat
%attr(755,root,root) %{_bindir}/jls
%attr(755,root,root) %{_bindir}/jpeg_extract
%attr(755,root,root) %{_bindir}/mactime
%attr(755,root,root) %{_bindir}/mmcat
%attr(755,root,root) %{_bindir}/mmls
%attr(755,root,root) %{_bindir}/mmstat
%attr(755,root,root) %{_bindir}/pstat
%attr(755,root,root) %{_bindir}/sigfind
%attr(755,root,root) %{_bindir}/sorter
%attr(755,root,root) %{_bindir}/srch_strings
%attr(755,root,root) %{_bindir}/tsk_comparedir
%attr(755,root,root) %{_bindir}/tsk_gettimes
%attr(755,root,root) %{_bindir}/tsk_loaddb
%attr(755,root,root) %{_bindir}/tsk_recover
%attr(755,root,root) %{_bindir}/usnjls
%{_datadir}/tsk
%{_mandir}/man1/blkcalc.1*
%{_mandir}/man1/blkcat.1*
%{_mandir}/man1/blkls.1*
%{_mandir}/man1/blkstat.1*
%{_mandir}/man1/fcat.1*
%{_mandir}/man1/ffind.1*
%{_mandir}/man1/fls.1*
%{_mandir}/man1/fsstat.1*
%{_mandir}/man1/hfind.1*
%{_mandir}/man1/icat.1*
%{_mandir}/man1/ifind.1*
%{_mandir}/man1/ils.1*
%{_mandir}/man1/img_cat.1*
%{_mandir}/man1/img_stat.1*
%{_mandir}/man1/istat.1*
%{_mandir}/man1/jcat.1*
%{_mandir}/man1/jls.1*
%{_mandir}/man1/mactime.1*
%{_mandir}/man1/mmcat.1*
%{_mandir}/man1/mmls.1*
%{_mandir}/man1/mmstat.1*
%{_mandir}/man1/sigfind.1*
%{_mandir}/man1/sorter.1*
%{_mandir}/man1/tsk_comparedir.1*
%{_mandir}/man1/tsk_gettimes.1*
%{_mandir}/man1/tsk_loaddb.1*
%{_mandir}/man1/tsk_recover.1*
%{_mandir}/man1/usnjls.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtsk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtsk.so.19
%if %{with java}
%attr(755,root,root) %{_libdir}/libtsk_jni.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtsk_jni.so.0
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtsk.so
%{_libdir}/libtsk.la
%if %{with java}
%attr(755,root,root) %{_libdir}/libtsk_jni.so
%{_libdir}/libtsk_jni.la
%endif
%{_includedir}/tsk

%files static
%defattr(644,root,root,755)
%{_libdir}/libtsk.a
%{?with_java:%{_libdir}/libtsk_jni.a}

%if %{with java}
%files java
%defattr(644,root,root,755)
%{_javadir}/%{name}-%{version}.jar
%endif
