<html>
<head>

<meta charset="UTF-8">
<link href="http://www.jqueryscript.net/css/jquerysctipttop.css" rel="stylesheetq" type="text/css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
 <title>Solar Data Web Tool</title>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">
    <!-- syntax highlighting CSS -->
    <link rel="stylesheet" href="syntax.css">
    <!-- Bootstrap core CSS -->
    <link href="bootstrap.min.css" rel="stylesheet">
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed:400,300italic,300,400italic,700&amp;subset=latin,latin-ext" rel="stylesheet" type="text/css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/super-search.css">
    <link rel="stylesheet" href="/thickbox.css">
    <link rel="stylesheet" href="/projects.css">
    <link rel="stylesheet" type="text/css" href="/main2.css">

<!-- -->
<script src="/jsroot/scripts/JSRootCore.js?2d&onload=createGUI"> type="text/javascript"></script>

<script type='text/javascript'>
var filename = "/SFS/SFSRANGE/SFSRange.root";
   JSROOT.OpenFile(filename, function(file) {
file.ReadObject("TOTAL Graph;1", function(obj) {
       JSROOT.draw("drawing", obj);
     });
   });
</script>



</head>


<!-- ***********************-->
<!-- ***********************-->
<!-- ***********************-->
<!-- ***********************-->
<!-- ***********************-->

<body>
  <div class="container">
    <div class="col-sm-3">
      <div class="fixed-condition text-center">
        <a href="/"><img class="profile-avatar" src="/static/img/me.png" height="75px" width="75px" /></a>
        <h4 class="author-name" style="color:rgb(60, 128, 214);"><b>Solar Data Tool</b></h4>

        <hr />
        <ul class="sidebar-nav text-left">
          <strong>Menu</strong>
          <li><a href="/index.html">Home</a></li>
          <li><a class="about" href="/SSN.html">Solar Spot Number</a></li>
          <li><a class="about" href="/SFS.html">Solar Field Strenght</a></li>
          <li><a class="about" href="/Tilt.html">Tilt Angle</a></li>
          <li><a class="about" href="/SolarSmoothed.html">SSN Smoothed & Monthly</a></li>
          <li><a class="about" href="/Resources.html">Resources</a></li>
          <li><a class="about" href="/Neutron.html">Neutron Monitor</a></li>
        </ul>
      </div>
    </div>
    <div class="col-sm-8 col-offset-1 main-layout">

<!-- INSERIRE QUI IL CODICE-->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

<?php
$myfile2 = fopen("E.txt", "w") or die("Unable to open file!");
$line2 = $_GET["birthday"];
$line = $_GET["birthday2"];
$data = $line2 . PHP_EOL . $line;
fwrite($myfile2, $line2);
//echo $line2;
//echo "\n\n\n";
//echo $line;
fwrite($myfile2, "\r\n");
fwrite($myfile2, $line);
fclose($myfile2);
exec("sh run.sh");
?>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<center><h3 style="color:rgb(60, 128, 214);"><b>Solar Field Strenght</b></h3></center>



<script>
n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
document.getElementById("date").innerHTML = m + "/" + d + "/" + y;
</script>


<br><br>
<center>
<div id="drawing" style="width:650px; height:400px"></div>
<script>
function Tree(){
    var now = new Date();
    var month = parseInt(now.getMonth())+1;
    var path = "SFSTree_" + month + "-" + now.getDate() + "-" +now.getFullYear() + ".root";
    window.location.href="/TREE/Download/"+path;
}
function Root(){
    var now = new Date();
    var month = parseInt(now.getMonth())+1;
    var path = "SFS_" + month + "-" + now.getDate() + "-" +now.getFullYear() + ".root";
    window.location.href="/SFS/Download/"+path;
}
</script>

<button><type="button"><a onclick="Root();">ROOT File</a></button>
<button><type="button"><a onclick="Tree();">ROOT Tree</a></button>
</center>




<!-- fine codice e inizio del Footer-->
      <footer>
        <!--  &copy; {{ site.author }} -->
         <a href="mailto:david.53211@gmail.com">David Pelosi</a> - Build by JSROOT.
      </footer>
    </div>
  </div>
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

</body>
</html>
