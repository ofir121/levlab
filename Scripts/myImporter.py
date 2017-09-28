import csv
from dataVisualizer.resources import AluHyper


path = "C:\django\levlab\Data\scatter.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) #The first line is the header

data = []
i = 0
for row in reader:
    sampleCode = int(row[0])
    sampleType = str(row[1])
    avg_Norm = "{0:.2f}".format(round(float(row[2]), 4))
    contIndex = "{0:.2f}".format(round(float(row[3]), 4))
    data.append([sampleCode, sampleType, avg_Norm, contIndex])
    aluData = AluHyper.objects.get_or_create(id=i, SampleCode=sampleCode, SampleType=sampleType, AVG_Norm=avg_Norm, contIndex=contIndex)
    print("Savingid " + str(id) + ":" + str(sampleCode) + ", " + sampleType + ", " + str(avg_Norm) + ", " + str(contIndex))
    if(False):
        try:
            aluData.save()
        except Exception as e:
            print(str(e) + ":" + str(sampleCode))
    i += 1


