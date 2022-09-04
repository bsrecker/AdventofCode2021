sonar_report = open("resources/sonar report", "r")
measurements = sonar_report.readlines()

increased_count = 0

for index, value in enumerate(measurements):
    current_depth = int(value.strip())
    previous_depth = int(measurements[index - 1].strip())

    if current_depth > previous_depth:
        increased_count += 1
        print(f'{current_depth} (increased)')

    else:
        print(f'{current_depth} (N/A)' if index == 0 else f"{current_depth} (decreased)")


print(f'Number of increases: {increased_count}')

