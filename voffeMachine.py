class CofeConstructor():
    espresso = {'water': 250,
                'milk': 0,
                'beans': 16,
                'cups': 1,
                'money': 4}
    latte = {'water': 350,
             'milk': 75,
             'beans': 20,
             'cups': 1,
             'money': 7}
    cappuccino = {'water': 200,
                  'milk': 100,
                  'beans': 12,
                  'cups': 1,
                  'money': 6,}
    def __init__(self, water = 400, milk = 540, beans = 120, cups = 9, money = 550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
    def __repr__(self):
        return f'\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\
        \n{self.beans} of coffee beans \n{self.cups} of disposable cups \n${self.money} of money\n'

    def fill(self):
        ''' add products in coffee mashine'''
        print('\nWrite how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:\n')
        self.cups += int(input())

    def buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        vid_koffee = input()
        z = {}
        if vid_koffee == '1':
            z = self.espresso
        elif vid_koffee == '2':
            z = self.latte
        elif vid_koffee == '3':
            z = self.cappuccino
        elif vid_koffee == 'back':
            return
        if self.is_machine_has_resource(z) and vid_koffee != 'back':
            print('I have enough resources, making you a coffee!\n')
            self.water -= z['water']
            self.milk -= z['milk']
            self.beans -= z['beans']
            self.cups -= z['cups']
            self.money += z['money']
        else:
             pass

    def is_machine_has_resource(self, vid_coff):
        flag = True
        if self.water - vid_coff['water'] < 0:
            flag = False
            print(f'Sorry, not enough water!\n')
        if self.milk - vid_coff['milk'] < 0:
            flag = False
            print(f'Sorry, not enough milk!\n')
        if self.beans - vid_coff['beans'] < 0:
            flag = False
            print(f'Sorry, not enough beans!\n')
        if self.cups - vid_coff['cups'] < 0:
            flag = False
            print(f'Sorry, not enough cups!\n')
        return flag
    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            self.state = input()
            if self.state == 'remaining':
                print(self)
                self.state = 'choosing_action'
            if self.state == 'exit':
                break
            if self.state == 'take':
                print(f'\nI gave you {self.money}')
                self.money = 0
                self.state = 'choosing_action'
            if self.state == 'fill':
                self.fill()
                self.state = 'choosing_action'
            if self.state == 'buy':
                self.buy()
cofemashin = CofeConstructor()
cofemashin.action()
