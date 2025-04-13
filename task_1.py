stroka = '1h 45m,360s,25m,30m 120s,2h 60s'
stroka = stroka.replace(' ',',')
list_time = stroka.split(',')
all_minuts = 0

for i in range(0,len(list_time)):
    if 'h' in list_time[i]:
        all_minuts += int(list_time[i].replace('h',''))*60
    if 's' in list_time[i]:
        all_minuts += int(list_time[i].replace('s',''))/60  
    if 'm' in list_time[i]:
        all_minuts += int(list_time[i].replace('m',''))

print('Общее количество минут = ',all_minuts)