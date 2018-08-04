import csv

def inputDataset(file_path):
	f = open(file_path, 'rb')
	data = list(csv.reader(f))
	del data[0]
	record_count = len(data)
	attribute_count = len(data[0])-1
	for i in xrange(record_count):
		data[i].append(i)
	return data

def createAttrLists(data):
	record_count = len(data)
	attribute_count = len(data[0])-2
	attr_list = [[[0 for x in range(3)] for y in range(record_count)] for z in range(attribute_count)]
	for attr in range(attribute_count):
		for record in xrange(record_count):
			attr_list[attr][record][0] = float(data[record][attr])
			attr_list[attr][record][1] = float(data[record][attribute_count])
			attr_list[attr][record][2] = int(data[record][attribute_count+1])
	return attr_list

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
	attr_list = createAttrLists(dataset)
	print attr_list[0][0]