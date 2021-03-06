Summary:     Application to detect if running in virtual machine
Name:        virt-what
Version:     1.20
Release:     1%{?dist}
URL:         https://people.redhat.com/~rjones/virt-what/files/
Source0:     https://people.redhat.com/~rjones/virt-what/files/%{name}-%{version}.tar.gz
License:     GPLv2
Group:       Applications/System
%define sha1 %{name}=0ca1802b454290c5b676609aa585f3f3d7597e47
Vendor:      VMware, Inc.
Distribution:  Photon
BuildRequires: gcc

%description
virt-what is a shell script which can be used to detect if the program is running in a virtual machine

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libexecdir}/virt-what-cpuid-helper
%{_sbindir}/virt-what
%{_mandir}/man1/virt-what.1.gz

%changelog
* Tue Aug 18 2020 Him Kalyan Bordoloi <bordoloih@vmware.com>  1.20-1
- Initial release.
