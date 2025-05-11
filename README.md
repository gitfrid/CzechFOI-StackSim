### CzechFOI-StackSim 
**CzechFOI Investigation into whether population trends per age and stacking events are fairly distributed**
<br>
<br>**Intention of code:**
    <br> Simulate a homogeneous population (split by age), where people:
    <br> -> Die randomly at a constant rate over time (Day 0..1100)
    <br> -> Some get vac on specific days. (Doses curve from real FOI data)
    <br> -> Compare how many people die in each group (normalized):
    <br> -> Vaccinated (vx), Unvaccinated (uvx)
    <br> **The idea is to see whether vx people die as often as uvx people — assuming everyone is otherwise equal from a homogen total population.**

<br>**But in practice, the code:**
    <br> Assigns a death date to everyone randomly ✅
    <br> Assigns doses starting at a certain day (FOI Data) ✅
    <br>
    <br> **Only labels a person as "vaccinated" if their death date is after their dose day! ❌**
    <br> So people who die early are forced into the unvaccinated group 
<br>**Trying to simulate vaccine effectiveness by comparing equal constant death rates, 
but introduces bias by only allowing people who survive long enough to become vx. Giving vx people an unfair survival advantage. This makes vx look better — even if vx had zero actual effect.**

_________________________________________
**D and Population Trends per Age simulation**

This example illustrates the normalized D-rate for individuals aged 70 within a heterogeneous population, where the D-rate remains constant but random over time (from day 0 to day 1100). 
The individuals in the vx group are randomly selected and shifted from the total population based on the number of doses administered to that age group, 
as indicated by FOI-Data, which tracks the distribution of doses over time.


**Total, vx and uvx normalized death rates should theoretically be equal**<br>
Shows normalized D rate for AGE 70.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM.png width="1280" height="auto">
<br>

Shows raw D rate for AGE 70.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses_SIM.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age (Aligned to Doses)**

**Stacked normalized curves (total, vx and uvx) should  theoretically have a horizontal course at the same level**<br>
Stacked curve normalized for AGE 70.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM.png width="1280" height="auto">
<br>

Stacked curve raw for AGE 70.<br><br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM_RAW.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20DoseAligned_Stacked_Normalized_Deaths_SIM.html)

_________________________________________
**D and Population Trends per Age real FOI data**

Shows normalized D rate for AGE 70.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_REAL.png width="1280" height="auto">
<br>

Shows raw D rate for AGE 70.<br>
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20Population_and_Deaths_Trends_with_All_Doses_RAW_REAL.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B%29%20event_stacking/B%29%20Population_and_Deaths_Trends_with_All_Doses.html)
_________________________________________
**Normalized Stacked Mean Deaths and Doses per Age real FOI data (Aligned to Doses)**

Stacked curve normalized for AGE 70.<br> 
<br>
<img src=https://github.com/gitfrid/CzechFOI-StackSim/blob/main/Plot%20Results/B)%20event_stacking/B)%20DoseAligned_Stacked_Normalized_Deaths_REAL.png width="1280" height="auto">
<br>

Stacked curve raw for AGE 70.<br><br>
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
