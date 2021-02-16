<?php
session_start();
if(isset($_SESSION['count']))
$_SESSION['count']=$_SESSION['count']+1;
else
$_SESSION['count']=1;
echo "count=".$_SESSION['count'];
echo "The counter is now $_SESSION[count] reload this page to increment ";
?>