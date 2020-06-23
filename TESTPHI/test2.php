<?php
$line = "OULU JUNG";
echo $line;
$stations = explode(" ", $line); 

$result = sizeof($stations);                                                   
$myfile = fopen("EXE.txt", "w") or die("Unable to open file!");            
 for ($i = 0; $i < $result; $i++) {                                            
 $txt = $stations[$i];                                                         
 fwrite($myfile, $txt);                                                        

 fwrite($myfile, "\n");                                                        
}
//echo $message;
echo "\n COMPLETED";
?>