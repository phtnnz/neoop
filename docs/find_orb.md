# Find_orb Command Line

Reference:  
https://www.projectpluto.com/fo_usage.htm


## Example Usage
```
cd .\find_orb\
.\fo64 DATAFILE  -C M49  -e ephem.txt  -E 3,5,10,27,28,29,35,36  "EPHEM_START=2026 Aug 24 22:00" EPHEM_STEPS=12 EPHEM_STEP_SIZE=5m
```

3 = Alt/az output  
5 = Apparent angular motion (total motion and PA)  
10 = Round to nearest step. If the ephem starts at 03:14:15.9 and the step size is one minute, the first output will be for 03:14  
27 = Show moon's altitude  
28 = Show moon's azimuth  
29 = Sky brightness, in magnitudes/arcsec^2  
35 = SNR  
36 = Exposure length

Text ephemeris in ```ephem.txt```, JSON ephemeris in ```ephemeri.json```
