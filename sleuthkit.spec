#
# TODO:
#	- devel, libs and static subpackages
#	- add afflib bcond (and prepare afflib package :)
#
Summary:	The Sleuth Kit - an forensic toolkit for analyzing file systems and disks
Summary(pl.UTF-8):	The Sleuth Kit - zestaw narzędzi wspomagających analizę systemów plików
Name:		sleuthkit
Version:	3.2.3
Release:	1
License:	IBM Public License/Common Public License
Group:		Applications
Source0:	http://downloads.sourceforge.net/sleuthkit/%{name}-%{version}.tar.gz
# Source0-md5:	29465ebe32cfeb5f0cab83e4e93823c5
URL:		http://www.sleuthkit.org/sleuthkit/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	libewf-devel
BuildRequires:	libstdc++-devel
#BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
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

%prep
%setup -q
sed -i -e 's/-static//' {samples,tests,tools/*tools}/Makefile.in

%build
%configure \
	--without-afflib

sed -i -e 's/^\(LIBS = -lewf\)/\1 -ldl -lpthread/' {tools/autotools,tsk3}/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
     DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.txt README.txt licenses/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tsk3
%{_includedir}/tsk3
%{_libdir}/libtsk3.*
%{_mandir}/man1/*
