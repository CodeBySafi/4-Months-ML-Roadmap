def celcius(f):
    return "Temperature in celcius is :", (f-32)*5/9

def farenheit(c):
    return "Temperature in farenheit is ",(c*9/5)+32

menu=(" ___________WELCOME TO TEMPERATURE CONVERTER __________________ \n"
"1.CELCIUS \n "
"2.FARENHEIT \n"
"0.EXIT \n")

while True:
    try:
        num=int(input(menu))
        if num==1:
            tem=float(input("Enter temperature in farenheit :"))
            print(celcius(tem))

        elif num==2:
            tem=float(input("Enter temperature in Celcius"))
            print(farenheit(tem))
        
        elif num==0:
            print("Thankyou")
            break
        else:
            print("Inavlid choice")
    
    except:  
        print("Please Enter number")








    


