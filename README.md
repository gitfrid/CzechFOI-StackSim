### CzechFOI-StackSim 
**CzechFOI Investigation into whether normalized population trends per age and stacking events are fairly distributed**

<br>

**Hypothesis: There is no way to compare vaccinated (VX) and unvaccinated (UVX) groups perfectly fair and exactly by measurement or mathematically when the groups are defined by a time-dependent, non-random vaccination schedule, even if the underlying individual death rates are the same!**

<br>Phyton script [B) event_stacking.py](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Py%20Scripts/B%29%20event_stacking.py)
<br>
<br>**Intention of code:**
    <br> Simulate a homogeneous population (split by age), where people:
    <br> -> Die randomly at a constant rate over time (Day 0..1100)
    <br> -> Some get vax on specific days. (Doses curve from real FOI data)
    <br> -> Compare how many people die in each group (normalized):
    <br> -> Vaccinated (vx), Unvaccinated (uvx)
    <br> **The idea is to see whether vx people die as often as uvx people — assuming everyone is otherwise equal from a homogen total population.**

<br>**But in practice, the code:**
    <br> Assigns a death date to everyone randomly ✅
    <br> Assigns doses starting at a certain day (FOI Data) ✅
    <br> **Only labels a person as "vaccinated" if their death date is after their dose day! ❌**
    <br> So people who die early are forced into the unvaccinated group 
    <br>
<br>**Simulates a homogeneous population with a constant death rate, then splits it into (vx) and (uvx) groups. However, it introduces bias by only allowing people who survive long enough to be (vx). This gives vx individuals an unfair survival advantage, making vx appear beneficial — even if it had zero actual effect..**

_________________________________________
**Death and Population Trends per Age simulation - Immortal Time Bias**

This example illustrates the normalized death rate for individuals aged 70 within a heterogeneous population, where the random death rate remains constant over time (from day 0 to day 1100). 
The individuals in the vx group are randomly selected and shifted from the total population based on the number of doses administered to that age group. (Distribution of doses over time from the real FOI-Data )  


**Total, vx and uvx normalized death rates should theoretically be equal**<br>
Shows normalized death rate for AGE 70 - simulated.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM.png width="1280" height="auto">
<br>

Shows raw death rate for AGE 70 - simulated.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age (Aligned to Doses)**

**Stacked normalized curves (total, vx and uvx) should  theoretically have a horizontal course at the same level**<br>
Stacked curve normalized for AGE 70 - simulated<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM.png width="1280" height="auto">
<br>

Stacked curve raw simulated for AGE 70 - simulated.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM.html)
_________________________________________
<br>

### Same sample with immune protection lag bias 
The study says protection starts after 21 days (the immune lag).
VX people are wrongly counted as UVX during the delay period - when not handled correctly.
Same homogeneous population as above with same random constant death rate over time 
_________________________________________
**Total, vx and uvx normalized death rates should theoretically be equal**<br>
Shows normalized death rate for AGE 70 - simulated with POST_VX_DELAY=21 days.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_POSTVXDELAY_21_SIM.png width="1280" height="auto">
<br>

Shows raw death rate for AGE 70 - simulated with POST_VX_DELAY=21 days.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_POSTVXDELAY_21_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_POSTVXDELAY_21_SIM.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age (Aligned to Doses)**

**Stacked normalized curves (total, vx and uvx) should  theoretically have a horizontal course at the same level**<br>
Stacked curve normalized for AGE 70 - simulated with POST_VX_DELAY=21 days<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_POSTVXDELAY_21_SIM.png width="1280" height="auto">
<br>

Stacked curve raw simulated for AGE 70 - simulated with POST_VX_DELAY=21 days.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_POSTVXDELAY_21_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_POSTVXDELAY_21_SIM.html)
_________________________________________
<br>

### Same sample with protection lag and few extra deaths 
Alright, let’s now add a few additional deaths to the homogeneous population and observe what happens when we randomly split them into (vx) and (uvx) groups.
<br>
<br>Note that the split is random, except that individuals who died before receiving a dose are not assigned to the (vx) group — **since you think including them would be paradoxical.** Instead, another random living individual is selected for (vx) group in their place.
<br>
<br>It is statistically difficult to detect a signal from such a small number of additional deaths, as the counterfactual baseline is unknown.
_________________________________________
**Total, vx and uvx normalized death rates should theoretically be equal**<br>
Shows normalized death rate for age 70 — simulated with POST_VX_DELAY = 21 days, and one extra death per 5,000 doses, occurring on a random day within a 248-day time window. These extra deaths are distributed to the hetrogen population around the time the doses were administered.<br> 
<br>
<img  src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_EXTRA_D_SIM.png width="1280" height="auto">
<br>

Shows rwaw death rate for age 70 — simulated with POST_VX_DELAY = 21 days, and one extra death per 5,000 doses, occurring on a random day within a 248-day time window.<br>
<br>
<img  src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_EXTRA_D_RAW_SIM.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_EXTRA_D_SIM.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age (Aligned to Doses)**

Stacked curve normalized for AGE 70 - simulated with POST_VX_DELAY=21 days, and one extra death per 5000 Doses on random day inside a time window of 248 days<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_EXTRA_D_SIM.png width="1280" height="auto">
<br>

Stacked curve raw simulated for AGE 70 - simulated with POST_VX_DELAY=21 days, and one extra death per 5000 Doses on random day inside a time window of 248 days.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_EXTRA_D_RAW_SIM.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_EXTRA_D_SIM.html)

_________________________________________
<br>

## Comparison with real FOI Data
_________________________________________
**Death and Population Trends per Age real FOI data**

Shows normalized death rate for AGE 70 - real.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_REAL.png width="1280" height="auto">
<br>

Shows raw death rate for AGE 70 - real.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_RAW_REAL.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age real FOI data (Aligned to Doses)**

Stacked curve normalized for AGE 70 - real.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_REAL.png width="1280" height="auto">
<br>

Stacked curve raw for AGE 70 - real.<br><br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_RAW_REAL.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths.html)
_________________________________________

<br>**Abbreviations:** The figures are per age group from the CSV files in the TERRA folder:
| **Deaths**        | **Definition**                                             | **Population/Doses**  | **Definition**                                        |
|-------------------|------------------------------------------------------------|-----------------------|-------------------------------------------------------|
| NUM_D             | Number deaths                                              | NUM_POP               | Total population of people                                          |
| NUM_DUVX          | Number unvaxed deaths                                      | NUM_UVX               | Number of unvaxed people                              |
| NUM_DVX           | Number vaxed deaths                                        | NUM_VX                | Number of vaxed people  (who get first dose)                              |
| NUM_DVD1-DVD7     | Number deaths doses 1 - 7                                  | NUM_VD1-VD7           | Number of vax doses 1 - 7                             |
| NUM_DVDA          | Number deaths from all doses                               | NUM_VDA               | Total number of all vax doses (sum)                   |
<br>

Uses real Czech FOI (Freedom of Information) data, to calculate normalized death rates and all doses given curves. 
[Python Scripts](https://github.com/gitfrid/CzechFOI-StackSim/tree/main/Py%20Scripts) process and visualize CSV data from the [TERRA folder](https://github.com/gitfrid/CzechFOI-StackSim/tree/main/TERRA), generating interactive HTML plots. To interact with the plots, click on a legend entry to show/hide curves.

Download the processed plots for analysis from the [Plot Results Folder](https://github.com/gitfrid/CzechFOI-StackSim/tree/main/Plot%20Results). 

Dates are counted as the number of days since [January 1, 2020](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/Days%20to%20Date%20Translation%20Day%20Date%20Translation/Days%20to%20Date%20Translation%20Day%20Date%20Translation.png), for easier processing. "AGE_2023" represents age on January 1, 2023. <br>The data are optionally normalized per 100,000 for comparison.

Access the original Czech FOI data from a [Freedom of Information request](https://github.com/PalackyUniversity/uzis-data-analysis/blob/main/data/Vesely_106_202403141131.tar.xz). To learn how the Pivot CSV files in the TERRA folder were created, see the [wiki](https://github.com/gitfrid/CzechFOI-DA/wiki)
_________________________________________

### Software Requirements:
- [Python 3.12.5](https://www.python.org/downloads/) to run the scripts.
- [Visual Studio Code 1.92.2](https://code.visualstudio.com/download) to edit and run scripts.
- [Optional - DB Browser for SQLite 3.13.0](https://sqlitebrowser.org/dl/) for database creation, SQL queries, and CSV export.

### Disclaimer:
**The results have not been checked for errors. Neither methodological nor technical checks or data cleansing have been performed.**
