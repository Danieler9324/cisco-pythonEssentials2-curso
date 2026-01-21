class Timer:
    def __init__(self, horas, minutos, segundos ):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"

    def next_second(self):
        self.segundos += 1
        
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
            
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1

                if self.horas >= 24:
                    self.horas = 0
                    
        

    def prev_second(self):
        self.segundos -=1
        
        if self.segundos < 0:
            self.segundos = 59
            self.minutos -= 1
            
            if self.minutos < 0:
                self.minutos = 59
                self.horas -=1
                
                if self.horas <0:
                    self.horas = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    