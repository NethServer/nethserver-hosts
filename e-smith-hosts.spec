Summary: e-smith module for managing hosts entries
Name: e-smith-hosts
%define version 1.13.3
%define release 01
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-base
Requires: e-smith-lib >= 1.15.1-19
Requires: e-smith-test >= 0.1.14
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
AutoReqProv: no

%description
e-smith module to allow the configuration of the hosts database, which is
used to build the DNS and DHCP configuration.

%changelog
* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.3-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.2-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-15]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-14]
- Only display the DNS Forwarder message if there are no domains
  set with Nameservers==localhost [SF: 1303422]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-13]
- Allow dnscache{Forwarder} to be configured, but empty [SF: 1303422]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-12]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Mon Aug 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-11]
- Avoid double reformatting of old host records, which breaks HostType == self
  records. [SF: 1275450]

* Mon Aug 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-10]
- Remove some remnant ServiceLink code
- Replace conf-migrate-hosts with some migrate fragments for the host db
- Restart dnscache during host-{create,delete,modify} events, so that
  cached information on hostnames is purged. [SF: 1243418,1243423]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-09]
- Hostnames panel updates from Shad Lords.

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-08]
- Complete the update to current db access APIs - a few esmith::db and
  esmith::config calls were found hiding. Rewrite conf-hostsdb as simple
  shell script. [SF: 1216546]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-07]
- Greatly simplify delete-hosts, and rename to purge-domain. Purge user@domain
  pseudonyms for deleted domains. [SF: 1193570 (Gordon)]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-06]
- Update to current db access APIs, in readiness for move of dbs to private
  directory. [SF: 1216546 (Shad)]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-05]
- Fix to ensure panel returns status if delete fails [SF: 1200284 (Shad)]

* Thu Jul  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-04]
- Include Shad's panel changes (publishglobal and formmagick patches)
  from e-smith-hosts-1.13.0-02sme04. [SF: 1234280]
- Avoid multiple re-openings of config db in panel code.

* Thu Jul  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-03]
- Move all host db manipulation actions to before template
  expansions (in all events, not just bootstrap-console-save).
  [SF: 1234255]

* Thu Apr 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-02]
- Use services2adjust symlink to reconfigure tinydns (tinydns-conf
  is obsolete).
- Move all host db manipulation actions to before template
  expansions in bootstrap-console-save.

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-01]
- Roll new dev stream - 1.13.1

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-06]
- Use generic_template_expand action in place of restart-dhcpd.
  Update e-smith-lib dependency. [MN00064130]

* Mon Mar  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-05]
- Fix RE used in untainting of hostname. [charlieb MN00050161]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-04]
- Only check if host exists on create not modify. [MN00065708]
- Remove stray ServiceLink action symlink. [MN00064757]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-03]
- Untaint hostname before using in system(). [charlieb MN00050161]

* Tue May 25 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-02]
- Fixing typo that prevented H&A panel from being disabled if a DNS forwarder
  was in use. [msoulier MN00034840]

* Tue May 25 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-01]
- rolling to dev stream - 1.13.0

* Thu Feb 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-04]
- Added a check in more_options() to reject the hostname if it's a dup.
  [msoulier dpar-20864]

* Thu Feb 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-03]
- Added further validation of the local IP address, to prevent the user using
  the external or internal interface IP, the gateway IP, or the loopback
  interface. [msoulier 8887]
- Added further validation of a host being added as local, to prevent users
  adding "local" hosts with are not local. [msoulier dpar-20865]

* Tue Aug 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-02]
- Fixed persistence problem with publish_globally field. [msoulier 9427]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Changing version to stable stream number - 1.12.0

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-01]
- Added order to migrate fragments [gordonr 9015]

* Fri Jun  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-32]
- Move force to lowercase to the correct place so we don't just bark
  if upper case hostnames are entered - we squash them to lower case
  before confirming [gordonr 8939]
- Correct the migrate fragment [gordonr 8939]

* Fri Jun  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-31]
- Force hostnames to lowercase on h&a panel [gordonr 8939]
- Sanitise hostsdb for old non-lowercase names (WIP) [gordonr 8939]

* Fri May 30 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-30]
- Updated delete-hosts to use esmith::HostsDB, and removed redundant bind db
  handling. [msoulier 8809]
- Updated delete-hosts to scan the entire hostsdb, cross-referencing with the
  domainsdb, and remove any host for a domain that we do not manage.
  [msoulier 8809]
- Added links to delete-hosts from bootstrap-console-save and
  registration-clear. [msoulier 8809]

* Tue May 20 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-29]
- Fixed indentation in lexicon files, and changed "Create/modify" to "Create
  or modify" in all lexicon files. [msoulier 8543]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-28]
- Add Spanish lexicon for hostentries [lijied 3793]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-27]
- Removed duplicate </trans> tag [gordonr 8613]

* Thu Apr 24 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-26]
- Deleted FIRSTPAGE_DESC text [lijied 8493]

* Tue Apr 22 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-25]
- Removed inline in text [lijied 7949]

* Mon Apr 21 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-24]
- Standardize Add/Save button name [lijied 7921]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-23]
- Added fr entry for previous change [gordonr 3722]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-22]
- Don't display H&A panel if DNS forwarder configured [gordonr 3722]
  
* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-21]
- Panel cleanup now all domains are in domains db [gordonr 8097]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-20]
- Standardized the button name [lijied 7921]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-19]
- Change $q->table to $q->start_table where necessary [lijied 8034]

* Fri Apr  4 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-18]
- Add tinydns-conf links in place of previous named-conf ones.
  [charlieb 8071]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-17]
- Removed 'Mitel Networks SME Server' branding [lijied 8016]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-16]
- Removed named links [gordonr 7659]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-15]
- Removed conf-dhcpd symlinks - now done in run script [gordonr 7771]

* Mon Mar 31 2003 Mike Dickson <miked@e-smith.com>
- [1.11.0-14]
- fixed the "Action" column to be several comns instead of one [miked 7761]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-13]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-12]
- Modified hostentries panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-11]
- Split en-us lexicon from hostentries panel [lijied 4030]

* Fri Feb 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-10]
- Added French lexicon for hostsentries. [lijied 5003]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Remove use of LocalDomainPrefix. [msoulier 4812]

* Fri Feb 21 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Remove deprecated WebServerName setting from canned test data. [charlieb 6861]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [1.11.0-07]
- added Action to the lexicon [miked 6363]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-06]
- minor UI updates [miked 5494]

* Mon Dec 16 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-05]
- Fix problem with globally visible (published) external IPs [charlieb 5816]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-04]
- ui update [miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-03]
- ui update  [miked 5494

* Fri Nov 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Removing explicit dependency on e-smith-named. [charlieb 4058]

* Fri Nov 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Rolling development stream to 1.11.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Roll to maintained version number to 1.10.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-11]
- Back out the check for duplicate hosts added at 1.9.0-04 - it prevents
  any modification of existing hostnames. [charlieb 3813]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-10]
- Check return value of open on NetworkServicesDB [gordonr 4760]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-09]
- Make use of NetworkServicesDB.pm in conf-migrate-hosts [gordonr 4773]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- Remove auto-creation of LocalDomainPrefix on upgrades. An existing
  value will be retained, but the implicit creation of e-smith.
  or mitel-networks. for the local prefix no longer happens. [gordonr 4811]

* Thu Sep  5 2002 Mark Knox <markk@e-smith.com>
- [1.9.0-07]
- Added 3 missing lexicon entries [markk 3812]

* Wed Sep  4 2002 Mark Knox <markk@e-smith.com>
- [1.9.0-06]
- Fixed some problems with dhcp range validator [markk 4513]

* Mon Aug 26 2002 Mark Knox <markk@e-smith.com>
- [1.9.0-05]
- Improved logic for when to clear global IP [markk 3816]

* Mon Aug 26 2002 Mark Knox <markk@e-smith.com>
- [1.9.0-04]
- Check for duplicate host names [markk 3813]

* Fri Aug 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Fix validator function from previous change [charlieb 4513]

* Fri Aug 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Include validator to ensure that host IP is not in DHCP range [charlieb 4513]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to development stream number to 1.9.0

* Mon Jun  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.8.6-01]
- Default for HostType is 'Self' [gordonr 3811]

* Mon Jun  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.8.5-01]
- Relaxed regexp to match text: [a-z0-9][a-z0-9-]* [gordonr 3684]

* Mon Jun  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.8.4-01]
- Validate that the (root of the) hostname matches [a-z][a-z0-9-]*
  Remove unused open of the ConfigDB [gordonr 3684]

* Mon Jun  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.8.3-01]
- Delete MACAddress when type is Remote
  Delete RemoteIP when type is Local [gordonr 3684]

* Mon Jun  3 2002 Mark Knox <markk@e-smith.com>
- [1.8.2-01]
- Resolved more confusion with addresses not displaying, naming conventions,
  delete non-essential fields in modification, and stop allowing change of 
  domain during modification. [markk 3684]

* Sat Jun  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.8.1-01]
- Resolved a lot of confusion about HostType, Visbility, local and 
  remote hosts and global publishing. These were all mixed up.
  TODO: Need to ensure that InternalIP and ExternalIP are deleted when
  changing host types from Remote->Local->Self [gordonr 3684]

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to maintained stream number to 1.8.0

* Fri May 31 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.20-01]
- removed SL-specific service domain stuff, now just calls a routine
  elsewhere [skud 3731]

* Fri May 31 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.19-01]
- Now checking for SL service domain in panel [skud 3684]

* Fri May 31 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.18-01]
- Made hosttyle (Local/Remote/Self) have first letter uppercase. 
  [skud 3684]

* Thu May 30 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.17-01]
- Default all hostentries props to empty string to avoid "odd number of
  elements in hash" warning and mixed up hosts config file. [skud 3684]

* Wed May 29 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.16-01]
- Added hostname l10n for previous hostname/name fix [skud 3684]

* Wed May 29 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.15-01]
- Fixed hostname/name CGI parameter mixup in hostentries.pm [skud 3684]
- Fixed ethernet address validation (should be allowed to be blank)
  
* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.14-01]
- RPM rebuild forced by cvsroot2rpm

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [1.7.13-01]
- Added missing </entry> tag [markk 3430]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [1.7.12-01]
- Removed extra lexicon data after the </form> tag. [markk 3430]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.11-01]
- Added english localisation for NO_HOSTS_FOR_THIS_DOMAIN [skud #3429]

* Wed May 15 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.10-01]
- Fixed broken links to hostentries.skud [skud #3430]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.9-01]
- Catch up with changes in action names in e-smith-named [gordonr 2733]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.8-01]
- Removed whitespace from nav bar entries. For some reason it resulted
  in another Configuration group. Probably funkiness in the navigation
  routine, but that's for ron. [gordonr 3155]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.7-01]
- removed dependency on esmith::NetworkServicesDB/ServiceLink-lib
  [skud 3353]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.6-01]
- And fixed tests to pick up en-us [gordonr 3155]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.5-01]
- Lexicon en->en-us [gordonr 3155]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.4-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.3-01]
- I18N'd version of hostentries [skud 3027]
- Nav bar entries for same [gordonr 3155]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.2-01]
- InternalIP & ExternalIPs now translated correctly from 4.1.2 style
  hosts databases by conf-migrate-hosts (2495)
- Added 'wpad' alias for Windows proxy autodetection - thanks Damien Curtain 
  [gordonr 3073]

* Wed Feb 27 2002 Jason Miller <jmiller@e-smith.com>
- [1.7.1-01]
- Rolling to new version 1.7.1-01, includes all patches up to 1.7.0-01,
  as part of testing that rpm2cvs was successfull 

* Wed Feb 27 2002 Jason Miller <jay@e-smith.com>
- [1.7.0-01]
- rollRPM: Rolled version number to 1.7.0-01. Includes patches up to 1.6.0-02.

* Fri Jan  4 2002 Adrian Chung <adrianc@e-smith.com>
- [1.6.0-02]
- Adding 'proxy' to the list of hostnames added to hosts database.
- Use passed in visibility argument for systemName.FQDN rather than always
  using 'Global'.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-01.

* Fri Nov 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-01]
- rollRPM: Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-05.
- s/march-networks/mitel-networks/ in conf-migrate-hosts

* Wed Nov 07 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-05]
- rebranding to Mitel Networks

* Wed Aug 22 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-04]
- Well, one more branding change

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Final branding cleanup

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-58.

* Tue Jul 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-58]
- Update to hostentries panel to change url 

* Tue Jul 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-57]
- Update conf-migrate-hosts to change default LocalDomainPrefix value from
  e-smith. to march-networks. 

* Sun Jul 29 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-56]
- Branding text changes to the hostentries web panel 

* Wed Jul 18 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-55]
- Updates to error message displays

* Wed Jul 18 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-54]
- Split actions

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.3.0-53]
- Changed license to GPL

* Tue Jun 12 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-52]
- Update to conf-migrate-hosts script to ignore hosts already in the new
  format

* Thu Jun 07 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-51]
- Fixed bug in create-default-hosts action

* Thu Jun 07 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-50]
- Update to hostentries panel to include a message about static
  host entries and why they are non-modifiable

* Thu Jun 07 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-49]
- Update to create-default-hosts to create a new host for SystemName
  with property static=yes
- Update to hostentries panel to not allow modifications for hosts
  that have the property static=yes

* Fri Jun 01 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-48]
- Updates to several of the panels to reflect better documentation habits

* Thu May 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-47]
- Re-did showInitial() text to be more in line with the text in -46 changes

* Thu May 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-46]
- Similar updates for createSelf(), createLocal(), createRemote(), modifyHost()
  as were done in 1.3.0-45.

* Thu May 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-45]
- Updates to the showInitial() subroutine in the hostentries panel to have
  better formatted warnings

* Wed May 30 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-44]
- Updates to createSelfHost, createLocalHost, createRemoteHost, modifyHost
  subroutines inside the hostentries panel to show marketing information

* Wed May 30 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-43]
- Updates to the showInitial panel to display marketing information 

* Wed May 16 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-42]
- Fixed subroutine genDomainMenu() in hostentries panel

* Thu May 10 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-41]
- Changed order of actions

* Wed May 09 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-40]
- Error handling fixes to 'hostentries' panel, and 'conf-migrate-hosts'

* Wed May 09 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-39]
- Forgot to change conf-service-name to look for correct event 

* Wed May 09 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-38]
- Moved the conf-service-name action 

* Wed May 09 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-37]
- Changes various templates and web panels to check for publishDomain
	- hostentries web panel
	- conf-migrate-hosts action
	- conf-service-name action

* Tue May 01 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-36]
- Added an optional parameter to create-default-hosts to allow one to make
  all the default hosts Globally published [i.e. service domain name]

* Wed Apr 25 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-35]
- Reorganization of createlinks
- Added action delete-hosts which is symlinked into domain-delete
  to automatically delete the host values for a particular domain

* Wed Apr 25 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-34]
- Re-added symlink for console-save -> conf-hostsdb as it would
  be required in the event that a domain is changed in the console
  configuration

* Wed Apr 25 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-33]
- Typo fix in genDomainMenu()

* Wed Apr 25 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-32]
- Changed showInitial() subroutine in hostentries panel to use the
  LocalDomainPrefix if one is set instead of DomainName
- Changed the ordering of genDomainMenu() subroutine in hostentries so that
  the list of domains in the system appears as:
	- Primary domain (with LocalDomainPrefix if applicable)
	- Service domain
	- Sorted i-bays

* Tue Apr 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-31]
- Added actions for service domain

* Tue Apr 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-30]
- Removed conf-hostsdb from console-save and host-delete events as it is not
  necessary
- Added new action create-default-hosts (linked to domain-create event) which
  takes the passed $domainName value and generates default hosts for that domain
- Changed conf-hostsdb to call create-default-hosts action passing it the
  primary domain

* Tue Apr 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-29]
- Cleaned up the Cgi code that displays the table of hosts (hostentries panel)
  so that it would properly display in lynx

* Mon Apr 16 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-28]
- Fixed up /etc/dhcpd.conf/60StaticEntries so that it also checks that
  MACAddress and LocalIP are defined AND not equal to ''

* Thu Apr 12 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-27]
- More panel text corrections
- Removed the autogeneration of hostname e-smith-manager.$DomainName as it
  won't work as expected anyways (needs an apache configuration to pass it
  on to the port 980)

* Thu Apr 12 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-26]
- More panel updates for textual content as well as some more cleanup of
  deprecated modules

* Thu Apr 12 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-25]
- Panel updates for textual content for deleteHostEntry() and modifyHostEntry()

* Wed Apr 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-24]
- Panel updates for textual content for showInitial(), createSelfHost(),
  createLocalHost(), createRemoteHost()
- Cleanup of several deprecated modules

* Wed Apr 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-23]
- changes to the layout of the manager text for the various panels
  of createSelfHost(), createLocalHost(), createRemoteHost() and modifyHost()
- changes to the display of some of the panels

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-22]
- Removed link to removed panel

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-21]
- Made a generic modifyHostEntry() function that is meant for all three host
  types and includes a drop-down to choose that type.
- Added 'FIXME' comments to locations that need to be removed

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-20]
- Removed conf-hostsdb and conf-migrate-hosts out of post-install/post-upgrade
  as this is a duplicated action set (bootstrap-console-save) which shouldn't
  need to occur

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-19]
- Changed conf-hostsdb and conf-migrate-hosts to not generate serviceDomain
  entries if configuration value for ServiceDomain = '' (default on install)

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-18]
- Added in the host-create and host-modify events to each of the performCreate()
  and performModify() sections so that named is updated with the new information

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-17]
- Merged the working prototype webpanel into the normal hostentries panel
  (still keeping the old create/modify/delete scripts for reference)
- Made stipulation to show hostname/addresses for the serviceDomainName
  if defined and not equal to '' (default on an installation)

* Thu Apr 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-16]
- Changed conf-migrate-hosts to be operation 06 in post-install/post-upgrade
  as it caused a failed dependency for 05init-accounts which MUST come first

* Wed Apr 04 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-15]
- Added $ServiceDomainName to the list of domains for both
  conf-hostsdb and conf-migrate-hosts scripts

* Wed Apr 04 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-14]
- added a new conf-migrate-hosts script to be included in
  post-install/post-upgrade (05) to migrate existing hosts to the new format
  as well as to check for special hosts being defined for all domains
  [note: this doesn't include service domain just yet]
- changed the meaning of conf-hostsdb for the default domains that it generates
- changed the panel to start using /home/e-smith/hosts instead of
  /home/e-smith/service_hosts (test centre)

* Mon Apr 02 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-13]
- added the functionality for modifiying all three host types

* Mon Apr 02 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-12]
- created user interface for modifySelfHostEntry(), modifyLocalHostEntry(),
  and modifyRemoteHostEntry()

* Mon Apr 02 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-11]
- prepared modify{$HostType}HostEntry and performModify{$HostType}Modify
  for actual content

* Tue Mar 27 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-10]
- Implemented the performCreateRemoteHostEntry() functionality

* Tue Mar 27 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-09]
- Updated performCreateSelfHostEntry() to do a check for a valid domain
  name first, and rearranged order of variable declarations
- Completed the logic for performCreateLocalHostEntry()

* Tue Mar 27 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-08]
- implemented deleteHostEntry() to work with the new schema

* Fri Mar 23 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-07]
- Created the interfaces for create self/local/remote
- Implemented performCreateSelfHostEntry() and prepared
  the logic for performCreateLocalHostEntry() and
  performCreateRemoteHostEntry() to occur
- Changed REGEX for HostName to not allow periods at all
- Added genDomain() subroutine to generate a list of domains
  to create host for.

* Fri Mar 23 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-06]
- Further prepared the links for create/modify/remove to include the
  relevant host information and the appropriate subroutines to handle
  them [minus the handling portions]

* Thu Mar 22 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-05]
- Prepared the links for create/modify/remove host entries

* Thu Mar 22 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-04]
- Added ability to store each service_host db value into a two-tiered hash
  which is then used to provide the host name values into the table structure
  previously layed out in the panel.
- Added code to show a 'No hosts for this domain' message if no hosts exist

* Thu Mar 22 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-03]
- Updated the new panel (service_hosts) to read from /home/e-smith/service_hosts
  and changed to reflect the new layout of host entries per domain on the system
  by providing menus only

* Wed Mar 21 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-02]
- Created a new panel 

* Wed Mar 21 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-01]
- Rolled to version 1.3.0-01. Includes all patches up to 1.2.0-04

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Tony Clayton <tonyc@e-smith.com>
- [1.2.0-03]
- changed conf-hostdb action order from 01 to 07 for all events

* Thu Jan 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Add code to set default string for LocalDomainPrefix.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-15.

* Tue Jan 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-15]
- Trim trailing periods from hostnames

* Mon Jan 15 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-14]
- Changed descriptive text for hosts and addresses panel to emphasize
  don't do anything unless you know what you're doing

* Mon Jan 15 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-13]
- Changed descriptive text for hosts and addresses panel

* Mon Jan 15 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-12]
- Changes to the navigation of the e-smith manager

* Wed Jan 10 2001 Paul Nesbit <pkn@e-smith.com>
- [1.1.0-11]
- If $MACAddress isn't defined, set it to " " for display.  This fixes
  "Use of uninitialised..." warnings in admin_error_log.

* Tue Jan 09 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-10]
- Create new bootstrap-console-save event

* Tue Jan 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-9]
- Redid panel

* Thu Dec 21 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-8]
- Removed unnecessary reconfig and restart of DHCPD from remoteaccess_update
  event.

* Thu Dec 21 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-7]
- Fixed case where a null host was added during post-install

* Tue Dec 19 2000 Jason Miller <jmiller@e-smith.com>
- [1.1.0-6]
- updated createlinks to include conf-hostsdb in the post-install and
  post-upgrade events

* Sun Dec 17 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-5]
- Removed console-save from %post - not required, and bad during installs

* Fri Dec 15 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-4]
- Actions may well be named dhcpd, but they shouldn't be here - they're
  duplicated in e-smith-base :-)

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-3]
- Actions are named dhcpd, not dhcp

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-2]
- Link actions into remoteaccess-update

* Tue Nov 28 2000 Adrian Chung <adrianc@e-smith.com>
- Branched to 1.1.0 for 4.1/7.0 release.
- Modified conf-dhcpd to look in /var/lib instead of /var/state

* Fri Nov 03 2000 Gordon Rowell <gordonr@e-smith.com>
- Clean up of web interface code

* Wed Nov 01 2000 Gordon Rowell <gordonr@e-smith.com>
- Put minor version numbers into patch file
- Changed test on web interface
- Modified conf-hostsdb to work for any event (including host-delete)

* Wed Nov 01 2000 Brett Jensen <brett@e-smith.com>
- Updates to the web interface

* Mon Oct 30 2000 Gordon Rowell <gordonr@e-smith.com>
- More functional web interface

* Sun Oct 29 2000 Gordon Rowell <gordonr@e-smith.com>
- Partially functional web interface

* Sun Oct 29 2000 Gordon Rowell <gordonr@e-smith.com>
- Added conf-hostsdb to prime hosts database with default entries

* Sat Oct 28 2000 Gordon Rowell <gordonr@e-smith.com>
- Renamed from e-smith-named-conf to e-smith-hosts
- Rewritten to use hosts database
- /var/named template changes moved to e-smith-named

* Fri Sep 1 2000 Damien Curtain <damien@pagefault.org>
- set -x added aswell as "accounts" replaced with "host name"
- on the web interface.

* Thu Aug 31 2000 Damien Curtain <damien@pagefault.org>
- Added some checking to ensure entered data is semi-valid

* Wed Aug 30 2000 Damien Curtain <damien@pagefault.org>
- Change of name. MAC Address no longer required.

* Sun Aug 20 2000 Damien Curtain <damien@pagefault.org>
- Initial Release

%prep
%setup
mkdir -p root/etc/e-smith/web/panels/manager/cgi-bin

%build
perl createlinks

%post

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
