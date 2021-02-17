#!/usr/bin/perl
use CGI;
$cgi=new CGI;
print $cgi->header;
print $cgi->start_html('Program 8b');
print $cgi->h1('<center>Server Page Visited Informations</center>');
print $cgi->hr;
$count_file="c:/count.txt";
if(open(FILE,"<".$count_file)) {
$no_accesses=<FILE>;
close(FILE);
if(open (FILE,">".$count_file)) {
$no_accesses++;
print FILE $no_accesses;
close(FILE);
}
else {
print "Cannot write the file. No Visitors information in the 
server";
} } else {
print "cannot read the counter database for visitors";
}
print "Welcome User";
print "<BR><BR>This page has been accessed <font color=red size=10> 
$no_accesses </font> times from the creation";
print $cgi->end_html;
