
from datetime import datetime

def importdata(path, delimiter, length=10000000000000, condition=""):
    start=datetime.now()
    f=open(path)
    data=[]
    i=0
    for row in f:
        if i <= length:
            if condition !="":
                if condition in str(row):
                    data.append(row.split(delimiter))
                    i += 1
            else:
                data.append(row.split(delimiter))
                i += 1
        else: break

    titles=data[0]
    data=data[1:]
    print path, "finished importing. Length:",len(data) ,". Elapsed time:",datetime.now()-start,"\n"
    f.close()
    return titles, data


CosmicMutantsPath="/Users/radhikarawat/Desktop/Programming/TCGA_projects/CosmicMutantExport.tsv"
ExonPath="/Users/radhikarawat/Downloads/wgEncodeGencodeExonSupportV20.txt"


CosmicMutants_data =importdata(CosmicMutantsPath,'\t',condition="BRCA2")[1]
Exon_data= importdata(ExonPath,'\t')[1]
f=open("/Users/radhikarawat/PycharmProjects/TCGA2/BRCA_Mutations.txt",'w+')
for CosmicMutant in CosmicMutants_data:
    for Exon in Exon_data:
        AccessionNumber = Exon[0].split(".")[0]
        if AccessionNumber in str(CosmicMutant):
            line=""
            for info in Exon:
                line+=info+"\t"
            for info in CosmicMutant:
                line+=info+"\t"
            line=line+"\n"
            f.write(line)
            print line
f.close()