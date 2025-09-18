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
        
minha_hora = Dayhour("08:10", "11:55", "13:07", "17:00")
print(minha_hora)