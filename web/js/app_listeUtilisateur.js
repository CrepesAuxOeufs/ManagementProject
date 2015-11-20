function getUsers(){
	
	
	
	var table = $('#dataTables-example').DataTable( {
								
								lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
								columns: [
										{ title: "id" },
										{ title: "name" },
										{ title: "nickname" },
										{ title: "mail" },
										{ title: "password" }
									]
							} );
							
	
	
	
	
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
				console.log("liste_userConnection");
				console.log(msg);
			updateData(msg.data);
			}
	});
	
}

function create_user(){
	var params_create_user = {
								request: "createUser",
								raw: {"name": $('#user_name').val(),"nickname": $('#user_nickname').val(),"mail": $('#user_mail').val(),"password": $('#user_password').val()}
							};
							
	$('#user_name').val("");
	$('#user_nickname').val("");
	$('#user_mail').val("");
	$('#user_password').val("");
							
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_create_user),
			dataType: 'json',
			success: function(msg){
				console.log("create_user");
				console.log(msg);
				getUsers();
				userAddMessage("success","success");
				
			}
	});
}




function GenAllUserPage(userobject){
	
	
	for (user in userobject){
		
		
		
		
		$('<tr>').append(
			$('<td>').text(userobject[user]["id"]),
			$('<td>').text(userobject[user]["name"]),
			$('<td>').text(userobject[user]["nickname"]),
			$('<td>').text(userobject[user]["mail"]),
			$('<td>').text(userobject[user]["password"])
		
		).appendTo('#user_data');
		
		
		/*var tr = document.createElement('tr');
		tr.html = "<td>"+userobject[user]["id"]+"</td>";
		tr.html +="<td>"+userobject[user]["name"]+"</td>";
		tr.html +="<td>"+userobject[user]["nickname"]+"</td>";
		tr.html +="<td>"+userobject[user]["mail"]+"</td>";
		tr.html +="<td>"+userobject[user]["password"]+"</td>";
		console.log(tr);
		$('#user_data').append(tr);*/
		
		
		
		
		
	}
	
	
	//$('body').append('<script src="../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>');
	//$('body').append('<script src="../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>');
	//$('body').append("<script>$(document).ready(function() {$('#dataTables-example').DataTable({responsive: true});});</script>");
}

function updateData(userobject){
	
	var table = $('#dataTables-example').DataTable();
	
	table.clear();
	for (user in userobject){
		table.row.add([userobject[user]["id"],
				userobject[user]["name"],
				userobject[user]["nickname"],
				userobject[user]["mail"],
				userobject[user]["password"]]
		);
	}
	
	table.draw();
	
	
	
	
	
	
}


function userAddMessage(msg,type){
	var uuid = generateUUID();
	console.log(uuid);
	$("#userMsg").append('<div class="alert alert-'+type+' alert-dismissable" id="' + uuid+ '" style="margin:5px 5px 0px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
	setTimeout(function()	{document.getElementById(uuid).remove();},5000);
}






