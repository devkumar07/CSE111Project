function createGrid(data){
	var result = "";

	for (var i in data){
		var cr = "<tr>";

		for (var j in data[i]){
            cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">"+data[i]+"</td>";
            //cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">";
		}

		cr = cr + "</tr>\n";
		result = result + cr;
	}

	$("#college").html(result);

}
$(document).ready(function(){
    $.get("/",'index.html')
    $.get("/init",{},function(response){
        var data = JSON.parse(response);
        createGrid(data);
    });
    $("#test").html("TESTING");
    
});