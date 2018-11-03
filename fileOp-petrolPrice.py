#!/usr/bin/python
#WAP to read statewise petrol prices and average price of each state record in other file
import io
def calcAvgPetrolPriceState(fname):
	fd=io.FileIO(fname)
	#fd=open(fname)
	petrolPriceMaharashtra=0.0
	petrolPriceGoa=0.0
	petrolPriceKarnataka=0.0
	cnt=0
	if fd != None:
		while True:
			data=fd.readline()
			if data == '':
				break
			l1=data.split(" ")
			petrolPriceMaharashtra+=int(l1[2])
			petrolPriceGoa+=int(l1[3])
			petrolPriceKarnataka+=int(l1[4])
			cnt+=1
	
	
	petrolPriceMaharashtra = petrolPriceMaharashtra/cnt
	petrolPriceGoa = petrolPriceGoa/cnt
	petrolPriceKarnataka = petrolPriceKarnataka/cnt
	fd1=io.FileIO("petrol_avg_out.txt","w")
	avgpetrolstr="Avg Petrol prices " + str(petrolPriceMaharashtra) + " " + str(petrolPriceGoa) + " " + str(petrolPriceKarnataka)
	fd1.write(avgpetrolstr)
	print "statewise Average petrol prices are written to petrol_avg_out.txt file"
	
			
def main():
	calcAvgPetrolPriceState("petrol_prices.txt")
	

	
if __name__=="__main__":
	main()
