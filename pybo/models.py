from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') #계정(사용자) 모델은 django.contrib.auth.models 패키지의 User이므로 글쓴이에 해당되는 author 속성은 User모델을 ForeignKey로 적용
    subject = models.CharField(max_length=200) #질문제목
    content = models.TextField() #글자수 제한 X
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)#질문이나 답변이 언제 수정되었는지 확인
    #null=True의 의미는 modify_date를 데이터베이스에 저장할때 null이 허용된다는 의미, blank=True의 의미는 입력 폼 데이터 체크시(form.is_valid()) 값이 없어도 오류를 내지 않는다는 의미
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가, ManyToManyField관계는 다대다관계의미.

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #답변해당질문
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #댓글작성자
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)  # 댓글의 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 댓글의 답변