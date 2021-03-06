"""LEADER BOARD CYCLOPEPTIDE SEQUENCING on Spectrum25 with N = 1000
Exercise Break: Run LeaderboardCyclopeptideSequencing on Spectrum25 with N = 1000.
You should find 38 linear peptides of maximum score 83 (corresponding to 15 different cyclic
peptides). What are they? (Return your peptides in integer format, with each peptide separated
by a single space, e.g., 113-147-71-129 71-147-129-113.)

____________________________________________✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧_____________________________________________

Fixed from BA4G:
    -> uses linear_spectra score to trim leaderboard
    -> return a list with all equally scoring peptides instead of just one

Input: An integer N and a collection of integers Spectrum.
Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).

Sample Input:
10
0 71 113 129 147 200 218 260 313 331 347 389 460
Sample Output:
113-147-71-129

"""


def Leaderboard_Cyclopeptide_Sequencing(Spectrum, N):
    def Expand_Peptides(peptides):

        new_peptides = []
        for peptide in peptides:
            for aa in mass:
                new_peptides.append(peptide + aa)

        return new_peptides

    #

    def Linear_Spectrum(peptide):

        spectrum = [0]
        for i in range(len(peptide)):
            for j in range(i + 1, len(peptide) + 1):
                spectrum.append(sum(mass[aa] for aa in peptide[i:j]))
        return spectrum

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

    def Score(Peptide_spectrum, Spectrum):

        peaks = list(Spectrum)
        score = 0

        for fragment in Peptide_spectrum:
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
    LeaderPeptides = []
    Best = 1
    while Leaderboard:

        Leaderboard = Expand_Peptides(Leaderboard)
        linear_scores = []

        for Peptide in Leaderboard:

            score = Score(Linear_Spectrum(Peptide), Spectrum)

            Mass_Peptide = max(Cyclo_Spectrum(Peptide))

            if Mass_Peptide == Parent_Mass:
                Final_Score = Score(Cyclo_Spectrum(Peptide), Spectrum)
                if Final_Score > Best:
                    LeaderPeptides = [Peptide]
                    Best = Final_Score
                elif Final_Score == Best:
                    LeaderPeptides.append(Peptide)

            elif Mass_Peptide > Parent_Mass:
                score = 0

            linear_scores.append(score)

        if len(Leaderboard) > N:

            cut_off = sorted(linear_scores)[-N]
            leaders = []

            for i in range(len(Leaderboard)):
                if linear_scores[i] >= cut_off and linear_scores[i] > 0:
                    leaders.append(Leaderboard[i])

            Leaderboard = leaders

    return LeaderPeptides


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

#

Leaders = Leaderboard_Cyclopeptide_Sequencing(Spectrum, N)

with open("cool_dataset.txt", 'w') as f:
    for Leader in Leaders:
        masses = [str(mass[aa]) for aa in Leader]
        string = '-'.join(masses)

        f.write(string + ' ')
    f.close()

#######