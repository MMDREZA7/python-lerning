class computer :
    count = 0
    def __init__(self,ram,hard,cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def get_ram(self):
        print('ram')

    def get_hard(self):
        print('hard')
    
    def get_cpu(self):
        print('cpu')    
    
    def value (self):
        return self.ram + self.hard + self.cpu
    
class laptap(computer) :
    def value (self):
        return self.ram + self.hard + self.cpu  + self.size



pc_1 = computer(int(input('insert ram: ')),int(input('insert hard: ')),int(input('insert cpu: ')))

print('pc_1 : ',pc_1.value())

# computers
laptap_1 = laptap(2,5,19)
laptap_1.size = 15
print('laptap_1: ' , laptap_1.value())
print(laptap_1.value( ))

input()
