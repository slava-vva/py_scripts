select COUNT(Attrition), avg(cast(DailyRate as float)), avg(HourlyRate) from [dbo].[Employee-Attrition]
group by Attrition

select avg(cast(DailyRate as float)) from [dbo].[Employee-Attrition]
where Attrition = 0
group by Department

select Age, count(*) from [dbo].[Employee-Attrition]
where BusinessTravel = 'Travel_Frequently'
group by BusinessTravel, Age

select t.group_age, count(*) cnt from (
select case when Age < 25 then 'yang' 
when Age >= 25 and Age <=45 then 'middle'
when Age > 45 then 'old' end [group_age] from [dbo].[Employee-Attrition]	 
where Businesstravel = 'Travel_Frequently'
) as t
group by group_age


select EducationField, count(*) from [dbo].[Employee-Attrition]
group by EducationField

select top 100 * from [dbo].[Employee-Attrition]
