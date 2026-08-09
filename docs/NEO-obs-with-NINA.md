# NEO Observations with N.I.N.A and the IAS Astro Python Scripts

## N.I.N.A Profiles

### IAS Telescope Remote2
Use profile "STD - Remote2 PHD2 NEOs" or "STD - Remote2 Mount Dither NEOs".

### IAS Telescope Remote3
Use profile "STD - Remote3 PHD2 NEOs" or "STD - Remote3 Mount Dither NEOs".

Images are stored under Image file path > _asteroids_YYYY-MM-DD > TARGET, must be the same as the 
```"subdir": "_asteroids_{1}"```
setting in nina-create-sequence.json. All dates use the DATEMINUS12 convention.

Important! N.I.N.A Image file pattern setting: ```_asteroids_$$DATEMINUS12$$\$$TARGETNAME$$\$$TARGETNAME$$_$$IMAGETYPE$$_$$DATETIME$$_$$FILTER$$_$$EXPOSURETIME$$s_$$SENSORTEMP$$_$$READOUTMODE$$_G$$GAIN$$_O$$OFFSET$$_$$FRAMENR$$```

## nina-create-sequence2

See [NEO-obs-planner.md](NEO-obs-planner.md)


## nina-zip-data

Part of my [IAS astro repository](https://github.com/phtnnz/astro)

nina-zip-data.py runs in parallel with the observation sequence in N.I.N.A, waiting for data to be flagged as ".ready". Compression default is fastest to speed up the archiving. The _YYYY-MM-DD suffix to _asteroids will be added automatically.

```
nina-zip-data.py -v --ready --subdir=_asteroids
```
Alternatively use the ```run-asteroids.bat``` batch file.

Example Output:

```
nina-zip-data.py -v --ready --subdir=_asteroids
nina-zip-data: config file .\.config\nina-zip-config.json
nina-zip-data: config keys: numenor-onedrive numenor IAS-Hakos-3-old IAS-Hakos-3 Hakos-Lukas-NEW IAS-Hakos-2
nina-zip-data: Data directory = D:\Users\remote\Documents\NINA-Data
nina-zip-data: Dest directory = iasdata:remote-upload2
nina-zip-data: Dest subdir    = 2025/08
nina-zip-data: Tmp directory  = D:\Users\remote\Documents\NINA-Tmp
nina-zip-data: 7z program     = C:\Program Files\7-Zip\7z.exe
nina-zip-data: rclone program = C:\Tools\rclone\rclone.exe
nina-zip-data: Use rclone     = True
nina-zip-data: Date minus 12h = 2025-08-20
nina-zip-data: Subdir         = _asteroids
nina-zip-data: WARNING: directory D:\Users\remote\Documents\NINA-Data\_asteroids_2025-08-20 doesn't exist, creating it
nina-zip-data: scanning directory D:\Users\remote\Documents\NINA-Data\_asteroids_2025-08-20
Waiting for ready data ... (Ctrl-C to interrupt)
```

Once a target is finished, all data will be packed in a 7z archive and uploaded.

```
[...]
nina-zip-data: target ready: 2025-08-20 003 P22d84P (n036)
2025-08-20 21:13:05 archiving target 2025-08-20 003 P22d84P (n036)
==================================================================
nina-zip-data: zip file D:\Users\remote\Documents\NINA-Tmp\2025-08-20 003 P22d84P (n036).7z
nina-zip-data: run C:\Program Files\7-Zip\7z.exe a -t7z -mx1 -r -spf D:\Users\remote\Documents\NINA-Tmp\2025-08-20 003 P22d84P (n036).7z 2025-08-20 003 P22d84P (n036)

7-Zip 25.00 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-07-05

Scanning the drive:
1 folder, 42 files, 470266473 bytes (449 MiB)

Creating archive: D:\Users\remote\Documents\NINA-Tmp\2025-08-20 003 P22d84P (n036).7z

Add new data to archive: 1 folder, 42 files, 470266473 bytes (449 MiB)

Files read from disk: 42
Archive size: 232694852 bytes (222 MiB)
Everything is Ok
==================================================================
nina-zip-data: upload to iasdata:remote-upload2 (+subdir)
nina-zip-data: run C:\Tools\rclone\rclone.exe moveto D:\Users\remote\Documents\NINA-Tmp\2025-08-20 003 P22d84P (n036).7z iasdata:remote-upload2/_asteroids/2025/08/_asteroids_2025-08-20/2025-08-20 003 P22d84P (n036).7z -v -P
2025/08/20 21:22:35 INFO  : 2025-08-20 003 P22d84P (n036).7z: Copied (new)
2025/08/20 21:22:35 INFO  : 2025-08-20 003 P22d84P (n036).7z: Deleted
Transferred:      221.915 MiB / 221.915 MiB, 100%, 165.286 KiB/s, ETA 0s
Checks:                 1 / 1, 100%
Deleted:                1 (files), 0 (dirs), 221.915 MiB (freed)
Renamed:                1
Transferred:            1 / 1, 100%
Elapsed time:      6m31.3s
2025/08/20 21:22:35 INFO  :
Transferred:      221.915 MiB / 221.915 MiB, 100%, 165.286 KiB/s, ETA 0s
Checks:                 1 / 1, 100%
Deleted:                1 (files), 0 (dirs), 221.915 MiB (freed)
Renamed:                1
Transferred:            1 / 1, 100%
Elapsed time:      6m31.3s
==================================================================
[...]
```

Archives will be uploaded to the S3 buckets remote-upload2 / remote-upload3 and a subdirectory structure SUBDIR/YYYY/MM/SUBDIR_YYYY-MM-DD. SUBDIR (--subdir option) for NEOs is "_asteroids".
