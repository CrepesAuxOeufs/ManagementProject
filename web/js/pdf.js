
$("#BTN_print").click(function() {
	var source = document.getElementById("BTN_print").parentElement;
	var doc = new jsPDF();          
	var elementHandler = {
	  '#ignorePDF': function (element, renderer) {
		return true;
	  }
	};
	
	doc.fromHTML(
		source,
		15,
		15,
		{
		  'width': 180,'elementHandlers': elementHandler
		});

	doc.output("dataurlnewwindow");
});