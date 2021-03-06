Summary:	gptfdisk-1.0.4
Name:		gptfdisk
Version:	1.0.5
Release:	1%{?dist}
License:	GPLv2+
URL:		http://sourceforge.net/projects/gptfdisk/
Group:		System Environment/Filesystem and Disk management
Vendor:		VMware, Inc.
Distribution: Photon
Source0:	http://downloads.sourceforge.net/project/gptfdisk/%{name}/%{version}/%{name}-%{version}.tar.gz
%define sha1 gptfdisk=b642aa628cbc9fa63e9a73dad5acc588042527ac
Patch0:	    gptfdisk-1.0.4-convenience-1.patch
Patch1:     gptfdisk-fix-compilation-1.0.5.patch
Requires: 	popt >= 1.16
BuildRequires:	popt-devel
BuildRequires:	ncurses-devel
Requires:	ncurses
Requires:	libstdc++
%description
The gptfdisk package is a set of programs for creation and maintenance of GUID Partition
Table (GPT) disk drives. A GPT partitioned disk is required for drives greater than 2 TB
and is a modern replacement for legacy PC-BIOS partitioned disk drives that use a
Master Boot Record (MBR). The main program, gdisk, has an inteface similar to the
classic fdisk program.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags} POPT=1

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install POPT=1
%{_fixperms} %{buildroot}/*

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
/sbin/*
%{_mandir}/man8/*

%changelog
*   Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 1.0.5-1
-   Automatic Version Bump
*   Tue Sep 11 2018 Anish Swaminathan <anishs@vmware.com> 1.0.4-1
-   Update version to 1.0.4
*   Mon Jun 05 2017 Bo Gan <ganb@vmware.com> 1.0.1-4
-   Fix dependency
*   Wed Oct 05 2016 ChangLee <changlee@vmware.com> 1.0.1-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.1-2
-   GA - Bump release of all rpms
*   Fri Feb 26 2016 Kumar Kaushik <kaushikk@vmware.com> 1.0.1-1
-   Updated Version.
*   Thu Oct 30 2014 Divya Thaluru <dthaluru@vmware.com> 0.8.10-1
-   Initial build.	First version
