#function to find the keys based on the value in the dictionaryObject
def getKeysByValue(dictionaryObject, valueToFind):
    listOfKeys = list()
    listOfItems = dictionaryObject.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

#Program
import csv 
inputFiles=['Input1.csv','Input2.csv','Input3.csv']
for iFile in inputFiles:
  # instantiating variables i as int, inputDictionary, computedDictionary as dictionary objects, temp as empty string object.
  #Instantiated dictionary object is by default an empty list
  groupIndex, inputDictionary, computedDictionary, temp=0,{},{},'';
  print("--------------------------------------------------------------------------------")
  print("----------------------- START OF {} TEST FILE -----------------------------".format(iFile))
  # Open input file in read mode, assumption is the input file is a legal, csv formatted.
  with open(iFile, 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      # next(csvreader) # UnComment this line if the input file has file header
      for row in csvreader: 
        #Read each row as key value pair dictionary object with Key as ID, and value as entire row.     
        inputDictionary[row[0]]=row
        #codeblock to create computedDictionary object, with key as ID, and Value as FIRSTNAMELASTNAME
        temp=row[1]
        if (temp.count("^")>1):    
          computedDictionary[row[0]]=temp[0:temp.rindex("^")].replace("^","").upper() 
        else :
          computedDictionary[row[0]]=temp.replace("^","").upper()
	  #Using set to get only uniqueValues
      uniquePatients = set(computedDictionary.values())
	  #Iterating through each value/patient from list of UniquePatients/Values
      for patient in uniquePatients:
		#Print groupIndex to match the expected output
        print("{} :".format(groupIndex))
        groupIndex+=1
		#Call to function to get the uniqueKeys by Value in the dictionaryObject
        listOfKeys = getKeysByValue(computedDictionary, patient)
        for key in listOfKeys:
          print(inputDictionary[key])
  print("----------------------- END OF {} TEST INPUT FILE -----------------------------".format(iFile))
  print("--------------------------------------------------------------------------------")
          