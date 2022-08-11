age = int( input( 'cual es tu edad?: ' ) )

if age >= 18 :
    print('mayor de edad')
else :
    print('no eres mayor de edad')


start = int( input( 'inicio: ' ) )
end = int( input( 'final: ' ) )

for n in range(start, end) :
    print(n)


n_100 = 100

while n_100 > 0 :
    print(n)
    n_100 = n_100 - 1