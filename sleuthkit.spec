#
# TODO	- autopsy compliance
#	- noarch or optflags?
#	- pl desc
#
Summary:	The Sleuth Kit - an forensic toolkit for analyzing file systems and disks
Summary(pl):	The Sleuth Kit - zestaw narz�dzi wspomagaj�cych analiz� system�w plik�w
Name:		sleuthkit
Version:	2.06
Release:	0.1
License:	IBM Public License/Common Public License
Group:		Applications
Source0:	http://dl.sourceforge.net/sleuthkit/%{name}-%{version}.tar.gz
# Source0-md5:	13e0d252df9e7a1d17da0db1b224c114
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

%description -l pl
The Sleuth Kit to maj�cy otwarte �r�d�a zestaw narz�dzi do analizy
system�w plik�w i dysk�w z systemami Microsoftu i uniksowymi. The
Sleuth Kit umo�liwia badaj�cym zidentyfikowa� i odtworzy� dowody
uzyskane podczas reakcji na incydent lub z �ywych system�w. The
Sleuth Kit ma otwarte �r�d�a, co pozwala badaj�cym zweryfikowa�
dzia�ania narz�dzia lub przystosowa� je do okre�lonych potrzeb.

Zalecane jest u�ywanie tych narz�dzi dzia�aj�cych z linii polece� wraz
z przegl�dark� Autopsy (<http://www.sleuthkit.org/autopsy/>), b�d�c�
graficznym interfejsem do narz�dzi z The Sleuth Kit i automatyzuj�c�
wiele procedur oraz udost�pniaj�c� mo�liwo�ci takie jak przeszukiwanie
obraz�w i sprawdzanie integralno�ci obraz�w za pomoc� sum MD5.

Podobnie jak przy dowolnym narz�dziu badawczym wszelkie wyniki
uzyskane przy u�yciu tego zestawu powinny by� odtworzone przy u�yciu
drugiego narz�dzia dla zweryfikowania wiarygodno�ci.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,4}

install bin/* $RPM_BUILD_ROOT%{_bindir}

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3
install man/man4/* $RPM_BUILD_ROOT%{_mandir}/man4

# we use the system file tool

rm $RPM_BUILD_ROOT%{_bindir}/file
rm $RPM_BUILD_ROOT%{_mandir}/man1/file.1

# for Date-Manip stuff look for the perl-Date-Manip package
# for libmagic stuff look for libmagic-{,devel} package

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/* tct.docs/* licenses/* 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man4/*
