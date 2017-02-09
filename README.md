**This is a cli tool for (de)interleaving files**
**Though its currently in the 'unstable' branch of cps2-file-manip, it will probably fork off into its own deal**
**tested to work on python3.6, confirmed to not work on python2.7**


**what it does**
* lets you (de)interleave files

**how to install**
* clone / download the repo
* pip install path/to/archive

**features**
* automatically recognizes whether to interleave or deinterleave based on number of input files
* can interleave an arbitrary amount of files together by an arbitrary number of bytes (this entire claim is untested)
* can deinterleave a file into an arbitrary amount of files together by an arbitrary number of bytes (this entire claim is untested)

**example use**
* deinterleave a file - saving to current working directory with default file name 
cps2-file-manip FILE NBYTES NOUTPUTS -v
* deinterleave a file - saving to a different directory with custom file name
cps2-file-manip FILE NBYTES NOUTPUTS -o testdir\howdy.pardner -v 
* deinterleave a file - saving to a different directory with default file name 
cps2-file-manip FILE NBYTES NOUTPUTS -o testdir\ -v

* interleave files - saving to current working directory with default file name
cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -v
* interleave files - saving to a different directory with custom file name
cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -o testdir\yeehaw -v
* interleave files - saving to a different directory with default file name 
cps2-file-manip FILE1 FILE2 .. FILEN NBYTES -o testdir\ -v
