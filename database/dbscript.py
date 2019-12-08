import os
import sqlite3   ## Include SQLite package 



################ Connect SQLite Database ################
db_connection = None # Define the connection parameter
db_name = "CollegeDB.db"	# Specify the full path of Database file

try:
	db_connection = sqlite3.connect(db_name)	# This line of code will try to 
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

def highgpa_Engr():
    # Find all the transfer students with gpa greater than 3.0 and engineering major
 
    query_11 = "SELECT t_id \
           FROM transfer_Acceptances, major \
           WHERE t_gpa > 3.0 \
           AND m_id = t_mid \
           AND m_cid = t_cid \
           AND m_department LIKE 'School of Engineering';"
    return query_11

def delete_lowScholarships():
    # Delete tuples in scholarships less than 1000
 
    query_12 = "DELETE FROM scholarships \
           WHERE s_amt < 1000;"
    return query_12

def increase_rentCA():
    # increase california rents by 10%
 
    query_13 = "UPDATE city \
           SET ci_rent = ci_rent * 1.1 \
           WHERE ci_state LIKE 'CA';"
    return query_13

def insert_newScholarship():
    # insert new scholarship
 
    query_14 = "INSERT into scholarships \
           values('bobcat grant', 'School of Engineering; School of Social Sciences, Humanities and Arts; School of Natural Science', 6, 'Financial Aid', 1000, 2019-10-01, 2);"
    return query_14


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
    return query_15

def Colleges_out_CA():
     # select colleges outside of california
 
    query_16 = "SELECT c_id \
           FROM College_info, city \
           WHERE c_citykey = ci_key \
           AND ci_state <> 'CA';"
    return query_16

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
    return query_17

def delete_students_2019():
     #  delete  incoming students if they enrolled in 2019
 
    query_18 = "DELETE FROM incoming_acceptances WHERE i_year LIKE '%2019%';"
    return query_18

def bs_majors():
    # find BS majors
 
    query_19 = "SELECT m_name \
           FROM major \
           WHERE m_degreetype LIKE 'Bachelor of Science';"
    return query_19

def high_genderRatio():
    # find all colleges with gender ratio higher than 0.6 and all offered majors gender ratio above 0.6
    query_20 = "SELECT distinct c_id FROM College_info, major WHERE c_genderRatio > 0.6 AND c_id = m_cid AND m_genderRatio > 0.6;"
    return query_20


################ Running query in sqlite ###############
 












query = high_genderRatio() # Can be replaced by select_query

db_cursor = db_connection.cursor() # Creating a cursor from db_connection

db_cursor.execute(query)	# Running the query

db_connection.commit()

result = db_cursor.fetchall() # Get results from connection object to a data-structure
print("Returned data-structure is a : ",type(result))

print("#################### Query result ####################")
for row in result:
	print(row)

