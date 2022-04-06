##### Conversor para dias ####

tempo_str = input("Por favor, entre com o número de segundos que deseja converter: ")
t1 = int(tempo_str)
dias = (t1 // (24 * 3600))
rest_dias = (t1 % (24 * 3600))
horas = rest_dias // 3600
rest_segs_horas = rest_dias % 3600
minutos = rest_segs_horas // 60
rest_segs_final = rest_segs_horas % 60


print(dias,"dias,",horas,"horas,",minutos,"minutos e",rest_segs_final,"segundos.")