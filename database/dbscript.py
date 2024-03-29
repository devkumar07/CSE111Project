import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "CollegeDB.db")
import sqlite3   ## Include SQLite package 



################ Connect SQLite Database ################
db_connection = None # Define the connection parameter
db_name = "CollegeDB.db"	# Specify the full path of Database file

try:
	db_connection = sqlite3.connect(db_path, check_same_thread=False)   	# This line of code will try to 
												# connect sqlite database with 
												# python and assign a cursor to 
												# connection parameter specified 
												# in left hand side
except sqlite3.Error as err: # If database connection failed this block of code 
							 # handles the exception
	print(err)

if db_connection:
	print(db_connection) # Printing the connection object
	print("Successfully Established connection with SQLite3")
	print("\n\n")

def get_main_table():
    q = "select * from college_info"
    result = get_query_result(q)
    return result


# Inserting college information to college info
def insert_college_info():
    query_1 = "insert into College_info (c_id,c_name, c_citykey, c_type, c_attendance, c_genderRatio, c_rankNation, c_avgscholarship) \
            values (6,'UC San Diego', 6, 'public', 4687, 0.60, 3, 2876)"
    result = get_query_result(query_1)
    return result


# Getting scholarship name and amt for UC Merced
def get_scholarship_merced():
    query_2 = "select s_name, s_amt \
           from scholarships, College_info, major \
           where s_collegeID = c_id \
           and c_id = m_cid \
           and c_name like 'UC Merced'"
    result = get_query_result(query_2)
    return result


# How many incoming students are in UC Merced
def get_incoming_students_merced():
    query_3 = "select count(*) \
           from ( \
               select * from Incoming_acceptances,College_info \
               where i_cid = c_id and c_name like 'uc merced')"
    result =  get_query_result(query_3)
    return result

def get_most_expensive_cityRent():
    query_4 = "select ci_name, max(ci_rent) \
           from city"
    result = get_query_result(query_4)
    return result


# Which college has the most number of current students?
def get_highest_attendance():
    query_5 = "select c_name, m\
           from(select c_id as college, Max(att) as m\
           from(select M1.c_id, count(*) as att \
           from(select i_id, c_id \
           from incoming_acceptances, college_info \
           where i_cid = c_id \
           union all \
           select t_id, c_id \
           from transfer_acceptances,college_info \
           where t_cid = c_id)M1 \
           group by M1.c_id))M2, college_info \
           where college = c_id"
    result = get_query_result(query_5)
    return result


# What scholarships provide grant to school of Engineering department?
def get_grants_SOE():
    query_6 = "select s_name \
           from scholarships \
           where s_dep like 'School of Engineering%_' or s_dep like 'School of Engineering'"
    result = get_query_result(query_6)
    return result


# Which private university offers the highest average scholarship?
def get_highest_scholarship():
    query_7 = "select c_name, Max(c_avgscholarship) \
           from (select c_name, c_avgscholarship \
           from college_info \
           where c_type = 'Private')"
    result = get_query_result(query_7)
    return result


def find_avgGPA_top_3():
    query_8 = "select c_name, avg(i_gpa) \
           from incoming_acceptances, college_info \
           where i_cid = c_id \
           and c_rankNation <= 3 group by c_name"
    result = get_query_result(query_8)
    return result

def display_majors_university():
    query_9 = "select c_name, count(*) \
           from major, college_info \
           where c_id = m_cid \
           group by m_cid"
    result = get_query_result(query_9)
    return result

# Find how many different types of scholarships are offered in the U.S
def find_distinct_scholarships():
    query_10 = "select s_type, count(*) \
           from scholarships \
           group by s_type"
    result = get_query_result(query_10)
    return result
 
def highgpa_Engr():
    # Find all the transfer students with gpa greater than 3.0 and engineering major
 
    query_11 = "SELECT t_id \
           FROM transfer_Acceptances, major \
           WHERE t_gpa > 3.0 \
           AND m_id = t_mid \
           AND m_cid = t_cid \
           AND m_department LIKE 'School of Engineering';"
    result = get_query_result(query_11)
    return result

def delete_lowScholarships():
    # Delete tuples in scholarships less than 1000
 
    query_12 = "DELETE FROM scholarships \
           WHERE s_amt < 1000;"
    result = get_query_result(query_12)
    return result

def increase_rentCA():
    # increase california rents by 10%
 
    query_13 = "UPDATE city \
           SET ci_rent = ci_rent * 1.1 \
           WHERE ci_state LIKE 'CA';"
    result = get_query_result(query_13)
    return result

def insert_newScholarship():
    # insert new scholarship
 
    query_14 = "INSERT into scholarships \
           values('bobcat grant', 'School of Engineering; School of Social Sciences, Humanities and Arts; School of Natural Science', 6, 'Financial Aid', 1000, 2019-10-01, 2);"
    result = get_query_result(query_14)
    return result


def find_femaleStudents():
     # find all the female incoming and transfer students
 
    query_15 = "SELECT t_id student, 'transfer' type \
           FROM transfer_Acceptances \
           WHERE t_gender LIKE 'female' \
           \
           UNION \
           \
           SELECT i_id student, 'incoming' type \
           FROM incoming_acceptances \
           WHERE i_gender LIKE 'female';"
    result = get_query_result(query_15)
    return result

def Colleges_out_CA():
     # select colleges outside of california
 
    query_16 = "SELECT c_name \
           FROM College_info, city \
           WHERE c_citykey = ci_key \
           AND ci_state <> 'CA';"
    result = get_query_result(query_16)
    return result

def count_per_major():
     # how many students does each major has?
 
    query_17 = "SELECT A.m_name, count1 + count2 count \
           FROM (SELECT m_name, count(*) count1 \
           FROM incoming_acceptances, major \
           WHERE m_id = i_majorid \
               AND m_cid = i_cid \
           GROUP BY m_name)A, \
           \
           (SELECT m_name, count(*) count2 \
           FROM transfer_Acceptances, major \
           WHERE m_id = t_mid \
               AND m_cid = t_cid \
           GROUP BY m_name) B \
           WHERE A.m_name = B.m_name;"
    result = get_query_result(query_17)
    return result

def delete_students_2019():
     #  delete  incoming students if they enrolled in 2019
 
    query_18 = "DELETE FROM incoming_acceptances WHERE i_year LIKE '%2019%';"
    result = get_query_result(query_18)
    return result

def bs_majors():
    # find BS majors
 
    query_19 = "SELECT m_name \
           FROM major \
           WHERE m_degreetype LIKE 'Bachelor of Science';"
    result = get_query_result(query_19)
    return result

def high_genderRatio():
    # find all colleges with gender ratio higher than 0.6 and all offered majors gender ratio above 0.6
    query_20 = "SELECT distinct c_name, c_genderRatio FROM College_info, major WHERE c_genderRatio > 0.6 AND c_id = m_cid AND m_genderRatio > 0.6;"
    result = get_query_result(query_20)
    return result

def get_query_result(query1):

    query = query1 # Can be replaced by select_query

    db_cursor = db_connection.cursor() # Creating a cursor from db_connection

    db_cursor.execute(query)	# Running the query

    db_connection.commit()

    result = db_cursor.fetchall() # Get results from connection object to a data-structure

    print("Returned data-structure is a : ",type(result))

    print("#################### Query result ####################")
    for row in result:
        print(row)
    return result

    

