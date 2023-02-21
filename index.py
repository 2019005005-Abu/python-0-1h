full_name='Abu Al Shahriar Rifat'
width,height=200,400;
print(height)
yourName=input("Please Enter Name");
print(yourName);
print('Hi'+"I am "+" "+yourName);
f=int(input("Enter first number"));
l=int(input("Enter the second number"));
print(f+l);
##Tip Calculator
##math operator=+
## food amount=100
food_amount=float(input("Enter the food amount"));
tip_parcentage=float(input('Enter you tips'))/100;
tip_amount=food_amount*tip_parcentage;
##get the total
PayingTota=food_amount+tip_amount
print('I have Paied'+''+'$'+" " +str(PayingTota))

print(f'food amount is ${food_amount}');
print(f'Tips amount  ${tip_amount}');

#############Boolean 
###########BOOLEAN
###Baby Weather application
weather=input("How is the weather ?");
if weather=='rain':
    print('Umbrella');
elif weather=='cloudy':
    print('I will have to prepare to take the umbrella')
elif weather=='thundarstom':
    print('Lighting and thundarstom')
else:
    print('sunglass')


score=50;
if score>90:
    print('A');
elif score>80:
    print('B');
elif score>70:
    print('C');
elif score>60:
    print('D');
elif score>=50:
    print('F');
else:
    print('Error')

marks=90;
if marks>=90 and marks<=100:
    print('A+');
else:
    print('Failed');




