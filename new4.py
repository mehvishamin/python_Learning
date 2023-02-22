
my_dict = {
    'Question1' :{
      'Question' : 'WHat is the capital of Saudi Arabia.',
      'Answers' : ['Riyadh','Jeddah','Mecca'],
      'CorrectAnswer' : 'Riyadh'
    },

    'Question2':{
      'Question' : 'What is the last surah revealed.',
      'Answers' : ['ikhlaas','kausar','nasr'],
      'CorrectAnswer' : 'nasr'
    },
    'Question3':{
        'Question' : 'Who lead the jinazah prayer of prophet.',
        'Answers' : ['abu bakr','umer','no-one'],
        'CorrectAnswer' : 'no-one'
    },
    'Question4':{
        'Question' : 'How many times prophet gave zakah',
        'Answers' : ['every year','every month','never'],
        'CorrectAnswer' : 'never'
    },
     'Question5':{
        'Question' : 'Who was the first convert to Islam',
        'Answers' : ['Abu Bakr','Ali','Khadijah'],
        'CorrectAnswer' : 'Khadijah'
    },
     'Question6':{
        'Question' : 'Name the companion whose name is mentioned in QUran',
        'Answers' : ['Ali','Umer','Zaid ibn thabit'],
        'CorrectAnswer' : 'Zaid'
    },
  
   'Question7':{
        'Question' : 'WHich is longest verse of QUran',
        'Answers' : ['Verse of throne','Verse of Prophet','Verse of Debt'],
        'CorrectAnswer' : 'Verse of Debt'
    },
    
   'Question8':{
        'Question' : 'Only prophet mentioned by his name and his mothers name',
        'Answers' : ['Moses','Jesus','Younus'],
        'CorrectAnswer' : 'Jesus'
    },
    'Question9':{
        'Question' : 'Where is Allahs throne',
        'Answers' : ['Water','Earth','Space'],
        'CorrectAnswer' : 'Water'
    },
     
}
for questionNo,data in my_dict.items():
    print(questionNo +":- "+ data["Question"])
    print("Correct Answer: "+data["CorrectAnswer"])
    print()
    


# abc={
#    'age': 12443,
#    'address': 'hhejfhjfj',
#    'phoneNo': 1233,
#     'marks': {
#         '10thClass': 567,
#         '12thClass': 4377,
#         'graduation': 8999
#     }

# }
# list1=list(abc.values())
# print(list1[3])