import os
import time
import ntplib_modified
import statistics



ntp_server_list = ['time.stdtime.gov.tw']
"""
ntp_server_list = [
  'time.google.com',
  'time.windows.com',
  'time.stdtime.gov.tw',
]
"""
	
offset_stats = []
RTD_stats = []
request_OWD_stats = []
response_OWD_stats = []
	

	
ntp_client_session = ntplib_modified.NTPClient()
	
for i in range(1,51):
  for server_address in ntp_server_list:
      response = ntp_client_session.request(server_address,version=4)
      offset_stats.append(response.offset)
      RTD_stats.append(response.round_trip_delay)
      request_OWD_stats.append(response.request_one_way_delay)
      response_OWD_stats.append(response.response_one_way_delay)


""" Statistics """
# Average
offset_avg = statistics.mean(offset_stats)
RTD_avg = statistics.mean(RTD_stats)
request_OWD_avg = statistics.mean(request_OWD_stats)
response_OWD_avg = statistics.mean(response_OWD_stats)
	



NTPClient_object=ntplib_modified.NTPClient()
response=NTPClient_object.request('time.stdtime.gov.tw')
ts=response.tx_time
destime=ts+RTD_avg*0.5
clock_ID = time.CLOCK_REALTIME
time.clock_settime(clock_ID,destime)




