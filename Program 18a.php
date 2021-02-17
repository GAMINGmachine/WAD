<?php
date_default_timezone_set('IST');
$cookie_name = "lastvisit";
$cookie_value = date("F j, Y, g:i a");
$cookie_expires=60*60*24*60+time(); 
if(!isset($_COOKIE[$cookie_name])) {
    if(setcookie($cookie_name, $cookie_value,$cookie_expires , "/")){
        echo "Cookie named '" . $cookie_name . "' is now set! refresh to see changes";
    } 
} else {
  echo "Cookie '" . $cookie_name . "' is set!<br>";
  echo "Value is: " . $_COOKIE[$cookie_name];
}
?>
