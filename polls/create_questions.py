from .models import Question, Choice
from django.utils import timezone

# ejecutar script:
# python3 manage.py shell
# se abre shell interactivo de django y escribir:
# import polls.create_questions
# se puede comprobar con Question.objects.all()

# elimina las filas que habia
Question.objects.all().delete()
# introduce filas
q = Question(question_text = 'xd?', pub_date = timezone.now())
q.save()
Question(question_text = 'mainkra?', pub_date = timezone.now()).save()

Choice.objects.all().delete()
Choice(choice_text = 'jaja', question = q).save()
# obtener objeto con get:
Choice(choice_text = 'jeje', question = Question.objects.get(question_text = 'xd?')).save()
# tambien vale con create:
Choice.objects.create(choice_text = 'jiji', question = q)
# ver choices?
# Question.objects.get(question_text = 'xd?').choice_set.all()
