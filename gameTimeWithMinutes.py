start_hour, start_minute, end_hour, end_minute = map(int, input().split())

start_total_minutes = start_hour * 60 + start_minute
end_total_minutes = end_hour * 60 + end_minute

if start_total_minutes < end_total_minutes:
    duration = end_total_minutes - start_total_minutes
else:
    duration = (24 * 60 - start_total_minutes) + end_total_minutes

duration_hours = duration // 60
duration_minutes = duration % 60

print(f"O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)")
