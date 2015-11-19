document.getElementById("box_loading").style.display = 'none';
var opts = {
      lines: 12             // The number of lines to draw
    , length: 7             // The length of each line
    , width: 5              // The line thickness
    , radius: 10            // The radius of the inner circle
    , scale: 1.0            // Scales overall size of the spinner
    , corners: 1            // Roundness (0..1)
    , color: '#000'         // #rgb or #rrggbb
    , opacity: 1/4          // Opacity of the lines
    , rotate: 0             // Rotation offset
    , direction: 1          // 1: clockwise, -1: counterclockwise
    , speed: 1              // Rounds per second
    , trail: 100            // Afterglow percentage
    , fps: 20               // Frames per second when using setTimeout()
    , zIndex: 2e9           // Use a high z-index by default
    , className: 'spinner'  // CSS class to assign to the element
    , top: '50%'            // center vertically
    , left: '50%'           // center horizontally
    , shadow: false         // Whether to render a shadow
    , hwaccel: false        // Whether to use hardware acceleration (might be buggy)
    , position: 'absolute'  // Element positioning
    }
var target = document.getElementById("box_loading");
var spinner = new Spinner(opts).spin(target);

var nbUsers = 0;
var params_allUsers = {
							request: "getAllAccount",
							raw: ["id"]
						};
$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allUsers),
		dataType: 'json',
		success: function(msg){
			var users = msg.data;
			for(user in users){
				nbUsers++;
			}
		document.getElementById("nbUsers").innerHTML = nbUsers;
		}
});

$('#label_nb_groups').on('input', function() {
    var nbGroup = $(this).val();
	if(nbGroup != "" && nbGroup <= nbUsers){
		document.getElementById("nbGroups").innerHTML = nbGroup;
		var nbUsersGroup = parseInt(nbUsers / nbGroup);
		var nbGroup_anormal = nbUsers % nbGroup;
		if(nbGroup_anormal>0)
			document.getElementById("groupes_draw").innerHTML = (nbGroup-nbGroup_anormal) + " équipes de " + nbUsersGroup + " personnes <br>" + (nbGroup_anormal) + " équipes de " + (nbUsersGroup+1) + " personnes" ;
		else
			document.getElementById("groupes_draw").innerHTML = (nbGroup-nbGroup_anormal) + " équipes de " + nbUsersGroup + " personnes";
	}
	else{
		document.getElementById("nbGroups").innerHTML = "";
		document.getElementById("groupes_draw").innerHTML = "";
		}
});




$("#groups_generate_sumbit").click(function() {
	if(document.getElementById("label_nb_groups").value == ""){
		errorHeaderAddMessage("Nombre de groupe non valide", "warning");
		return;
	}
	if( parseInt(document.getElementById("label_nb_groups").value) > nbUsers){
		errorHeaderAddMessage("Impossible de lancer la génération avec un nombre d'équipe supérieur aux nombre de personnes", "warning");
		return;
	}
	

	console.log(document.getElementById("select_generate_type").options[document.getElementById("select_generate_type").selectedIndex].innerHTML);
	if(document.getElementById("select_generate_type").options[document.getElementById("select_generate_type").selectedIndex].innerHTML != "solveur"){
		document.getElementById("box_loading").style.display = 'block';
		document.getElementById("box_param").style.display = 'none';
		var params_allGroups = {
									request: "generateGroups",
									data: {nbGroup : document.getElementById("label_nb_groups").value, type : document.getElementById("select_generate_type").options[document.getElementById("select_generate_type").selectedIndex].innerHTML}
								};
		
		$.ajax(	{
				type: "POST",
				url: "../controller/generateGroups.php",
				data: JSON.stringify(params_allGroups),
				dataType: 'json',
				success: function(msg){
					document.getElementById("box_loading").style.display = 'none';
					console.log(msg);
					if(msg.success){
						window.location.replace("index.html");
						errorHeaderAddMessage("Groupe généré avec succés", "success");
					}
					else{
						document.getElementById("box_param").style.display = 'block';
						errorHeaderAddMessage(msg.message, "warning");
					}
				}
		});
	}
	else{
		window.location.href='../controller/exportcsv.php';
		errorHeaderAddMessage("Téléchargement du tableur pour le solveur en cours, redirection ...", "success");
		setInterval(function()	{window.location.replace("index.html");},3000);
	}

	
});

//type info warning danger success
function errorHeaderAddMessage(msg,type){
	var uuid = generateUUID();
	console.log(uuid);
	$("#errorHeader").append('<div class="alert alert-'+type+' alert-dismissable" id="' + uuid+ '" style="margin:5px 5px 0px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
	setInterval(function()	{document.getElementById(uuid).remove();},5000);
}

function generateUUID(){
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now();; //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}
