'''
Code Challenge: Implement ApproximatePatternCount.

      Input: Strings Pattern and Text as well as an integer d.
      Output: Countd(Text, Pattern).

    Sample Input:
      GAGG
      TTTAGAGCCTTCAGAGG
      2
    Sample Output:
      4
'''

def HammingDistance(p, q):
  ham_dis = 0
  for i in range(0, len(q)):
    if p[i] != q[i]:
      ham_dis += 1
  return(ham_dis)

def ApprPatternCount(Pattern, Text, d):
  count = 0
  for i in range(0, (len(Text) - len(Pattern) +1)):
    if HammingDistance(Text[i:(i+len(Pattern))], Pattern) <= d:
      count += 1
  return(count)

#input
with open('dataset.txt', 'r') as file:
  Pattern = file.readline().strip()
  Text = file.readline().strip()
  d = int(file.readline().strip())

a = str(ApprPatternCount(Pattern, Text, d))

#Output
with open('dataset.txt', 'w') as output:
  output.write(a)