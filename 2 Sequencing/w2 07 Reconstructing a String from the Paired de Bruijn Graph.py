'''RECONSTRUCTING A STRING FROM THE PAIRED DE BRUIJN GRAPH
Code Challenge: Implement StringSpelledByGappedPatterns

Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn)
such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in
Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists).
______________________________________(◡ ‿ ◡ ✿)____________________________________________________
INPUT: dos números enteros correspondientes a "k" y "d" (en la primera línea
 separados por un espacio) y una serie de secuencias con la forma (k, d)-mers
 es decir GACC|GCGC en las que una pertenecerá al prefijo y la otra al sufijo
OUTPUT: una sola secuencia con una longitud equivalente a "k + d + k + n - 1"
 igual a (ai|bi) (en dónde i es un sufijo para ambas).

Sample Input:
4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA
Sample Output:
GACCGAGCGCCGGA

'''

import sys;
sys.setrecursionlimit(10 ** 6)
def DeBruijn_pairs(reads):
    Adjacency = {}
    for read in reads:
        prefix = (read[0][:-1], read[1][:-1])
        suffix = (read[0][1:], read[1][1:])
        if prefix not in Adjacency:
            Adjacency[prefix] = [suffix]
        else:
            Adjacency[prefix].append(suffix)

    return Adjacency


##

def get_source(graph):
    deg = {}
    for v in graph:
        if v not in deg.keys():
            deg[v] = -len(graph[v])
        else:
            deg[v] -= len(graph[v])
        for u in graph[v]:
            if u not in deg.keys():
                deg[u] = 1
            else:
                deg[u] += 1
    for v in deg:
        if deg[v] == -1:
            return v
    print('graph got no eulerian path, no source.')


def dfs(v, graph, eulerian, stack):
    """Eularian path/circuit dfs"""

    if v not in graph.keys():
        eulerian.append(v)
        if len(stack) == 0:
            return
        else:
            dfs(stack.pop(), graph, eulerian, stack)

    elif len(graph[v]) == 0:
        eulerian.append(v)
        if len(stack) > 0:
            dfs(stack.pop(), graph, eulerian, stack)
    else:
        stack.append(v)
        dfs(graph[v].pop(-1), graph, eulerian, stack)
    #


def reconstruct(eulerian):
    prefs, suffs = eulerian[0][0], eulerian[0][1]

    for pair in eulerian[1:]:
        prefs += pair[0][-1]
        suffs += pair[1][-1]

    if prefs[k + d:] == suffs[:-(k + d)]:
        print('aligned pref + suff strings')
    seq = prefs + suffs[-(k + d):]

    return seq


#####

f = open('cool_dataset.txt', 'r')
k, d = (int(i) for i in f.readline().strip().split(' '))
reads = list(tuple(i.strip('()').strip().split('|')) for i in f.readlines())

graph = DeBruijn_pairs(reads)
source = get_source(graph)
eulerian = []
stack = []
dfs(source, graph, eulerian, stack)

eulerian.reverse()
seq = reconstruct(eulerian)
print(seq)

