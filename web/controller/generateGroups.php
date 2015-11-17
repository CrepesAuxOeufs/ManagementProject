<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	/* for test */
    $json = '{
    			"request":"generateGroups",
    			"data":{
    					"nbGroup":"7"
    					}
    		}';

	$parsed_json = json_decode($json);
	$nbGroup = $parsed_json -> {'data'} -> {'nbGroup'};

	echo "json : " . $json . "<br>";
	echo "nbGroup : " . $nbGroup . "<br>";

	$use = getIdUserList();

	print_r($use);

	//$result = exec('python ./Groupe2.py ' . $nbGroup . ' ' . $use);

function getIdUserList()
{		
    $result = mysql_query("SELECT id FROM `USER`");

	$users = array();

    while($row = mysql_fetch_assoc($result))
    {
		array_push($users, $row['id']);
	}
	
	return $users;
}

?>