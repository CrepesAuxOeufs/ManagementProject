<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	$json = json_decode(file_get_contents("php://input"),true);

	$request = $json["request"];
	$dataResponse = null;
	

    if ($request == 'showGroups'){
        $dataResponse = getAllGroup($json["data"]);
    }

   if($dataResponse == null)
		$response = getJSONFromCodeError(202);
	else{
		$response = getJSONFromCodeError(200);
		$response["data"] = $dataResponse;
	}
	
	echo json_encode($response);

	
    function getAllGroup($data)
    {
        $result = mysql_query( "SELECT `GROUP`.name, `USER`.id,`USER`.name,`USER`.nickname
                            FROM `GROUP`, `USER`, `USER_GROUP` 
                            WHERE `GROUP`.id = `USER_GROUP`.group_id 
                            AND `USER`.id = `USER_GROUP`.user_id 
                            AND `GROUP`.project_id = '". $data["project_id"] . "'");

        if (!$result) 
        {
            echo "Impossible d'exécuter la requête dans la base : " . mysql_error();
            exit;
        }

        $groupArrayName = array();
        $groupArray = array();
		
        while($row = mysql_fetch_row($result))
        {
            $nameGroup = $row[0];
            $userID = $row[1];
            $useName = $row[2];
            $userNickname = $row[3];
			
			$found = null;
			foreach($groupArray as &$group){
				if($group["name"] == $nameGroup){
					$found=$group;
				}
			}
			
			if($found == null){
				$found = array();
				$found["name"] = $nameGroup;
				$found["users"] = array(); 
				array_push($groupArray, $found);
			}
				
				
			$user = array();
			$user["id"] = $userID;
			$user["name"] = $useName;
			$user["nickname"] = $userNickname;
			
			foreach($groupArray as &$group){
				if($group["name"] == $nameGroup){
					array_push($group["users"], $user);
				}
			}
        }
        return $groupArray;
    }



?>