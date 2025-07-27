# context_processors.py
# Es una función que inyecta variables en el contexto de todas las plantillas de tu proyecto Django,
# sin necesidad de pasarlas desde cada vista.
from django.utils.timezone import now

def current_year(request):
    return {'now': now()}
