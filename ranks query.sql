Create table new_ranks as(
	Select stunum, gpa, pgmdesc, 
rank() over (partition by pgmdesc, class order by gpa desc) as class_rank, 
advisors_by_class.class as class, 
percent_rank() over (partition by pgmdesc, class order by gpa) as percent_rank
from ranks
inner join advisors_by_class on advisors_by_class.studentid = ranks.stunum
)
	