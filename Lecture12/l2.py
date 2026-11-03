#!/usr/bin/python3
# Split plain_genomic_seq.txt into coding (exons) and non-coding (intron) parts
# and write each to a FASTA file named after its header.

# Read the whole file
with open("plain_genomic_seq.txt") as localDNA:
    localdna = localDNA.read()

# Clean the WHOLE sequence first: uppercase, keep only A/C/G/T
localdna = localdna.upper()
clean = ""
for base in localdna:
    if base in "ACGT":
        clean = clean + base
localdna = clean

# Slice: exon1 = bases 1-63, intron = 64-90, exon2 = 91-end
exon1 = localdna[0:63]
intron = localdna[63:90]
exon2 = localdna[90:]
exon = exon1 + exon2

# Headers with no spaces, so they can also be the file names
exon_header = "exon_length_" + str(len(exon))
intron_header = "intron_length_" + str(len(intron))

# Write each sequence to <header>.fasta
with open(exon_header + ".fasta", "w") as out:
    out.write(">" + exon_header + "\n" + exon + "\n")

with open(intron_header + ".fasta", "w") as out:
    out.write(">" + intron_header + "\n" + intron + "\n")

# Show what was written (useful for checking)
print(exon_header + ".fasta")
print(intron_header + ".fasta")
