<html>
<head>
<?php include "/var/www/html/CSS2/header.html" ?>
<?php include "/var/www/html/CSS2/SSNRANGE/java.html" ?>
</head>
<style>
<?php include "/var/www/html/CSS2/style.html" ?>
</style>

<body>
<?php include "/var/www/html/CSS2/menu.html" ?>
<?php include "/var/www/html/CSS2/SSNRANGE/script.html" ?>

<center><h3 style="color:rgb(60, 128, 214);"><b>SUNSPOTS</b></h3>
<?php
$line2 = $_GET["birthday"];
$line = $_GET["birthday2"];
echo "Time range selected:  ";
echo $line2;
echo "  -  ";
echo $line;
?>
</center>
<?php
$myfile2 = fopen("SSN/E.txt", "w") or die("Unable to open file!");
$line2 = $_GET["birthday"];
$line = $_GET["birthday2"];
$data = $line2 . PHP_EOL . $line;
//fwrite($myfile2, "Time range selected:  ");
fwrite($myfile2, $line2);
//echo $line2;
//echo "\n\n\n";
//echo $line;
fwrite($myfile2, "\r\n");
fwrite($myfile2, $line);
fclose($myfile2);
exec("sh SSN/run.sh");
?>

<br><br>
<center>
<div id="drawing" style="width:650px; height:400px"></div>

<button><type="button"><a href="SSN/SSNRANGE/SSNRange.root">ROOT File</a></button>
</center>



<?php include "/var/www/html/CSS2/footer.html" ?>
</body>
</html>