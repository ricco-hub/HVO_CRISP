<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
 <title>NEUTRON MONITOR</title>
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

    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">
    <!-- syntax highlighting CSS -->
    <link rel="stylesheet" href="/static/css/syntax.css">
    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed:400,300italic,300,400italic,700&amp;subset=latin,latin-ext" rel="stylesheet" type="text/css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/static/css/super-search.css">
    <link rel="stylesheet" href="/static/css/thickbox.css">
    <link rel="stylesheet" href="/static/css/projects.css">
    <link rel="stylesheet" href="/static/css/main.css">

<!-- -->
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
        <h5 class="author-name" style="color:rgb(60, 128, 214);"><b>HELIOPHYSICS VIRTUAL OBSERVATORY</b></h5>

        <hr />
        <ul class="sidebar-nav text-left">
          <strong>Menu</strong>
                        <li><a href="/index.html"><b>HOME</b></a></li>
              <li><a class="about" href="/SSN.html"><b>SUNSPOT NUMBER</b></a></li>
              <li><a class="about" href="/SFS.html"><b>SOLAR FIELD STRENGHT</b></a></li>
              <li><a class="about" href="/Tilt.html"><B>TILT ANGLE</b></a></li>
<li><a class="about" href="/Resources.html"><b>RESOURCES</b></a></li>
              <li><a class="about" href="/Neutron.html"><b>NEUTRON MONITOR</b></a></li>

       

 </ul>
      </div>
    </div>
    <div class="col-sm-8 col-offset-1 main-layout">

<!-- INSERIRE QUI IL CODICE-->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<center><h3 style="color:rgb(60, 128, 214);"><b>NM Station Set</b></h3></center
>
<?php
$myfile = fopen("SFS/Set.txt", "w") or die("Unable to open file!"); 
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

$myfile3 = fopen("SFS/E.txt", "w") or die("Unable to open file!");
$line3 = $_GET["birthday"];
$line4 = $_GET["birthday2"];
fwrite($myfile3, $line3);
fwrite($myfile3, "\r\n");
fwrite($myfile3, $line4);

fclose($myfile);
fclose($myfile3);
exec("sh SFS/runSFS.sh");

exec("sh SFS/runEXE.sh");

header("Location: http://10.2.201.68/SFS.html");
exit();

echo "<br>";
echo("<button onclick=\"location.href='/SFS.html'\">See Result</button>");

?>

<!--
<a class="about" href="/SSN.html">Solar Spot Number</a> (<b>SSN</b>) Data (monthly and daily) are taken from <a href="http://sidc.oma.be/silso/ ">SILSO</a>: World Data Center for the production, preservation and dissemination of the international sunspot number.<br>
<b>SSN(t)</b> descibes the mean number of SSN (averaged over a month or day) as a function of time.
<br><br>

About <a class="about" href="/Tilt.html">Tilt Angle</a> e <a class="about" href="/SFS.html">Solar Polar Field Strenght</a>, data are taken from <a href="http://wso.stanford.edu">Wilkox Solar Observatory</a>.<br>

<li>Tilt Angle data are updated about every month.</li>
<li>Solar Polar Field Strength data are updated about every 10 days.</li>
<br>
Data about CR fluxes measured by <a class="about" href="/Neutron.html">Neutron Monitor</a> are taken from  <a href="http://www01.nmdb.eu">NMDB Neutron Monitor DataBase</a>. All data start from 1/1/1960.<br>
The selected stations are:
 <li>JUNG (Switzerland)</li>
<li>APTY(Russia)</li>
<li> KIEL(Germany)</li>
  <li>OULU(Finland)</li>
<li> NEWK(USA)</li>
<li> MOSC(Moscow)</li>
<br>
<a href="https://tools.ssdc.asi.it/CosmicRays/ ">ASI-SSDC CosmicRay database at the Italian Space Agency</a> <br>

<a href="https://lpsc.in2p3.fr/cosmic-rays-db/">LPSC-CRDB, Database of Charged Cosmic Rays at LPSC/IN2P3 Grenoble</a> <br>
<a href="http://cosmicrays.oulu.fi">Sodankyla Geophysical Observatory at Oulu</a> <br>
<a href="https://spdf.gsfc.nasa.gov">NASA-SPDF, Space Physics Data Facility</a> <br>
<a href="https://umbra.nascom.nasa.gov">NASA-SDAC, Solar Data Analysis Center</a> <br>
<a href="https://oltaris.nasa.gov">NASA-OLTARIS, OnLine Tool for the Assessment of Radiation in Space</a> <br>
<a href="https://omniweb.gsfc.nasa.gov">NASA-OmniWeb, Web interface to the OMNI dataset</a> <br>
<a href="https://heliophysicsdata.gsfc.nasa.gov">NASA Heliophysics Data</a> <br>

<a href="https://ccmc.gsfc.nasa.gov/modelweb">NASA-ModelWeb Modeling Center</a> <br>
<a href="https://vepo.gsfc.nasa.gov">NASA-VEPO, Virtual Energetic Particle Observatory</a> <br>
<a href="https://voyager.gsfc.nasa.gov">NASA-GSFC Voyager mission data</a> <br>
<a href="https://voyager.jpl.nasa.gov"> NASA-JPL Voyager mission page</a> <br>
<a href="https://soho.nascom.nasa.gov/data/data.html">SWERTO, Space Weather at Roma Tor Vergata Roma</a> <br>
<a href="http://spaceweather.roma2.infn.it">SOHO Solar Heliospheric Observatory</a> <br>
<a href="http://www.swpc.noaa.gov">NOAA Space Weather Prediction Center</a> <br>

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
