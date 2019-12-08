import os
import sqlite3   ## Include SQLite package 



################ Connect SQLite Database ################
db_connection = None # Define the connection parameter
db_name = "CollegeDB.db"	# Specify the full path of Database file

try:
	db_connection = sqlite3.connect(db_name)   	# This line of code will try to 
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

# Inserting college information to college info
def insert_college_info():
    query_1 = "insert into College_info (c_id,c_name, c_citykey, c_type, c_attendance, c_genderRatio, c_rankNation, c_avgscholarship) \
            values (6,'UC San Diego', 6, 'public', 4687, 0.60, 3, 2876)"
    return query_1

# Getting scholarship name and amt for UC Merced
def get_scholarship_merced():
    query_2 = "select s_name, s_amt \
           from scholarships, College_info, major \
           where s_collegeID = c_id \
           and c_id = m_cid \
           and c_name like 'UC Merced'"
    return query_2

# How many incoming students are in UC Merced
def get_incoming_students_merced():
    query_3 = "select count(*) \
           from ( \
               select * from Incoming_acceptances,College_info \
               where i_cid = c_id and c_name like 'uc merced')"
    return query_3

def get_most_expensive_cityRent():
    query_4 = "select ci_name, max(ci_rent) \
           from city"
    return query_4

# Which college has the most number of current students?
def get_highest_attendance():
    query_5 = "select c_name \
           from(select c_id as college, Max(att) \
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
    return query_5

# What scholarships provide grant to school of Engineering department?
def get_grants_SOE():
    query_6 = "select count(*) \
           from scholarships \
           where s_dep like 'School of Engineering%_' or s_dep like 'School of Engineering'"
    return query_6

# Which private university offers the highest average scholarship?
def get_highest_scholarship():
    query_7 = "select c_name, Max(c_avgscholarship) \
           from (select c_name, c_avgscholarship \
           from college_info \
           where c_type = 'Private')"
    return query_7

def find_avgGPA_top_3():
    query_8 = "select avg(i_gpa) \
           from incoming_acceptances, college_info \
           where i_cid = c_id \
           and c_rankNation <= 3"
    return query_8

def display_majors_university():
    query_9 = "select c_name, count(*) \
           from major, college_info \
           where c_id = m_cid \
           group by m_cid"
    return query_9

# Find how many different types of scholarships are offered in the U.S
def find_distinct_scholarships():
    query_10 = "select s_type, count(*) \
           from scholarships \
           group by s_type"
    return query_10

query = find_distinct_scholarships() # Can be replaced by select_query

db_cursor = db_connection.cursor() # Creating a cursor from db_connection

db_cursor.execute(query)	# Running the query

db_connection.commit()

result = db_cursor.fetchall() # Get results from connection object to a data-structure
print("Returned data-structure is a : ",type(result))

print("#################### Query result ####################")
for row in result:
	print(row)

