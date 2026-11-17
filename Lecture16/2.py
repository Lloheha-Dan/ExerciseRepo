#!/usr/bin/env python3
gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

# Dictionary for complementing bases (N pairs with N)
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}


def translate(dna):
    """Translate DNA into protein, one codon (3 bases) at a time."""
    protein = ""
    # stop at len(dna) - 2 so we never use an incomplete codon at the end
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i + 3]
        # .get() returns 'X' if the codon isn't in the table (e.g. 'ANG')
        amino_acid = gencode.get(codon, 'X')
        if amino_acid == '_':   # stop codon (TAA, TAG, TGA) - stop translating
            break
        protein += amino_acid
    return protein


def reverse_complement(dna):
    """Return the bottom strand, read 5' to 3'."""
    revcomp = ""
    for base in reversed(dna):
        revcomp += complement.get(base, 'N')
    return revcomp


dna = input("Enter a DNA sequence: ").replace(" ", "").upper()

print("\nTop strand frames")
for frame in range(3):
    print("Frame", frame + 1, "-->", translate(dna[frame:]))

print("\nBottom strand frames")
bottom = reverse_complement(dna)
for frame in range(3):
    print("Frame", frame + 1, "<--", translate(bottom[frame:]))
