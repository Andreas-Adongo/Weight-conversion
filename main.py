name = input('what is your name: ')
first = input('Do you want to check your height or weight? ')
bmi = input('Do you also want to calculate your BMI? YES/NO: ')


def bmi_calc(weight, Nheight):
    if bmi.lower() == 'yes' and first.lower() == 'weight':
        calc = weight/Nheight**2
        print(f'{name} your bmi is {calc: .2f}')



def bmi_calc_2(Weight, height):
    if bmi.lower() == 'yes' and first.lower() == 'height':
        calc = Weight/height**2
        print(f'{name} your bmi is {calc: .2f}')

def height_conversion(new_height):
    new = input('what do you want to convert your heigt to Ft, In, or Cm: ')
    if new.lower() == 'ft':
        new_height = new_height / 12
        print(f'{name} you are {new_height:.1f} {new}')
    elif new.lower() == 'in':
        print(f'{name} you are {new_height:.1f} {new}')
    elif new.lower() == 'cm':
        new_height = new_height * 2.54
        print(f'{name} you are {new_height:.1f} {new}')

def weight_conversion(weight_convert):
    new = input('What do you want to convert your weight to? Kg or Lbs: ')
    if new.lower() == 'kg':
        weight_convert = weight_convert / 1000
        print(f'{name} you weigh {weight_convert: .2f} {new}')
    elif new.lower() == 'lbs':
        weight_convert = weight_convert / 453.6
        print(f'{name} you weigh {weight_convert:.2f} {new}')
    else:
        None



if first.lower() == 'height':
    height = float(input('how tall are you: '))
    unit = input('is your unit of measurement in CM or Ft: ')



    if unit.lower() == 'cm':
        new_height = height / 2.54
    elif unit.lower() == 'ft':
        new_height = height * 12
    else:
        print('An error occured')

    
    height_conversion(new_height)

elif first.lower() == 'weight':
    weight = float(input('how much do you weigh: '))
    unit_weight = input('is your unit of measurement in Kg or Lbs: ')

    if unit_weight.lower() == 'kg':
        weight_convert = weight * 1000
    elif unit_weight.lower() == 'lbs' :
        weight_convert = weight * 453.6
    else:
        print('An error occured. unexpected value type')


    weight_conversion(weight_convert)
else:
    print('An error occured. Invalid imput')
    
if (bmi.lower() == 'yes') and (first.lower() == 'weight'):
    if unit_weight.lower() == 'lbs':
        weight = weight/2.205
    elif unit_weight.lower() == 'kg':
        weight = weight
    Nheight = float(input('Please input your height to calculate your bmi: '))
    Nheight_unit = input('what is it measured in CM / M / FT: ')
    if Nheight_unit.lower() == 'cm':
        Nheight = Nheight / 100
    elif Nheight_unit.lower() == 'm':
        Height = Nheight
    elif Nheight_unit.lower == 'ft':
        Height = Nheight / 3.281
    bmi_calc(weight,Nheight)

elif bmi.lower() == 'yes' and first.lower() == 'height':
    if unit.lower() == 'cm':
        height = height / 100
    elif unit.lower() == 'm':
        height = height
    elif unit.lower == 'ft':
        height = height / 3.281

    Weight = float(input('Please input your weight to calculate your bmi: '))
    Weight_unit = input('what is it measured in KG / LBS: ')
    if Weight_unit.lower() == 'lbs':
        Weight = Weight / 2.205
    elif Weight_unit.lower() == 'kg':
        Weight = Weight
    bmi_calc_2(Weight,height)

elif bmi.lower == 'no':
    pass


