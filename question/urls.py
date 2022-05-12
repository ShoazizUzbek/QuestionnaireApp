from django.urls import path

from question.views import StartSession, AnswerPage, EngagementView, QuestionList, QuestionnaireList, AddQuestionnaire, \
    AddQuestion, AddGuest, GuestList

urlpatterns = [
    path('add', AddQuestionnaire.as_view(),),
    path('list', QuestionnaireList.as_view(),),
    path('add/question', AddQuestion.as_view(),),
    path('add/guest', AddGuest.as_view(),),
    path('guest/list', GuestList.as_view(),),
    path('question/list/<int:questionnaire_id>', QuestionList.as_view(),),
    path('start/session', StartSession.as_view(),),
    path('answer/page', AnswerPage.as_view(),),
    path('engagement/<int:session_id>', EngagementView.as_view(),),
    path('start/session', StartSession.as_view(),),

]
