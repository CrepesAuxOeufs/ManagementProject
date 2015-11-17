var ObligatoryLogin = true;
var AutoHide = true;
var loadDashboard = false;
var loadUserListe = true;


if(ObligatoryLogin)		$('#myModal').modal({backdrop:'static',keyboard:false, show:true});

if(AutoHide) 		{setInterval(function(){ $('#myModal').modal('hide');},2000);}

if(loadDashboard) {$('#contentContainer').load("module/dashboardAdmin.html");}
if(loadUserListe) {$('#contentContainer').load("module/listeUser.html");}


$( document ).ready( getUsers );


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
				console.log("liste_userConnection");
				
			GenAllUserPage(msg.data);
			}
	});
	
}

function create_user(){
	var params_create_user = {
								request: "createUser",
								raw: {"name": $('#user_name').val(),"nickname": $('#user_nickname').val(),"mail": $('#user_mail').val(),"password": $('#user_password').val()}
							};
							
							
							
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(params_create_user),
			dataType: 'json',
			success: function(msg){
				console.log("create_user");
				
			//GenAllUserPage(msg.data);
			}
	});
}




function GenAllUserPage(userobject){
	
	
	for (user in userobject){
		
		
		console.log(userobject[user]);
		
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
	
	
	$('body').append('<script src="../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>');
	$('body').append('<script src="../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>');
	$('body').append("<script>$(document).ready(function() {$('#dataTables-example').DataTable({responsive: true});});</script>");
	
	
		
	
	
	
}




