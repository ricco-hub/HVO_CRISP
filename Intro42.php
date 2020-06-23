<html>
<head>
<meta charset="UTF-8">
<link href="http://www.jqueryscript.net/css/jquerysctipttop.css" rel="stylesheetq" type="text/css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="date.format.js"></script>
<script src="jquery-dropdate.js"></script> 
<script>
$(document).ready(function(){
    $('.dropdate').dropdate({
        dateFormat:'mm/dd/yyyy'
    });
});
</script>

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
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
 <title>Solar Data Web Tool</title>



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
<center><h3 style="color:rgb(60, 128, 214);"><b>Resources</b></h3></center>


<br><br><h4>Select Neutron Monitor stations</h4>

<div class="jquery-script-clear"></div>

<br>
<form action="WW2.php" method="get">
    OULU         <input type="checkbox" name="station[]" id="station" value="OULU"><br>
    JUNG <input type="checkbox" name="station[]" id="station" value="JUNG"><br>
    NEWK <input type="checkbox" name="station[]" id="station" value="NEWK"><br>
    APTY <input type="checkbox" name="station[]" id="station" value="APTY"><br>
    ROME <input type="checkbox" name="station[]" id="station" value="ROME"><br>
    MOSC <input type="checkbox" name="station[]" id="station" value="MOSC"><br>
    MXCO <input type="checkbox" name="station[]" id="station" value="MXCO"><br>
<br>    
<form action="WW2.php" method="get">
Set Energy [GeV]: <input type="text" name="energy"><br>
<input type="submit">
</form>


<form method="get" action="WW6.php">
  <input type="text" name="birthday" value="" class="dropdate"><br><br>
  <input type="text" name="birthday2" value="" class="dropdate"><br><br>
  <input type="submit">
</form>

 
<!-- fine codice e inizio del Footer-->
 
<br><br><br>
</div>
</body>
</html>
