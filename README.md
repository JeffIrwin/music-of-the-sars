![](https://github.com/JeffIrwin/music-of-the-sars/workflows/CI/badge.svg)

# music-of-the-sars
Encoding the complete genome of the SARS-CoV-2 virus as a MIDI file

## Dependencies
- Python (3.8.1)
- `pip3 install mido`

## Run
`python sars.py sars-cov-2-genome.txt`

## Sample output
See https://soundcloud.com/jirwin505/sars-cov-2-genome

## References
The SARS-CoV-2 genome was taken from https://www.ncbi.nlm.nih.gov/nuccore/MN908947.3

## My God!  What have I done?
SARS-CoV-2 has four genomic bases, `A`, `C`, `G`, and `T`.  These can be interpreted as the numbers 0 through 3.  Taking each group of two genomic bases, there are 16 combinations:

```
AA -> 0
AC -> 1
AG -> 2
AT -> 3

CA -> 4
CC -> 5
CG -> 6
CT -> 7

GA -> 8
GC -> 9
GG -> 10
GT -> 11

TA -> 12
TC -> 13
TG -> 14
TT -> 15
```

Ok, I actually used the opposite endianness, but that's an unimportant implementation detail.

With a little artistic interpretation, we can map this to a 16 note scale:

![Image of a scale with sixteen notes](https://raw.githubusercontent.com/JeffIrwin/music-of-the-sars/master/doc/scale.PNG)

The complete SARS-CoV-2 genome has about 30 kb (kilobases), so this gives us about 15,000 notes of "music".
