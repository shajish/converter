class CalculationFunction:
    'This class is for conversion purpose'

    def introduction(self):
        print ('\n\n')
        title = '*****CONVERSION APPLICATION*****'
        body ='This application is for converting numbers into roman number format.Feel free to use the service.'
        print (title.center(90,' '))
        print('\n')
        print ( body.center(90,' '))
        print('\n')


    def toRoman(self , val):
        value = int(val)
        if (value < 5000):
            romanValues = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
            roman = ''
            while(value > 0):
                for i,r in romanValues:
                    while value >= i:
                        roman += r
                        value -=i

            return roman
        else:
            return "false"




