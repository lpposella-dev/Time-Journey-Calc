import time

class Dayhour:
    
    def __init__(self, entr, salm, valm, said):
    
        self.entr_hora = (entr)
        self.salm_hora = (salm)
        self.valm_hora = (valm)
        self.said_hora = (said)
        
        self.hora_feita_dia = Timecalc.sum_hour(Timecalc.subtract_hour(self.salm_hora, self.entr_hora), Timecalc.subtract_hour(self.said_hora, self.valm_hora))
        
    def __str__(self):
        return self.hora_feita_dia
        
    def __repr__(self):
        return self.hora_feita_dia
    
class Monthcalc:
    
    def __init__(self, month_logs: list):
        init_time = "00:00"
        for month_day_time in month_logs:
            init_time = Timecalc.sum_hour(init_time, month_day_time)
        self.final_time = init_time
            
    def __str__(self):
        return str(self.final_time)
        
    def __repr__(self):
        return str(self.final_time)
    
class Timecalc:
    
    def __init__(self):
        pass
    
    @staticmethod
    def sum_hour(take, over):
        take_split = take.split(":")
        over_split = over.split(":")
        
        take_hour = take_split[0]
        take_min = take_split[1]
        over_hour = over_split[0]
        over_min = over_split[1]
        
        general_hour = int(take_hour) + int(over_hour)
        general_min = int(take_min) + int(over_min)
        
        if general_min >= 60:
            general_min -= 60
            general_hour += 1
            
        return f"{general_hour:02}:{general_min:02}"
        
    @staticmethod
    def subtract_hour(take, over):
        take_split = take.split(":")
        over_split = over.split(":")
        
        take_hour = take_split[0]
        take_min = take_split[1]
        over_hour = over_split[0]
        over_min = over_split[1]
        
        general_hour = int(take_hour) - int(over_hour)
        general_min = int(take_min) - int(over_min)
        
        if general_min < 0:
            general_min += 60
            general_hour -= 1
            
        return f"{general_hour:02}:{general_min:02}"
        
class Menu:
    
    def __init__(self):
        menuopt = 0

        while menuopt != 3:
            menuopt = int(input("1 - Calcular Dia\n2 - Calcular Mes\n3 - Sair\n"))
    
            if menuopt > 3 or menuopt <= 0:  #error handler
                print("Escolha uma opção do menu!")
                menuopt = 0
            else:
                if menuopt == 1:
                    print(f"\nNeste dia voce trabalhou: {self.calc_day()} horas\n")
                    time.sleep(2)
                    menuopt = 0
            
                if menuopt == 2:
                    month_hours = []
                    menuopt_2 = 0
                    while menuopt_2 != 3:
                        menuopt_2 = int(input("1 - Incluir dia\n2 - Pular dia\n3 - Fechar mes\n"))
                
                        if menuopt_2 == 1:
                            
                            current_day = self.calc_day()
                            month_hours.append(str(current_day))
                            #print(month_hours) just for verify
                            
                        elif menuopt_2 == 2:
                            
                            month_hours.append("00:00")
                            #print(month_hours) just for verify
                            
                        elif menuopt_2 == 3:
                            print(f"O total de horas trabalhadas neste mes foi de: {Monthcalc(month_hours)}\n")
                            
    def calc_day(self):
                        entr = input("\nQue horas voce chegou no trabalho? ")
                        salm = input("\nQue horas voce saiu para almoço? ")
                        valm = input("\nQue horas voce voltou do almoço? ")
                        said = input("\nQue horas voce foi embora do trabalho? ")
                
                        return Dayhour(entr, salm, valm, said)
                        
Menu()
