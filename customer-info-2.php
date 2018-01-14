<html>
<head></head>
<body>
<H3>SA TEST</H3>
<?php 
$output1=array();

exec('ls -l 2>&1', $output);
print_r($output); 
	

?> 

<H3>Completed...</H3>
<form name="input" action="index.php" method="get">
<input type="submit" value="Back">
</form>
</body>
</html>
