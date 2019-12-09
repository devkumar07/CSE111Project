function createGrid(data){
	var result = "";
    var d =  "<thead> <tr><th>ID</th><th>University</th><th>Rank</th><th>Type</th><th>Attendance</th><th>Gender Ratio</th><th>Rank</th><th>Average Scholarship</th></tr></thead>"
	for (var i in data){
        cr = "<tr>";

		for (var j in data[i]){
            cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">"+data[i][j]+"</td>";
            //cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">";
		}

		cr = cr + "</tr>\n";
		result = result + cr;
    }
    var final = d + result

	$("#college").html(final);

}
$(document).ready(function(){
    $.get("/",'index.html')
    $.get("/init",{},function(response){
        var data = JSON.parse(response);
        createGrid(data);
    });
});