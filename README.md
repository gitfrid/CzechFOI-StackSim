### CzechFOI-SIM 
**Czech FOI Simulation Analysis** 
<br>
<br>**Investigates whether there is a reliable statistical way to determine the dAEFI rate when the baseline is unknown (real world).**
**As far as I know, this (vital) problem is still waiting for the head that can solve it?**

Simulates dAEFIs to analyse the impact on the curve and back-calculate the dAEFIs rate (comparing known and unknown baseline).
Uses real Czech FOI (Freedom of Information) data, or generates d, dvx, duvx data in modulated sine wave form.

Simulated data can be used to check for calculation errors in your code, it is possible to create a CSV file with the data of all Plot curves (from day 1-1534).

The [Python Scripts](https://github.com/gitfrid/CzechFOI-SIM/tree/main/Py%20Scripts) process and visualize CSV data from the [TERRA folder](https://github.com/gitfrid/CzechFOI-SIM/tree/main/TERRA), generating interactive HTML plots. <br>Each plot compares two age groups. To interact with the plots, click on a legend entry to show/hide curves.

**Refactored Scripts AF) and AG)** compare AG groups (e.g., 1-year intervals) by calculating differences between closely positioned age groups. The differences are summed, and simulated dAEFIs are added to examine the curves with and without dAEFIs. Multiple AG groups are plotted into a single HTML file for comparison

Download the processed plots for analysis from the [Plot Results Folder](https://github.com/gitfrid/CzechFOI-SIM/tree/main/Plot%20Results/dAEFI). Or simply adapt and run the [Python script](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AB%29%20backcalc%20dAEFI%20simulation.py) to meet your own analysis requirements!

Dates are counted as the number of days since [January 1, 2020](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/Days%20to%20Date%20Translation%20Day%20Date%20Translation/Days%20to%20Date%20Translation%20Day%20Date%20Translation.png), for easier processing. "AGE_2023" represents age on January 1, 2023. <br>The data can optionally be normalized per 100,000 for comparison.

Access the original Czech FOI data from a [Freedom of Information request](https://github.com/PalackyUniversity/uzis-data-analysis/blob/main/data/Vesely_106_202403141131.tar.xz). To learn how the Pivot CSV files in the TERRA folder were created, see the [wiki](https://github.com/gitfrid/CzechFOI-DA/wiki)

<br>**Abbreviations:** The figures are per age group from the CSV files in the TERRA folder:
| **Deaths**        | **Definition**                                             | **Population/Doses**  | **Definition**                                        |
|-------------------|------------------------------------------------------------|-----------------------|-------------------------------------------------------|
| NUM_D             | Number deaths                                              | NUM_POP               | Total people                                          |
| NUM_DUVX          | Number unvaxed deaths                                      | NUM_UVX               | Number of unvaxed people                              |
| NUM_DVX           | Number vaxed deaths                                        | NUM_VX                | Number of vaxed people                                |
| NUM_DVD1-DVD7     | Number deaths doses 1 - 7                                  | NUM_VD1-VD7           | Number of vax doses 1 - 7                             |
| NUM_DVDA          | Number deaths from all doses                               | NUM_VDA               | Total number of all vax doses (sum)                   |
| dAEFI             | simulated death Adverse Events following imunis.             |                       |                                                       |
<br>

_________________________________________
**DoWhy Analysis of Causal Impact Estimates**

**Phyton script [AI) dowhy diff all-agegrp-in-same-plot](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AI%29%20dowhy%20diff%20all-agegrp-in-same-plot.py)**
Uses the DoWhy Library https://github.com/py-why/dowhy
<br>
<p>DoWhy is a Python library for causal inference that allows modeling and testing of causal assumptions, based on a unified language for causal inference.
<strong>See the book <em>Models, Reasoning, and Inference</em> by Judea Pearl for deeper insights, that goes far beyond my horizon.</strong></p>
<br>

**mean (RAW) blue** actual raw data averages of doses and deaths for an age group, along with estimated causal impact of doses on deaths by DoWhy.
**mean (AEF) red** simulation of one additional death per 5000 doses, added to the raw data, along with estimated causal impact of doses on deaths by DoWhy.
<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AW)%20dowhy%20diff%20all-agegrp-in-same-plot/AW)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20mean%20AG_15-85.png width="1280" height="auto">
<br>
<br>
DoWhy causal impact estimates: comparing real (RAW) data in green with simulated (AEF) data in yellow, where one additional death per 5000 doses is simulated, for age group 15-84
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AW)%20dowhy%20diff%20all-agegrp-in-same-plot/AW)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20estimate%20AG_15-85.png width="1280" height="auto">
<br>
<br>
The difference between DoWhy's estimate of the causal effect of the simulated data (AEF) and the real data (RAW), converted into the number of doses per death.
**DoWhy's estimate of the causal effect per number of doses is fairly close to the simulation of 5000 doses per additional death.**
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AW)%20dowhy%20diff%20all-agegrp-in-same-plot/AW)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20Doses%20per%20Death%20AG_15-85.png width="1280" height="auto">
<br>
<br>
Phase diagram of absolute values: D_Curve to Doses_curve for days 0-1533 and age group 15-84 (RAW, AEF) 
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AW)%20dowhy%20diff%20all-agegrp-in-same-plot/AW)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20phase%20curve%20AG_15-85.png width="1280" height="auto">
<br>
[Download html](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AW%29%20dowhy%20diff%20all-agegrp-in-same-plot/AW%29%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20AG_15-85.html)
<br>
<br>
_________________________________________
**Below is the same simulation, but instead of using the absolute values of doses and deaths for each age group, it shows the differences in doses and deaths between neighboring age groups at one-year intervals. This method helps to cancel out external disturbances.**
<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AX)%20dowhy%20diff%20all-agegrp-in-same-plot/AX)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20mean%20AG_15-85.png width="1280" height="auto">
<br>
<br>
DoWhy causal impact estimates: comparing real (RAW) data in green with simulated (AEF) data in yellow, where one additional death per 5000 doses is simulated, for age group 15-84
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AX)%20dowhy%20diff%20all-agegrp-in-same-plot/AX)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20AG_15-85.png width="1280" height="auto">
<br>
<br>
The difference between DoWhy's estimate of the causal effect of the simulated data (AEF) and the real data (RAW), converted into the number of doses per death.
**DoWhy's estimate of the causal effect per number of doses is fairly close to the simulation of 5000 doses per additional death.**
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AX)%20dowhy%20diff%20all-agegrp-in-same-plot/AX)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20Doses%20per%20Death%20AG_15-85.png width="1280" height="auto">
<br>
<br>
Phase diagram difference values: D_Curve and Doses_curve between neighboring age groups at one-year intervals, for days 0-1533 and age group 15-84 (RAW, AEF) 
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AX)%20dowhy%20diff%20all-agegrp-in-same-plot/AX)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20phase%20curve%20AG_15-85.png width="1280" height="auto">
<br>

[Download html](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AX%29%20dowhy%20diff%20all-agegrp-in-same-plot/AX%29%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20AG_15-85.html)
**Phyton script [AX) dowhy diff all-agegrp-in-same-plot](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AX%29%20dowhy%20diff%20all-agegrp-in-same-plot.py)**
<br>
_________________________________________
**Below is the same simulation. Instead of comparing the real curve with the simulated curve, I compared the real absolute data (RAW) of two neighboring age groups. The population at one-year intervals should be quite similar, thus minimizing possible confounders**
<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AY)%20dowhy%20diff%20all-agegrp-in-same-plot/AY)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20mean%20AG_15-85.png width="1280" height="auto">
<br>
<br>
DoWhy causal impact estimates: comparing real absolute (RAW) data in yellow with the absolute (RAW) data of neigbouhr age group one year appart, for age group 15-84
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AY)%20dowhy%20diff%20all-agegrp-in-same-plot/AY)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20AG_15-85.png width="1280" height="auto">
<br>
<br>
The difference between DoWhy's estimate of the causal effect of the absolute real data (RAW) of two neigboughr age groups, converted into the number of doses per death for age group 15-84
**DoWhy's estimate of the causal effect per number of doses, the outliers are not visible, because zoomed in**
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AY)%20dowhy%20diff%20all-agegrp-in-same-plot/AY)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20Doses%20per%20Death%20AG_15-85.png width="1280" height="auto">
<br>
<br>
Phase diagram difference values: D_Curve and Doses_curve between neighboring age groups at one-year intervals, for days 0-1533 and age group 15-84 (RAW, AEF) 
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AY)%20dowhy%20diff%20all-agegrp-in-same-plot/AY)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20phase%20diagram%20AG_15-85.png width="1280" height="auto">
<br>

[Download html](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AY%29%20dowhy%20diff%20all-agegrp-in-same-plot/AY%29%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20AG_15-85.html)
**Phyton script [AY) dowhy diff all-agegrp-in-same-plot](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AY%29%20dowhy%20diff%20all-agegrp-in-same-plot.py)**
<br>
_________________________________________
**Here Instead of comparing the real curve with the simulated curve, I compared the real (RAW) difference of Doses_Curve and Death_Curve for two neighboring age groups. This method helps to cancel out external disturbances. The population at one-year intervals should be quite similar, thus minimizing possible confounders**
<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20mean%20AG_15-85.png width="1280" height="auto">
<br>
<br>
DoWhy causal impact estimates: comparing death and doses difference in real (RAW) data between two neigbour age groups one year appart, for age group 15-84
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20AG_15-85.png width="1280" height="auto">
<br>
<br>
The difference between DoWhy's estimate of the causal effect of difference in doses deaths of real data (RAW) between two neigbour age groups, converted into the number of doses per death.
**DoWhy's estimate of the causal effect per number of doses, the outliers are not visible, because zoomed in**
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20causal%20estimate%20Doses%20per%20Death%20AG_15-85.png width="1280" height="auto">
<br>
<br>
Phase diagram difference values: D_Curve and Doses_curve between neighboring age groups at one-year intervals, for days 0-1533 and age group 15-84 (RAW, AEF) 
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot/AZ)%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20phase%20diagram%20AG_15-85.png width="1280" height="auto">
<br>

[Download html](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AZ%29%20dowhy%20diff%20all-agegrp-in-same-plot/AZ%29%20dowhy%20diff%20all-agegrp-in-same-plot%20dAEFI%20causalimpact%20AG_15-85.html)
**Phyton script [AZ) dowhy diff all-agegrp-in-same-plot](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AZ%29%20dowhy%20diff%20all-agegrp-in-same-plot.py)**
<br>
_________________________________________
**dAEFI simulation known Basline. <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_50-54**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20known%20basline%20DAY_RNG_250%20WD_14%20%20AG_50-54.png width="1280" height="auto">
<br>

**If the baseline is known (which is not the case in practice), the estimated dAEFIs per dose are quite accurate, e.g., 4408 vs. 5000.** .

_________________________________________
**dAEFI simulation known Basline. <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_75-79**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20known%20basline%20DAY_RNG_250%20WD_14%20%20AG_75-79.png width="1280" height="auto">
<br>

**The estimated dAEFIs per dose, e.g., 4179 vs. 5000.** .
_________________________________________
**dAEFI simulation unknown Basline real world. <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_50-54**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20%20AG_50-54.png width="1280" height="auto">
<br>

**If the baseline is unknown (which is the case in practice), the estimated dAEFI per dose are not reliable , e.g., 136 vs. 5000.** .

_________________________________________
**dAEFI simulation unknown Basline (real world). <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_75-79**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20%20AG_75-79.png width="1280" height="auto">
<br>

**The estimated dAEFIs per dose, e.g.,  39 vs. 5000.** .
_________________________________________

**D, DVX, DUVX plots.<br>Added dAEFIs (1/5000 Doses) vs non added AEFIs: AG_50-54 vs 75-79**
<br>
<br>
**As you can see, the added dAEFIs have little impact on the top D-curves for age group 75-79, making it hard to detect a signal without knowing the baseline.
I struggled to find a reliable method to back-calculate the dAEFIs ratio using only the moving average as the baseline (real world). This is particularly true for the older age groups.**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20d-duvx-dvx%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20%20AG_50-54.png width="1280" height="auto">
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20d-duvx-dvx%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20%20AG_75-79.png width="1280" height="auto">
<br>
_________________________________________

**dAEFI simulation known Basline. <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_54-59**
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20d-duvx-dvx%20sinus%20curve%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20%20AG_50-54.png width="1280" height="auto">
<br>

**Simulation of sinus curves for D, DVX, and DUVX, adding one dAEFI per 5000 doses in a random 1-250 day window after dose** .
The estimated dAEFIs per dose, e.g., 5138 vs. 5000 - if basline is known.
_________________________________________

**dAEFI simulation unknown Basline. <br>One dAEFI per 5000 Doses RAND_DAY_RANGE 1-250 AVG_WND 14: AG_54-59**
<br>

The legend label "pr" calculates the mortality curves for D, DUVX, and DVX, assuming that the vx and uvx populations have the same hypothetical mortality probability (distribution), see upper part of the first plot.
<br>

The lower part of the first plot shows the result of the normalized mortality curves (deaths/100,000 people - legend label "n"). Since the mortality probability for D, VX, and UVX is assumed to be identical, the normalized curves overlap.
<br>
Additionally, 1/5000 dAEFIs are added (legend label "ae")
<br>

<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/dAEFI/AB)%20backcalc%20dAEFI%20simulation%20sin%20unknown%20real%20world%20basline%20DAY_RNG_250%20WD_14%20leged%20an_pr_n%20%20AG_50-54.png width="1280" height="auto">
<br>

The estimated dAEFIs per dose, e.g., 388 vs. 5000 - if basline is unknown.
_________________________________________

**Phyton script [AC) calc dAEFI diff all-agegrp-in-same-plot](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AC%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot.py)**

The script compares age groups in 1-year intervals. 

The idea is that the two populations, which are one year apart, can be considered comparable. 

It calculates the difference in normalized death rates (per 100,000 people) and takes a rolling average of this difference as the baseline. It also calculates the difference in normalized doses administered (per 100,000 doses). However, a reliable and accurate method for calculating estimated dAEFIs has not yet been found.

Can also calculate rolling and phaseshift correlation 

For Database and CSV File creation in the Terra folder [All AG SQL Time.sql]() was used.
_________________________________________

**DIF-VDA n all AgeGroups**

Shows the estimated mean dAEFI values for AG 1 to 113.
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/Maean%20estimate%20dAEFI%20all-AgeGroups.png width="1280" height="auto">
<br>

Shows the normalized DIF-VDA (All Doses difference for all AG) 
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20n%20all%20AgeGroups.png width="1280" height="auto">
<br>
_________________________________________

**DIF-VDA Basline Mean estimate dAEFI n - Some examples of different AGs**
<br>**For AG 13-14**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG13-14.png width="1280" height="auto">
<br>**For AG 14-15**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG14-15.png width="1280" height="auto">
<br>**For AG 17-18**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG17-18.png width="1280" height="auto">
<br>
<br>**For AG 42-43**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG42-43.png width="1280" height="auto">
<br>
<br>**For AG 71-72**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG71-72.png width="1280" height="auto">
<br>
<br>**For AG 81-82**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG81-82.png width="1280" height="auto">
<br>
<br>**For AG 107-108**
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AC)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/DIF-VDA%20Basline%20Mean%20estimate%20dAEFI%20n%20AG107-108.png width="1280" height="auto">
<br>
_________________________________________

**Refactored Scripts AF)**


The [Python script](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Py%20Scripts/AF%29%20calc%20dAEFI%20diff%20norm%20all-agegrp-in-same-plot.py) calculates the differences in doses and deaths for similar age bands (one year appart), as specified in the `age_band_compare` list. It then summarizes the differences and adds dAEFIs (one per 5,000 doses). Additionally, it compares the rolling and shift correlations of the raw D-curve with the D-curve that includes the added dAEFI events.

With one dAEFI per 5,000 doses, there is no significant change in the D-curves, including the rolling Pearson correlation, making it irrelevant in this context. 
Although the amplitude of the phase shift correlation has changed significantly, this is not helpful since the baseline is unknown

<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AF)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AF)%20calc%20dAEFI%20diff%20norm%20all-agegrp-in-same-plot%20dAEFI%20AG_15-85.png width="1280" height="auto">
<br>

Zoomed in to highlight the minimal difference at 1/5,000 doses.
<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AF)%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AF)%20calc%20dAEFI%20diff%20norm%20all-agegrp-in-same-plot%20dAEFI%20AG_15-85%20zoom.png width="1280" height="auto">
<br>
<br>
[Download html](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AF%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AF%29%20calc%20dAEFI%20diff%20norm%20all-agegrp-in-same-plot%20dAEFI%20AG_15-85.html)
<br>
_________________________________________

**Refactored Scripts AG)**

This [Python script](https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot.py) employs a different approach but produces results similar to those of the AF script.
It calculates the rolling Pearson correlation based on changes in cumulative doses, revealing a strong correlation. 
However, this correlation is not relevant in the context of rare dAEFIs. Additionally, although the amplitude of the phase shift correlation changes significantly, this information is not useful without a known baseline

<br>
<img src=https://github.com/gitfrid/CzechFOI-SIM/blob/main/Plot%20Results/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot%20dAEFI%20AG_15-85.png width="1280" height="auto">
<br>
<br>

[Download html](https://github.com/gitfrid/CzechFOI-SIM/raw/main/Plot%20Results/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot/AG%29%20calc%20dAEFI%20diff%20all-agegrp-in-same-plot%20dAEFI%20AG_15-85.html)
<br>
_________________________________________

### Software Requirements:
- [Python 3.12.5](https://www.python.org/downloads/) to run the scripts.
- [Visual Studio Code 1.92.2](https://code.visualstudio.com/download) to edit and run scripts.
- [Optional - DB Browser for SQLite 3.13.0](https://sqlitebrowser.org/dl/) for database creation, SQL queries, and CSV export.

### Disclaimer:
**The results have not been checked for errors. Neither methodological nor technical checks or data cleansing have been performed.**
