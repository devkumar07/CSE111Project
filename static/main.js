function createGrid(data){
	var result = "";
    var d =  "<thead> <tr><th>ID</th><th>University</th><th>Rank</th><th>Type</th><th>Attendance</th><th>Gender Ratio</th><th>Rank</th><th>Average Scholarship</th></tr></thead>"
	for (var i in data){
        cr = "<tr>";

		for (var j in data[i]){
            cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">"+data[i][j]+"</td>";
		}

		cr = cr + "</tr>\n";
		result = result + cr;
    }
    var final = d + result

	$("#college").html(final);

}
function generateQuery(data, title){
    var result = "";
	for (var i in data){
        cr = "<tr>";

		for (var j in data[i]){
            cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\">"+data[i][j]+"</td>";
		}

		cr = cr + "</tr>\n";
		result = result + cr;
    }
    
    $("#college").html(result);
    $("#title").html(title);

}
$(document).ready(function(){
    $.get("/",'index.html')
    $.get("/init",{},function(response){
        var data = JSON.parse(response);
        createGrid(data);
    });
    $("#btn1").click(function(){
        $.get("/q1",{},function(response){
            var data = JSON.parse(response)
            title = "Inserting college information to college info"
            generateQuery(data,title);
        });
    });
    $("#btn2").click(function(){
        $.get("/q2",{},function(response){
            var data = JSON.parse(response)
            title = "Getting scholarship name and amt for UC Merced"
            generateQuery(data,title);
        });
    });
    $("#btn3").click(function(){
        $.get("/q3",{},function(response){
            var data = JSON.parse(response)
            title = "Get number of incoming students in UC Merced"
            generateQuery(data,title);
        });
    });
    $("#btn4").click(function(){
        $.get("/q4",{},function(response){
            var data = JSON.parse(response)
            title = "Which city has the most expensive rent"
            generateQuery(data,title);
        });
    });
    $("#btn5").click(function(){
        $.get("/q5",{},function(response){
            var data = JSON.parse(response)
            title = "What college has the highest attendance"
            generateQuery(data,title);
        });
    });
    $("#btn6").click(function(){
        $.get("/q6",{},function(response){
            var data = JSON.parse(response)
            title = "Find grants for Engineering schools"
            generateQuery(data,title);
        });
    });
    $("#btn7").click(function(){
        $.get("/q7",{},function(response){
            var data = JSON.parse(response)
            title = "Find the highest scholarship in terms of money"
            generateQuery(data,title);
        });
    });
    $("#btn8").click(function(){
        $.get("/q8",{},function(response){
            var data = JSON.parse(response)
            title = "Average GPA of top 3 universities"
            generateQuery(data,title);
        });
    });
    $("#btn9").click(function(){
        $.get("/q9",{},function(response){
            var data = JSON.parse(response)
            title = "Number of majors offered by each university"
            generateQuery(data,title);
        });
    });
    $("#btn10").click(function(){
        $.get("/q10",{},function(response){
            var data = JSON.parse(response)
            title = "Find how many different types of scholarships are offered in the U.S"
            generateQuery(data,title);
        });
    });
    $("#btn11").click(function(){
        $.get("/q11",{},function(response){
            var data = JSON.parse(response)
            title = "Find all the transfer students with gpa greater than 3.0 and engineering major"
            generateQuery(data,title);
        });
    });
    $("#btn12").click(function(){
        $.get("/q12",{},function(response){
            var data = JSON.parse(response)
            title = "Delete tuples in scholarships less than 1000"
            generateQuery(data,title);
        });
    });
    $("#btn13").click(function(){
        $.get("/q13",{},function(response){
            var data = JSON.parse(response)
            title = "increase california rents by 10%"
            generateQuery(data,title);
        });
    });
    $("#btn14").click(function(){
        $.get("/q14",{},function(response){
            var data = JSON.parse(response)
            title = "insert new scholarship"
            generateQuery(data,title);
        });
    });
    $("#btn15").click(function(){
        $.get("/q15",{},function(response){
            var data = JSON.parse(response)
            title = "find all the female incoming and transfer students"
            generateQuery(data,title);
        });
    });
    $("#btn16").click(function(){
        $.get("/q16",{},function(response){
            var data = JSON.parse(response)
            title = "select colleges outside of california"
            generateQuery(data,title);
        });
    });
    $("#btn17").click(function(){
        $.get("/q17",{},function(response){
            var data = JSON.parse(response)
            title = "how many students does each major has?"
            generateQuery(data,title);
        });
    });
    $("#btn18").click(function(){
        $.get("/q18",{},function(response){
            var data = JSON.parse(response)
            title = "delete  incoming students if they enrolled in 2019"
            generateQuery(data,title);
        });
    });
    $("#btn19").click(function(){
        $.get("/q19",{},function(response){
            var data = JSON.parse(response)
            title = "find BS majors"
            generateQuery(data,title);
        });
    });
    $("#btn20").click(function(){
        $.get("/q20",{},function(response){
            var data = JSON.parse(response)
            title = "find all colleges with gender ratio higher than 0.6 and all offered majors gender ratio above 0.6"
            generateQuery(data,title);
        });
    });
});