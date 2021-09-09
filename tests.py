
import requests


CANVAS_ID = 30940
URL_API = "https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/" + str(CANVAS_ID)


i = 1
all_users = []
while i < 99:
    URL_USERS = URL_API + "/users?_page=" + str(i)
    response = requests.get(URL_USERS)
    response = response.json()

    if len(response) == 0:
        break
    all_users += response
    i +=1
return render(request, 'core/users.html', all_users)