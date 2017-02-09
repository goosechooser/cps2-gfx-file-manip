## what it does
* lets you (de)interleave files

## other info
* though its currently in the 'unstable' branch of cps2-file-manip, it will probably fork off into its own deal
* tested to work on python 3.6, confirmed to not work on python 2.7

## how to install
* clone / download the repo
* pip install path/to/archive

## features
* automatically recognizes whether to interleave or deinterleave based on number of input files
* can interleave an arbitrary amount of files together by an arbitrary number of bytes (this entire claim is untested)
* can deinterleave a file into an arbitrary amount of files together by an arbitrary number of bytes (this entire claim is untested)

## usage - deinterleaving
* saving to current working directory with default file name  
`cps2-file-manip FILE NBYTES NOUTPUTS -v`

* saving to a different directory with custom file name  
`cps2-file-manip FILE NBYTES NOUTPUTS -o testdir\howdy.pardner -v`

* saving to a different directory with default file name  
`cps2-file-manip FILE NBYTES NOUTPUTS -o testdir\ -v` 

## usage - interleaving
* saving to current working directory with default file name  
`cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -v`

* saving to a different directory with custom file name  
`cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -o testdir\yeehaw -v`

* saving to a different directory with default file name  
`cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -o testdir\ -v`
