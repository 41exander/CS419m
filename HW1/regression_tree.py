import csv

def inputDataset(file_path):
	f = open(file_path, 'rb')
	data = list(csv.reader(f))
	record_count = len(data)-1
	attribute_count = len(data[0])
	data[0].append('RID')
	for i in xrange(1,record_count+1):
		data[i].append(i-1)
	return data

def GrowTree(D):
	Partition(D)

# def Partition(D):
# 	if(D belongs to same label):
# 		return
# 	for each attribute in list of attributes do:
# 		splitEvaluation(attribute)
# 	best split to partition D into D1,D2
# 	Partition(D1)
# 	Partition(D2)

if __name__ == '__main__':
	
	dataset = inputDataset('train.csv')

	


