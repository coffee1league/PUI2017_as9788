
#!/data/data/com.termux/files/usr/bin/python2.7

import sys
import json
import urllib2

def main ():
	count=0
	KEY=sys.argv[1]
	BUS=sys.argv[2]
	
	count2=0
	url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+KEY+"&VehicleMonitoringDetailLevel=calls&LineRef="+BUS
	response=urllib2.urlopen(url)
	

	book=json.load(response)
#	print book
	#printing the header
	print "Latitude, Longitude, Stop Name, Stop Status"

#	print "The bus is :" +BUS

	for i in book['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
#		print i['MonitoredVehicleJourney']['VehicleLocation']
		count=count+1
#		print count
	print "The total nuber of busses is : "  +str(count)
	
	for j in book['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
		count2=count2+1		
		print ""+ str(j['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) +"," + str(j['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])+","  + str(['StopPointName'])

# f=open("/data/data/com.termux/files/home/PUI2017/HW2_as9788/b52_out.txt","r")

# s=f.read()

if __name__=="__main__":
	main()
