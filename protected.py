class student1:
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self.branch = branch
    
    def _roll_branch(self):
        print('roll',self._roll)
        print('branch',self._branch)


class student2(student1):
    def __init__(self, name, roll, branch):
        student1.__init__(self, name, roll, branch)
    
    def details(self):
        print('name : ', self._name)
        self._roll_branch()

info = student2('s', '학부', '메디컬')
info._branch = '컴공'
info.details()
