from ai import cdas
from datetime import datetime
from datetime import timedelta
import json
import os
import numpy as np

Data = open("/pathtoFile/File1.dat", 'w')
Data_Plasma = open("/pathtoFile/File2.dat", 'w')
Data_Velocity = open("/pathtoFile/File3.dat", 'w')
Data_Density = open("/pathtoFile/File4.dat", 'w')


#Downloading the Wind s/c plasma data of ICME sheaths listed by Palmerio et al. (2016) 
day = 1
while day != 92:
	Ehto = 0
	print day
 	if day == 1:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1997,1,10,00,47), datetime(1997,1,10,5,3), ['BF1','BGSE'])
			Ehto = 1
		except:
			Ehto = 0
			print "skip"
			day = day + 1
	if day == 2:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1997,2,9,12,46), datetime(1997,2,10,2,49), ['BF1','BGSE']) 
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 3:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1997,5,15,1,10), datetime(1997,5,15,9,57), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 4:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1997,11,6,22,14), datetime(1997,11,7,5,33), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
	
	if day == 5:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1997,11,22,9,8), datetime(1997,11,22,18,57), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 6:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,1,6,13,24), datetime(1998,1,7,2,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 7:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,1,28,15,49), datetime(1998,1,29,20,17), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 8:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,5,1,21,16), datetime(1998,5,2,9,17), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 9:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,8,19,18,35), datetime(1998,8,20,9,5), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 10:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,9,24,23,14), datetime(1998,9,25,6,33), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 11:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1998,10,18,19,24), datetime(1998,10,19,4,27), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 12:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1999,2,18,2,42), datetime(1999,2,18,10,33), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 13:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1999,3,10,1,28), datetime(1999,3,10,18,59), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 14:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(1999,4,16,11,7), datetime(1999,4,16,15,40), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 15:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,2,11,23,29), datetime(2000,2,12,12,27), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 16:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,2,14,7,8), datetime(2000,2,14,17,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 17:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,2,20,20,59), datetime(2000,2,21,5,32), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 18:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,8,11,18,45), datetime(2000,8,12,5,37), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 19:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,9,4,13,10), datetime(2000,9,4,21,57), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 20:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,9,17,16,44), datetime(2000,9,17,23,5), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 21:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,10,3,00,57), datetime(2000,10,3,17,5), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 22:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,10,12,22,28), datetime(2000,10,13,5,57), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 23:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,11,6,9,25), datetime(2000,11,6,22,32), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 24:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2000,11,10,6,14), datetime(2000,11,10,11,51), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 25:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,1,23,10,43), datetime(2001,1,24,00,45), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 26:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,1,31,8,29), datetime(2001,2,1,2,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 27:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,3,19,11,29), datetime(2001,3,19,18,6), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 28:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,3,27,18,3), datetime(2001,3,27,23,7), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 29:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,4,4,14,36), datetime(2001,4,4,18,10), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 30:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,4,11,14,3), datetime(2001,4,11,22,50), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 31:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,4,18,00,45), datetime(2001,4,18,12,19), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 32:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,4,21,15,23), datetime(2001,4,22,00,13), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 33:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,4,28,5,00), datetime(2001,4,28,16,25), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 34:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,5,27,14,40), datetime(2001,5,28,4,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 35:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,8,17,10,56), datetime(2001,8,17,21,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 36:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,8,27,19,33), datetime(2001,8,28,5,33), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 37:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,9,25,20,12), datetime(2001,9,26,10,17), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 38:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,9,29,9,25), datetime(2001,9,29,12,1), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 39:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,10,28,3,8), datetime(2001,10,29,5,53), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 40:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,10,31,13,40), datetime(2001,10,31,18,40), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 41:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2001,11,24,5,48), datetime(2001,11,24,14,5), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 42:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,2,28,5,1), datetime(2002,2,28,18,41), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 43:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,3,18,13,8), datetime(2002,3,19,6,17), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 44:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,3,23,11,19), datetime(2002,3,24,11,44), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 45:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,5,11,10,25), datetime(2002,5,11,16,21), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 46:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,5,18,19,41), datetime(2002,5,19,3,25), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 47:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,8,1,5,14), datetime(2002,8,1,12,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 48:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,8,18,18,36), datetime(2002,8,19,22,5), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 49:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,9,7,16,16), datetime(2002,9,8,4,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 50:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,9,30,7,49), datetime(2002,9,30,21,31), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 51:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,11,16,23,26), datetime(2002,11,17,7,25), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 52:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2002,11,26,21,40), datetime(2002,11,27,7,53), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 53:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2003,3,20,4,22), datetime(2003,3,20,8,50), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 54:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2003,5,29,18,25), datetime(2003,5,30,3,23), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 55:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,7,22,9,40), datetime(2004,7,22,13,6), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 56:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,7,24,5,25), datetime(2004,7,24,11,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 57:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,7,26,22,19), datetime(2004,7,27,1,45), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 58:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,8,29,9,3), datetime(2004,8,29,18,36), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 59:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,11,7,17,54), datetime(2004,11,7,22,44), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 60:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2004,11,9,18,30), datetime(2004,11,9,20,32), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 61:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,5,15,2,16), datetime(2005,5,15,5,37), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 62:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,6,12,6,52), datetime(2005,6,12,14,46), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 63:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,6,14,17,51), datetime(2005,6,15,5,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 64:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,7,10,2,37), datetime(2005,7,10,10,15), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 65:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,7,17,00,48), datetime(2005,7,17,15,22), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 66:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2005,9,2,13,45), datetime(2005,9,2,18,48), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 67:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2006,4,13,11,14), datetime(2006,4,13,15,30), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 68:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2006,12,8,3,56), datetime(2006,12,8,14,58), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 69:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2006,12,14,13,47), datetime(2006,12,14,22,32), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 70:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2007,11,19,17,17), datetime(2007,11,19,23,25), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 71:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2009,2,3,19,16), datetime(2009,2,4,2,18), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 72:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2009,12,12,4,33), datetime(2009,12,12,18,12), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 73:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2010,4,5,7,51), datetime(2010,4,5,12,11), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 74:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2010,5,28,1,48), datetime(2010,5,28,19,55), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 75:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2011,3,29,15,5), datetime(2011,3,30,00,26), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 76:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2011,9,17,2,52), datetime(2011,9,17,15,45), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 77:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2011,9,26,11,39), datetime(2011,9,26,19,47), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 78:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,4,23,2,10), datetime(2012,4,23,16,48), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 79:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,6,16,19,30), datetime(2012,6,16,22,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 80:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,7,14,17,34), datetime(2012,7,15,6,24), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 81:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,10,8,4,7), datetime(2012,10,8,17,20), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 82:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,10,11,22,42), datetime(2012,10,12,15,57), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 83:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,10,31,14,23), datetime(2012,10,31,23,39), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 84:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2012,11,23,20,46), datetime(2012,11,24,11,39), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
	
	if day == 85:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2013,3,17,5,17), datetime(2013,3,17,12,00), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 86:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2013,4,13,22,8), datetime(2013,4,14,16,45), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 87:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2013,7,12,16,38), datetime(2013,7,13,5,1), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 88:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2014,4,20,10,15), datetime(2014,4,21,7,30), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 89:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2014,8,19,5,42), datetime(2014,8,19,17,35), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 90:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2014,9,12,15,12), datetime(2014,9,12,21,40), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
			
	if day == 91:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H2_MFI', datetime(2015,3,17,3,55), datetime(2015,3,17,13,14), ['BF1','BGSE'])
			Ehto = 1     
		except:
			Ehto = 0
			print "skip"
			day = day + 1
					
	if Ehto == 1:					
		mask = np.abs(data_mfi['B']) < 1e3
		data_mfi['B'] = data_mfi['B'][mask]
		data_mfi['EPOCH'] = np.array(data_mfi['EPOCH'])[mask]
		data_mfi['BX_(GSE)'] = data_mfi['BX_(GSE)'][mask]
		data_mfi['BY_(GSE)'] = data_mfi['BY_(GSE)'][mask]
		data_mfi['BZ_(GSE)'] = data_mfi['BZ_(GSE)'][mask]

		TIME = data_mfi['EPOCH']
		B = data_mfi['B']
		B_x = data_mfi['BX_(GSE)']
		B_y = data_mfi['BY_(GSE)']
		B_z = data_mfi['BZ_(GSE)']	

		#The beginning and the length of a sheath
		TheBeginning = data_mfi['EPOCH'][0]
		TheLength = (data_mfi['EPOCH'][-1]-data_mfi['EPOCH'][0]).total_seconds()

		i = 0
		while i < np.shape(B)[0]:
			Data.write(str((TIME[i]-TIME[0]).total_seconds()))
			Data.write("	")
			Data.write(str(B[i]))
			Data.write("	")
			Data.write(str(B_x[i]))
			Data.write("	")
			Data.write(str(B_y[i]))
			Data.write("	")
			Data.write(str(B_z[i]))
			Data.write("	")
			Data.write("\n")
			i = i + 1
	
	if Ehto == 1:
	
		Ehto2 = 0
		if day == 1:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,1,10,00,47), datetime(1997,1,10,5,3), ['B3F1','B3GSE'])
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,1,10,00,47), datetime(1997,1,10,5,3),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,1,10,00,47), datetime(1997,1,10,5,3),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 2:
			try: 
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,2,9,12,46), datetime(1997,2,10,2,49), ['B3F1','B3GSE'])      
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,2,9,12,46), datetime(1997,2,10,2,49),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,2,9,12,46), datetime(1997,2,10,2,49),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 3:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,5,15,1,10), datetime(1997,5,15,9,57), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,5,15,1,10), datetime(1997,5,15,9,57),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,5,15,1,10), datetime(1997,5,15,9,57),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 4:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,11,6,22,14), datetime(1997,11,7,5,33), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,6,22,14), datetime(1997,11,7,5,33),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,6,22,14), datetime(1997,11,7,5,33),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 5:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,11,22,9,8), datetime(1997,11,22,18,57), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,22,9,8), datetime(1997,11,22,18,57),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,22,9,8), datetime(1997,11,22,18,57),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 6:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,1,6,13,24), datetime(1998,1,7,2,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,6,13,24), datetime(1998,1,7,2,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,6,13,24), datetime(1998,1,7,2,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 7:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,1,28,15,49), datetime(1998,1,29,20,17), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,28,15,49), datetime(1998,1,29,20,17),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,28,15,49), datetime(1998,1,29,20,17),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 8:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,5,1,21,16), datetime(1998,5,2,9,17), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,5,1,21,16), datetime(1998,5,2,9,17),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,5,1,21,16), datetime(1998,5,2,9,17),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 9:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,8,19,18,35), datetime(1998,8,20,9,5), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,8,19,18,35), datetime(1998,8,20,9,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,8,19,18,35), datetime(1998,8,20,9,5),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 10:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,9,24,23,14), datetime(1998,9,25,6,33), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,9,24,23,14), datetime(1998,9,25,6,33),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,9,24,23,14), datetime(1998,9,25,6,33),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 11:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,10,18,19,24), datetime(1998,10,19,4,27), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,10,18,19,24), datetime(1998,10,19,4,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,10,18,19,24), datetime(1998,10,19,4,27),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 12:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,2,18,2,42), datetime(1999,2,18,10,33), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,2,18,2,42), datetime(1999,2,18,10,33),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,2,18,2,42), datetime(1999,2,18,10,33),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 13:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,3,10,1,28), datetime(1999,3,10,18,59), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,3,10,1,28), datetime(1999,3,10,18,59),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,3,10,1,28), datetime(1999,3,10,18,59),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 14:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,4,16,11,7), datetime(1999,4,16,15,40), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,4,16,11,7), datetime(1999,4,16,15,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,4,16,11,7), datetime(1999,4,16,15,40),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 15:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,11,23,29), datetime(2000,2,12,12,27), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,11,23,29), datetime(2000,2,12,12,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,11,23,29), datetime(2000,2,12,12,27),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 16:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,14,7,8), datetime(2000,2,14,17,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,14,7,8), datetime(2000,2,14,17,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,14,7,8), datetime(2000,2,14,17,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 17:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,20,20,59), datetime(2000,2,21,5,32), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,20,20,59), datetime(2000,2,21,5,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,20,20,59), datetime(2000,2,21,5,32),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 18:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,8,11,18,45), datetime(2000,8,12,5,37), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,8,11,18,45), datetime(2000,8,12,5,37),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,8,11,18,45), datetime(2000,8,12,5,37),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 19:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,9,4,13,10), datetime(2000,9,4,21,57), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,4,13,10), datetime(2000,9,4,21,57),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,4,13,10), datetime(2000,9,4,21,57),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 20:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,9,17,16,44), datetime(2000,9,17,23,5), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,17,16,44), datetime(2000,9,17,23,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,17,16,44), datetime(2000,9,17,23,5),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 21:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,10,3,00,57), datetime(2000,10,3,17,5), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,3,00,57), datetime(2000,10,3,17,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,3,00,57), datetime(2000,10,3,17,5),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 22:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,10,12,22,28), datetime(2000,10,13,5,57), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,12,22,28), datetime(2000,10,13,5,57),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,12,22,28), datetime(2000,10,13,5,57),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 23:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,11,6,9,25), datetime(2000,11,6,22,32), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,6,9,25), datetime(2000,11,6,22,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,6,9,25), datetime(2000,11,6,22,32),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 24:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,11,10,6,14), datetime(2000,11,10,11,51), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,10,6,14), datetime(2000,11,10,11,51),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,10,6,14), datetime(2000,11,10,11,51),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 25:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,1,23,10,43), datetime(2001,1,24,00,45), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,23,10,43), datetime(2001,1,24,00,45),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,23,10,43), datetime(2001,1,24,00,45),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 26:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,1,31,8,29), datetime(2001,2,1,2,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,31,8,29), datetime(2001,2,1,2,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,31,8,29), datetime(2001,2,1,2,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 27:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,3,19,11,29), datetime(2001,3,19,18,6), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,19,11,29), datetime(2001,3,19,18,6),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,19,11,29), datetime(2001,3,19,18,6),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 28:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,3,27,18,3), datetime(2001,3,27,23,7), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,27,18,3), datetime(2001,3,27,23,7),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,27,18,3), datetime(2001,3,27,23,7),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 29:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,4,14,36), datetime(2001,4,4,18,10), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,4,14,36), datetime(2001,4,4,18,10),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,4,14,36), datetime(2001,4,4,18,10),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 30:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,11,14,3), datetime(2001,4,11,22,50), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,11,14,3), datetime(2001,4,11,22,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,11,14,3), datetime(2001,4,11,22,50),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 31:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,18,00,45), datetime(2001,4,18,12,19), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,18,00,45), datetime(2001,4,18,12,19),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,18,00,45), datetime(2001,4,18,12,19),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 32:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,21,15,23), datetime(2001,4,22,00,13), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,21,15,23), datetime(2001,4,22,00,13),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,21,15,23), datetime(2001,4,22,00,13),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 33:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,28,5,00), datetime(2001,4,28,16,25), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,28,5,00), datetime(2001,4,28,16,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,28,5,00), datetime(2001,4,28,16,25),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 34:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,5,27,14,40), datetime(2001,5,28,4,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,5,27,14,40), datetime(2001,5,28,4,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,5,27,14,40), datetime(2001,5,28,4,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 35:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,8,17,10,56), datetime(2001,8,17,21,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,17,10,56), datetime(2001,8,17,21,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,17,10,56), datetime(2001,8,17,21,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 36:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,8,27,19,33), datetime(2001,8,28,5,33), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,27,19,33), datetime(2001,8,28,5,33),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,27,19,33), datetime(2001,8,28,5,33),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 37:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,9,25,20,12), datetime(2001,9,26,10,17), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,25,20,12), datetime(2001,9,26,10,17),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,25,20,12), datetime(2001,9,26,10,17),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 38:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,9,29,9,25), datetime(2001,9,29,12,1), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,29,9,25), datetime(2001,9,29,12,1),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,29,9,25), datetime(2001,9,29,12,1),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 39:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,10,28,3,8), datetime(2001,10,29,5,53), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,28,3,8), datetime(2001,10,29,5,53),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,28,3,8), datetime(2001,10,29,5,53),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 40:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,10,31,13,40), datetime(2001,10,31,18,40), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,31,13,40), datetime(2001,10,31,18,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,31,13,40), datetime(2001,10,31,18,40),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 41:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,11,24,5,48), datetime(2001,11,24,14,5), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,11,24,5,48), datetime(2001,11,24,14,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,11,24,5,48), datetime(2001,11,24,14,5),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 42:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,2,28,5,1), datetime(2002,2,28,18,41), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,2,28,5,1), datetime(2002,2,28,18,41),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,2,28,5,1), datetime(2002,2,28,18,41),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 43:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,3,18,13,8), datetime(2002,3,19,6,17), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,18,13,8), datetime(2002,3,19,6,17),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,18,13,8), datetime(2002,3,19,6,17),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 44:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,3,23,11,19), datetime(2002,3,24,11,44), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,23,11,19), datetime(2002,3,24,11,44),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,23,11,19), datetime(2002,3,24,11,44),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 45:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,5,11,10,25), datetime(2002,5,11,16,21), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,11,10,25), datetime(2002,5,11,16,21),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,11,10,25), datetime(2002,5,11,16,21),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 46:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,5,18,19,41), datetime(2002,5,19,3,25), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,18,19,41), datetime(2002,5,19,3,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,18,19,41), datetime(2002,5,19,3,25),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 47:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,8,1,5,14), datetime(2002,8,1,12,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,1,5,14), datetime(2002,8,1,12,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,1,5,14), datetime(2002,8,1,12,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 48:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,8,18,18,36), datetime(2002,8,19,22,5), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,18,18,36), datetime(2002,8,19,22,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,18,18,36), datetime(2002,8,19,22,5),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 49:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,9,7,16,16), datetime(2002,9,8,4,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,7,16,16), datetime(2002,9,8,4,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,7,16,16), datetime(2002,9,8,4,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 50:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,9,30,7,49), datetime(2002,9,30,21,31), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,30,7,49), datetime(2002,9,30,21,31),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,30,7,49), datetime(2002,9,30,21,31),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 51:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,11,16,23,26), datetime(2002,11,17,7,25), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,16,23,26), datetime(2002,11,17,7,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,16,23,26), datetime(2002,11,17,7,25),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 52:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,11,26,21,40), datetime(2002,11,27,7,52), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,26,21,40), datetime(2002,11,27,7,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,26,21,40), datetime(2002,11,27,7,52),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 53:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2003,3,20,4,22), datetime(2003,3,20,8,50), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,3,20,4,22), datetime(2003,3,20,8,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,3,20,4,22), datetime(2003,3,20,8,50),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 54:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2003,5,29,18,25), datetime(2003,5,30,3,23), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,5,29,18,25), datetime(2003,5,30,3,23),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,5,29,18,25), datetime(2003,5,30,3,23),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 55:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,22,9,40), datetime(2004,7,22,13,6), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,22,9,40), datetime(2004,7,22,13,6),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,22,9,40), datetime(2004,7,22,13,6),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 56:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,24,5,25), datetime(2004,7,24,11,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,24,5,25), datetime(2004,7,24,11,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,24,5,25), datetime(2004,7,24,11,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 57:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,26,22,19), datetime(2004,7,27,1,35), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,26,22,19), datetime(2004,7,27,1,35),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,26,22,19), datetime(2004,7,27,1,35),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 58:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,8,29,9,3), datetime(2004,8,29,18,36), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,8,29,9,3), datetime(2004,8,29,18,36),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,8,29,9,3), datetime(2004,8,29,18,36),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 59:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,11,7,17,54), datetime(2004,11,7,22,44), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,7,17,54), datetime(2004,11,7,22,44),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,7,17,54), datetime(2004,11,7,22,44),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 60:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,11,9,18,20), datetime(2004,11,9,20,32), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,9,18,20), datetime(2004,11,9,20,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,9,18,20), datetime(2004,11,9,20,32),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 61:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,5,15,2,6), datetime(2005,5,15,5,37), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,5,15,2,6), datetime(2005,5,15,5,37),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,5,15,2,6), datetime(2005,5,15,5,37),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 62:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,6,12,6,42), datetime(2005,6,12,14,46), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,12,6,42), datetime(2005,6,12,14,46),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,12,6,42), datetime(2005,6,12,14,46),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 63:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,6,14,17,51), datetime(2005,6,15,5,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,14,17,51), datetime(2005,6,15,5,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,14,17,51), datetime(2005,6,15,5,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 64:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,7,10,2,37), datetime(2005,7,10,10,15), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,10,2,37), datetime(2005,7,10,10,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,10,2,37), datetime(2005,7,10,10,15),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 65:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,7,17,00,48), datetime(2005,7,17,15,22), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,17,00,48), datetime(2005,7,17,15,22),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,17,00,48), datetime(2005,7,17,15,22),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 66:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,9,2,13,45), datetime(2005,9,2,18,48), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,9,2,13,45), datetime(2005,9,2,18,48),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,9,2,13,45), datetime(2005,9,2,18,48),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 67:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,4,13,11,14), datetime(2006,4,13,15,30), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,4,13,11,14), datetime(2006,4,13,15,30),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,4,13,11,14), datetime(2006,4,13,15,30),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 68:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,12,8,3,56), datetime(2006,12,8,14,58), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,8,3,56), datetime(2006,12,8,14,58),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,8,3,56), datetime(2006,12,8,14,58),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 69:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,12,14,13,47), datetime(2006,12,14,22,32), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,14,13,47), datetime(2006,12,14,22,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,14,13,47), datetime(2006,12,14,22,32),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 70:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2007,11,19,17,17), datetime(2007,11,19,23,25), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2007,11,19,17,17), datetime(2007,11,19,23,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2007,11,19,17,17), datetime(2007,11,19,23,25),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 71:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2009,2,3,19,16), datetime(2009,2,4,2,18), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,2,3,19,16), datetime(2009,2,4,2,18),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,2,3,19,16), datetime(2009,2,4,2,18),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 72:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2009,12,12,4,33), datetime(2009,12,12,18,12), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,12,12,4,33), datetime(2009,12,12,18,12),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,12,12,4,33), datetime(2009,12,12,18,12),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 73:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2010,4,5,7,51), datetime(2010,4,5,12,11), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,4,5,7,51), datetime(2010,4,5,12,11),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,4,5,7,51), datetime(2010,4,5,12,11),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 74:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2010,5,28,1,48), datetime(2010,5,28,19,55), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,5,28,1,48), datetime(2010,5,28,19,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,5,28,1,48), datetime(2010,5,28,19,55),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 75:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,3,29,15,5), datetime(2011,3,30,00,26), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,3,29,15,5), datetime(2011,3,30,00,26),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,3,29,15,5), datetime(2011,3,30,00,26),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 76:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,9,17,2,52), datetime(2011,9,17,15,45), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,17,2,52), datetime(2011,9,17,15,45),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,17,2,52), datetime(2011,9,17,15,45),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 77:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,9,26,11,39), datetime(2011,9,26,19,47), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,26,11,39), datetime(2011,9,26,19,47),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,26,11,39), datetime(2011,9,26,19,47),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 78:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,4,23,2,10), datetime(2012,4,23,16,48), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,4,23,2,10), datetime(2012,4,23,16,48),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,4,23,2,10), datetime(2012,4,23,16,48),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 79:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,6,16,19,30), datetime(2012,6,16,22,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,6,16,19,30), datetime(2012,6,16,22,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,6,16,19,30), datetime(2012,6,16,22,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 80:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,7,14,17,34), datetime(2012,7,15,6,24), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,7,14,17,34), datetime(2012,7,15,6,24),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,7,14,17,34), datetime(2012,7,15,6,24),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 81:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,8,4,7), datetime(2012,10,8,17,20), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,8,4,7), datetime(2012,10,8,17,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,8,4,7), datetime(2012,10,8,17,20),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 82:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,11,22,42), datetime(2012,10,12,15,57), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,11,22,42), datetime(2012,10,12,15,57),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,11,22,42), datetime(2012,10,12,15,57),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 83:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,31,14,23), datetime(2012,10,31,23,39), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,31,14,23), datetime(2012,10,31,23,39),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,31,14,23), datetime(2012,10,31,23,39),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 84:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,11,23,20,46), datetime(2012,11,24,11,39), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,11,23,20,46), datetime(2012,11,24,11,39),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,11,23,20,46), datetime(2012,11,24,11,39),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 85:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,3,17,5,17), datetime(2013,3,17,12,00), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,3,17,5,17), datetime(2013,3,17,12,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,3,17,5,17), datetime(2013,3,17,12,00),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 86:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,4,13,22,8), datetime(2013,4,14,16,45), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,4,13,22,8), datetime(2013,4,14,16,45),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,4,13,22,8), datetime(2013,4,14,16,45),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 87:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,7,12,16,38), datetime(2013,7,13,5,1), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,7,12,16,38), datetime(2013,7,13,5,1),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,7,12,16,38), datetime(2013,7,13,5,1),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 88:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,4,20,10,15), datetime(2014,4,21,7,30), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,4,20,10,15), datetime(2014,4,21,7,30),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,4,20,10,15), datetime(2014,4,21,7,30),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 89:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,8,19,5,42), datetime(2014,8,19,17,35), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,8,19,5,42), datetime(2014,8,19,17,35),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,8,19,5,42), datetime(2014,8,19,17,35),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 90:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,9,12,15,12), datetime(2014,9,12,21,40), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,9,12,15,12), datetime(2014,9,12,21,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,9,12,15,12), datetime(2014,9,12,21,40),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
		if day == 91:
			try:
				data_mfi2 = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2015,3,17,3,55), datetime(2015,3,17,13,14), ['B3F1','B3GSE'])       
				data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2015,3,17,3,55), datetime(2015,3,17,13,14),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
				data_swe2 = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2015,3,17,3,55), datetime(2015,3,17,13,14),['Proton_V_nonlin','Proton_VX_nonlin','Proton_VY_nonlin','Proton_VZ_nonlin'])
				Ehto2 = 1
			except:
				Ehto2 = 0
							
	
		if Ehto2 == 0:
			print day
			print "skip plasma"
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")	
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("\n")
			
			Data_Velocity.write(str(0))
			Data_Velocity.write(" ")	
			Data_Velocity.write(str(0))
			Data_Velocity.write(" ")
			Data_Velocity.write(str(0))
			Data_Velocity.write(" ")
			Data_Velocity.write(str(0))
			Data_Velocity.write(" ")
			Data_Velocity.write(str(0))
			Data_Velocity.write("\n")
			
			Data_Density.write(str(0))	
			Data_Density.write("\n")
	
		if Ehto2 == 1:

			mask = np.abs(data_mfi2['B']) < 1e3
			data_mfi2['B'] = data_mfi2['B'][mask]
			data_mfi2['EPOCH'] = np.array(data_mfi2['EPOCH'])[mask]
			data_mfi2['BX_(GSE)'] = data_mfi2['BX_(GSE)'][mask]
			data_mfi2['BY_(GSE)'] = data_mfi2['BY_(GSE)'][mask]
			data_mfi2['BZ_(GSE)'] = data_mfi2['BZ_(GSE)'][mask]

			B = data_mfi2['B']
			B_x = data_mfi2['BX_(GSE)']
			B_y = data_mfi2['BY_(GSE)']
			B_z = data_mfi2['BZ_(GSE)']
			TIME = data_mfi['EPOCH']

			#The beginning and the length of a sheath
			TheBeginning = data_mfi2['EPOCH'][0]
			TheLength = (data_mfi2['EPOCH'][-1]-data_mfi2['EPOCH'][0]).total_seconds()	

			mask = np.abs(data_swe['P+_WPERP_NONLIN']) < 1e3
			data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
			data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
			data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
			data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]

			data_swe2['PROTON_BULK_SPEED'] = data_swe2['PROTON_BULK_SPEED'][mask]
			data_swe2['EPOCH'] = np.array(data_swe2['EPOCH'])[mask]
			data_swe2['P+_VX_GSE_NONLIN'] = data_swe2['P+_VX_GSE_NONLIN'][mask]
			data_swe2['P+_VY_GSE_NONLIN'] = data_swe2['P+_VY_GSE_NONLIN'][mask]
			data_swe2['P+_VZ_GSE_NONLIN'] = data_swe2['P+_VZ_GSE_NONLIN'][mask]

			mask = np.abs(data_swe['P+_DENSITY']) < 1e3
			data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
			data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
			data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
			data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]
		
			data_swe2['PROTON_BULK_SPEED'] = data_swe2['PROTON_BULK_SPEED'][mask]
			data_swe2['EPOCH'] = np.array(data_swe2['EPOCH'])[mask]
			data_swe2['P+_VX_GSE_NONLIN'] = data_swe2['P+_VX_GSE_NONLIN'][mask]
			data_swe2['P+_VY_GSE_NONLIN'] = data_swe2['P+_VY_GSE_NONLIN'][mask]
			data_swe2['P+_VZ_GSE_NONLIN'] = data_swe2['P+_VZ_GSE_NONLIN'][mask]
		
		
			mask = np.abs(data_swe['P+_WPAR_NONLIN']) < 1e3
			data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
			data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
			data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
			data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]
				
			data_swe2['PROTON_BULK_SPEED'] = data_swe2['PROTON_BULK_SPEED'][mask]
			data_swe2['EPOCH'] = np.array(data_swe2['EPOCH'])[mask]
			data_swe2['P+_VX_GSE_NONLIN'] = data_swe2['P+_VX_GSE_NONLIN'][mask]
			data_swe2['P+_VY_GSE_NONLIN'] = data_swe2['P+_VY_GSE_NONLIN'][mask]
			data_swe2['P+_VZ_GSE_NONLIN'] = data_swe2['P+_VZ_GSE_NONLIN'][mask]	
			
			
			WPERP = data_swe['P+_WPERP_NONLIN']
			WPAR = data_swe['P+_WPAR_NONLIN']
			DENSITY = data_swe['P+_DENSITY']	
			TIME2 = data_swe['EPOCH']
			
			
			V = data_swe2['PROTON_BULK_SPEED']
			VX = data_swe2['P+_VX_GSE_NONLIN']
			VY = data_swe2['P+_VY_GSE_NONLIN']
			VZ = data_swe2['P+_VZ_GSE_NONLIN']

			values = []
			k = 0
			while k < np.shape(DENSITY)[0]:
				spot = 0
				variable1 = data_mfi2['EPOCH'][0]
				variable2 = data_mfi2['EPOCH'][0]
				Difference1 = abs((data_swe['EPOCH'][k]-variable1).total_seconds())
				Difference2 = (variable2-data_swe['EPOCH'][k]).total_seconds()

				slot1 = spot
			
				while spot < np.shape(data_mfi2['EPOCH'])[0]:
				
					if abs((data_swe['EPOCH'][k]-variable1).total_seconds()) > abs((data_swe['EPOCH'][k]-data_mfi2['EPOCH'][spot]).total_seconds()):
						variable1 = data_mfi2['EPOCH'][spot]
						Difference1 = abs((data_swe['EPOCH'][k]-data_mfi2['EPOCH'][spot]).total_seconds())
						slot1 = spot
					spot = spot + 1
				values.append(slot1)	
				k = k + 1
					
			#Laskee betat ja thresholdin koko sheathissa ja kirjaa ylos
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")	
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("	")
			Data_Plasma.write(str(0))
			Data_Plasma.write("\n")	
			
			Data_Velocity.write(str(0))
			Data_Velocity.write("	")	
			Data_Velocity.write(str(0))
			Data_Velocity.write("	")
			Data_Velocity.write(str(0))
			Data_Velocity.write("	")
			Data_Velocity.write(str(0))
			Data_Velocity.write("	")
			Data_Velocity.write(str(0))
			Data_Velocity.write("\n")	
				
			Data_Density.write(str(0))
			Data_Density.write("	")
			Data_Density.write(str(0))
			Data_Density.write("	")
			Data_Density.write(str(0))	
			Data_Density.write("\n")
				
			index = 0
			while index < np.shape(TIME2)[0]:
				TheSpotInSheath = (TIME2[index]-TheBeginning).total_seconds()
				TheSpotInSheath = TheSpotInSheath/TheLength
				TPERP = ((WPERP[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
				TPAR  = ((WPAR[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
	
				Threshold = TPERP/TPAR-1
		
				Beta = 2*(12.566370614e-7)*(1.38064881e-23)
				Beta = Beta/( (B[values[index]]*10**(-9.0))**2 )

				BetaPAR = Beta*(DENSITY[index]*10**6)*TPAR
				BetaPERP = Beta*(DENSITY[index]*10**6)*TPERP

				ThresHoldi = Threshold - 1/BetaPERP
				ThresHoldi_IC = TPERP/TPAR - 1 - 0.43/( (BetaPAR+0.0004)**0.42  )
				#Data_Plasma.write(str(TheSpotInSheath))
				#Data_Plasma.write(str(TIME2[index]))
				#Data_Plasma.write("	")	
				Data_Plasma.write(str((TIME2[index]-TIME[0]).total_seconds()))
				Data_Plasma.write("	")	
				Data_Plasma.write(str(BetaPAR))
				Data_Plasma.write("	")
				Data_Plasma.write(str(BetaPERP))
				Data_Plasma.write("	")
				Data_Plasma.write(str(ThresHoldi))
				Data_Plasma.write("	")
				Data_Plasma.write(str(ThresHoldi_IC))
				Data_Plasma.write("\n")
				
				Data_Velocity.write(str((TIME2[index]-TIME[0]).total_seconds()))
				Data_Velocity.write("	")	
				Data_Velocity.write(str(V[index]))
				Data_Velocity.write("	")
				Data_Velocity.write(str(VX[index]))
				Data_Velocity.write("	")
				Data_Velocity.write(str(VY[index]))
				Data_Velocity.write("	")
				Data_Velocity.write(str(VZ[index]))
				Data_Velocity.write("\n")
				
				Data_Density.write(str((TIME2[index]-TIME[0]).total_seconds()))
				Data_Density.write("	")	
				Data_Density.write(str(DENSITY[index]*10**6))
				Data_Density.write("	")	
				Data_Density.write(str(WPERP[index]*1000))	
				Data_Density.write("\n")
				
				index = index + 1

	day = day + 1

Data.close()	
Data_Plasma.close()
Data_Velocity.close()
Data_Density.close()
						
			
			
			
