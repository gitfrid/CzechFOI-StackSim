import numpy as np

# Parameters
pop = 10  # Total people
first_dose = [3, 2, 0, 1]  # Real dose schedule: day 0→3, day 1→2, day 3→1
num_days = 5

# Step 1: Build dose schedule
dose_schedule = np.zeros(num_days, dtype=int)
dose_schedule[:len(first_dose)] = first_dose
total_dosed = dose_schedule.sum()

# Step 2: Initialize -1 for "not vaccinated"
dose_day_assignments = np.full(pop, -1, dtype=int)

# Step 3: Randomly pick people to vaccinate
dose_person_ids = np.random.choice(np.arange(pop), size=total_dosed, replace=False)

# Step 4: Assign vaccination days
pointer = 0
for day in range(num_days):
    count = dose_schedule[day]
    if count > 0 and pointer + count <= total_dosed:
        selected_ids = dose_person_ids[pointer:pointer+count]
        dose_day_assignments[selected_ids] = day
        pointer += count

# Output
print("Dose Schedule (real):", dose_schedule.tolist())
print("Selected vaccinated person IDs:", dose_person_ids.tolist())
print("Dose Day Assignments (per person ID):")
for pid, day in enumerate(dose_day_assignments):
    print(f"  Person {pid}: Vaccinated on Day {day if day != -1 else 'Never'}")
