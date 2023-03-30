from datetime import datetime
now = datetime.now()
print(now) 
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                
minute = now.minute             
second = now.second
timestamp = now.timestamp()

print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time:", t)

# 3. Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4. Calculate the time difference between now and new year.
from datetime import date
today = date(year=2023, month=3, day=29)
new_year = date(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)


# 5. Calculate the time difference between 1 January 1970 and now.
t1 = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
print(t1)
t2 = datetime(year = 2023, month = 3, day = 29, hour = 0, minute = 0, second = 0)
print(t2)
diff = t2 - t1
print('Diferencia entre 1 de enero de 1970 y hoy:', diff) 

# 6. Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# calcular horas trabajadas
# organizar facturas por fecha
# calcular eficiencia de programas (tiempo de ejecución)
# hacer cronogramas para trenes o autobuses
# armar agendas
# diagramas de Gantt 

