##creating class ranks and class percentile ranks for Pharm.D students 
Create table ranks as(

select directory.stunum, 
directory.studentname,
spring_grades_2020.gpa,
spring_grades_2020.pgmdesc,
directory.graddate,
rank() over (partition by directory.graddate, spring_grades_2020.pgmdesc order by gpa desc) as class_rank,
percent_rank() over (partition by directory.graddate, spring_grades_2020.pgmdesc order by gpa) as percentile_rank
from directory 
join spring_grades_2020 on spring_grades_2020.stunum = directory.stunum
where directory.graddate = '6/26/2022' or directory.graddate ='6/27/2021' 
and spring_grades_2020.pgmdesc = 'Doctor of Pharmacy')
