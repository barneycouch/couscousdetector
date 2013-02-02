use strict;
 
use WWW::Mechanize;
use HTTP::Cookies;
use warnings;
use IPC::System::Simple qw(system capture);

#!/usr/bin/perl -w


my $file = "users.txt";
open (FH, "< $file") or die "Can't open $file for read: $!";
my @lines;
while (<FH>) {
    push (@lines, $_);
}
close FH or die "Cannot close $file: $!";

print @lines;    # see if it worked

foreach my $val (@lines) {
    `logIn.pl nb455 v8Fz8A6QTA IEGNAQrJ $val`;
  }

# `logIn.pl nb455 v8Fz8A6QTA IEGNAQrJ @lines[0]`;
# `logIn.pl nb455 v8Fz8A6QTA IEGNAQrJ @lines[1]`;

