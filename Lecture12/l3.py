#!/usr/bin/python3
import sys
with open("AJ223353_seq.txt") as infile:
    dna = infile.read()
dna = dna.replace("\n", "").replace(" ", "").upper()
utr5 = dna[0:28]      # bases 1-28    non-coding (5' UTR)
cds  = dna[28:409]    # bases 29-409  coding
utr3 = dna[409:]      # bases 410-end non-coding (3' UTR)
utr5_header = "AJ223353_5UTR_length_" + str(len(utr5))
cds_header  = "AJ223353_CDS_length_"  + str(len(cds))
utr3_header = "AJ223353_3UTR_length_" + str(len(utr3))

#coding and non-coding
with open("AJ223353_coding.fasta", "w") as out:
    out.write(">" + cds_header + "\n" + cds + "\n")

with open("AJ223353_noncoding.fasta", "w") as out:
    out.write(">" + utr5_header + "\n" + utr5 + "\n")
    out.write(">" + utr3_header + "\n" + utr3 + "\n")
print("Wrote: AJ223353_coding.fasta, AJ223353_noncoding.fasta")


