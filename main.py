from CalculationFunctions import *
from utility import *


calc = CalculationFunction()
util = utility()

class main:

    def tryAgain(self):
        user_input = util.askInput('Wanna try again ( y/n ) :')

        if (user_input.lower() == 'y'):
            self.startApp()
        elif (user_input.lower() == 'n'):
            util.terminatedMessage()
            print('\n')
            print('We are pleased to serve you. Please visit us again. ')
            print('\n')
        else:
            util.invalidResponse()



    def startApp(self):
        # Clearing the screen
        util.clearScreen()

        # Give introduction of the application
        calc.introduction()

        # Taking user input
        user_input = util.askInput('Enter an integer value.\nInteger value -> ')

        try:
            user_input = int(user_input)
        except:
            print('Please check if the input is not integer')
            self.tryAgain()

        else:
            result = calc.toRoman(user_input)
            if (result == 'false'):
                print('please enter value less than 5000 ')
                self.tryAgain()
            else:
                print('Roman Number -> %s' % (result))
                self.tryAgain()


# Starting the Application
app = main()
app.startApp()
