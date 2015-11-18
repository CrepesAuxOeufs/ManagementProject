





function getGroups(){
	
	
	var params_allGroups = {
							request: "showGroups",
							data:{project_id:1}
						};
								
	$.ajax(	{
		type: "POST",
		url: "../controller/recupgroup.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			console.log(msg);
			
			
			GenAllGroupPage(msg.data);
		}
});
	
}

function GenAllGroupPage(groupobject){
	
	for (group in groupobject){

		var body = document.getElementById("body_list");
		
		// On crée un nouveau Div et on ajoute En Titre le nom du groupe
		var nouveauDiv = document.createElement("div");
		nouveauDiv.id = "id_group"+group;
		nouveauDiv.innerHTML = "<h1>"+groupobject[group]["name"]+"</h1>";
		body.appendChild(nouveauDiv);
		
		//AJOUT DU SCORING ICI
		
		
		
		
		

		// crée un élément <table> et un élément <tbody>
        var table     = document.createElement("table");
        var tablebody = document.createElement("tbody");
		table.id = "table"+group;
		console.log(table.id);
		
		var group_users = groupobject[group].users;
		
		for (user in group_users){
			
			//On Crée une nouvelle ligne
			var row = document.createElement("tr");
			
			//On crée la colonne id
			cellid = document.createElement("td");
			textecellid = document.createTextNode(group_users[user]["id"] );
			cellid.appendChild(textecellid);
			row.appendChild(cellid);
			cellid.style.display = 'none';
			
			//On crée la colonne prénom
			cellnickname = document.createElement("td");
			textenickname = document.createTextNode(group_users[user]["nickname"] );
			cellnickname.appendChild(textenickname);
			row.appendChild(cellnickname);
			
			//On Crée la colonne Nom
			cellname = document.createElement("td");
			textename = document.createTextNode(group_users[user]["name"] );
			cellname.appendChild(textename);
			row.appendChild(cellname);
			
			//On ajout un bouton en fin de ligne
			var button = document.createElement("input" ) ;
			button.type = "button" ;
			button.value = "X" ;
			button.name = "button"+group+user ;
			button.setAttribute("onClick","EnleverUser("+group_users[user]["id"]+")") ;
			row.appendChild(button) ;
			
			// ajoute la ligne à la fin du corps du tableau
            tablebody.appendChild(row);
			 
		
		}		  
        // place <tbody> dans l'élément <table>
        table.appendChild(tablebody);
        // ajoute <table> à l'élément <body>
        body.appendChild(table);
        // définit l'attribut border du tableau à 2
        table.setAttribute("border", "2");
		table.setAttribute("width", "100%");
		
	}
	
	
	
}


function EnleverUser(id){
	console.log("dans fonction user "+id);
	
	var params_delete_user_from_group = {
								request: "removeUserFromGroup",
								data: {user_id: id}
							};
							
	console.log(params_delete_user_from_group);						
							
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_delete_user_from_group),
			dataType: 'json',
			success: function(msg){
				console.log(msg);
				
			//GenAllUserPage(msg.data);
			}
	});	
}
