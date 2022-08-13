def area_triangle(b, h) : 
    return (b * h) / 2


def area_circle(r) :
    return (r ** 2) * 3.14



def is_counsin(n) :
    
    if n == 0 :
        print('not counsin')

    if n % 2 == 1 or n == 2:
        print('counsin')


def leap_year(year) :

    if not year % 100 == 0 or year % 400 == 0 or year % 4 == 0 :
        print('leap_year')



    