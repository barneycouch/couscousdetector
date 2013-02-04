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
my $emailJ = "$ARGV[1]";
my $passJ = "$ARGV[2]";
my $passR = "$ARGV[3]"; 
my $recipient ="$ARGV[4]";

$mech -> form_name("credentials") or die "form name error";
$mech -> field("pwd" , $passR);# or die "password error";
$mech -> field("userid", $user);# or die "user id error";

$mech -> click () or die "click error" ;
 


$mech->get('http://www.mealbookings.cai.cam.ac.uk/') or die "Booking homepage GET fail";

print "Good morning sir, shall we have a check for couscous?\n\n";
#sleep(2);


print(`food_search.py "couscous"`);


my $couscousValue = `food_search.py "couscous"`;

`send_email.py $emailJ $passJ $recipient`


