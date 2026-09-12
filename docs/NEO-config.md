# NEO Config Parameters

## JSON Config Files

All scripts search the corresponding JSON config in the following directories and in this order:
- Current directory/.config/
- Current directory/.config/astro-python/
- %LOCALAPPDATA%/astro-python/
- %APPDATA%/astro-python/
- All directories from Python search path sys.path with added /.config/

Run ```python -c "import sys; print('\n'.join(sys.path))"``` to list the search path.

See sample-config/ in the repository for configuration examples.


## Config file: ```neo-config.json```

```
{
    "requests_timeout":         60,
```
Timeout for web URL requests
```
    "##1": "Config for NEOCP planning (mpcneocp)",
    "exposure_times":           [ 2, 5, 10, 15, 20, 30, 45, 60 ],
```
List of used exposure times
```
    "url_neocp_query":          "https://cgi.minorplanetcenter.net/cgi-bin/confirmeph2.cgi",
    "url_neocp_list":           "https://minorplanetcenter.net/iau/NEO/neocp.txt",
    "url_pccp_list":            "https://minorplanetcenter.net/iau/NEO/pccp.txt",
```
URLs of MPC NEOCP pages and lists
```
    "neo_obs_data_dir":         "NEOOP-data",
```
Directory for log, observation plan, exposure data, sky plot image
```
    "code":                     "M49",
```
MPC station code of location
```
    "neocp_mag_limit":          20.5,
```
Magnitude limit for NEOCP objects
```
    "sbwobs_mag_limit":         19.5,
```
Magnitude limit for SBWObs objects
```
    "min_alt":                  26,
```
Minimum altitude of objects
```
    "pixel_tolerance":          2,
```
Tolerance for moving objects to calculate max exposure time / pixel
```
    "pixel_min_motion":         6,
```
Min total motion of objects to calculate number of exposures / pixel
```
    "resolution":               1.33,
```
Telescope and camera resolution / arcsec
```
    "dead_time_slew_center":    90,
```
Dead time for slewing to target / sec
```
    "dead_time_af":             100,
```
Dead time for autofocus / sec
```
    "dead_time_image":          1.5,
```
Dead time *per* image / sec
```
    "dead_time_guiding":        30,
```
Dead time to start guiding / sec
```
    "safety_margin":            150,
```
Dead time safety margin
```
    "base_exp":                 240,
```
Base total exposure for objects at ```base_mag```` magnitude / sec
```
    "base_mag":                 18,
```
Base magnitude
```
    "min_n_obs":                4,
```
Min number of required observations, otherwise skipped
```
    "max_notseen":              4,
```
Max time object not seen, otherwise skipped / days
```
    "opt_alt":                  50,
```
Optimal, preferred altitude of objects
```
    "min_n_exp":                30,
```
Min number of exposures per object
```
    "max_n_exp":                250,
```
Max number of exposures per object
```
    "min_perc_required":        45,
```
Min percentage of required total exposure time, otherwise skipped
```
    "min_moon_dist":            50,
```
Min required Moon distance, otherwise skipped / degrees
```
    "min_arc":                  0.05,
```
Min required arc length, otherwise skipped / days
```
    "##2": "Config for JPL What's Observable? (sbwobs)",
    "sbwobs_url":   "https://ssd-api.jpl.nasa.gov/sbwobs.api",
```
URL of JPL SBWobs API
```
    "output_sort":  "vmag",
```
Sort order for JPL SBWObs
```
    "sb_ns":        "u",
```
JPL SBWObs parameter ```sb-ns```: ```n```=numbered objects, ```u```=unnumbered objects
```
    "sb_kind":      "a",
```
JPL SBWObs parameter ```sb-kind```: ```a```=asteroid, ```c```=comet
```
    "sb_group":     "neo",
```
JPL SBWObs parameter ```sb-group```: ```neo```=Near Earth Object, ```pha```=Potentially Hazardous Asteroid
```
    "##3": "Config for MPC Dates Of Last Observation Of NEOs (sbwobs)",
    "lastobs_url":      "https://www.minorplanetcenter.net/iau/NEO/LastObsNEO.txt",
    "customize_page":   "https://www.minorplanetcenter.net/iau/lists/Customize.html",
    "customize_url":    "https://cgi.minorplanetcenter.net/cgi-bin/customize.cgi",
```
URLs of MPC last observation lists
```
    "##3a": "Automatically calculated from location in neo-obs-planner and sbwobs",
    "min_dec":      -90,
```
Min DEC value, automatically calculated from location
```
    "max_dec":      40,
```
Max DEC value, automatically calculated from location
```

    "max_last_obs":     14,
```
Max time for object not seen in SBWObs filtering / days  
(Redundant with ```max_notseen```?)
```
    "min_uncertainty":  3,
```
Min uncertainty from MPC last observation lists in SBWObs filtering
```
    "##4": "Config for Previous NEO Confirmation Page Objects",
    "prev_neocp_url":   "https://www.minorplanetcenter.net/iau/NEO/ToConfirm_PrevDes.html",
    "mpc_url":          "https://www.minorplanetcenter.net"
```
URLs of MPC previous NEOCP objects and MPC
```
}
```

FIXME: add new config stuff
