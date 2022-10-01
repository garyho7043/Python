import os 
import time 
import ntplib

#programmingtime1=time.process_time () 
#print('programmingtime1:',programmingtime1)

#perf_countertime1=time.perf_counter () 
#print('perf_countertime1:',perf_countertime1)

systemtime1=time.time()
print('systemtime1:',systemtime1)
#############################################################

c = ntplib.NTPClient() 
response = c.request('time.stdtime.gov.tw')
ts = response.tx_time 


#programmingtime2=time.process_time () 
#print('programmingtime2:',programmingtime2)
#elapsed1 = programmingtime2 - programmingtime1
#print('Process_Time_delta1：', elapsed1, 'seconds\n\n')

#perf_countertime2=time.perf_counter () 
#print('perf_countertime2:',perf_countertime2)
#elapsed1 = perf_countertime2 - perf_countertime1
#print('perf_countertime_delta1：', elapsed1, 'seconds\n\n')

systemtime2=time.time()
print('systemtime2:',systemtime2)
elapsed1 = systemtime2 - systemtime1
print('systemtime_delta1：', elapsed1, 'seconds\n\n')








timeString = time.strftime("%Y/%m/%d %H:%M",time.localtime(ts)) 
timeString = time.strftime("%Y/%m/%d %H:%M",time.localtime(response.tx_timestamp)) 
_date = time.strftime('%Y-%m-%d',time.localtime(ts)) 
_time = time.strftime('%X',time.localtime(ts)) 
os.system('date {} && time {}'.format(_date,_time)) 

############################################################


#programmingtime3=time.process_time () 
#print('programmingtime3:',programmingtime3)
#elapsed2 = programmingtime3 - programmingtime1
#print('Process_Time_delta2：', elapsed2, 'seconds\n\n')

#perf_countertime3=time.perf_counter () 
#print('perf_countertime3:',perf_countertime3)
#elapsed2 = perf_countertime3 - perf_countertime1
#print('perf_countertime_delta2：', elapsed2, 'seconds\n\n')

systemtime3=time.time()
print('systemtime2:',systemtime2)
elapsed3 = systemtime3 - systemtime1
print('systemtime_delta3：', elapsed3, 'seconds\n\n')

