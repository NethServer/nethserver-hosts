#!/usr/bin/perl -w 

#----------------------------------------------------------------------
# copyright (C) 1999-2005 Mitel Networks Corporation
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
#----------------------------------------------------------------------

package    esmith::FormMagick::Panel::hostentries;

use strict;

use esmith::FormMagick;
use esmith::ConfigDB;
use esmith::DomainsDB;
use esmith::HostsDB;
use esmith::NetworksDB;
use esmith::cgi;
use esmith::util;
use File::Basename;
use Exporter;
use Carp;
use Net::IPv4Addr;

our @ISA = qw(esmith::FormMagick Exporter);

our @EXPORT = qw(
    print_hosts_tables
    print_hostname_field
    print_domain_field
    domains_list
    more_options
    goto_confirm
    print_confirmation_details
    create_or_modify
    lexicon_params
    remove
    mac_address_or_blank
    not_in_dhcp_range
    print_save_or_add_button
    not_taken
    must_be_local
);

our $VERSION = sprintf '%d.%03d', q$Revision: 1.54 $ =~ /: (\d+).(\d+)/;

our $db = esmith::ConfigDB->open();

=pod 

=head1 NAME

esmith::FormMagick::Panels::hostentries - useful panel functions 

=head1 SYNOPSIS

use esmith::FormMagick::Panels::hostentries;

my $panel = esmith::FormMagick::Panel::hostentries->new();
$panel->display();

=head1 DESCRIPTION

=head2 new();

Exactly as for esmith::FormMagick

=begin testing

$ENV{ESMITH_ACCOUNT_DB} = "10e-smith-base/accounts.conf";
$ENV{ESMITH_CONFIG_DB} = "10e-smith-base/configuration.conf";

use_ok('esmith::FormMagick::Panel::hostentries');
use vars qw($panel);
ok($panel = esmith::FormMagick::Panel::hostentries->new(), 
"Create panel object");
isa_ok($panel, 'esmith::FormMagick::Panel::hostentries');

=end testing

=cut

sub new 
{
    shift;
    my $self = esmith::FormMagick->new();
    $self->{calling_package} = (caller)[0];
    bless $self;
    # Uncomment the next line for debugging.
    #$self->debug(1);
    return $self;
}

=head1 HTML GENERATION ROUTINES

Routines for generating chunks of HTML needed by the panel.

=for testing
use_ok('esmith::DomainsDB');
my $d = esmith::DomainsDB->create();
isa_ok($d, 'esmith::DomainsDB');
can_ok($d, 'domains');
#can_ok($d, 'get_by_prop');

=cut

sub print_hosts_tables
{ 
    my $self = shift;                                                                                      
    my $q = $self->{cgi};                                                                                  
    unless ($db)
    {
        $self->error('UNABLE_TO_OPEN_CONFIGDB', 'First');
        $self->print_status_message();
        return undef;
    }

    unless (scalar @{$self->domains_list()})
    {
        $self->success('DNS_FORWARDER_ENABLED', 'First');
        $self->print_status_message();
        return undef;
    }

    print $q->start_Tr,"<td>",$q->start_table ({-CLASS => "sme-noborders"}),"\n";
    print $q->start_Tr,"<td>",$self->localise('ADD_HOSTNAME'),"</td>",$q->end_Tr,"\n";

    my $hosts_db = esmith::HostsDB->open();

    foreach my $d (@{$self->domains_list()})
    {
        print $q->start_Tr,"<td>","\n";
        print $q->h3($self->localise('CURRENT_HOSTNAMES_FOR_DOMAIN', {domain => $d})),"\n";
        print "</td>",$q->end_Tr,"\n";

        if (my @hosts = $hosts_db->get_hosts_by_domain($d))
        {
            print $q->start_Tr,"<td>\n",$q->start_table ({-CLASS => "sme-border"}),"\n";
            print $q->Tr (esmith::cgi::genSmallCell($q, $self->localise('HOSTNAME'),"header"),
            esmith::cgi::genSmallCell($q, $self->localise('LOCATION'),"header"),
            esmith::cgi::genSmallCell($q, $self->localise('IP_ADDRESS'),"header"),
            esmith::cgi::genSmallCell($q, $self->localise('ETHERNET_ADDRESS'),"header"),
            esmith::cgi::genSmallCell($q, $self->localise('COMMENT'),"header"),
            esmith::cgi::genSmallCell($q, $self->localise('ACTION'),"header",2));
            $self->print_host_row($_) foreach @hosts;
            print $q->end_table, "\n";
            print "</td>",$q->end_Tr,"\n";
        }
        else
        {
            print $q->start_Tr,"<td>\n";
            print $self->localise('NO_HOSTS_FOR_THIS_DOMAIN');
            print "</td>",$q->end_Tr,"\n";
        }
    }
    print $q->end_table,"\n";
    return undef;
}

=head2 $panel->print_table_headers()

Prints the table header row for the hosts tables.

=for testing
can_ok($panel, 'print_table_headers');
can_ok($panel, 'localise');
$panel->print_table_headers;
like($_STDOUT_, qr(HOSTNAME), "Printed table headers");

=cut

sub print_table_headers 
{

}

sub print_host_row 
{
    my ($self,$host_record) = @_;
    my $q = $self->{cgi};                                                                                  
    my $ht = $host_record->prop('HostType');
    my $ip =
	($ht eq 'Self') ? $db->get_value('LocalIP') :
	    ($ht eq 'Remote') ? $host_record->prop('ExternalIP') :
		$host_record->prop('InternalIP');

    print $q->start_Tr;

    $self->print_td($host_record->key());
    $self->print_td($self->localise($host_record->prop('HostType')) || "&nbsp;");
    $self->print_td($ip);
    $self->print_td($host_record->prop('MACAddress') || "&nbsp;");
    $self->print_td($host_record->prop('Comment') || "&nbsp;");
    my $static = $host_record->prop('static') || "no";
    if ($static ne 'yes') {
        my $propstring = $self->build_host_cgi_params($host_record->key(), $host_record->props());
        $self->print_td(qq(<a href="hostentries?wherenext=CreateModify&$propstring">) 
        . $self->localise('MODIFY')
        . qq(</a>\n));
        $self->print_td(qq(<a href="hostentries?wherenext=Remove&$propstring">) 
        . $self->localise('REMOVE')
        . qq(</a>\n));
    } else {
        $self->print_td("&nbsp;");
        $self->print_td("&nbsp;");
    }
    print "</tr>\n";
}

=for testing
$panel->print_td("foo");
like($_STDOUT_, qr(<td>foo</td>), "print_td");

=cut

sub print_td
{
    my ($self, $value) = @_;
    print "<td class=\"sme-border\">$value</td>\n";
}

sub build_host_cgi_params {
    my ($self, $hostname, %oldprops) = @_;

    my ($host, $domain) = $self->split_hostname($hostname);

    my %props = (
        page    => 0,
        page_stack => "",
        ".id"         => $self->{cgi}->param('.id') || "",
        name             => $host,
        domain           => $domain,
        local_ip         => $oldprops{InternalIP},
        global_ip        => $oldprops{ExternalIP},
        ethernet_address => $oldprops{MACAddress},
        hosttype         => $oldprops{HostType},
        comment          => $oldprops{Comment},
    );

    return $self->props_to_query_string(\%props);
}

=for testing
my @expect = qw(foo bar.com);
is_deeply(\@expect, [$panel->split_hostname("foo.bar.com")], "Split hostname");

=cut

sub split_hostname {
    my ($self, $hostname) = @_;
    return ($hostname =~ /^([^\.]+)\.(.+)$/);
}

sub print_hostname_field {
    my $fm = shift;

    print qq(<tr><td colspan=2>) . $fm->localise('HOSTNAME_DESCRIPTION') . qq(</td></tr>);
    print qq(<tr><td class="sme-noborders-label">) . $fm->localise('HOSTNAME') . qq(</td>\n);

    my $h = $fm->{cgi}->param('name');

    if ($h) {
        print qq(
            <td>$h 
            <input type="hidden" name="name" value="$h">
            <input type="hidden" name="action" value="modify">
            </td>
        );
    } else {
        print qq(
            <td><input type="text" name="name">
            <input type="hidden" name="action" value="create">
            </td>
        );
    }

    print qq(</tr>\n);
    return undef;

}

sub print_domain_field
{
    my $fm = shift;
    print qq(        <tr>) ."\n". qq(          <td class="sme-noborders-label">) . $fm->localise('DOMAIN') . qq(</td>\n);

    my $h = $fm->{cgi}->param('name');
    my $dom = $fm->{cgi}->param('domain');
    if ($h) {
        print qq(
            <td>$dom 
            <input type="hidden" name="domain" value="$dom">
            </td>
        );
    } else {
        print qq(
            <td>
            <select type="select" name="domain">\n);
        foreach my $d (@{$fm->domains_list()})
        {
            print "              <option>$d\n";
        }
        print qq(
            </select>
            </td>\n);
    }

    print qq(        </tr>\n);
    return undef;
}

=head2 mac_address_or_blank

Validation routine for optional ethernet address

=for testing
can_ok('main', 'mac_address_or_blank');
is(mac_address_or_blank(undef, ""), "OK", "blank mac address is OK");
is(mac_address_or_blank(undef, "aa:bb:cc:dd:ee:ff"), "OK", "OK mac address is OK");
isnt(mac_address_or_blank(undef, "blah"), "OK", "wrong mac address is not OK");

=cut

sub mac_address_or_blank {
    my ($fm, $data) = @_;
    return "OK" unless $data;
    return CGI::FormMagick::Validator::mac_address($fm, $data);
}

=for testing
can_ok('main', 'domains_list');

=cut

sub domains_list
{
    my $self = shift;

    my $d = esmith::DomainsDB->open_ro() or die "Couldn't open DomainsDB";

    my @domains;

    for ($d->domains)
    {
	my $ns = $_->prop("Nameservers") || 'localhost';
	push @domains, $_->key if ($ns eq 'localhost');
    }

    return \@domains;
}

=for testing
can_ok('main', 'more_options');

=cut


sub more_options 
{
    my $self = shift;
    my $q = $self->{cgi};
    my $hostsdb = esmith::HostsDB->open_ro;

    my $hostname = lc $q->param('name');
    my $domain = lc $q->param('domain');
    my $fqdn = "$hostname.$domain";
    $self->cgi->param(-name=>'name', -value=>$hostname);

    unless ( $hostname =~ /^[a-z0-9][a-z0-9-]*$/ )
    {
        return $self->error('HOSTNAME_DESCRIPTION');
    }
    # Look for duplicate hosts.
    my $hostrec = undef;
    if ($self->cgi->param('action') eq 'create' and $hostrec = $hostsdb->get($fqdn))
    {
        return $self->error(
            $self->localise('HOSTNAME_EXISTS_ERROR',
                            {fullHostName => $fqdn,
                             type => $hostrec->prop('HostType')}));
    }

    my $hosttype = $self->cgi->param('hosttype');
    if ($hosttype eq 'Self') {
        $self->wherenext('Confirm');
    } elsif ($hosttype eq 'Local') {
        $self->wherenext('Local');
    } elsif ($hosttype eq 'Remote') {
        $self->wherenext('Remote');
    } else {
        $self->wherenext('Confirm');
    }
}

=for testing
can_ok('main', 'goto_confirm');

=cut

sub goto_confirm
{
    my $self = shift;
    $self->wherenext('Confirm');
}

=for testing
can_ok('main', 'print_confirmation_details');

=cut

sub print_confirmation_details {
    my ($self) = @_;
    my $q = $self->{cgi};                                                                                  
    print $q->start_table ({-CLASS => "sme-border"}),"\n"; 

    my $type = $self->{cgi}->param('hosttype') || '';
    if ($type eq "Self")
    {
        $self->{cgi}->delete('local_ip');
        $self->{cgi}->delete('global_ip');
        $self->{cgi}->delete('ethernet_address');
    }

    if ($type eq "Remote")
    {
        $self->{cgi}->delete('local_ip');
        $self->{cgi}->delete('ethernet_address');
    }

    if ($type eq "Local")
    {
        $self->{cgi}->delete('global_ip');
    }

    my %label_map = (
	    global_ip => "IP_ADDRESS",
	    local_ip => "IP_ADDRESS",
	);
    foreach my $f (qw( name domain hosttype local_ip global_ip
    ethernet_address comment) ) {
        my $val = $self->cgi->param($f) || '';
        $self->debug_msg("looping on param $f, val is $val");
	next unless $val;
	my $label = $label_map{$f} || uc($f);
        print $q->Tr (esmith::cgi::genSmallCell($q, $self->localise($label),"normal"),
        esmith::cgi::genSmallCell($q, $val,"normal"));
    }

    print qq(</table>);

    return "";
}

=head2 create_or_modify()

This is the subroutine that does the actual work when you create/modify
a host.

=begin testing

#$ENV{ESMITH_HOSTS_DB} = scratch_copy("50-hosts/hosts.conf");
$ENV{ESMITH_HOSTS_DB} = "50-hosts/hosts.conf";

ok($panel = esmith::FormMagick::Panel::hostentries->new(), 
"Create panel object");
isa_ok($panel, 'esmith::FormMagick::Panel::hostentries');

$panel->{cgi} = CGI->new({
    name        => 'wibble',
    domain          => 'invalid.tld',
    hosttype        => 'Self',
    action          => 'create',
});

$panel->create_or_modify();
isnt($panel->cgi->param('status_message'), undef, "Set status message");

my $h = esmith::HostsDB->open();
ok($h->get('wibble.invalid.tld'), "Host added to db");

=end testing

=cut

sub create_or_modify {
    my ($self) = @_;
    $self->wherenext('First');
    my $h = esmith::HostsDB->open() || esmith::HostsDB->create();
    my $hostname = $self->cgi->param('name') . "." .
			$self->cgi->param('domain');

    # Untaint and lowercase $hostname
    $hostname =~ /([\w\.-]+)/; $hostname = lc($1);

    my %props = (
        type        => 'host',
        HostType    => $self->cgi->param('hosttype') || "",
        ExternalIP  => $self->cgi->param('global_ip') || "",
        InternalIP  => $self->cgi->param('local_ip') || "",
        MACAddress  => $self->cgi->param('ethernet_address') || "",
        Comment     => $self->cgi->param('comment') || "",
    );

    if ($self->cgi->param('action') eq 'create') {
        if ($h->new_record($hostname, \%props)) {
            if (system("/sbin/e-smith/signal-event", "host-create", $hostname) == 0) {
                return $self->success('SUCCESSFULLY_CREATED');
            }
        }
        return $self->error('ERROR_WHILE_CREATING_HOST');
    } else {
        my $record = $h->get($hostname);
        if ($record->merge_props(%props)) {
            if (system("/sbin/e-smith/signal-event", "host-modify", $hostname) == 0) {
                return $self->success('SUCCESSFULLY_MODIFIED');
            }
        }
        $self->error('ERROR_WHILE_MODIFYING_HOST');
    }
}

=head2 print_save_or_add_button()

=cut

sub print_save_or_add_button {
    my ($self) = @_;

    if ($self->cgi->param('action') eq 'modify') {
        $self->print_button("SAVE");
    } else {
        $self->print_button("ADD");
    }
}

=head2 remove()

=for testing
can_ok('main', 'remove');

=cut

sub remove {
    my ($self) = @_;
    $self->wherenext('First');
    my $h = esmith::HostsDB->open();
    my $hostname = $self->cgi->param('name') . "." .
    $self->cgi->param('domain');

    # Untaint $hostname before use in system()
    $hostname =~ /([\w\.-]+)/; $hostname = $1;

    my $record = $h->get($hostname);
    if ($record->delete()) {
        if (system("/sbin/e-smith/signal-event", "host-delete", $hostname) == 0) {
            return $self->success('SUCCESSFULLY_DELETED');
        }
    }
    return $self->error('ERROR_WHILE_DELETING_HOST');
}

=head2 lexicon_params()

Provides lexicon parameters for interpolation.

=for testing
can_ok('main', 'lexicon_params');
my $panel = esmith::FormMagick::Panel::hostentries->new();
my %expect = (
    hostname        => 'wibble',
    domain          => 'invalid.tld'
);
$panel->{cgi} = CGI->new({
    name        => 'wibble',
    domain          => 'invalid.tld'
});
is_deeply({lexicon_params($panel)}, \%expect, "Get lexicon params");

=cut

sub lexicon_params {
    my ($self) = @_;
    return (
        hostname    => $self->cgi->param('name') || "",
        domain      => $self->cgi->param('domain') || "",
    );
}

sub not_in_dhcp_range
{
    my $self = shift;
    my $address = shift;
    my $status = $db->get('dhcpd')->prop('status') || "disabled";
    return "OK" unless $status eq "enabled";
    my $start = $db->get('dhcpd')->prop('start');
    my $end = $db->get('dhcpd')->prop('end');
    return (esmith::util::IPquadToAddr($start)
        <= esmith::util::IPquadToAddr($address)
        &&
        esmith::util::IPquadToAddr($address)
        <= esmith::util::IPquadToAddr($end)) ?
        "ADDR_IN_DHCP_RANGE" :
        "OK";
}

=head2 not_taken

This function checks the local ip address being set in the panel, and 
ensures that it is not already taken as the gateway ip or the local ip
of the server.

=cut

sub not_taken
{
    my $self = shift;
    my $q = $self->{cgi};
    my $localip = $q->param('local_ip');
    
    my $server_localip = $db->get_value('LocalIP') || '';
    my $server_gateway = $db->get_value('GatewayIP') || '';
    my $server_extip = $db->get_value('ExternalIP') || '';

    $self->debug_msg("\$localip is $localip");
    $self->debug_msg("\$server_localip is $server_localip");
    $self->debug_msg("\$server_gateway is $server_gateway");
    $self->debug_msg("\$server_extip is $server_extip");

    if ($localip eq $server_localip)
    {
        return 'ERR_IP_IS_LOCAL_OR_GATEWAY';
    }
    elsif ($localip eq $server_gateway)
    {
        return 'ERR_IP_IS_LOCAL_OR_GATEWAY';
    }
    elsif (($db->get_value('SystemMode') ne 'serveronly') &&
           ($server_extip eq $localip))
    {
        return 'ERR_IP_IS_LOCAL_OR_GATEWAY';
    }
    elsif ($localip eq '127.0.0.1')
    {
        return 'ERR_IP_IS_LOCAL_OR_GATEWAY';
    }
    else
    {
        return 'OK';
    }
}

sub must_be_local
{
    my $self = shift;
    my $q = $self->{cgi};
    my $localip = $q->param('local_ip');

    # Make sure that the IP is indeed local.
    my $ndb = esmith::NetworksDB->open_ro;
    my @local_list = $ndb->local_access_spec;

    foreach my $spec (@local_list)
    {
        next if $spec eq '127.0.0.1';
        if (Net::IPv4Addr::ipv4_in_network($spec, $localip))
        {
            return 'OK';
        }
    }
    # Not OK. The IP is not on any of our local networks.
    return 'ERR_IP_NOT_LOCAL';
}

1;
