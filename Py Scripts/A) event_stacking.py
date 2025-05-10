import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Simulate death data with identical constant death rates across total population group.
# - Randomly assigns deaths over days 0–END_MEASURE per age group using the real total death counts of the age groups.
# - Applies real vaccination schedule from dose_first_df.
# - Classifies randomly each death into vx or uvx based on vaccination timing.
# - Outputs raw daily deaths for validation as csv files: total, vaccinated, and unvaccinated.
# - Plots raw / normalized death traces for total, vaccinated, and unvaccinated group
# - Additional plots raw / normalized stacked event curves for each age group

# Load CSV files
dose_first_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_VX.csv").set_index("DAY")
dose_all_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_VDA.csv").set_index("DAY")
deaths_total_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_D.csv").set_index("DAY")
deaths_uvx_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DUVX.csv").set_index("DAY")
deaths_vx_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DVX.csv").set_index("DAY")
pop_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_POP.csv").set_index("DAY")


END_MEASURE = 1110
POST_VX_DELAY = 0
sim_extension = ""

# Set a fixed seed for reproducibility
np.random.seed(42)

# --- Dynamically determine dimensions ---
days = pop_df.index.to_numpy()
ages = pop_df.columns.astype(int).to_numpy()

num_days = len(days)
num_ages = len(ages)

# --- Initialize simulation arrays ---
deaths_sim_total = np.zeros((num_days, num_ages), dtype=int)
deaths_sim_vx = np.zeros_like(deaths_sim_total)
deaths_sim_uvx = np.zeros_like(deaths_sim_total)

# --- Simulate per age group ---
for age_idx, age in enumerate(ages):
    pop = int(pop_df.iloc[0, age_idx])
    total_deaths = int(deaths_total_df.iloc[:, age_idx].sum())
    first_dose = dose_first_df.iloc[:, age_idx].to_numpy()

    # Assign random death days
    death_days = np.random.choice(np.arange(END_MEASURE), size=total_deaths, replace=True)
    death_day_counts = np.bincount(death_days, minlength=num_days)
    deaths_sim_total[:, age_idx] = death_day_counts

    # Assign simulated people
    person_ids = np.random.choice(np.arange(pop), size=total_deaths, replace=True)

    # Assign doses based on real schedule
    dose_schedule = np.zeros(num_days, dtype=int)
    dose_schedule[:len(first_dose)] = first_dose
    total_dosed = dose_schedule.sum()

    dose_day_assignments = np.full(pop, -1, dtype=int)  # -1 means not vaccinated
    if total_dosed > 0:
        dose_person_ids = np.random.choice(np.arange(pop), size=total_dosed, replace=False)
        pointer = 0
        for day in range(num_days):
            count = dose_schedule[day]
            if count > 0 and pointer + count <= total_dosed:
                dose_day_assignments[dose_person_ids[pointer:pointer+count]] = day
                pointer += count

    # Classify each death as vx or uvx
    for dday_idx, pid in zip(death_days, person_ids):
        vday_idx = dose_day_assignments[pid]
        if vday_idx != -1 and dday_idx >= vday_idx + POST_VX_DELAY:
            deaths_sim_vx[dday_idx, age_idx] += 1
        else:
            deaths_sim_uvx[dday_idx, age_idx] += 1

# --- Save results ---
index = pop_df.index
columns = pop_df.columns

pd.DataFrame(deaths_sim_total, index=index, columns=columns).to_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_D_SIM.csv")
pd.DataFrame(deaths_sim_uvx, index=index, columns=columns).to_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DUVX_SIM.csv")
pd.DataFrame(deaths_sim_vx, index=index, columns=columns).to_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DVX_SIM.csv")

# for test with simulated data uncoment the four lines below
sim_extension += "_sim"
deaths_total_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_D_SIM.csv").set_index("DAY")
deaths_uvx_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DUVX_SIM.csv").set_index("DAY")
deaths_vx_df = pd.read_csv(r"C:\CzechFOI-StackSim\TERRA\PVT_NUM_DVX_SIM.csv").set_index("DAY")


# --- Plotting and Calculations (Rest of the code stays unchanged) ---
# (Use the same plot creation code you already had for the rest of the analysis)

# Use the first row as initial population (constant)
initial_population = pop_df.iloc[0]

# Compute cumulative deaths
cumulative_deaths_total = deaths_total_df.cumsum()
cumulative_deaths_vx = deaths_vx_df.cumsum()
cumulative_deaths_uvx = deaths_uvx_df.cumsum()
cumulative_first_dose = dose_first_df.cumsum()

# Create figure for trends
fig = go.Figure()

# Window size for rolling average
window = 21

# --- Original Plotting Loop ---
for age in range(114):
    age_str = str(age)

    # Extract data for current age
    pop = initial_population[age_str]
    deaths_total = deaths_total_df[age_str]
    deaths_vx = deaths_vx_df[age_str]
    deaths_uvx = deaths_uvx_df[age_str]
    first_dose = dose_first_df[age_str]
    all_dose = dose_all_df[age_str]

    cum_deaths_total = cumulative_deaths_total[age_str]
    cum_deaths_vx = cumulative_deaths_vx[age_str]
    cum_deaths_uvx = cumulative_deaths_uvx[age_str]
    cum_first_dose = cumulative_first_dose[age_str]

    # Remaining pop (pop - deaths) 
    remaining_pop = pop - cum_deaths_total
    vx_pop = cum_first_dose - cum_deaths_vx
    uvx_pop = pop - cum_first_dose - cum_deaths_uvx

    # --- Consistency Checks  -> delete it if you like ---
    valid_mask = (remaining_pop > 0) & (vx_pop > 0) & (uvx_pop > 0)

    # Skip if any population is zero to avoid division errors
    if not valid_mask.any():
        print(f"Skipping age {age} due to zero population")
        continue

    # Normalized deaths per 100k
    norm_deaths_total = (deaths_total / remaining_pop) * 100000
    norm_deaths_vx = (deaths_vx / vx_pop) * 100000
    norm_deaths_uvx = (deaths_uvx / uvx_pop) * 100000

    # --- Normalized Population Check -> delete it if you want ---
    # Skip this check entirely if no valid data remains
    if not valid_mask.any():
        print(f"Skipping normalized check at age {age} due to zero population")
    else:
        sum_norm = norm_deaths_vx * (vx_pop / remaining_pop) + norm_deaths_uvx * (uvx_pop / remaining_pop)
        if not np.allclose(norm_deaths_total[valid_mask], sum_norm[valid_mask], rtol=1e-3, atol=0.1):
            raise ValueError(
                f"Normalized mismatch at age {age}\n"
                f"Remaining pop:\n{remaining_pop}\n"
                f"VX pop:\n{vx_pop}\n"
                f"UVX pop:\n{uvx_pop}\n"
                f"Norm deaths total:\n{norm_deaths_total}\n"
                f"Norm deaths vx:\n{norm_deaths_vx}\n"
                f"Norm deaths uvx:\n{norm_deaths_uvx}\n"
                f"Sum norm:\n{sum_norm}"
            )

    # --- further Checks  -> delete it if you like ---
    assert np.allclose(deaths_total, deaths_vx + deaths_uvx, rtol=1e-6), f"Mismatch in raw deaths for age {age}"
    day = 500
    expected_norm = (deaths_total.iloc[day] / (initial_population[age_str] - cumulative_deaths_total[age_str].iloc[day])) * 100_000
    assert np.isclose(norm_deaths_total.iloc[day], expected_norm, rtol=1e-6), f"Normalization error at age {age}, day {day}"

    # Rolling means
    deaths_total_roll = deaths_total.rolling(window, center=True).mean()
    deaths_vx_roll = deaths_vx.rolling(window, center=True).mean()
    deaths_uvx_roll = deaths_uvx.rolling(window, center=True).mean()
    norm_total_roll = norm_deaths_total.rolling(window, center=True).mean()
    norm_vx_roll = norm_deaths_vx.rolling(window, center=True).mean()
    norm_uvx_roll = norm_deaths_uvx.rolling(window, center=True).mean()
    all_dose_roll = all_dose.rolling(window, center=True).mean()
    
    # Death Traces
    fig.add_trace(go.Scatter(x=deaths_vx.index, y=deaths_vx, mode='lines', name=f"Age {age} VX Deaths", line=dict(width=1)))
    fig.add_trace(go.Scatter(x=deaths_vx.index, y=deaths_vx_roll, mode='lines', name=f"Age {age} VX Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    fig.add_trace(go.Scatter(x=deaths_uvx.index, y=deaths_uvx, mode='lines', name=f"Age {age} UVX Deaths", line=dict(width=1)))
    fig.add_trace(go.Scatter(x=deaths_uvx.index, y=deaths_uvx_roll, mode='lines', name=f"Age {age} UVX Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    fig.add_trace(go.Scatter(x=deaths_total.index, y=deaths_total, mode='lines', name=f"Age {age} Total Deaths", line=dict(width=0.8)))
    fig.add_trace(go.Scatter(x=deaths_total.index, y=deaths_total_roll, mode='lines', name=f"Age {age} Total Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    
    fig.add_trace(go.Scatter(x=deaths_vx.index, y=norm_deaths_vx, mode='lines', name=f"Age {age} Norm VX Deaths", line=dict(width=1)))
    fig.add_trace(go.Scatter(x=deaths_vx.index, y=norm_vx_roll, mode='lines', name=f"Age {age} Norm VX Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    fig.add_trace(go.Scatter(x=deaths_uvx.index, y=norm_deaths_uvx, mode='lines', name=f"Age {age} Norm UVX Deaths", line=dict(width=1)))
    fig.add_trace(go.Scatter(x=deaths_uvx.index, y=norm_uvx_roll, mode='lines', name=f"Age {age} Norm UVX Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    fig.add_trace(go.Scatter(x=deaths_total.index, y=norm_deaths_total, mode='lines', name=f"Age {age} Norm Total Deaths", line=dict(width=1)))
    fig.add_trace(go.Scatter(x=deaths_total.index, y=norm_total_roll, mode='lines', name=f"Age {age} Norm Total Deaths ({window}d avg)", line=dict(width=0.8, dash='solid')))
    
    # Dose and population traces
    fig.add_trace(go.Scatter(x=deaths_total.index, y=remaining_pop, mode='lines', name=f"Age {age} Remaining Total Pop", line=dict(width=0.8), yaxis="y2" ))
    fig.add_trace(go.Scatter(x=all_dose.index, y=vx_pop, mode='lines', name=f"Age {age} VX Pop", line=dict(width=1), yaxis="y2"))
    fig.add_trace(go.Scatter(x=all_dose.index, y=uvx_pop, mode='lines', name=f"Age {age} UVX Pop", line=dict(width=1), yaxis="y2"))
    fig.add_trace(go.Scatter(x=all_dose.index, y=all_dose, mode='lines', name=f"Age {age} All Doses", line=dict(width=1), yaxis="y3"))
    fig.add_trace(go.Scatter(x=all_dose.index, y=all_dose_roll, mode='lines', name=f"Age {age} All Doses ({window}d avg)", line=dict(width=0.8, dash='solid'), yaxis="y3"))

# Update layout for the main figure
fig.update_layout(
    title=f"Deaths and Population Trends per Age Group {sim_extension}",
    colorway=px.colors.qualitative.Plotly[1:] + [px.colors.qualitative.Plotly[0]] ,  # Using a predefined qualitative color palette
    xaxis_title="Day",
    yaxis=dict(title="Raw Deaths / Normalized Deaths per 100k"),
    yaxis2=dict(
        title="Population", 
        overlaying='y', 
        side='right', 
        showgrid=False
    ),
    yaxis3=dict(
        title="Doses",   # Title for the new y-axis
        overlaying='y',  # Make it overlay the existing y-axis
        side='right',    # Place it on the right side
        position=0.95,   # Adjust the position for the new axis (further right)
        showgrid=False,  # Hide gridlines for this axis
    ),
    legend=dict(
        x=1.05,  # Move it farther to the right (default is 1.0 = just outside plot)
        y=1.0,
        xanchor='left',
        yanchor='top'
    ),    
    template="plotly_white",
    height=1000,
    width=1800
)


# Save original plot
output_path = fr"C:\CzechFOI-StackSim\Plot Results\A) event_stacking\A) Population_and_Deaths_Trends_with_All_Doses{sim_extension}.html"
fig.write_html(output_path)
print(f"Plot saved to {output_path}")


# --- Dose-Aligned Event Stacking Plot ---
days_before = 125
days_after = 125
window_size = days_before + days_after + 1

age_curves = {}
x = np.arange(-days_before, days_after + 1)

for age in range(114):
    age_str = str(age)
    doses = dose_all_df[age_str]
    deaths_total = deaths_total_df[age_str]
    deaths_vx = deaths_vx_df[age_str]
    deaths_uvx = deaths_uvx_df[age_str]

    pop = initial_population[age_str]
    cum_deaths_total = cumulative_deaths_total[age_str]
    cum_first_dose = cumulative_first_dose[age_str]

    if pop == 0 or np.isnan(pop):
        print(f"Skipping age {age_str}: zero or NaN initial population")
        continue

    dose_threshold = 0.02 * doses.max()
    dose_days = doses[doses > dose_threshold].index

    for label, deaths, calc_pop in zip(
        ["Total", "VX", "UVX"], 
        [deaths_total, deaths_vx, deaths_uvx], 
        [lambda: pop - cum_deaths_total, 
         lambda: cum_first_dose - cum_deaths_vx, 
         lambda: pop - cum_first_dose - cum_deaths_uvx]
    ):
        stacked_deaths = np.zeros(window_size)
        stacked_pops = np.zeros(window_size)
        valid_stacks = 0

        for dose_day in dose_days:
            start_day = dose_day - days_before
            end_day = dose_day + days_after

            try:
                deaths_window = deaths.loc[start_day:end_day]
                pop_window = calc_pop().loc[start_day:end_day]

                if len(deaths_window) != window_size or len(pop_window) != window_size:
                    print(f"Skipping dose day {dose_day} for age {age_str}, label {label}, invalid window size")
                    continue

                stacked_deaths += deaths_window.values
                stacked_pops += pop_window.values
                valid_stacks += 1

            except KeyError:
                print(f"Skipping dose day {dose_day} for age {age_str}, label {label}, KeyError")
                continue

        if valid_stacks == 0:
            print(f"No valid stacks for age {age_str}, label {label}")
            continue

        mean_deaths = stacked_deaths / valid_stacks
        mean_pop = stacked_pops / valid_stacks

        # Day-by-day normalization: return 0 if pop is 0 or NaN
        normalized_curve = np.zeros(window_size)
        for i in range(window_size):
            p = mean_pop[i]
            d = mean_deaths[i]
            normalized_curve[i] = (d / p * 100_000) if p > 0 and not np.isnan(p) else 0.0

        age_curves[(age, label)] = normalized_curve

# --- Plot ---
stack_fig = go.Figure()

for (age, label), curve in age_curves.items():
    early_pre = (x >= -125) & (x < -60)
    late_pre = (x >= -60) & (x < 0)
    post = (x >= 0) & (x <= 125)

    mean_early_pre = np.mean(curve[early_pre])
    mean_late_pre = np.mean(curve[late_pre])
    mean_post = np.mean(curve[post])

    summary_text = (
        f"Age {age} {label}<br>"
        f"-125:-60: {mean_early_pre:.6f}<br>"
        f"-60:-1: {mean_late_pre:.6f}<br>"
        f"0:125: {mean_post:.6f}"
    )

    stack_fig.add_trace(go.Scatter(
        x=x,
        y=curve,
        mode="lines",
        name=f"Age {age} {label}",
        line=dict(width=1),
        hovertemplate=summary_text + "<br>Day %{x}, Value %{y:.6f}<extra></extra>"
    ))

stack_fig.update_layout(
    title=f"Normalized Stacked Mean Deaths per Age (Aligned to Doses) {sim_extension}",
    xaxis_title="Days Relative to Dose",
    yaxis_title="Normalized Stacked Mean Death",
    legend_title="Age Group",
    template="plotly_white",
    height=900,
    width=1600
)

# --- Add Raw (Non-normalized) Traces to Existing stack_fig ---
for (age, label), norm_curve in age_curves.items():
    age_str = str(age)
    doses = dose_all_df[age_str]
    deaths = {
        "Total": deaths_total_df[age_str],
        "VX": deaths_vx_df[age_str],
        "UVX": deaths_uvx_df[age_str]
    }[label]

    dose_threshold = 0.02 * doses.max()
    dose_days = doses[doses > dose_threshold].index

    stacked_raw = np.zeros(window_size)
    valid_raw_stacks = 0

    for dose_day in dose_days:
        start_day = dose_day - days_before
        end_day = dose_day + days_after

        try:
            deaths_window = deaths.loc[start_day:end_day]
            if len(deaths_window) != window_size:
                continue
            stacked_raw += deaths_window.values
            valid_raw_stacks += 1
        except KeyError:
            continue

    if valid_raw_stacks == 0:
        continue

    raw_mean_curve = stacked_raw / valid_raw_stacks

    # Add raw trace to existing figure using dashed line and secondary y-axis
    stack_fig.add_trace(go.Scatter(
        x=x,
        y=raw_mean_curve,
        mode="lines",
        name=f"Age {age} {label} (Raw)",
        line=dict(width=0.8),
        yaxis="y2",
        hovertemplate=f"Age {age} {label} (Raw)<br>Day %{{x}}, Deaths %{{y:.6f}}<extra></extra>"
    ))


# Update layout with secondary y-axis for raw deaths
stack_fig.update_layout(
    yaxis2=dict(
        title="Raw Stacked Mean Deaths",
        overlaying='y',
        side='right',
        showgrid=False
    )
)

# Save
stack_output_path = fr"C:\CzechFOI-StackSim\Plot Results\A) event_stacking\A) DoseAligned_Stacked_Normalized_Deaths{sim_extension}.html"
stack_fig.write_html(stack_output_path)
print(f"Stacked plot saved to {stack_output_path}")