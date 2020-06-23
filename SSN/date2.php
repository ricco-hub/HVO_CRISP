<?php
$line = "OULU JUNG NEWK ROME MOSC ";
echo $line;
$stations = explode(" ", $line);                                               

$result = sizeof($stations);                                                   
$myfile = fopen("STAZIONI4.txt", "w") or die("Unable to open file!");            
 for ($i = 0; $i < $result; $i++) {                                            

 $txt = $stations[$i];                                                         

 fwrite($myfile, $txt);                                                        

 fwrite($myfile, "\n");                                                        

}
//echo $message;
echo "\n COMPLETED";
?>
