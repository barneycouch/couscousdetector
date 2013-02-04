use strict;
 
use WWW::Mechanize;
use HTTP::Cookies;
use warnings;
use IPC::System::Simple qw(system capture);

#!/usr/bin/perl -w

my $user = "$ARGV[0]";
my $emailJ = "$ARGV[1]";
my $passJ = "$ARGV[2]";
my $passR = "$ARGV[3]"; 

 


my $file = "crs_ids.txt";
open (FH, "< $file") or die "Can't open $file for read: $!";
my @lines;
while (<FH>) {
    push (@lines, $_);
}
close FH or die "Cannot close $file: $!";

print @lines;    # see if it worked

foreach my $val (@lines) {
	my $recipient = $val."\@cam.ac.uk";
    `logIn.pl $user $emailJ $passJ $passR $recipient`;
  }


