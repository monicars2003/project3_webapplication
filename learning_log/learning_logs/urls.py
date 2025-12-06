"Url patterns for learning_logs"

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    #Pages shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding new topics
    path('new topic/', views.new_topic, name='new_topic'),
    #Adding a New Entry
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    #Editing the entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]