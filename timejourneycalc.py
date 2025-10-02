class Dayhour:
    
    def __init__(self, entr, salm, valm, said):
    
        self.entr_hora = (entr)
        self.salm_hora = (salm)
        self.valm_hora = (valm)
        self.said_hora = (said)
        
        self.hora_feita_dia = Timecalc.sum_hour(Timecalc.subtract_hour(self.salm_hora, self.entr_hora), Timecalc.subtract_hour(self.said_hora, self.valm_hora))
    
    def __str__(self):
        return f"Horas trabalhadas no dia: \"{self.hora_feita_dia}\""
    
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
        
menuopt = 0

while menuopt != 3:
    menuopt = int(input("1 - Calcular Dia\n2 - Calcular Mes\n3 - Sair\n"))
    
    if menuopt > 3 or menuopt <= 0:  #error handler
        print("Escolha uma opção do menu!")
        menuopt = 0
    else:
        if menuopt == 1:
            entr = input("\nQue horas voce chegou no trabalho? ")
            salm = input("\nQue horas voce saiu para almoço? ")
            valm = input("\nQue horas voce voltou do almoço? ")
            said = input("\nQue horas voce foi embora do trabalho? ")
        
            print(f"\nNeste dia voce trabalhou: {Dayhour(entr, salm, valm, said)} horas\n")
            time.sleep(2)
            menuopt = 0
