var grp_idName = [];




$(document).ready(function(){
	$("#user_groupe").change(function(){
		$("#id_grp").val(grp_idName[$("#user_groupe").val()]);
	});
});


function getGroups(){
	
	var table = $('#dataTables-example').DataTable( {
								
								lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
								columns: [
										{ title: "id user" },
										{ title: "id_groupe"},
										{ title: "Groupe" },
										{ title: "Nom" },
										{ title: "Prenom" }										
									]
							} );
							
	$('#dataTables-example tbody').on( 'click', 'tr', function () {
	
	
	
	
        if ( $(this).hasClass('clicked') ) {
            $(this).removeClass('clicked');
			
        }
        else {
            table.$('tr.clicked').removeClass('clicked');
            $(this).toggleClass('clicked');
			
			var elem = $(this).children();
			
			$("#id_user").val($(elem[0]).text());
			$("#id_grp").val($(elem[1]).text())
			$("#user_groupe").val($(elem[2]).text());
			$("#user_name").val($(elem[3]).text());
			$("#user_nickname").val($(elem[4]).text());
			
        }
    } );
	
	
	
	
	
	
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
			
			
			GenALLGroupV2(msg.data);
		}
	});
	
	
}


function update_grp(){
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
			
			
			GenALLGroupV2(msg.data);
		}
	});
}


function Create_group(){
	
	
	
	var params_allGroups = {
							request: "createGroup",
							data:{"group_name":$("#grp_name").val()}
						};
								
	$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			logingHeaderAddMessage("Nouveau groupe "+$("#grp_name").val()+" créer","success");
			$("#grp_name").val(""); 
			
			console.log(msg);
			update_grp();
		}
	});
}
function add_userToGroup(){
	var params_allGroups = {
							request: "addUserToGroup",
							data:{"user_id":$("#id_user").val(),
									"group_id":$("#id_grp").val()}
						};
						
						
	console.log(params_allGroups);
								
	$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			logingHeaderAddMessage("L'utilisateur "+$("#user_nickname").val()+ " " +$("#user_name").val() + " a été ajouté avec succès au groupe " +$("#user_groupe").val()  ,"success");
			
			console.log(msg);
			update_grp();
		}
	});
}




function GenALLGroupV2(gobject){

	var table = $('#dataTables-example').DataTable();
	
	table.clear();
	
	for (group in gobject){
		var group_users = gobject[group].users;
		
		for (user in group_users){
			
		
			
			
			table.row.add([
				group_users[user]["id"],
				gobject[group].id,
				gobject[group].name,
				group_users[user]["name"],
				group_users[user]["nickname"]
				]
		);
			 
		
		}
	}
	table.draw();
	
	
	
	var params_allGroups = {
							request: "getUsersUngroup",
							data:{}
						};
								
	$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			console.log(msg);
			addUngrp(msg.data);
			
		}
	});
	
	
	var params_allGroups = {
							request: "showGroupsOnly",
							data:{project_id:1}
						};
								
	$.ajax(	{
		type: "POST",
		url: "../controller/recupGroup.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			
			console.log("showGroupsOnly");
			console.log(msg.data);
			
			
			$("#user_groupe").empty();
			$("#sup_grp").empty();
			
			for (blop in msg.data) {
				
				grp_idName[msg.data[blop].name] = msg.data[blop].id;
				
				
				var option1 = $('<option></option>').attr("value", msg.data[blop].name).text(msg.data[blop].name);
				var option2 = $('<option></option>').attr("value", msg.data[blop].name).text(msg.data[blop].name);
				$("#user_groupe").append(option1);
				$("#sup_grp").append(option2);
			}
			console.log(grp_idName);
			
			
			
		}
	});
	
	
	
	
	
}


function addUngrp(gobject){
	var table = $('#dataTables-example').DataTable();
	
	for (group in gobject){
		table.row.add([
				gobject[group]["id"],
				"0",
				"aucun",
				gobject[group]["name"],
				gobject[group]["nickname"]
				]);
	}
	table.draw();
	
}

function editGrp(){





var params_allUsers = {
								request: "addUserToGroup",
								data: {"user_id":481,"group_id":9}
							};
								
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_allUsers),
			dataType: 'json',
			success: function(msg){
				console.log(msg);
				
			}
	});

}



function Supp_group(){
	
	var params_allUsers = {
								request: "removeGroup",
								data: {"group_id":grp_idName[$("#sup_grp").val()]}
							};
	console.log(params_allUsers)							
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_allUsers),
			dataType: 'json',
			success: function(msg){
				console.log(msg);
				console.log(grp_idName[$("#sup_grp").val()]);
				logingHeaderAddMessage("Groupe "+$("#sup_grp").val()+" supprimé","success");
				
				update_grp();
				
			},
			error: function (xhr, ajaxOptions, thrownError) {
				logingHeaderAddMessage("Error","warning");
				//alert(xhr.status);
				//alert(thrownError);
			}
	});
	
}

function logingHeaderAddMessage(msg,type){
	var uuid = generateUUID();
	console.log(uuid);
	$("#MsgHeader").append('<div class="alert alert-'+type+' alert-dismissable" id="' + uuid+ '" style="margin:5px 5px 5px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
	setTimeout(function()	{document.getElementById(uuid).remove();},50000);
}







