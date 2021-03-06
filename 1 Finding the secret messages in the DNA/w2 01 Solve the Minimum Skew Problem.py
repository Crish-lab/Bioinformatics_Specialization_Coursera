'''
Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

Input: A DNA string Genome.
Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

Sample Input:
TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
Sample Output:
11 24

'''
#by: Animesh Sinha

class Skew():
    def __init__(self, seq_dna):
        self.seq_dna = seq_dna

    def skew(self):
        skew = ['0']
        count = 0
        for nc in self.seq_dna:
            if nc == 'C':
                count -= 1
            elif nc == 'G':
                count += 1
            skew.append(str(count))

        return ' '.join(skew)

    def min_skew(self):
        skew = [int(i) for i in self.skew().split(' ')]
        min_skew = []
        min_value = min(skew)
        print('>> min_value:', min_value)

        for i, sk in enumerate(skew):
            if sk == min_value:
                min_skew.append(str(i))

        return ' '.join(min_skew)


if __name__ == '__main__':
    with open('dataset.txt') as file:
        seq_dna = file.readline()

    #seq_dna = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

    #skew = Skew(seq_dna).skew()
    #print(skew)

    min_skew = Skew(seq_dna).min_skew()
    print(min_skew)