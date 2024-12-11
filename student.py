'''idz 6 (student group), Бессонова А.С., гр.3588'''
class Student:
    '''Group'''
    last_name_len=0
    first_name_len=0
    second_name_len=0

    def __init__(self, last_name:str, first_name:str, second_name:str = ''):
        self.last_name=last_name
        self.first_name=first_name
        self.second_name=second_name
        Student.last_name_len=max(Student.last_name_len, len(self.last_name))
        Student.first_name_len=max(Student.first_name_len, len(self.first_name))
        Student.second_name_len=max(Student.second_name_len, len(self.second_name))

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}' if self.second_name\
            else f'{self.last_name} {self.first_name}'

    def __repr__(self) -> str:
        return '|'\
            f'{self.last_name:<{Student.last_name_len}}'\
            '|'\
            f'{self.first_name:<{Student.first_name_len}}'\
            '|'\
            f'{self.second_name:<{Student.second_name_len}}'\
            '|'
    
    @staticmethod
    def line():
        '''line'''
        return('-' * (Student.last_name_len + Student.first_name_len + Student.second_name_len + 10))
