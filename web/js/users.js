
function getUsers(){
	var params_allUsers = {
								request: "getAllAccount",
								raw: ["id","name","nickname","mail","password"]
							};
								
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_allUsers),
			dataType: 'json',
			success: function(msg){
				var users = msg.data;
				//Clear users tab
				
				for(user in users){
					//Add user to tab
				}
			}
	});
	
}

//Exemple recup users
getUsers();