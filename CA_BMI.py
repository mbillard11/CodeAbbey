tot_lines = int(raw_input())

for i in range(0, tot_lines):
    line = raw_input()
    num = map(float, line.split())
    weight = num[0]
    height = num[1]
    BMI = weight / (height**2)

    if (BMI < 18.5):
        print 'under',
    elif (18.5 <= BMI < 25.0):
        print 'normal',
    elif (25.0 <= BMI < 30.0):
        print 'over',
    else:
        print 'obese',





Underweight     -           BMI < 18.5
Normal weight   -   18.5 <= BMI < 25.0
Overweight      -   25.0 <= BMI < 30.0
Obesity         -   30.0 <= BMI