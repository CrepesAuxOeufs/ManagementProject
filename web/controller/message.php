<?php
	/* 
	* create json response with code error
	*/
	
	function getJSONFromCodeError($code){
	
		$enum_message = array(
			200  => "ok",
			201  => "cant connect bdd",
			202  => "Request cant be executed",
			300 => "Login not exist",
			301 => "Password not correct",
			302 => "User already disconnected"
		);
	
		if($code == 200)
			$success = true;
		else 
			$success = false;
			
		$response = array(
				"success" => $success, 
				"code" => $code,
				"message" => $enum_message[$code]);
		return $response;
	}
	
?>