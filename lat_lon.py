import math as m
def multiplication(*numbers):
    a =1   
    for number in numbers:
        a*=number
    return a
def summation(*numbers):
    a =1   
    for number in numbers:
        a+=number
    return a
def substraction(*numbers):
    a =1   
    for number in numbers:
        a-=number
    return a
def division(*numbers):
    a =1   
    for number in numbers:
        a/=number
    return a
    
    
def degrees_to_decimal(degree, minute, second):
    return degree + (minute/60) + (second/3600)
    
def decimal_to_degrees(decimal):
    degree = m.floor(decimal)
    minute=round((decimal - m.floor(decimal))*60)
    second = abs(round((((decimal - m.floor(decimal)) *60) - minute)*60))
    return(f"{degree}°{minute}'{second}\"")
    
def degrees_to_lat_lon(degree, minute, second,degree1, minute1, second1):
    print (f"{degrees_to_decimal(degree, minute, second)},{degrees_to_decimal(degree1, minute1, second1)}")


def main():
  
    print(decimal_to_degrees(27.9409282),decimal_to_degrees(-81.6069761))
   
  
if __name__=="__main__":
    main()
    #20.958333333333332
