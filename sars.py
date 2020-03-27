
import sys
import math
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

this = "sars:  "

def printf(anything):
    print(this + str(anything), flush = True)

def load_genome(infile):

    # Load genome from a text file into a string and convert to lowercase
    string = ""
    with open(infile) as f:
        for line in f:
            for char in line:
                #printf(char)

                # Ignore whitespace, numbers, etc.  TODO:  uracil
                if (char == "a" or char == "A"):
                    string += "a"

                elif (char == "c" or char == "C"):
                    string += "c"

                elif (char == "g" or char == "G"):
                    string += "g"

                elif (char == "t" or char == "T"):
                    string += "t"

    printf("number of genome bases = " + str(len(string)))

    #printf(string)
    return string

def gtoi(g):
    # Cast genome character [acgt] to integer in range(0, 3)
    if (g == "a"):
        return 0
    elif (g == "c"):
        return 1
    elif (g == "g"):
        return 2
    else:  # t
        return 3

def genome2vector(string):

    # Cast lowercase alphabetical genome string into an integer vector

    # Interpret ACGT as numeric base-4
    base = 4

    # Map each group of two genome bases to an integer range 4**2 = [0, 15]
    step = 2

    bvec = [0] * step
    for i in range(0, step):
        bvec[i] = base ** i
    #printf(bvec)

    vec = [0] * math.ceil(len(string) / step)
    j = 0
    for i in range(0, len(string) - step + 1, step):
        #printf(i)
        #printf(str(gtoi(string[i])) + str(gtoi(string[i+1])))

        # Note that the step size is hard-coded into this formula.  Ideally a
        # dot product would be used.
        vec[j] = gtoi(string[i]) * bvec[0] + gtoi(string[i+1]) * bvec[1]

        j += 1

    #printf(vec)
    return vec

def vector2midi(vec):

    ## Major (boring!)
    #scale = [
    #         0,    2,    4,  5,    7,    9,   11,
    #        12,   14,   16, 17,   19,   21,   23,
    #        24,   26
    #        ]

    ## Exotic (exciting!)
    #scale = [
    #         0,                    7,      10,   
    #        12, 13,     16, 17,   19,      22,   
    #        24, 25,     28, 29,   31,   33,
    #        36
    #        ]

    ## Exotic with a 4th near bass
    #scale = [
    #         0,              5,    7,      10,   
    #        12,         16, 17,   19,      22,   
    #        24, 25,     28,       31, 32,  34,
    #        36
    #        ]

    ## Exotic with a major 6
    #scale = [
    #         0,              5,    7,      10,   
    #        12,         16, 17,   19,      22,   
    #        24, 25,     28,       31,  33, 34,
    #        36
    #        ]

    ## Exotic with a sharp 4
    #scale = [
    #         0,              5,    7,      10,   
    #        12,         16, 17,   19,      22,   
    #        24, 25,     28,   30, 31,      34,
    #        36
    #        ]

    # Exotic with a sharp 4 and leading tone
    scale = [
             0,              5,    7,      10,   
            12,         16, 17,   19,      22,   
            24, 25,     28,   30, 31,        35,
            36
            ]

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    #track.append(Message('program_change', program=8, time=0))  # celesta
    track.append(Message('program_change', program=9, time=0))  # glock
    #track.append(Message('program_change', program=46, time=0))  # harp

    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(90)))

    dt = 30

    # One octave below middle C
    scale_root = 60 - 12

    ## G
    #scale_root = 60 - 12 - 5

    for i in vec:
        n = scale_root + scale[i]
        track.append(Message('note_on' , note=n, time=dt))
        track.append(Message('note_off', note=n, time=dt))

    return mid

def genome2midi(infile, outfile):
    io = 0

    printf("converting genome...")
    printf("input  file = " +  infile)
    printf("output file = " + outfile)

    string = load_genome(infile)
    vec = genome2vector(string)
    mid = vector2midi(vec)
    io = mid.save(outfile)

    return io

def main():
    printf("From the top!")

    infile = "sars-cov-2-genome.txt"
    outfile = "sars-cov-2.mid"
    io = genome2midi(infile, outfile)

    printf("Bravo!")
    return io

sys.exit(main())

