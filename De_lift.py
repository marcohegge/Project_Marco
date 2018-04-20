from random import randint

class Floors:
    ''' Input for amount of floors starting by zero '''
    def __init__(self, no_floors = 0):
        self._no_floors = no_floors

    def Input_floors(self,no_floors):
        '''Give number of floors. Input has to be an integer and larger than 0'''
        while True:
            try:
                self._no_floors = int(input('Give number of floors ( >0 ): '))
                return self._no_floors
                break
            except:
                print('Input is not a integer larger than 0! Try again')

class Customer:
    ''' Input for amaount of customers including check '''
    def __init__(self, no_customers = 0, no_floors=0):
        self._no_customers = no_customers
        self._no_floors = no_floors

    def Input_customers(self,_no_customers):
        '''Give number of passengers of the elevator. Input has to be an integer and larger than 0'''
        while True:
            try:
                self._no_customers = int(input('Give number of passengers  ( >0 ): '))
                return self._no_customers
                break
            except:
                print('Input is not a integer larger than 0! Try again')

    def Traffic(self,_no_customers,_no_floors,up,down):
        '''Make lift program and add passengers'''
        #config an up and down dicionary.
        for x in range(_no_floors):
            up[x] = [0,0]
            down[x] = [0,0]

        # make a random elevator plan for every Customer
        print(self._no_customers)
        for person in range(self._no_customers):
            into= randint(0,_no_floors - 1)
            out = into
            while out == into:
                out = randint(0,_no_floors - 1)
            #print(into)
            #print(out)
            if into < out:
                up[into][0] += 1
                up[out][1] += 1
            else:
                down[into][0] += 1
                down[out][1] += 1
            #print(up)
            #print(down)
        return up, down

class Controll:
    ''' Make a overview of customer on which floor they starts and which floor they get out '''
    def __init__(self, no_customers=0, no_floors=0):
        self._no_customers = no_customers
        self._no_floors = no_floors

    def Program(self):
        '''Program for the elevator; check floor, customers, get traffic information and send instructions to the elevator'''
        floors=Floors()
        customer=Customer()
        lift=Lift()
        up={}
        down={}
        self._no_floors = floors.Input_floors(0)
        self._no_customers = customer.Input_customers(0)
        customer.Traffic(self._no_customers,self._no_floors,up,down)
        #print(up)
        #print(down)
        for floor in range(self._no_floors):
            into_lift = up[floor][0]
            out_lift = up[floor][1]
            lift.Movements(floor, into_lift, out_lift)
        for floor in range(self._no_floors-1,-1,-1):
            into_lift = down[floor][0]
            out_lift = down[floor][1]
            lift.Movements(floor, into_lift, out_lift)

class Lift:
    ''' Lift will go form floor to floor and use the output of Program to check how many customers are in the elevator'''
    def __init__(self, into_lift=0, out_lift=0, in_lift=0):
        self._into_lift = into_lift
        self._out_lift = out_lift
        self._in_lift = in_lift

    def Movements(self, floor, into_lift, out_lift):
        self._in_lift = self._in_lift + into_lift - out_lift
        print('The elevator is on floor ' + str(floor) + '. People getting in: ' + str(into_lift) + '. People getting out: ' + str(out_lift) + '. People in elevator: ' + str(self._in_lift))


if __name__ == '__main__':
    #starts lift via controll
    cont = Controll()
    Start_programm = cont.Program()
