class Volunteer:
    def __init__(self, name='', surname='', city='', status=''):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def getInfo(self):
        return {self.name, self.surname, self.city, self.status}

