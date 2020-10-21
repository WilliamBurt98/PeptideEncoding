def master(string, motif):

    '''initialize DNA codon Dictionary'''

    codonD = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
              "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
              "TAT": "Y", "TAC": "Y", "TAA": "STOP", "TAG": "STOP",
              "TGT": "C", "TGC": "C", "TGA": "STOP", "TGG": "W",
              "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
              "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
              "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
              "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
              "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
              "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
              "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    """Define function that returns reverse complement of a DNA string"""

    def ReverseComplement(DNA):
        try:
            complements = {'A': 'T',
                           'C': 'G',
                           'T': 'A',
                           'G': 'C'}

            reverseDNA = DNA[::-1]

            complementDNA = ''

            for x in reverseDNA:
                complementDNA += complements[x]

            return complementDNA

        except (KeyError, TypeError):
            print('Failed: Incorrect string format entered')

            raise

    """Define function that finds all motifs in a DNA string"""

    def find_motifs(string, motif, codonD):
        allcodonsfound = []

        for x in range(0, len(string)):
            AAstring = ''
            codonstring = string[x:x + (len(motif) * 3)]

            for y in range(0, len(codonstring), 3):
                codon = codonstring[y:y + 3]
                if len(codon) == 3:
                    AA = codonD[codon]
                    AAstring += AA

            if AAstring == motif:
                allcodonsfound.append(codonstring)

        return allcodonsfound

    """
    Define function that finds all motifs in a reversed DNA string
    then finds the reverse complement of the motif that appears in
    the original string
    """

    def find_revmotifs(string, motif, codonD):
        allcodonsfound = []

        for x in range(0, len(string)):
            AAstring = ''
            codonstring = string[x:x + (len(motif) * 3)]

            for y in range(0, len(codonstring), 3):
                codon = codonstring[y:y + 3]
                if len(codon) == 3:
                    AA = codonD[codon]
                    AAstring += AA

            if AAstring == motif:
                revc = ReverseComplement(codonstring)

                allcodonsfound.append(revc)

        return allcodonsfound

    """return user-input as upper-case, then execute functions"""

    motif=motif.upper()
    string=string.upper()
    revstring = ReverseComplement(string)
    normal = find_motifs(string, motif, codonD)
    rev = find_revmotifs(revstring, motif, codonD)

    all_motifs = normal + rev

    """initialize a dictionary that keeps a tally of all the motifs found"""

    am_d={}

    for motif in all_motifs:
        if motif not in am_d:
            am_d[motif]='1'

        elif motif in am_d:
            number=int(am_d[str(motif)])
            new=number+1
            am_d[motif]=str(new)


    """format output string"""

    output=''

    for key, value in am_d.items():
        output+=( '\n'+ '  '+ key + " : " + value)

    if output=='':
        output='The DNA string does not encode for the amino acid motif.'

    return output





