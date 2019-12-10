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
function createGrid1(data){
    var result = "";
	for (var i in data){
        cr = "<tr>";

		for (var j in data[i]){
            cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">"+data[i][j]+"</td>";
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
    $.get("/init",{},function(response){
        var data = JSON.parse(response);
        createGrid(data);
    });
    $("#btn1").click(function(){
        $.get("/test",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    })
});