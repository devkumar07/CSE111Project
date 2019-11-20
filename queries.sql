1) Inserting college information to college info:

insert into College_info (c_id,c_name, c_citykey, c_type, c_attendance, c_genderRatio, c_rankNation, c_avgscholarship)
values (6,'UC San Diego', 6, 'public', 4687, 0.60, 3, 2876)

2) Getting scholarship name and amt for UC Merced:

select s_name, s_amt
from scholarships, College_info, major
where s_collegeID = c_id
and c_id = m_cid
and c_name like 'UC Merced'

3)  How many incoming students are in UC Merced

select count(*)
from (select * from Incoming_acceptances,College_info where i_cid = c_id and c_name like 'uc merced')

4)  What city has the most expensive rent?
select ci_name, max(ci_rent)
from city

5) Which college has the most number of current students?

select c_name
from(select c_id as college, Max(att)
from(select M1.c_id, count(*) as att
from(select i_id, c_id
from incoming_acceptances, college_info
where i_cid = c_id
union all
select t_id, c_id
from transfer_acceptances,college_info
where t_cid = c_id)M1
group by M1.c_id))M2, college_info
where college = c_id

6) What scholarships provide grant to school of Engineering department?

select count(*)
from scholarships
where s_dep like 'School of Engineering%_' or s_dep like 'School of Engineering'

7) Which private university offers the highest average scholarship?

select c_name, Max(c_avgscholarship)
from (select c_name, c_avgscholarship
from college_info
where c_type = 'Private')

8) What is the average incoming students gpa for the top 3 universities in the U.S?

select avg(i_gpa)
from incoming_acceptances, college_info
where i_cid = c_id
and c_rankNation <= 3

9) How many different majors does each university in the U.S offer?

select c_name, count(*)
from major, college_info
where c_id = m_cid
group by m_cid

10) Find how many different types of scholarships are offered in the U.S

select s_type, count(*)
from scholarships
group by s_type


11) Find all the transfer students with gpa greater than 3.0 and engineering major
SELECT t_id
FROM transfer_Acceptances, major
WHERE t_gpa > 3.0
AND m_id = t_mid
AND m_cid = t_cid
AND m_department LIKE 'School of Engineering';

12) Delete tuples in scholarships less than 1000
DELETE FROM scholarships
WHERE s_amt < 1000;


13) increase california rents by 10%
UPDATE city
SET ci_rent = ci_rent * 1.1
WHERE ci_state LIKE 'CA';

14) insert new scholarship
INSERT into scholarships values(‘bobcat grant’, ‘School of Engineering; School of Social Sciences, Humanities and Arts; School of Natural Science’, 6, ‘Financial Aid’, 1000, 2019-10-01, 2);

15) find all the female incoming and transfer students
SELECT t_id student, 'transfer' type
FROM transfer_Acceptances
WHERE t_gender LIKE 'female'

UNION

SELECT i_id student, 'incoming' type
FROM incoming_acceptances
WHERE i_gender LIKE 'female';


16) select colleges outside of california
SELECT c_id
FROM College_info, city
WHERE c_citykey = ci_key
AND ci_state <> 'CA';


17) how many students does each major has?
SELECT A.m_name, count1 + count2 count
FROM (SELECT m_name, count(*) count1
FROM incoming_acceptances, major
WHERE m_id = i_majorid
        AND m_cid = i_cid
GROUP BY m_name)A,

(SELECT m_name, count(*) count2
FROM transfer_Acceptances, major
WHERE m_id = t_mid
        AND m_cid = t_cid
GROUP BY m_name) B
WHERE A.m_name = B.m_name;

18) delete  incoming students if they enrolled in 2019
DELETE FROM incoming_acceptances WHERE i_year LIKE ‘%2019%’;

19) find BS majors
SELECT m_name
FROM major
WHERE m_degreetype LIKE ‘Bachelor of Science’;

20) find all colleges with gender ratio higher than 0.6 and all offered major’s gender ratio above 0.6
SELECT distinct c_id
FROM College_info, major
WHERE c_genderRatio > 0.6
	AND c_id = m_cid
	AND m_genderRatio > 0.6;