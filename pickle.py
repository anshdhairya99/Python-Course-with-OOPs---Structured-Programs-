# Pickle Module in Python:-------------


#import pickle

#cars = ["Audi","BMW","Maruti Suzuki"]
#file = "mycars.pkl"
#fileobj = open(file,'wb')
#pickle.dump(cars,fileobj)
#fileobj.close()


import pickle
file = "mycars.pkl"
fileobj = open(file,'rb')
mycars = pickle.load(fileobj)
print(mycars)





