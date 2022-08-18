from datetime import datetime

from op import suma, resta, div, mul

suma(1,3)
resta(2,3)
div(4,2)
mul(3,3)


now = datetime.now()
current_time =  now.strftime("%H:%M:%S")

if not current_time.split(':')[0] == '19' :
    print()
    current = int( current_time.split(':')[0] )
    r = current - 19
    print(f'te faltan #{r} para salir de trabajar')
else :
    print('ya no estás trabajando')
