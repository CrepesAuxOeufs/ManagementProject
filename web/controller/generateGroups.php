<?php
	include 'message.php';
	//$result = exec('python ./Groupe2.py');
	//echo $result;
	$response = getJSONFromCodeError(200);
	echo json_encode($response);
?>