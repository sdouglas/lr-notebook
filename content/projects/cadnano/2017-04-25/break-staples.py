# break-staples.py
# Shawn M Douglas, April 2017
# BSD-3 open-source license.

from datetime import datetime

import cadnano
from cadnano.document import Document
from cadnano.data.dnasequences import sequences

src_file = '/Users/shawn/Dropbox (DouglasLab)/notebooks/active/nb-shawn/content/projects/cadnano/2017-04-25/a.json'

# src_file = 'a.json'
timestamp = "{:%y%m%d-%H%M%S}".format(datetime.now())
out_file = '.'.join(src_file.split('.')[:-1] + [timestamp, 'json'])

# basic init
app = cadnano.app()
doc = app.document = Document()

# read input design
doc.readFile(src_file)
part = doc.activePart()
oligos = part.oligos()

# we might hard code the scaffold start
start_vh = 0
start_strand = 0
start_idx = 21
# cadnano2.5 makes no distinction between "scaffold" and "staples"
# we must specify the strand, 0 is always top (5->3), 1 is bottom (3'<-5')
scaf_start = (start_vh, start_strand, start_idx)

# for fun we might guess that the scaffold is simply the longest oligo
# for oligo in oligos:
#     print(oligo, oligo.length(), oligo.sequence())

oligos_by_length = sorted(oligos, key=lambda x: x.length(), reverse=True)
scaffold = oligos_by_length[0]
staples = oligos_by_length[1:]

# print(scaffold, scaffold.length(), scaffold.sequence())
p7560 = sequences['p7560']

print("Circular sequences:")
for staple in staples:
    if staple.isLoop():
        print(staple)
        for strand in staple.strand5p().generator3pStrand():
            print (strand, strand.idxs(), strand.length(), )

    # print(staple, staple.dump())

# split

# for staple in staples:
#     # print(staple, staple.length(), staple.getColor())
#     print(staple, staple.dump())

# break every staple at midpoint

# print staples

# save modified file

# part.getSequences()
