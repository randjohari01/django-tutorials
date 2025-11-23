from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question , choice
from django.shortcuts import render , get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.utils import timezone

"""
def index(request):
    latest_question= Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question" : latest_question}
    return render(request , "polls/index.html" , context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {"question":question})    

def results(request , question_id):
    question = get_object_or_404(Question ,pk =  question_id)
    return render(request,  "polls/results.html", {"question": question} )

def vote(request , question_id):
    question = get_object_or_404(Question ,pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, choice.DoesNotExist):
        return render(request, 
                     "polls/detail.html", 
                    {
                        "question": question,
                        "error_message": "you didnt select a choice",
                    },
                )
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))
"""

from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model  = Question
    template = "polls:detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template = "polls:results.html"

def vote(request , question_id):
    question = get_object_or_404(Question ,pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, choice.DoesNotExist):
        return render(request, 
                     "polls/detail.html", 
                    {
                        "question": question,
                        "error_message": "you didnt select a choice",
                    },
                )
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))