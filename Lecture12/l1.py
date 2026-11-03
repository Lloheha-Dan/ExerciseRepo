#!/usr/bin/python3
with open("plain_genomic_seq.txt") as localDNA:
	localdna=localDNA.read()
	exon1=localdna[0:63].upper()
	exon2=localdna[90:-1].upper()
exon_=exon1+exon2
#remove lefts that are not ATCG
clean=""
for base in exon_:
	if base in "ATCG":
		clean=clean+base
exon=clean

intron_=localdna[63:90].upper()
clean1 = ""
for base in intron_:
    if base in "ACGT":
        clean1 = clean1 + base
intron=clean1
print(">exon length",str(len(exon)),"\n"+exon)
print(">intron length",str(len(intron)),"\n"+intron)
