sonar_report = open("resources/sonar report", "r")
measurements = sonar_report.readlines()

increased_count = 0

for i in range(len(measurements)):
    current_depth = int(measurements[i].strip())
    previous_depth = int(measurements[i - 1].strip())

    if current_depth > previous_depth:
        increased_count += 1
        print(f'{current_depth} (increased)')

    else:
        print(f'{current_depth} (N/A)' if i == 0 else f"{current_depth} (decreased)")


print(f'Number of increases: {increased_count}')

