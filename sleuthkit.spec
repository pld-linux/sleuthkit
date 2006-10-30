#
# TODO	- autopsy compliance
#	- pl desc
#
Summary:	The Sleuth Kit is an forensic toolkit for analyzing file systems and disks
Summary(pl):	The Sleuth Kit jest zestawem narzêdzi wspomagaj±cych analizê systemów plików
Name:		sleuthkit
Version:	2.06
Release:	0.1
#Epoch:		-
License:	IBM Public License/Common Public License
Group:		Applications
Source0:	http://heanet.dl.sourceforge.net/sourceforge/sleuthkit/%{name}-%{version}.tar.gz
# Source0-md5:	13e0d252df9e7a1d17da0db1b224c114
URL:		http://www.sleuthkit.org/sleuthkit
BuildRequires:	openssl-devel
BuildRequires:	perl-base
Requires:	coreutils
Requires:	perl-Date-Manip
Requires:	openssl
Requires:	libmagic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sleuth Kit is an open source forensic toolkit for analyzing
Microsoft and UNIX file systems and disks.  The Sleuth Kit enables
investigators to identify and recover evidence from images acquired
during incident response or from live systems.  The Sleuth Kit is
open source, which allows investigators to verify the actions of
the tool or customize it to specific needs.

It is recommended that these command line tools can be used with
the Autopsy Forensic Browser.  Autopsy, (http://www.sleuthkit.org/autopsy),
is a graphical interface to the tools of The Sleuth Kit and automates
many of the procedures and provides features such as image searching
and MD5 image integrity checks.

As with any investigation tool, any results found with The Sleuth
Kit should be be recreated with a second tool to verify the data.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,4}

install bin/* $RPM_BUILD_ROOT%{_bindir}

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3
install man/man4/* $RPM_BUILD_ROOT%{_mandir}/man4

# we use the file tool from coreutils package

rm $RPM_BUILD_ROOT%{_bindir}/file
rm $RPM_BUILD_ROOT%{_mandir}/man1/file.1

# for Date-Manip stuff look for the perl-Date-Manip package
# for libmagic stuff look for libmagic-{,devel} package

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc README.txt docs/* tct.docs/* licenses/* 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man4/*
