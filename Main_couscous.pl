use strict;
 
use WWW::Mechanize;
use HTTP::Cookies;
use warnings;
use IPC::System::Simple qw(system capture);

#!/usr/bin/perl -w

my $user = "$ARGV[0]";
my $passR = "$ARGV[1]";
my $passH = "$ARGV[2]"; 


my $file = "users.txt";
open (FH, "< $file") or die "Can't open $file for read: $!";
my @lines;
while (<FH>) {
    push (@lines, $_);
}
close FH or die "Cannot close $file: $!";

print @lines;    # see if it worked

foreach my $val (@lines) {
    `logIn.pl $user $passR $passH $val`;
  }


