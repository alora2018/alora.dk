from django.apps import AppConfig


class TodoListConfig(AppConfig):
    name = 'todo_list'

 def ready(self):
    	import accounts.signals