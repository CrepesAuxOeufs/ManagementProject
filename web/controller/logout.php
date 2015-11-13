<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	$testConnect = isConnected();

	if ($testConnect)
	{
		destroySession();
	    $response = getJSONFromCodeError(200);
	}
	else
	{
		$response = getJSONFromCodeError(302);
	}
	echo json_encode($response);

?>