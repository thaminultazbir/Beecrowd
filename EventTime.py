start_day = int(input().split()[1])
start_time = list(map(int, input().split(' : ')))
end_day = int(input().split()[1])
end_time = list(map(int, input().split(' : ')))

# Convert start and end times to minutes
start_minutes = start_day * 24 * 60 + start_time[0] * 60 + start_time[1] + start_time[2] / 60
end_minutes = end_day * 24 * 60 + end_time[0] * 60 + end_time[1] + end_time[2] / 60

# Calculate duration in minutes
duration_minutes = end_minutes - start_minutes

# Convert back to days, hours, minutes, and seconds
days = duration_minutes // (24 * 60)
duration_minutes %= 24 * 60
hours = duration_minutes // 60
duration_minutes %= 60
minutes = int(duration_minutes)
seconds = int((duration_minutes - minutes) * 60)

print(f"{int(days)} dia(s)")
print(f"{int(hours)} hora(s)")
print(f"{int(minutes)} minuto(s)")
print(f"{int(seconds)} segundo(s)")