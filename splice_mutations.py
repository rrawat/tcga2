

def importdata(path, delimiter, length=10000000000000, condition=""):
    f=open(path)
    data=[]
    i=0
    for row in f:
        if i <= length - 1:
            if condition !="":
                if condition in str(row):
                    data.append(row.split(delimiter))
                    i += 1
            else:
                data.append(row.split(delimiter))
                i += 1
    titles=data[0]
    data=data[1:]
    print path, "finished importing"
    return titles, data


CosmicMutantsPath="/Users/radhikarawat/Desktop/Programming/TCGA_projects/CosmicMutantExport.tsv"
ExonPath="/Users/radhikarawat/Downloads/wgEncodeGencodeExonSupportV20.txt"


CosmicMutants_data =importdata(CosmicMutantsPath,'\t',condition="BRCA2")[1]
Exon_data= importdata(ExonPath,'\t')[1]

i=0
for Exon in Exon_data:
    i+=1
    for CosmicMutant in CosmicMutants_data:
        #print i
        if Exon[0].split(".")[0] in str(CosmicMutant):
            ##Exon.append(CosmicMutant[0])
            print i, "A", Exon
        if CosmicMutant[1] in str(Exon):
            print i, "B", Exon