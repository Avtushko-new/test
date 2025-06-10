class User:

    def __init__(self, имя, фамилия):
        self.first_name = имя
        self.last_name = фамилия


    def get_first_name(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name
    
    
    def get_full_name(self):
       return f'{self.first_name} {self.last_name}'
