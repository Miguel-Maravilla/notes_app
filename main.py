"""
Proyecto Python y MySQL:

- Abrir asistente
- Log in o registro
- Si elegimos "registro", creará un usuario en la db
- Si elegimos "login", identificará al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas
"""


from users import actions


print("""
Available actions:
    - Registration
    - Login
""")

makeThe = actions.Actions()
action = input("What would you like to do? ").lower()

if action == "registration":
    makeThe.registration()

elif action == "login":
    makeThe.login()
    


