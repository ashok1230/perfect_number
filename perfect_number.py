class perfect:
    def __init__(self):
	self.number=int(raw_input("enter number:"))
	sum=0
	for i in range(1,self.number/2+1):
	    if self.number%i==0:
		sum+=i
	if sum==self.number:
	    print self.number,' is perfect number'
	else:
	    print self.number,'is not perfect number'
a=perfect()	    
