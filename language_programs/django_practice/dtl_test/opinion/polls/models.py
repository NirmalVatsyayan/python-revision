from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    edit_date = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,related_name="question_choice")
    
    def __str__(self):
        return self.choice_text
