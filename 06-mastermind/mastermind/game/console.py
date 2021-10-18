class Console:
    
    def read(self, prompt):
        return input(prompt)
    
    def read_num(self,num):
        return int(input(num))

    def write(self,text):
        print(text)

    def write_list(self,list):
        print(list)