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
    $("#btn20").click(function(){
        $.get("/q1",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn1").click(function(){
        $.get("/q2",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn2").click(function(){
        $.get("/q3",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn3").click(function(){
        $.get("/q4",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn4").click(function(){
        $.get("/q5",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn5").click(function(){
        $.get("/q6",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn6").click(function(){
        $.get("/q7",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn7").click(function(){
        $.get("/q8",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn8").click(function(){
        $.get("/q9",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn9").click(function(){
        $.get("/q10",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn10").click(function(){
        $.get("/q11",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn11").click(function(){
        $.get("/q12",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn12").click(function(){
        $.get("/q13",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn13").click(function(){
        $.get("/q14",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn14").click(function(){
        $.get("/q15",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn15").click(function(){
        $.get("/q16",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn16").click(function(){
        $.get("/q17",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn17").click(function(){
        $.get("/q18",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn18").click(function(){
        $.get("/q19",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
    $("#btn19").click(function(){
        $.get("/q20",{},function(response){
            var data = JSON.parse(response)
            createGrid1(data);
        });
    });
});