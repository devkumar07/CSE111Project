from database.dbscript import *
import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/init')
def init():
    print("Test")
    output = json.dumps(get_main_table())
    return output


@app.route('/q1')
def q1():
    output = json.dumps(insert_college_info())
    return output

@app.route('/q2')
def q2():
    output = json.dumps(get_scholarship_merced())
    return output

@app.route('/q3')
def q3():
    output = json.dumps(get_incoming_students_merced())
    return output

@app.route('/q4')
def q4():
    output = json.dumps(get_most_expensive_cityRent())
    return output

@app.route('/q5')
def q5():
    output = json.dumps(get_highest_attendance())
    return output

@app.route('/q6')
def q6():
    output = json.dumps(get_grants_SOE())
    return output

@app.route('/q7')
def q7():
    output = json.dumps(get_highest_scholarship())
    return output

@app.route('/q8')
def q8():
    output = json.dumps(find_avgGPA_top_3())
    return output

@app.route('/q9')
def q9():
    output = json.dumps(display_majors_university())
    return output

@app.route('/q10')
def q10():
    output = json.dumps(find_distinct_scholarships())
    return output

@app.route('/q11')
def q11():
    output = json.dumps(highgpa_Engr())
    return output

@app.route('/q12')
def q12():
    output = json.dumps(delete_lowScholarships())
    return output

@app.route('/q13')
def q13():
    output = json.dumps(increase_rentCA())
    return output

@app.route('/q14')
def q14():
    output = json.dumps(insert_newScholarship())
    return output

@app.route('/q15')
def q15():
    output = json.dumps(find_femaleStudents())
    return output

@app.route('/q16')
def q16():
    output = json.dumps(Colleges_out_CA())
    return output

@app.route('/q17')
def q17():
    output = json.dumps(count_per_major())
    return output

@app.route('/q18')
def q18():
    output = json.dumps(delete_students_2019())
    return output

@app.route('/q19')
def q19():
    output = json.dumps(bs_majors())
    return output

@app.route('/q20')
def q20():
    output = json.dumps(high_genderRatio())
    return output

if __name__ == '__main__':
    app.run(debug=False, threaded=True, host= '0.0.0.0')