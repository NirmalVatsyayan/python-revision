from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from polls.models import Question, Choice


def index(request):
    print("Inside index function")
    latest_question = Question.objects.all().order_by('-pub_date')
    print("All questons fetched from DB are :")
    for ques in latest_question:
        print(ques.id, "  >>>>>  ", ques.question_text)
    context = {'latest_question':latest_question}
    return render(request,'polls/index.html',context)


def detail(request, question_id):
    print("we are in detail")
    question = get_object_or_404(Question,pk=question_id)
    print("Question id fetched is ", question.id,"  >>>>  ", question.question_text)
    choices = Choice.objects.filter(question=question)
    print("choices of question id ", question.id, " are below:")
    for c in choices:
        print(c.id, " >>>>  ", c.choice_text)
    return render(request,'polls/detail.html',{'question':question,'choices':choices})
    
    #return HttpResponse("This is the detail view of question : %s" % question_id)

def vote(request, question_id):
    print("Inside vote function with question id ", question_id)
    question = get_object_or_404(Question,pk=question_id)
    print("fetched question ", question.id, "  >>>  ", question.question_text)
    
    print("Form data received from request is ",request.POST)

    try:
        selected_choice = Choice.objects.get(question=question,pk=request.POST['choice'])
        print("selected_choice is ", selected_choice.id)
    except:
        return render(request,'polls/detail.html',{'question':question,'error_message':'Please select a choice'})
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        print('new vote count is ', selected_choice.votes)
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,))) 
    
    #return HttpResponse("This is the vote detail of question : %s" % question_id)

def results(request, question_id):
    print("inside results view ", question_id)
    
    question = get_object_or_404(Question,pk=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request,'polls/result.html',{'question':question,'choices':choices})
    
    #return HttpResponse("This is the result of question : %s" % question_id)
