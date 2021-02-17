<?php
session_start();
if (isset($_SESSION['count'])) {
	# code...
	$_SESSION["count"]++;
	echo "<h2>The counter value is:".$_SESSION['count']."<h2>";
}else{
	$_SESSION["count"]=0;
	echo "<h1>The counter value has been initialized. refresh to increment the counter";
}
?>
