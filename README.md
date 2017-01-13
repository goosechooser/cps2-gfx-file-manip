# What it does
* lets you (de)interleave CPS2 graphics files

#How to install
* clone / download the repo
* cd cps2-gfx-file-manip
* pip install .

#Example use
* cps2-file-manip gfx\sfx.14m -i (interleave sfx.14m, sfx.16m, sfx.18m, sfx.20m)
* cps2-file-manip gfx\sfx.14m.16m.18m.20m.combined -d -v (deinterleave file with verbose flag)
* cps2-file-manip -h (help)

# dont @ me about roms