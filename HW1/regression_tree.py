import csv

######################################################################################################
# This method creates the dataset from the train.csv file
# Headers are removed to make further calculations easier
# Also appending each record with the resource ID for SPRINT implementation
######################################################################################################

def inputDataset(file_path):
	f = open(file_path, 'rb')
	data = list(csv.reader(f))
	del data[0]
	record_count = len(data)
	attribute_count = len(data[0])-1
	for i in xrange(record_count):
		data[i].append(i)
	return data


######################################################################################################
# This method generates attribute lists from the data, need to implement sorting
# The attrribute lists are stored as a 3D array, A[i][j][k]
# i -> attribute index (among Xi's)
# j -> record index 
# k -> value index (there will be only 3 values in this, the attribute value, output and RID)
# Finally, each of these attrbiute lists is sorted so as to increase computation efficiency
######################################################################################################

def createAttrLists(data):
	record_count = len(data)
	attribute_count = len(data[0])-2
	attr_list = [[[0 for x in range(3)] for y in range(record_count)] for z in range(attribute_count)]
	sorted_attr_list = [[[0 for x in range(3)] for y in range(record_count)] for z in range(attribute_count)]
	for attr in range(attribute_count):
		for record in xrange(record_count):
			attr_list[attr][record][0] = float(data[record][attr])
			attr_list[attr][record][1] = float(data[record][attribute_count])
			attr_list[attr][record][2] = int(data[record][attribute_count+1])
		sorted_attr_list[attr] = sortAttrList(attr_list[attr])
	return sorted_attr_list

def sortAttrList(attr_list):
	sorted_attr_list = sorted(attr_list, key=lambda item:item[0])
	return sorted_attr_list

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