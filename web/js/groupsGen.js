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

$("#groups_generate_sumbit").click(function() {
	if(document.getElementById("label_nb_groups").value == "")
		return;
	document.getElementById("box_loading").style.display = 'block';
	document.getElementById("box_param").style.display = 'none';
	
	var params_allGroups = {
								request: "generateGroups",
								data: {nbGroup : document.getElementById("label_nb_groups").value}
							};
							
	$.ajax(	{
			type: "POST",
			url: "../controller/generateGroups.php",
			data: JSON.stringify(params_allGroups),
			dataType: 'json',
			success: function(msg){
				document.getElementById("box_loading").style.display = 'none';
				console.log(msg);
				//window.location.replace("index.html");
			}
	});
});
