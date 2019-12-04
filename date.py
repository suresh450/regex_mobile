
import time
import datetime
ticks=time.time()
localtime=time.localtime()


current_datetime=datetime.datetime.now()
print(current_datetime)
current_datetime="2019-11-29 05:44:17.479806"
(current_date, current_time) = current_datetime.split(' ')
yy, mm, dd = current_date.split('-')
print (int(yy), int(mm), int(dd))
((hh), minu, sec) = current_time.split(':')
sec, msec = sec.split('.')
current=datetime.datetime(int(yy),int(mm),int(dd),int(hh),int(minu),int(sec))
print(current.day)



str_datetime =  "2016-12-29T10:30:07.119045211Z"
(new_date, new_time) = str_datetime.split('T')
yy, mm, dd = new_date.split('-')
(int(yy), int(mm), int(dd))
(hh, minu, sec) = new_time.split(':')
sec, msec = sec.split('.')
msec = msec.rstrip('Z')
(int(hh), int(minu), int(sec), int(msec))
start=datetime.datetime(int(yy),int(mm),int(dd),int(hh),int(minu),int(sec))
print(start)
print(current-start)

