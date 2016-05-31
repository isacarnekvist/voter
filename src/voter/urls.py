"""voter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from web.views import frontpage, login_view, logout_view, frontpage, \
                      add_deck, delete_deck, edit_deck, start_class, \
                      class_teacher_view, delete_class, question_state, \
                      question_teacher_view, poll_question, class_view, \
                      answer_question, poll_active_question

urlpatterns = [
    url(r'^general/', include(admin.site.urls)),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^add_deck/$', add_deck, name='add_deck'),
    url(r'^edit_deck/([0-9]+)/$', edit_deck, name='edit_deck'),
    url(r'^$', frontpage, name='frontpage'),
    url(r'^start_class/([0-9]+)/$', start_class, name='start_class'),
    url(r'^class_teacher/([0-9]+)/$', class_teacher_view, name='class_teacher'),
    url(r'^class/$', class_view, name='class_view'),
    url(r'^question_teacher/([0-9]+)/([0-9]+)/$', question_teacher_view, name='question_teacher'),
    # ajax
    url(r'^delete_deck/$', delete_deck, name='delete_deck'),
    url(r'^delete_class/$', delete_class, name='delete_class'),
    url(r'^question_state/$', question_state, name='question_state'),
    url(r'^poll_question/$', poll_question, name='poll_question'),
    url(r'^answer_question/$', answer_question, name='answer_question'),
    url(r'^poll_active_question/$', poll_active_question, name='poll_active_question'),
]
