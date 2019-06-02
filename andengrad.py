import math

def andengradsligning(a, b, c, bool):
    if a == 0:
        return "a kan ikke være 0, hvis a er = 0, så er det en retlinje"
    else:
        diskriminanten = pow(b, 2) - (4*a*c)
        if diskriminanten == 0:
            x1 = (-b / (2*a))
            if bool == True:
                return '''a({0}), b({1}), c({2})
                
{0}x^2 + {1}x + {2} = 0

Diskriminanten = {3}

Der er en løsning for x: 
			x1 = {4}'''.format(a,b,c,diskriminanten, x1)
            else:
                return x1
        elif diskriminanten > 0:
            x1 = (-b + math.sqrt(diskriminanten)) / (2*a)
            x2 = (-b - math.sqrt(diskriminanten)) / (2*a)
            if bool == True:
                return '''a({0}), b({1}), c({2})

{0}x^2 + {1}x + {2} = 0

Diskriminanten = {3}

Der er to løsninger for x: 
			x1 = {4} 
			x2 = {5}'''.format(a,b,c,diskriminanten, x1, x2)
            else:
                return x1, x2
        else: #diskriminanten < 0
            if bool == True:
                return "Der er ingen løsninger for x"