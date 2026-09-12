@echo off
set TMPDIR=tmp
set FIND_ORB_DIR=find_orb
set PROG_7Z=C:\Program Files\7-Zip\7z.exe

if not exist %TMPDIR% mkdir %TMPDIR%
if not exist %FIND_ORB_DIR% mkdir %FIND_ORB_DIR%

echo Retrieving find_orb from project pluto ...

set FIND_C64=https://www.projectpluto.com/find_c64.zip
set FIND_C64_OUT=find_c64.zip
set FO=https://www.projectpluto.com/devel/fo64.exe
set FO_OUT=fo64.exe
set JPL_EPH=ftp://ssd.jpl.nasa.gov/pub/eph/planets/Linux/de423/lnxp1800p2200.423
set JPL_EPH_OUT=lnxp1800p2200.423
set OBSCODES=https://www.minorplanetcenter.net/iau/lists/ObsCodes.html
set OBSCODES_OUT=ObsCodes.htm
set OBSCODES_DEL=ObsCodesF.html

curl -s -o %TMPDIR%\%FIND_C64_OUT% %FIND_C64%
echo Downloaded %FIND_C64%
"%PROG_7Z%" e -o%FIND_ORB_DIR% %TMPDIR%\%FIND_C64_OUT%
echo Unpacked %TMPDIR%\%FIND_C64_OUT%

curl -s -o %FIND_ORB_DIR%\%FO_OUT% %FO%
echo Downloaded %FO%

curl -s -o %FIND_ORB_DIR%\%JPL_EPH_OUT% %JPL_EPH%
echo Downloaded %JPL_EPH%

curl -s -o %FIND_ORB_DIR%\%OBSCODES_OUT% %OBSCODES%
echo Downloaded %OBSCODES%

del /q %FIND_ORB_DIR%\%OBSCODES_DEL%
echo Deleted %OBSCODES_DEL%
