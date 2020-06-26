<html>
<?php
$myfile = fopen("SSN/Set.txt", "w") or die("Unable to open file!");
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

$myfile3 = fopen("SSN/E.txt", "w") or die("Unable to open file!");
$line3 = $_GET["birthday"];
$line4 = $_GET["birthday2"];
fwrite($myfile3, $line3);
fwrite($myfile3, "\r\n");
fwrite($myfile3, $line4);

fclose($myfile);
fclose($myfile3);
exec("sh SSN/runSFS.sh");

exec("sh SSN/runEXE.sh");

header("Location: /SSN.html");
exit();

echo "<br>";
echo("<button onclick=\"location.href='/SSN.html'\">See Result</button>");

?>

</html>
