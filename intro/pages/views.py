from django.shortcuts import render
# render

# Create your views here.
def index(request):
    hello = 'hello :)'
    lunch = '라멘'
    context = {
        'hello':hello,
        'l': lunch
        }
    
    return render(request, 'index.html', context) 
    # index.html은 pages안에 templates안에 있어야함
    # 변수를 넣어줄때는 dictionary형태
    # dictionary는 하나

def hello(request, name): # urls에 있는 변수 명과 동일 해야함!
    context = {
        'name':name,
    }
    return render(request, 'hello.html', context)

def multiply(request, num1, num2):
    result = int(num1)*int(num2)
    # result = num1*num2
    context = {
        'num1': num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'multiply.html', context)


from datetime import datetime
def dtl(request):
    foods = ['짜장면','탕수육', '짬뽕', '양장피']
    sentence = 'Life is short, you need python'
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'foods':foods,
        'sentence':sentence,
        'fruits':fruits,
        'datetimenow':datetimenow,
        'empty_list':empty_list,
    }
    return render(request, 'dtl.html', context)

def isUrBRD(request):
    # 오늘 날짜
    today = datetime.now()
    # 생일인지
    result = (today.month == 1) and (today.day == 7)

    context = {
        'result' : result,
        'datetimenow':today,
    }
    return render(request, 'isUrBRD.html', context)