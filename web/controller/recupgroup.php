<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	//$json = json_decode(file_get_contents("php://input"),true);
	$json = '{  "request": "showGroups", 
                "project_id": 1, 
                "group_id": 1 
            }';


	$parsed_json = json_decode($json);

	$request =    $parsed_json -> {'request'};
	$project_id = $parsed_json -> {'project_id'};
    $group_id =   $parsed_json -> {'group_id'};

    echo '$json: ' . $json . ' <br> ';
    echo '$request: ' . $request . ' <br> ';
    echo '$project_id: ' . $project_id . ' <br> ';
    echo '$group_id: '. $group_id . ' <br> ';

    $result = mysql_query( "SELECT * 
                            FROM GROUP 
                            WHERE project_id = '". $project_id . "'" );

    if (!$result) 
    {
        echo "Impossible d'exécuter la requête dans la base : " . mysql_error();
        exit;
    }

    while($row = mysql_fetch_assoc($result))
    {
        echo $row['id'] . ' ' . $row['project_id'] . ' ' . $row['name'] . ' <br>';
    }

?>