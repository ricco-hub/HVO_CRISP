<html>
<?php
$myfile = fopen("NeutronMonitor_Rate/Set.txt", "w") or die("Unable to open file!");
$name = $_GET['station'];
foreach ($name as $station){
 fwrite($myfile, $station);
 fwrite($myfile, "\n");
}

echo "Data selected: ";
$name = $_GET['station'];
foreach ($name as $station){
echo $station;
echo "\n\n";
}

$myfile3 = fopen("NeutronMonitor_Rate/E.txt", "w") or die("Unable to open file!");
$line3 = $_GET["birthday"];
$line4 = $_GET["birthday2"];
fwrite($myfile3, $line3);
fwrite($myfile3, "\r\n");
fwrite($myfile3, $line4);


$myfile4 = fopen("NeutronMonitor_Rate/Res.txt", "w") or die("Unable to open file!");
$res = $_GET['resolution'];
foreach ($res as $resolution){
 fwrite($myfile4, $resolution);
 fwrite($myfile4, "\n");
}



fclose($myfile4);
fclose($myfile);
fclose($myfile3);
exec("sh NeutronMonitor_Rate/runSFS.sh");

exec("sh NeutronMonitor_Rate/runEXE.sh");



header("Location: /Monitor.html");
exit();

echo "<br>";
echo("<button onclick=\"location.href='/Monitor.html'\">See Result</button>");

?>

</html>
