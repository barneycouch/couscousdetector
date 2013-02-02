use strict;
 
use WWW::Mechanize;
use HTTP::Cookies;
use warnings;
use IPC::System::Simple qw(system capture);


my $mech = WWW::Mechanize->new();
# look like a real person
$mech->agent('User-Agent=Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5');
# we need cookies
my $myCookies = $mech->cookie_jar(HTTP::Cookies->new);

# we start at login
$mech->get('https://raven.cam.ac.uk/auth/login.html');
$mech->success or die "login GET fail";
my $user = "$ARGV[0]";
my $passR = "$ARGV[1]";
my $passH = "$ARGV[2]"; 
my $recipients ="$ARGV[3]";
$mech -> form_name("credentials") or die "form name error";
$mech -> field("pwd" , $passR);# or die "password error";
$mech -> field("userid", $user);# or die "user id error";

$mech -> click () or die "click error" ;
 


$mech->get('http://www.mealbookings.cai.cam.ac.uk/') or die "Booking homepage GET fail";

print "Good morning sir, shall we have a check for couscous?\n\n";
#sleep(2);


system("couscous_mk2.py");


my $couscousValue = `couscous_mk2.py`;

$mech->get('https://webmail.hermes.cam.ac.uk/login/nb455') or die "Hermes GET failed";
$mech -> form_number(2) or die "form name error";
$mech -> field("password" , $passH);# or die "password error";
$mech -> field("userid", $user);# or die "user id error";
$mech -> click ("login") or die "click error" ;

my $sessionUri = $mech -> uri;
my @values = split('/', $sessionUri);

#foreach my $val (@values) {
#    print "$val\n";
#  }
my @values2 = split(':',$values[4]);
#foreach my $val2 (@values2) {
#    print "$val2\n";
#  }

my $sessionCode = $values2[1];

#print $mech -> uri;

$mech->get('https://webmail.hermes.cam.ac.uk/session/'.$user.':'.$sessionCode.'//AAAc@compose?postponed_fresh=Compose+a+fresh+message') or die "Hermes GET failed";

print "\n\nLet me send the morning mail for you sir, don't you worry about such trifles.";

print $mech -> uri;

$mech -> form_number(1) or die "form name error";



#
 #foreach ($recipients) {
 #	if (($recipients[scalar @recipients]) = $_) {
 #	$recipientList = ($recipientList.$_."\@cam.ac.uk");}
 #	else {
 #		$recipientList = ($recipientList.$_."\@cam.ac.uk ,");
 #	}
# } 
# my $recipientList = join(',', $recipients[0..$#recipients]);

# my $recipientList = join(' ,',@recipients);
# print "\n".$recipientList;
# $mech -> field("hdr_To",$recipientList);

$mech -> field("hdr_To",$recipients);
print $recipients;

$mech -> field("hdr_Subject","Good morning, sir");
$mech -> field("body","You'll be pleased to know I have had our minions check the fine dining menus for us - here is what they have reported\n\n           -\n".$couscousValue."
	                       -Jeeves");
$mech -> click ("sub_send") or die "click error" ;
