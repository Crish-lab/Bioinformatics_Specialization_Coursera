'''LEADER BOARD CYCLOPEPTIDE SEQUENCING
Code Challenge: Implement LeaderboardCyclopeptideSequencing.

Input: An integer N and a collection of integers Spectrum.
Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).

Sample Input:
10
0 71 113 129 147 200 218 260 313 331 347 389 460
Sample Output:
113-147-71-129

Created on Sat Dec 28 17:26:09 2019
@author: jasonmoggridge
BA4_G - Leaderboard cyclopeptide sequencing
    *** Adapting earlier algos to accept not perfect matching
    substrings, but still want a strict bound on possible solutions
    carried forward after each expansion of candidates.

    -> Leaderboard, the N-best candidates
    or 19 + multiple if tie for 20th

________________________________________♥╣[-_-]╠♥______________________________________________

 El score es la cantidad de elementos de un espectro que coinciden con los aminoácidos
  de un péptido, en este caso el score más alto será N. El OBJETIVO de éste código es obtener
  los péptidos líder, es decir, aquellos que cumplen con el score en el espectro
  este proceso es equivalente a hacer el "CUT"
INPUT: el score "N" en número entero y una secuencia equivalente al espectro
OUTPUT: una secuencia numérica equivalente a las masas de aquellos que cumplen con el score
'''
#   # Pseudocode for LeaderboardSeqng(Spectrum, N):
#
#
# LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N)
#    Leaderboard ← {0-peptide}
#    LeaderPeptide ← 0-peptide
#    while Leaderboard is non-empty
#        Leaderboard ← Expand(Leaderboard)
#        for each Peptide in Leaderboard
#            if Mass(Peptide) = ParentMass(Spectrum)
#                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
#                    LeaderPeptide ← Peptide
#            else if Mass(Peptide) > ParentMass(Spectrum)
#                remove Peptide from Leaderboard
#        Leaderboard ← Cut(Leaderboard, Spectrum, N)
#    output LeaderPeptide


def Leaderboard_Cyclopeptide_Sequencing(Spectrum, N):
    def Expand_Peptides(peptides):

        new_peptides = []
        for peptide in peptides:
            for aa in mass:
                new_peptides.append(peptide + aa)

        return new_peptides

    #

    def Cyclo_Spectrum(Peptide):

        if Peptide in cyclospectra:
            return cyclospectra[Peptide]
        else:
            spectrum = [0, int(sum(mass[aa] for aa in Peptide))]
            cycle = Peptide * 2
            for i in range(len(Peptide)):
                for j in range(i + 1, i + len(Peptide)):
                    spectrum.append(sum(mass[aa] for aa in cycle[i:j]))

            cyclospectra[Peptide] = spectrum
            return cyclospectra[Peptide]

    #

    def Score(Peptide, Spectrum):

        peaks = list(Spectrum)
        score = 0

        for fragment in Cyclo_Spectrum(Peptide):
            if fragment in peaks:
                score += 1
                peaks.remove(fragment)
            elif fragment > Parent_Mass:
                return 0
        return score

    #

    cyclospectra = {}
    Parent_Mass = Spectrum[-1]

    Leaderboard = ['']
    LeaderPeptide = ''

    while Leaderboard:

        Leaderboard = Expand_Peptides(Leaderboard)
        scores = []

        for Peptide in Leaderboard:

            score = Score(Peptide, Spectrum)
            Mass_Peptide = max(Cyclo_Spectrum(Peptide))

            if Mass_Peptide == Parent_Mass and score > Score(LeaderPeptide, Spectrum):
                LeaderPeptide = Peptide

            elif Mass_Peptide > Parent_Mass:
                score = 0

            scores.append(score)

        if len(Leaderboard) > N:

            cut_off = sorted(scores)[-N]
            leaders = []

            for i in range(len(Leaderboard)):
                if scores[i] >= cut_off and scores[i] > 0:
                    leaders.append(Leaderboard[i])

            Leaderboard = leaders

    return LeaderPeptide


#######

mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, \
    'I': 113, 'N': 114, 'D': 115, 'E': 129, 'K': 128, 'M': 131, 'H': 137, \
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}
#######

f = open("cool_dataset.txt", 'r')

N = int(f.readline())
Spectrum = [int(i) for i in f.readline().split(' ')]

Leader = Leaderboard_Cyclopeptide_Sequencing(Spectrum, N)
masses = [str(mass[aa]) for aa in Leader]
string = '-'.join(masses)

with open("cool_dataset.txt", 'w') as f:
    f.write(string)
    f.close()

#######