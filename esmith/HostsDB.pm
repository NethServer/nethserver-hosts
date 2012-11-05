#----------------------------------------------------------------------
# Copyright 1999-2003 Mitel Networks Corporation
# This program is free software; you can redistribute it and/or
# modify it under the same terms as Perl itself.
#----------------------------------------------------------------------

package esmith::HostsDB;

use strict;
use warnings;

use esmith::DB::db;
our @ISA = qw( esmith::DB::db );

=head1 NAME

esmith::HostsDB - interface to esmith hostnames/addresses database

=head1 SYNOPSIS

    use esmith::HostsDB;
    my $hosts = esmith::HostsDB->open;

    # everything else works just like esmith::DB::db

    # these methods are added
    my @hosts     = $hosts->hosts;
    my @new_hosts = $hosts->propogate_hosts;

=head1 DESCRIPTION

This module provides an abstracted interface to the esmith hosts
database.

Unless otherwise noted, esmith::HostsDB acts like esmith::DB::db.

=cut

=head2 Overridden methods

=over 4

=item I<open>

Like esmith::DB->open, but if given no $file it will try to open the
file in the ESMITH_HOSTS_DB environment variable or hosts.

=begin testing

use_ok("esmith::HostsDB");

$H = esmith::HostsDB->open('10e-smith-lib/hosts.conf');
isa_ok($H, 'esmith::HostsDB');
is( $H->get("otherhost.mydomain.xxx")->prop('InternalIP'), "192.168.1.3", 
                                    "We can get stuff from the db");

=end testing

=cut

sub open {
    my($class, $file) = @_;
    $file = $file || $ENV{ESMITH_HOSTS_DB} || "hosts";
    return $class->SUPER::open($file);
}

=head2 open_ro()

Like esmith::DB->open_ro, but if given no $file it will try to open the
file in the ESMITH_HOSTS_DB environment variable or hosts.

=begin testing

=end testing

=cut

sub open_ro {
    my($class, $file) = @_;
    $file = $file || $ENV{ESMITH_HOSTS_DB} || "hosts";
    return $class->SUPER::open_ro($file);
}
=back

=head2 Additional Methods

These methods are added be esmith::HostsDB

=over 4

=item I<hosts>

    my @hosts = $hosts->hosts;

Returns a list of all host records in the database.

=begin testing

$db = esmith::HostsDB->open('10e-smith-lib/hosts.conf');
isa_ok($db, 'esmith::HostsDB');
can_ok($db, 'hosts');
my @hosts = $db->hosts();
isnt( @hosts, 0 );
is_deeply(\@hosts, [$db->get_all_by_prop('type' => 'host')]);

=end testing

=cut

sub hosts {
    my ($self) = @_;
    return $self->get_all_by_prop('type' => 'host');
}

=item I<propogate_hosts>

    my @new_hosts = $hosts->propogate_hosts($old_name, $new_name);

When the name of your e-smith machine changes, this will change the
name of any hosts which also started with $old_name to use the
$new_name.

Returns a list of the newly tranlsated host records.

=begin testing

use esmith::ConfigDB;

my $hosts_file = '10e-smith-lib/propogate_hosts.conf';
END { unlink $hosts_file }

my $db     = esmith::HostsDB->create($hosts_file);

use esmith::TestUtils qw(scratch_copy);
my $c_scratch = scratch_copy('10e-smith-lib/configuration.conf');
my $config = esmith::ConfigDB->open($c_scratch);
isa_ok($config, 'esmith::ConfigDB');

my $name   = $config->get('SystemName')->value;

# setup some dummy hosts to propogate.
foreach my $host ( "$name.tofu-dog.com", "$name.wibble.org",
                     "wibble.$name.org", "yarrow.hack" )
{
    $db->new_record($host, { type => 'host',  HostType => 'Self',
                             ExternalIP => '', InternalIP => ''
                           });
}

$db->reload;
my @new_hosts = $db->propogate_hosts($name, "armondo");
my @hosts = $db->hosts;
is( @hosts, 4 );
is_deeply( [sort map { $_->key } @hosts], 
           [sort +('armondo.tofu-dog.com',
                   'armondo.wibble.org',
                   "wibble.$name.org",
                   'yarrow.hack',
                  )] 
);

is( @new_hosts, 2 );
is_deeply( [sort map { $_->key } @new_hosts],
           [sort qw(armondo.tofu-dog.com armondo.wibble.org)] 
         );

=end testing

=cut

sub propogate_hosts 
{
    my($self, $old_name, $new_name) = @_;

    my @new_hosts = ();
    foreach my $host ($self->hosts)
    {
        my $new_host = $host->key;
        if( $new_host =~ s/^\Q$old_name.\E/$new_name./ ) 
        {
            push @new_hosts, $self->new_record($new_host, 
                                               { $host->props }
                                              );
            $host->delete;
        }
    }

    return @new_hosts;
}


=head2 $db->get_hosts_by_domain

Given a domain name (as a string), finds any hosts which match it and
return them as a list of record objects.

=begin testing

my $h = esmith::HostsDB->open('10e-smith-lib/hosts.conf');
my @hosts = $h->get_hosts_by_domain('otherdomain.xxx');
is(scalar(@hosts), 2, "Found two hosts in otherdomain.xxx");
isa_ok($hosts[0], 'esmith::DB::Record');

=end testing

=cut

sub get_hosts_by_domain {
    my ($self, $domain) = @_;
    my @all = $self->get_all();
    my @return;
    foreach my $h (@all) {
        push @return, $h if $h->key() =~ /^[^\.]+\.$domain$/;
    }
    return @return;
}

=back

=head1 AUTHOR

SME Server Developers <bugs@e-smith.com>

=head1 SEE ALSO

L<esmith::ConfigDB>

=cut

1;
