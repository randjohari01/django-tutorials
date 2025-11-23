import datetime 
from django.utils import timezone 
from django.test import TestCase
from django.urls import reverse
from .models import Question


class QuestionTest(TestCase):
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()- datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date =time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now()- datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date =time)
        self.assertIs(old_question.was_published_recently(), False)


def create_question(question_text , days ):
        time = timezone.now() + datetime.timedelta(days = days)
        return Question.objects.create(question_text =question_text ,pub_date = time )

    
class QuestionIndexViewTest(TestCase):

    def test_no_question(self):
        response =  self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code , 200)
        self.assertContains(response , "no polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text ="past question", days = -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        question = create_question(question_text = "future question", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text ="past question", days = -30)
        create_question(question_text = "future question", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_2_past_question(self):
        question1 = create_question(question_text ="past question1", days = -30)
        question2 = create_question(question_text ="past question2", days = -6)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question2 , question1]) #pub_date descending


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        question = create_question(question_text = "future_question" , days =5)
        url = reverse("polls:detail", args=(question.id,)) #get does not accept args
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        question = create_question(question_text = "future_question" , days = -5)
        url = reverse("polls:detail", args=(question.id,)) 
        response = self.client.get(url)
        self.assertContains(response, question.question_text)


