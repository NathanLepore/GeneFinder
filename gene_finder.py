    # -*- coding: utf-8 -*-
"""
Here is my gene finder script. It works but it takes a long time to run the salmonella gene. 

@author: Nathan Lepore

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful

from load import load_seq
dna = load_seq("./data/X73525.fa")



def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    if nucleotide == "A":
        return "T"
    if nucleotide == "T":
        return "A"
    if nucleotide == "G":
        return "C"
    if nucleotide == "C":
        return "G"


# TODO: implement this
    pass


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    NumberOfBases = len(dna)
    placeholder = '.'
    ReverseComplement = list(NumberOfBases*placeholder)
    for a in range(NumberOfBases, 0, -1):
                ReverseComplement[NumberOfBases-a] = get_complement(dna[a-1])
    return "".join(ReverseComplement)

    # TODO: implement this
    pass


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # TODO: implement this
    pass
    length = len(dna)
    ORF = list(length*" ")
    for i in range(0, length, 3):
        a = dna[i:i+3]
        if a == "TAG" or a == "TGA" or a == "TAA":
            ORF = ''.join(ORF)
            ORF = ORF.strip()
            return ORF
        else:
            ORF[int(i/3)] = a
    ORF = ''.join(ORF)
    ORF = ORF.strip()
    return(ORF)


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA
        sequence and returns them as a list.  This function should
        only find ORFs that are in the default frame of the sequence
        (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    pass

def find_all_ORFs_oneframe(dna):
    startcodon = 'ATG'
    length = len(dna)
    occurances = dna.count(startcodon)
    ORF = list('')

    i = 0
    while i < length:
        a = dna[i: i+3]
        if a == startcodon:
            dna1 = dna[i:]
            ORFreturn = rest_of_ORF(dna1)
            ORFreturn = [ORFreturn]
            ORF = ORF + ORFreturn
            i = len(ORFreturn)
        i = i+3
    return ORF


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in
        all 3 possible frames and returns them as a list.  By non-nested we
        mean that if an ORF occurs entirely within another ORF and they are
        both in the same frame, it should not be included in the returned list
        of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    pass
    NewORF = list('')
    for a in range(0, 3):
        dna1 = dna[a:]
        NewORF = NewORF + find_all_ORFs_oneframe(dna1)
    return NewORF


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    pass
    ORF = find_all_ORFs(dna)
    dna = get_reverse_complement(dna)
    ORF = ORF + find_all_ORFs(dna)
    return ORF


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this

    ORFS = find_all_ORFs_both_strands(dna)
    length = len(ORFS)
    ORFlength = 0
    for i in range(length):
        compare = ORFlength
        ORFlength = len(ORFS[i])
        if ORFlength > compare:
            final = ORFS[i]
    return final


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass
    ORFlength = 0
    for i in range(num_trials):
        dna = shuffle_string(dna)
        compare = ORFlength
        ORF = longest_ORF(dna)
        ORFlength = len(ORF)
        if ORFlength > compare:
            final = ORF
    return final


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

    length = len(dna)
    fix_length = length % 3
    # dna = dna[0:length-fix_length]
    aalength = int(length/3)
    aa = list(' '*aalength)
    i = 0
    from amino_acids import aa_table
    while i < length - fix_length:
        codon = dna[i:i+3]
        amino_acid = aa_table[codon]
        aa[int(i/3)] = amino_acid
        i = i+3
    aa = ''.join(aa)
    return aa


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass
    ORFS = find_all_ORFs_both_strands(dna)
    length = len(ORFS)
    sequence = list(length*' ')
    for i in range(length):
        sequence[i] = coding_strand_to_AA(ORFS[i])
    return sequence


print(gene_finder(dna))


# if __name__ == "__main__":
# import doctest
# doctest.run_docstring_examples(gene_finder, globals(),
#                               verbose=True)
