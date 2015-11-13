<?php
	/* 
	* create json response with code error
	*/
	
	function getJSONFromCodeError($code){
	
		$enum_message = array(
			200  => "ok",
			201  => "cant connect bdd"
		);
	
		if($code == 200)
			$success = true;
		else 
			$success = false;
			
		$response = json_encode(array(
				"success" => $success, 
				"code" => $code,
				"message" => $enum_message[$code]));
		return $response;
	}
	
?>