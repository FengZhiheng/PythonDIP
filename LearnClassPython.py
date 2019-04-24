class myClass:
    """Just one demo for me to learn class
    concept in python
    """

    name = ''
    age = 0
    __weight = 0

    def f(self):
        return 'hello world'

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('I can speak')
        print('%s say: I am %d years old'%(self.name, self.age))
    # def __init__(self, realPart, imagePart):
    #     self.r = realPart
    #     self.i = imagePart


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s say: I am %d years old'%(self.name, self.age))


class student(people):
    grad = ''
    def __init__(self, n, a, w, g):
        people.__init__(self,n, a, w)
        self.grad = g

    def speak(self):
        print("%s say: I am %d years old and my grade is %d"%(
            self.name, self.age, self.grad))

if __name__ == '__main__':
    print('hello')
    aa = myClass('tony', 10, 11)

    one = people('sansa',22, 50)
    one.speak()

    s = student('Fzh', 24, 60, 100)
    s.speak()