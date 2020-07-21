<html>
<?php

$myfile2 = fopen("Forecast/E.txt", "w") or die("Unable to open file!");
$line2 = $_GET['energy'];
fwrite($myfile2, $line2);
$myfile = fopen("Forecast/NM_Set.txt", "w") or die("Unable to open file!");
$name = $_GET['station'];
foreach ($name as $station){
 fwrite($myfile, $station);
 fwrite($myfile, "\n");
}




$myfile3 = fopen("Forecast/Etime.txt", "w") or die("Unable to open file!");
$line3 = $_GET["birthday"];
$line4 = $_GET["birthday2"];
fwrite($myfile3, $line3);
fwrite($myfile3, "\r\n");
fwrite($myfile3, $line4);

exec("sh Forecast/convert.sh");


exec("sh Forecast/runEXE.sh");




$myfileN = fopen("NeutronMonitor_Rate/Set.txt", "w") or die("Unable to open file!");
$name = $_GET['station'];
foreach ($name as $station){
 fwrite($myfileN, $station);
 fwrite($myfileN, "\n");
}

$myfile3N = fopen("NeutronMonitor_Rate/E.txt", "w") or die("Unable to open file!");
$line3N = $_GET["birthday"];
$line4N = $_GET["birthday2"];
fwrite($myfile3N, $line3N);
fwrite($myfile3N, "\r\n");
fwrite($myfile3N, $line4N);


$myfile4N = fopen("NeutronMonitor_Rate/Res.txt", "w") or die("Unable to open file!");
fwrite($myfile4N, "month\n");




fclose($myfile4);
fclose($myfile);
fclose($myfile3);

exec("sh NeutronMonitor_Rate/runSFS.sh");


exec("sh NeutronMonitor_Rate/runEXE.sh");





header("Location: ForceField.html");
exit();





?>
</html>
