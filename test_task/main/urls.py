from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from main.views import TestView, PollsList, PollsDetail, \
    QuestionsList, QuestionsDetail, ActivePolls, \
    LeaveAnAnswer, AnswersList

# router = SimpleRouter()

# router.register(r'polls', PollsView, basename='polls')

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('', TestView.as_view()),
    path('polls/', PollsList.as_view()),
    path('polls/<int:pk>', PollsDetail.as_view()),
    path('questions/', QuestionsList.as_view()),
    path('questions/<int:pk>', QuestionsDetail.as_view()),
    path('active-polls/', ActivePolls.as_view()),
    path('leave-an-answer/', LeaveAnAnswer.as_view()),
    path('answers/<int:pk>', AnswersList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += router.urls
