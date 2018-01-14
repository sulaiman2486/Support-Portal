<html>
<head></head>
<body>
<H3>RIPE Database Object Are:</H3>
<?php 
$output1=array();

$command1="python -c \"import ssht; ssht.current('";
$command2 = $_GET['un'];

$command3=$command1.$command2."')\"";

echo "<br />";
echo $command3;
exec($command3,$output1);

echo "<br />";

foreach ($output1 as $item)
{
     echo $item;
     echo "<br />";
}	

?> 

<H3>Completed...</H3>
<form name="input" action="index.php" method="get">
<input type="submit" value="Back">
</form>
</body>
</html>