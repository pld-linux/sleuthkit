#
# TODO:
#	- optflags?
#	- add afflib ewf bconds (and prepare afflib and ewf packages :)
#
Summary:	The Sleuth Kit - an forensic toolkit for analyzing file systems and disks
Summary(pl.UTF-8):	The Sleuth Kit - zestaw narzędzi wspomagających analizę systemów plików
Name:		sleuthkit
Version:	3.0.1
Release:	1
License:	IBM Public License/Common Public License
Group:		Applications
Source0:	http://dl.sourceforge.net/sleuthkit/%{name}-%{version}.tar.gz
# Source0-md5:	55956dd3bbfa6c9e2ebcc685c2a9569d
URL:		http://www.sleuthkit.org/sleuthkit/
BuildRequires:	openssl-devel
BuildRequires:	perl-base
Requires:	coreutils
Requires:	file
# XXX: openssl library (should be autodetected) or openssl-tools or perl-OpenSSL-??? ?
Requires:	openssl
Requires:	perl-Date-Manip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sleuth Kit is an open source forensic toolkit for analyzing
Microsoft and UNIX file systems and disks. The Sleuth Kit enables
investigators to identify and recover evidence from images acquired
during incident response or from live systems. The Sleuth Kit is open
source, which allows investigators to verify the actions of the tool
or customize it to specific needs.

It is recommended that these command line tools can be used with
the Autopsy Forensic Browser. Autopsy,
(<http://www.sleuthkit.org/autopsy/>), is a graphical interface to the
tools of The Sleuth Kit and automates many of the procedures and
provides features such as image searching and MD5 image integrity
checks.

As with any investigation tool, any results found with The Sleuth
Kit should be be recreated with a second tool to verify the data.

%description -l pl.UTF-8
The Sleuth Kit to mający otwarte źródła zestaw narzędzi do analizy
systemów plików i dysków z systemami Microsoftu i uniksowymi. The
Sleuth Kit umożliwia badającym zidentyfikować i odtworzyć dowody
uzyskane podczas reakcji na incydent lub z żywych systemów. The
Sleuth Kit ma otwarte źródła, co pozwala badającym zweryfikować
działania narzędzia lub przystosować je do określonych potrzeb.

Zalecane jest używanie tych narzędzi działających z linii poleceń wraz
z przeglądarką Autopsy (<http://www.sleuthkit.org/autopsy/>), będącą
graficznym interfejsem do narzędzi z The Sleuth Kit i automatyzującą
wiele procedur oraz udostępniającą możliwości takie jak przeszukiwanie
obrazów i sprawdzanie integralności obrazów za pomocą sum MD5.

Podobnie jak przy dowolnym narzędziu badawczym wszelkie wyniki
uzyskane przy użyciu tego zestawu powinny być odtworzone przy użyciu
drugiego narzędzia dla zweryfikowania wiarygodności.

%prep
%setup -q

%build

%configure \
	--disable-afflib \
	--disable-ewf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
     DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt docs/* licenses/* 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/libtsk3.*

%dir %{_includedir}/tsk3
%dir %{_includedir}/tsk3/base
%dir %{_includedir}/tsk3/fs
%dir %{_includedir}/tsk3/hashdb
%dir %{_includedir}/tsk3/img
%dir %{_includedir}/tsk3/vs
%{_includedir}/tsk3/*.h
%{_includedir}/tsk3/base/*.h
%{_includedir}/tsk3/fs/*.h
%{_includedir}/tsk3/hashdb/*.h
%{_includedir}/tsk3/img/*.h
%{_includedir}/tsk3/vs/*.h

%dir %{_datadir}/tsk3
%dir %{_datadir}/tsk3/sorter
%{_datadir}/tsk3/sorter/default.sort
%{_datadir}/tsk3/sorter/freebsd.sort
%{_datadir}/tsk3/sorter/images.sort
%{_datadir}/tsk3/sorter/linux.sort
%{_datadir}/tsk3/sorter/openbsd.sort
%{_datadir}/tsk3/sorter/solaris.sort
%{_datadir}/tsk3/sorter/windows.sort
