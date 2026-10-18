#7.2 Problem 2: Work hours and overtime payment

hours_worked = float (input("Type your total worked hours in the week: "))
hourly_rate = float (input("Type your hourly wage: "))
overtime = False 

#delimitando las horas
regular_hours = min(hours_worked, 40)
overtime_hours = max(0, hours_worked - 40)


if hours_worked< 0 or hourly_rate <= 0:
    print ("Error: invalid input")
	#pagando 
else:
	wage = hourly_rate * regular_hours
	extra_wage = overtime_hours*1.5 *hourly_rate
	if hours_worked > 40:
		overtime = True 
		
	print (f"Regular pay: {wage}")
	print (f"Overtime pay: {extra_wage}")
	print (f"Total pay: {extra_wage+wage}")
	print (f"Has overtime: {overtime}")
