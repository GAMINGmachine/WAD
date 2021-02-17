#!/usr/bin/perl
use CGI;
$cgi=new CGI;
print $cgi->header;
print $cgi->start_html('Prog9sss');
print $cgi->h1('OS Command Executor');
print $cgi->hr;
print $cgi->h3('Please enter the OS command');
print $cgi->start_form( -method=>'post',
-action=>'/cgi-enabled/9b.cgi');
print "OS Command:";
print $cgi->textfield( -name=>'command',-value=>
'');
print $cgi->submit( -name=>'submit',-value=>
'Execute');
print $cgi->reset;
print $cgi->end_form;
print $cgi->hr;
$command=$cgi->param("command");
if($command ne "")
{
print " The output of the OS command:
$command";
$output=`$command`;
print "<pre>";
print $output;
print "</pre>";
}
print $cgi->hr;
print $cgi->end_html;
