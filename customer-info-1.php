<html>
<head></head>
<body>

<H3 align="center" style="font-size:40px;color:blue;"><u>REQUESTED CUSTOMER INFORMATION</u></H3>
<?php 
$output1=array();
$i=0;
$j=0;
$flag2=0;
$flat3=0;
$flag4=0;
$flag5=0;
$flag6=0;
$command1="sudo python -c 'import ipdata; ipdata.current(\"";
/*$command2 = getenv("var");*/
$command2 = $_GET['un'];

$command3=$command1.$command2."\")'";


echo "<br />";

$command4=$command3." 2>&1";


exec($command4,$output1);

echo "<br />";

foreach ($output1 as $item)
{
     if ($i == "0")
	 {
		echo "<u> <font color=blue font face='arial' size='5pt'>$item</font></u> "; 
		echo "<br />";
	 }
	 else if ($i == "6")
	 {
		echo " <u><font color=blue font face='arial' size='5pt'>$item</font></u> "; 
		echo "<br />";
	 }
	 else if ($i == "10")
	 {
		 if ($item=="online")
		 {
			 $j=0; 
		 }
		 else
		 {
			 $j=1; 
		 }
		
	 }
	 else if ($i == "11")
	 {
		 if ($j=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		
	 }
	 else if ($i == "20")
	 {
		 if ($item=="fine")
		 {
			 $flag2=0; 
		 }
		 else
		 {
			 $flag2=1; 
		 }
		
	 }
	 else if ($i == "21")
	 {
		 if ($flag2=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		
	 }
	 else if ($i == "22")
	 {
		 if ($item=="fine")
		 {
			 $flag3=0; 
		 }
		 else if ($item=="notfine")
		 {
			 $flag3=1; 
		 }
		 else
		 {
			 $flag3=2;
		 }
		
	 }
	 else if ($i == "23")
	 {
		 if ($flag3=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else if ($flag3=="1")
		 {
			 echo "<font color=orange >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		 
		
	 }
	 
	 else if ($i == "29")
	 {
		echo "<u> <font color=blue font face='arial' size='5pt'>$item</font></u> "; 
		echo "<br />";
	 }
	 
	  else if ($i == "34")
	 {
		 if ($item=="fine")
		 {
			 $flag4=0; 
		 }
		 else
		 {
			 $flag4=1; 
		 }
		
	 }
	 else if ($i == "35")
	 {
		 if ($flag4=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		
	 }
	   else if ($i == "36")
	 {
		 if ($item=="fine")
		 {
			 $flag5=0; 
		 }
		 else
		 {
			 $flag5=1; 
		 }
		
	 }
	 else if ($i == "37")
	 {
		 if ($flag5=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		
	 }
	   else if ($i == "38")
	 {
		 
		 if ($item=="fine")
		 {
			 $flag6=0; 
		 }
		 else
		 {
			 $flag6=1; 
		 }
		
	 }
	 else if ($i == "39")
	 {
		 if ($flag6=="0")
		 {
			 echo "<font color=green >$item</font> "; 
			 echo "<br />";
		 }
		 else
		 {
			 echo "<font color=red >$item</font> "; 
			 echo "<br />";
		 }
		
	 }
	 
	 else
	 {
		 echo $item;
		 echo "<br />";
		 
	 }
	 
	 
     
	 $i=$i+1;
	 
}
echo "<br />";

?> 

<!-- <H3>Completed...</H3> -->

<form name="input" action="index.php" method="get">
<input type="submit" value="Back">
</form>
</body>
</html>
