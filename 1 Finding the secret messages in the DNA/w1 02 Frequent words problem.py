'''
Solve the Frequent Words Problem.

Input: A string Text and an integer k.
Output: All most frequent k-mers in Text.

Sample Input:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
Sample Output:
CATG GCAT
'''
#Chunyu Zhao 20150902

def find_kmers(dna, k):
    dict = {}
    for i in range(0, len(dna)- k  +1):
        kmer = dna[i: i+k]
        if kmer not in dict:
            dict[kmer] = 1
        else:
            dict[kmer] += 1
    max_freq = max(dict.values())
    output = []
    for key in dict.keys():
        if dict[key] == max_freq:
            output.append(key)
    print('output', output, max_freq)
    return output
print(find_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))
