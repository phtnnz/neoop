# NEO / Comet / NEOCP Observation Planning

## NEO Obs Planner

```
usage: neo-obs-planner [-h] [-v] [--verbose-ephem] [-d] [-l LOCATION] [-f FILE] [-s START] [-e END] [-o OUTPUT] [-C] [-P] [--clear] [-M MAG_LIMIT]
                       [--neocp-mag-limit NEOCP_MAG_LIMIT] [--sbwobs-mag-limit SBWOBS_MAG_LIMIT] [-m MIN_ALT] [--neocp] [--sbwobs] [--asteroids] [--neo] [--pha]
                       [--comets] [-p PREFIX] [--force FORCE]
                       [object ...]

NEOCP/NEO observation planner

positional arguments:
  object                object name

options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose messages
  --verbose-ephem       verbose ephemerides
  -d, --debug           more debug messages
  -l, --location LOCATION
                        coordinates, named location or MPC station code, default M49
  -f, --file FILE       read list of objects from file
  -s, --start START     start time (UTC) (default naut. dusk)
  -e, --end END         end time (UTC) (default naut. dawn)
  -o, --output OUTPUT   write CSV to OUTPUT file
  -C, --csv             use CSV output format
  -P, --plot            create altitude and sky plot with objects
  --clear               clear MPC cache
  -M, --mag-limit MAG_LIMIT
                        override *mag_limits from config (see below)
  --neocp-mag-limit NEOCP_MAG_LIMIT
                        override neocp_mag_limit from config (20.5)
  --sbwobs-mag-limit SBWOBS_MAG_LIMIT
                        override sbwobs_mag_limit from config (19.5)
  -m, --min-alt MIN_ALT
                        override min_alt/elev_min from config
  --neocp               observable NEOCP objects
  --sbwobs              observable objects from JPL WOBS service
  --asteroids           sbwobs: get asteroids default=a
  --neo                 sbwobs: get NEOs default=neo
  --pha                 sbwobs: get PHAs
  --comets              sbwobs: get comets (overrides asteroids options)
  -p, --prefix PREFIX   prefix for planner data, default 20260815
  --force FORCE         skip checks for FORCE objects, include in observation plan

Version 2.2 / 2026-07-04 / Martin Junius
```

Retrieve lists and ephemerides for upcoming night
```
> neo-obs-planner.py -v --neocp --sbwobs 
```
```--neocp``` = get NEOCP objects, ```--sbwobs``` get observable "unusual" NEO objects

Use options ```-CP``` to create CSV plan output and graphic plot
```
> neo-obs-planner.py -v --neocp --sbwobs -CP
```

Use option ```-M``` to limit magnitude for *both* NEOCP and NEO around full moon phase
```
> neo-obs-planner.py -v --neocp --sbwobs -M 19.5
```

Output (Log, CSV, PNG plot) saved to ./NEOOP-data/


## NINA

```
usage: nina-create-sequence2 [-h] [-v] [-d] [-A] [-D DESTINATION_DIR] [-o OUTPUT] [-n] [-l] [-S SETTING] [--date DATE] filename [filename ...]

Create/populate multiple N.I.N.A target templates/complete sequence with data from NEO Planner CSV

positional arguments:
  filename              CSV target data list

options:
  -h, --help            show this help message and exit
  -v, --verbose         debug messages
  -d, --debug           more debug messages
  -A, --debug-print-attr
                        extra debug output
  -D, --destination-dir DESTINATION_DIR
                        output dir for created sequence
  -o, --output OUTPUT   output .json file
  -n, --no-output       dry run, don't create output files
  -l, --list-targets    list targets only
  -S, --setting SETTING
                        use template/target SETTING from config
  --date DATE           use DATE for generating sequence (default 2026-08-15)

Version: 2.0 / 2026-06-16 / Martin Junius
```

Create sequence:
```
> nina-create-sequence2.py -v --setting remote3-neo .\NEOOP-data\YYYYMMDD-neo-obs-plan.csv
```


## Utilities

```
usage: neo-list-prev [-h] [-v] [-d] [-f FILE] [object ...]

Query previous NEOCP list from MPC

positional arguments:
  object           object name

options:
  -h, --help       show this help message and exit
  -v, --verbose    verbose messages
  -d, --debug      more debug messages
  -f, --file FILE  read objects from CSV FILE

Version 0.2 / 2026-06-23 / Martin Junius
```

```
usage: neo-sbephem [-h] [-v] [-d] [-l LOCATION] [-f FILE] [-t TIME] [-J] [-a] [--obs] [--lastobs] [--clear] [object ...]

Ephemeris for solar system objects

positional arguments:
  object                object name

options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose messages
  -d, --debug           more debug messages
  -l, --location LOCATION
                        coordinates, named location or MPC station code, default M49
  -f, --file FILE       read list of objects from file
  -t, --time TIME       start time for ephemeris (1h, 5min steps)
  -J, --jpl             use JPL Horizons ephemeris, default MPC
  -a, --allnight        ephemeris for midnight +/- 8h (30min steps)
  --obs                 output MPC obs
  --lastobs             output MPC obs last row
  --clear               clear MPC cache

Version 0.5 / 2026-06-25 / Martin Junius
```

```
usage: neo-sbwobs [-h] [-v] [-d] [--asteroids] [--neo] [--pha] [--comets] [-o OUTPUT] [-M MAG_LIMIT] [-l LOCATION] [--dln] [--lastobs]

Retrieve observable NEOs/comets from JPL/MPC

options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose messages
  -d, --debug           more debug messages
  --asteroids           get asteroids default=a
  --neo                 get NEOs default=neo
  --pha                 get PHAs
  --comets              get comets (overrides asteroid options)
  -o, --output OUTPUT   write object list to OUTPUT
  -M, --mag-limit MAG_LIMIT
                        override mag_limit from config
  -l, --location LOCATION
                        coordinates, named location or MPC station code, default M49
  --dln                 use DLN list (default: DLU)
  --lastobs             use LastObs list (default: DLU)

Version 0.1 / 2026-06-22 / Martin Junius
```


## Example

```
> neo-obs-planner -v --neocp --sbwobs -CP -M 19.5   
neo-obs-planner: download ephemerides from https://cgi.minorplanetcenter.net/cgi-bin/confirmeph2.cgi
neo-obs-planner: download NEOCP list from https://minorplanetcenter.net/iau/NEO/neocp.txt
neo-obs-planner: download PCCP list from https://minorplanetcenter.net/iau/NEO/pccp.txt
neo-obs-planner: NEOCP objects (6): E000011, P12pb3b, P12pkXl, Roc4012, ST26H36, TF26H53
neo-obs-planner: query https://ssd-api.jpl.nasa.gov/sbwobs.api
neo-obs-planner: WOBS objects (34): 2001 FF90, 2001 PG14, 2007 QA2, 2007 TO74, 2008 CO, 2008 GA4, 2010 QN1, 2011 AA37, 2011 LA19, 2011 SZ21, 2012 LE11, 2013 GZ79, 2013 QC11, 2014 QS168, 2016 FQ13, 2017 KN4, 2019 LK5, 2019 LL5, 2022 HP7, 2022 MO, 2022 MO2, 2023 ME6, 2025 AL2, 2026 LJ2, 2026 MD5, 2026 MM, 2026 NT2, 2026 PB, 2026 PB6, 2026 PD, 2026 PP, 2026 PP1, 2026 PT6, 2026 PX
neo-obs-planner: query https://cgi.minorplanetcenter.net/cgi-bin/customize.cgi
neo-obs-planner: DLU objects (11): 2015 GL13, 2017 EP25, 2019 EF3, 2020 HU7, 2021 AS2, 2021 EF1, 2021 GN10, 2022 EV3, 2022 WJ1, 2025 BP4, 2026 PJ7
neo-obs-planner: 2025 BP4: last obs 2025-01-26 00:00:00.000 too old, not included
neo-obs-planner: 2022 WJ1: last obs 2022-11-19 00:00:00.000 too old, not included
neo-obs-planner: 2022 EV3: last obs 2022-03-09 00:00:00.000 too old, not included
neo-obs-planner: 2021 GN10: last obs 2021-04-15 00:00:00.000 too old, not included
neo-obs-planner: 2021 EF1: last obs 2021-03-07 00:00:00.000 too old, not included
neo-obs-planner: 2021 AS2: last obs 2021-01-09 00:00:00.000 too old, not included
neo-obs-planner: 2020 HU7: last obs 2020-04-24 00:00:00.000 too old, not included
neo-obs-planner: 2019 EF3: last obs 2019-03-12 00:00:00.000 too old, not included
neo-obs-planner: 2017 EP25: last obs 2017-03-05 00:00:00.000 too old, not included
neo-obs-planner: 2015 GL13: last obs 2015-04-16 00:00:00.000 too old, not included
neo-obs-planner: WOBS & DLU objects (0): 
neo-obs-planner: ------------------------------------------------------------
neo-obs-planner: Type   Designation Rise   Trans  Set     Vmag  U  Last Obs
neo-obs-planner: ------------------------------------------------------------
neo-obs-planner: ------------------------------------------------------------
neo-obs-planner: location lon=16d21m42.2s lat=-23d14m11.6s height=1853. m code M49
neo-obs-planner: nautical twilight 2026-08-15 17:28:10.956 / 2026-08-16 04:29:31.351 (UTC)
neo-obs-planner: already got ephemeris for E000011
neo-obs-planner: already got ephemeris for P12pb3b
neo-obs-planner: already got ephemeris for P12pkXl
neo-obs-planner: already got ephemeris for Roc4012
neo-obs-planner: already got ephemeris for ST26H36
neo-obs-planner: already got ephemeris for TF26H53
neo-obs-planner: WARNING: exposure calculation for P12pkXl failed, too fast?
neo-obs-planner: WARNING: motion=621.20 arcsec / min, limit=79.80 arcsec / min
neo-obs-planner: original object sequence: E000011, P12pb3b, Roc4012, ST26H36, TF26H53
neo-obs-planner: NEOCP E000011 2026-08-15 21:00:00.000
neo-obs-planner: PCCP P12pb3b 2026-08-16 01:00:00.000
neo-obs-planner: NEOCP Roc4012 2026-08-15 21:00:00.000
neo-obs-planner: NEOCP ST26H36 2026-08-15 20:30:00.000
neo-obs-planner: NEOCP TF26H53 2026-08-15 20:00:00.000
neo-obs-planner: sorted object sequence: TF26H53, ST26H36, E000011, Roc4012, P12pb3b
neo-obs-planner: forced objects: 
neo-obs-planner: 
neo-obs-planner: obs-planner-1 2026-08-15 09:39:45 UTC
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner:                  Score       Mag #Obs      Arc NotSeen  Time start ephemeris/ end ephemeris                 Max motion
neo-obs-planner:           /Uncertainty                                  Time before         / after meridian             Moon distance
neo-obs-planner:                                                         Time start exposure / end exposure                    Moon alt
neo-obs-planner:                                                         # x Exp = total exposure time
neo-obs-planner:                                                         RA, DEC, Alt, Az
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: TF26H53      NEOCP 100  18.4 mag    2   0.00 d   0.0 d  2026-08-15 18:00:00 / 2026-08-16 01:30:00     1.0 arcsec / min
neo-obs-planner: SKIPPED: only 2 obs (< 4)
neo-obs-planner: http://cgi.minorplanetcenter.net/cgi-bin/uncertaintymap.cgi?Obj=TF26H53&JD=2461268.312500&Ext=VAR&OC=M49&META=apm11
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: ST26H36      NEOCP  98  19.5 mag   12   0.12 d   0.0 d  2026-08-15 18:30:00 / 2026-08-16 02:00:00    13.0 arcsec / min
neo-obs-planner:                                                         2026-08-15 22:00:00 / 2026-08-15 22:30:00              133 deg
neo-obs-planner:                                                         2026-08-15 20:30:00 / 2026-08-15 20:54:34               -7 deg
neo-obs-planner:                                                         96 x 10 s = 16.0 min (100%) / total 24.6 min
neo-obs-planner:                                                         RA 20.9416 hourangle, DEC 4.6414 deg, Alt 47 deg, Az 54 deg
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: E000011      NEOCP  10  15.7 mag    2   0.00 d   1.5 d  2026-08-15 19:30:00 / 2026-08-16 03:30:00     0.6 arcsec / min
neo-obs-planner: SKIPPED: only 2 obs (< 4)
neo-obs-planner: http://cgi.minorplanetcenter.net/cgi-bin/uncertaintymap.cgi?Obj=E000011&JD=2461268.354167&Ext=VAR&OC=M49&META=apm11
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: Roc4012      NEOCP 100  19.5 mag    3   0.00 d   3.4 d  2026-08-15 17:30:00 / 2026-08-16 02:30:00     3.5 arcsec / min
neo-obs-planner: SKIPPED: only 3 obs (< 4)
neo-obs-planner: http://cgi.minorplanetcenter.net/cgi-bin/uncertaintymap.cgi?Obj=Roc4012&JD=2461268.354167&Ext=VAR&OC=M49&META=apm11
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: P12pb3b      PCCP   35  19.4 mag   45   3.53 d   0.3 d  2026-08-15 23:30:00 / 2026-08-16 04:00:00     0.1 arcsec / min
neo-obs-planner:                                                         2026-08-16 03:00:00 / 2026-08-16 03:30:00              152 deg
neo-obs-planner:                                                         2026-08-16 01:00:00 / 2026-08-16 01:36:55              -58 deg
neo-obs-planner:                                                         30 x 60 s = 30.0 min (214%) / total 36.9 min
neo-obs-planner:                                                         RA 2.0178 hourangle, DEC -2.4411 deg, Alt 44 deg, Az 69 deg
neo-obs-planner: ----------------------------------------------------------------------------------------------------------------------
neo-obs-planner: 2 object(s) planned: ST26H36, P12pb3b
neo-obs-planner: 3 object(s) skipped: TF26H53, E000011, Roc4012
neo-obs-planner: planned objects for nina-create-sequence2: NEOOP-data\20260815-neo-obs-plan.csv
neo-obs-planner: exposure data for analysis: NEOOP-data\20260815-neo-exposure.csv
neo-obs-planner: altitude and sky plot for objects: NEOOP-data\20260815-neo-obs-plot.png
```

```
> nina-create-sequence2 -v --setting remote2-neo .\NEOOP-data\20260815-neo-obs-plan.csv         
nina-create-sequence2: processing target template D:/Users/mj/Documents/N.I.N.A/Templates/NINA-Templates-IAS-Common/Target NEO.template.json
nina-create-sequence2: processing sequence template D:/Users/mj/Documents/N.I.N.A/Templates/NINA-Templates-IAS-Common/Base Remote2 NAUTICAL.json
nina-create-sequence2: target format (0=target, 1=date, 2=seq, 3=number) {1} {2:03d} {0} (n{3:03d})
nina-create-sequence2: output format (1=date) NEO-{1}.json
nina-create-sequence2: add target items to container '', empty=target area
nina-create-sequence2: timezone Africa/Windhoek
nina-create-sequence2: subdir (1=date) _asteroids_{1}
nina-create-sequence2: autofocus first target only = False
nina-create-sequence2: destination directory D:\Users\mj\Documents\N.I.N.A
nina-create-sequence2: output file NEO-2026-08-15.json
nina-create-sequence2: NINATarget(process_data): name = Target NEO
nina-create-sequence2: NINASequence(process_data): name = Base Remote2 NAUTICAL
nina-create-sequence2: processing CSV file .\NEOOP-data\20260815-neo-obs-plan.csv
nina-create-sequence2: ------------------------------------------------------------------
nina-create-sequence2: #001 2026-08-15 001 ST26H36 (n096)    20h56m29.800s +04d38m29.000s
nina-create-sequence2: UT=2026-08-15 20:30:00+00:00 / local 2026-08-15 22:30:00+02:00
nina-create-sequence2: 96x10.0s filter=L
nina-create-sequence2: ------------------------------------------------------------------
nina-create-sequence2: #002 2026-08-15 002 P12pb3b (n030)    02h01m04.100s -02d26m28.000s
nina-create-sequence2: UT=2026-08-16 01:00:00+00:00 / local 2026-08-16 03:00:00+02:00
nina-create-sequence2: 30x60.0s filter=L
nina-create-sequence2: ------------------------------------------------------------------
nina-create-sequence2: writing JSON sequence D:\Users\mj\Documents\N.I.N.A\NEO-2026-08-15.json
```

```
> nina-create-sequence2 -l --setting remote2-neo .\NEOOP-data\20260815-neo-obs-plan.csv
2026-08-15 001 ST26H36 (n096)   NEOCP 20 56 29.80 +04 38 29.0  19.5
2026-08-15 002 P12pb3b (n030)   PCCP  02 01 04.10 -02 26 28.0  19.3
```

```
> neo-list-prev.exe -v -f .\NEOOP-data\20260815-neo-obs-plan.csv
neo-list-prev: query https://www.minorplanetcenter.net/iau/NEO/ToConfirm_PrevDes.html
neo-list-prev: processing CSV file .\NEOOP-data\20260815-neo-obs-plan.csv
neo-list-prev: ST26H36   not in previous NEOCP list
neo-list-prev: P12pb3b   not in previous NEOCP list
```
