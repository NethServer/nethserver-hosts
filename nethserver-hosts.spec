Name: nethserver-hosts
Summary: NethServer module for managing hosts entries
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name} 
BuildArch: noarch
Requires: nethserver-base
BuildRequires: nethserver-devtools

%description
NethServer module to allow the configuration of the hosts database, which is
used to build the DNS and DHCP configuration.

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root%{perl_vendorlib}
mv -v esmith root%{perl_vendorlib}

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Mon Nov 30 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Invalid traffic shaping rules after deleting host object - Bug #3173 [NethServer]

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.2-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Wed Jan 21 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1.ns6
- DHCP LeaseStatus prop persisted to DB - Bug #2985 [NethServer]

* Wed Oct 15 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1.ns6
- Support DHCP on multiple interfaces - Feature #2849

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.8-1.ns6
- Firewall rules: preserve references to other DB records - Enhancement #2835 [NethServer]

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.7-1.ns6
- Help: remove NethServer name occurrences. Refs #2656

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.6-1.ns6
- Show text labels in DNS & DHCP - Enhancement #2642 [NethServer]
- RST format for help files - Enhancement #2627 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Thu Oct 17 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.5-1.ns6
- Add domain to loca host records #2209

* Wed Jun 12 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1.ns6
- Remove /etc/ethers template #1917

* Wed May 29 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- /etc/hosts template (30hosts_remote): added short hostname aliases #1746
- Bugfix #1983

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870
- Various fixes #1834 #1845

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Add migration code #1668 #1670

