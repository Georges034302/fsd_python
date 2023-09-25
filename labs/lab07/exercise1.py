import random as ran


class Numbers:
    def __init__(self):
        self.numbers = []

    def populate(self):
        if len(self.numbers) == 0:
            self.numbers = ran.sample(range(0, 101), int(input('Size = ')))
        else:
            print('List is not empty')

    def clear(self):
        self.numbers.clear()

    def show(self):
        print(self.numbers)

    def number(self, number):
        return self.numbers.count(number) > 0

    def targets(self, target):
        temp = []
        if self.number(target):
            temp.append(target)
        return temp

    def find(self, target):
        if self.number(target):
            print(f'{target} is at position {self.numbers.index(target)}')
        else:
            print(f'{target} does not exist')

    def findAll(self, target):
        if self.number(target):
            print(f'{self.targets(target)}')
        else:
            print(f'{target} does not exist')

    def delete(self, target):
        if self.number(target):
            self.numbers.remove(target)
        else:
            print(f'{target} does not exist')

    def update(self):
        value = int(input('Value: '))
        pos = int(input("Position: "))
        self.numbers.insert(pos, value)
        
    def view(self):
        print(self.numbers)

    def menu(self):
        choice = input('Choice(p/c/f/F/d/u/v/x): ')

        while choice != 'x':
            match choice:
                case 'p': self.populate()
                case 'c': self.clear()
                case 'f': self.find(int(input('Target: ')))
                case 'F': self.findAll(int(input('Target: ')))
                case 'd': self.delete(int(input('Target: ')))
                case 'u': self.update()
                case 'v': self.view()
                case _: print('Unknown choice')
            choice = input('Choice(p/c/f/F/d/u/v/x): ')


def main():
    Numbers().menu()

if __name__ == '__main__':
    main()
