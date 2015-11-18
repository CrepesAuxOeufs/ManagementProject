<?php
	include 'message.php';
	/* 
	* Create session (login): createSession(5,"Sarah","CROCHE","sarah.croche@imerir.com");
	* Destroy current session (logout) : destroySession();
	* Test is user online : isConnected();
	*/
	error_reporting(0);
	session_start(); 
	
	$dataResponse = array();
	$dataResponse['id'] = $_SESSION['id'];
	$dataResponse['name'] = $_SESSION['name'];
	$dataResponse['nickname'] = $_SESSION['nickname'];
	$dataResponse['mail'] = $_SESSION['mail'];
	$dataResponse['connect'] = $_SESSION['connect'];
	$dataResponse['admin'] = $_SESSION['admin'];
	$dataResponse['profil'] = $_SESSION['profil'];
	
	$response = array(
			"success" => true, 
			"code" => 200,
			"message" => "ok");
	$response["data"] = $dataResponse;
	echo json_encode($response);
?>