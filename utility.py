import os

class utility():
    'this class is for basic utility functions for calculator'

    def askInput(self,message):
        return input(message)


    def terminatedMessage(self):
        print ('\n\n')
        message = '****Program terminated****'
        print(message)


    def invalidResponse(self):
        print ('\n')
        self.terminatedMessage()
        print('\n')
        print('Reason ->  invalid input. ')
        print('Please restart the application.')
        print('\n')

    # To clear terminal
    def clearScreen(self):
        try:
            # for linux
            os.system('clear')
        except:
            # for windows
            os.system('cls')
