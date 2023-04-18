import random

book = {'rec0': 'engr0, engr1', 
        'rec1': 'engr2, engr3, engr4', 
        'rec2': 'eng5, engr6',
        'rec3': 'eng7',
        }

lenght_book = len(book)

while True:
    question_one = input('Do you know what you will eat? Yes or No:') #condition 1
    if question_one == 'Yes' or question_one == 'yes' :
        print("Bon Appetit")
    elif question_one == "No" or question_one == "no": #print('random ime na recepta')
        list_keys = list(book.keys())
        rand_num = random.randint(0,lenght_book)
        num_recepie = rand_num
        founded_recepie = list_keys[num_recepie]
        print(founded_recepie)
    else:
        break
    question_two = input('Do you have all ingredients? Yes or No:') #condition 2
    if question_two == 'Yes' or question_two == 'yes' :
        
        question_three = input('Are you sure you have all ingredients? Yes or No:') #condition 3
        if question_three == "Yes" or question_three =='yes':
            print("Bon Appetit")
        elif question_three == "No" or question_three =='no': #print('sustavki random recepta ')
            
            ingr = book.get(founded_recepie)
            print(ingr)
        else:
            break
    elif question_two == "No" or question_two == "no": #print('sustavki random recepta ')
        ingr = book.get(founded_recepie)
        print(ingr)
    else:
        break



