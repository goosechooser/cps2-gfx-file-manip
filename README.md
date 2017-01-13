##This is a cli tool based off [gfx_file_handler] (https://github.com/goosechooser/cps2-gfx-editor) but for people who dont want all the other modules in that repo

#:weary: what it does :weary:
* lets you (de)interleave CPS2 graphics files

#how to install
* clone / download the repo
* cd cps2-gfx-file-manip
* pip install .

#example use :fire: :100: :100:
* cps2-file-manip gfx\sfx.14m -i (interleave sfx.14m, sfx.16m, sfx.18m, sfx.20m)
* cps2-file-manip gfx\sfx.14m.16m.18m.20m.combined -d -v (deinterleave file with verbose flag)
* cps2-file-manip -h (help)

# :clap: dont :clap: @ :clap: me :clap: about :clap: roms :clap: :joy: :joy: :joy: :joy: 