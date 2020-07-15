<html>
<?php

$myfile3 = fopen("WIND/E.txt", "w") or die("Unable to open file!");
$line3 = $_GET["birthday"];
$line4 = $_GET["birthday2"];
fwrite($myfile3, $line3);
fwrite($myfile3, "\r\n");
fwrite($myfile3, $line4);

fclose($myfile);
fclose($myfile3);


exec("sh WIND/runSFS.sh");

exec("sh WIND/runEXE.sh");

header("Location: /SolarWind.html");
exit();

echo "<br>";
echo("<button onclick=\"location.href='/SolarWind.html'\">See Result</button>");

?>

</html>
