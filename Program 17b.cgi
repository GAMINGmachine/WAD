#!"C:\xampp\perl\bin\perl.exe"
use CGI;
$cgi=new CGI;
print "Content-type: text/html\n\n";
print "<html>\n<body>\n";
print "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">\n";
print $cgi->h1('OS Command Executor');
print $cgi->hr;
print $cgi->h3('Please enter the Dos command');
print $cgi->start_form( -method=>'post', -action=>'/cgi-enabled/prog9b.cgi');
print "Os Command:";
print $cgi->textfield( -name=>'command',-value=>'');
print $cgi->submit( -name=>'submit',-value=>'Execute');
print $cgi->reset;
print $cgi->end_form;
print $cgi->hr;
$command=$cgi->param("command");
if($command ne "")
{
print " The output of the Os command: $command";
$output=`$command`;
print "<pre>";
print $output;
print "</pre>";
}
print $cgi->hr;
print "\n</div>\n";
print "</body>\n</html>\n";