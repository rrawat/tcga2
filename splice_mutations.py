
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
    print path, "finished importing. Length:",len(data) ,". Elapsed time:",datetime.now()-start,
    f.close()
    return titles, data


CosmicMutantsPath="/Users/radhikarawat/Desktop/Programming/TCGA_projects/CosmicMutantExport.tsv"
ExonPath="/Users/radhikarawat/Downloads/wgEncodeGencodeExonSupportV20.txt"


CosmicMutants_data =importdata(CosmicMutantsPath,'\t',condition="BRCA2",length=100)[1]
Exon_data= importdata(ExonPath,'\t',length=8000000)[1]

i=0
length=len(Exon_data)
start=datetime.now()


f=open("/Users/radhikarawat/PycharmProjects/TCGA2/ExonData.csv","w+")
for Exon in Exon_data:
    i+=1
    #print i, "out of", length, "elapsed time:", datetime.now()-start
    for CosmicMutant in CosmicMutants_data:
        if "-" in str(CosmicMutant[23]):
            if Exon[0].split(".")[0] in str(CosmicMutant):

                line=str(Exon)+','+str(CosmicMutant)+"\n"
                f.write(line)

                #condition 1
                ExonChromosome=Exon[4].split("chr"[1])
                ExonStart=Exon[5]
                ExonEnd=Exon[6].split('\n')[0]
                MutantChromosome,MutantEnd=CosmicMutant[23].split("-")
                MutantChromosome,MutantStart=MutantChromosome.split(":")
                if [ExonChromosome,ExonStart,ExonEnd]==[MutantChromosome,MutantStart,MutantEnd]:
                    print Exon, CosmicMutant, i, "out of", length, "elapsed time:", datetime.now()-start
            #Exon.append(CosmicMutant[0])
f.close()