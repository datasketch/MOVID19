
from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

URL = "<insert URL>"


INTRO_MSG = "*Bienvenido al sistema de Trazabilidad del COVID19*"

HEADERS = {
    "Content-Type": "application/json"
}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Test area

    # Check if the user is already registered
    # if the user is registered then check in which stage of the process he/she is in
    # if registration is complete then just wait for bus number

    # create a function for registering

    msg = request.form.get('Body')
    print(msg)
    phone = request.form.get('From').split(":")[1][1:]
    userInfo = isUser(phone)
    if userInfo[0]:
        print("User Found")
        if msg is "0":
            # set the user stage to a specific number 8
            setUserStage(phone, 8)
            resp = MessagingResponse()
            resp.message(
                "Bienvenido al sistema de Trazabilidad del COVID19\nResponde con uno de los siguientes numeros:\n 1. Corrige tu numero de identificación\n 2. Deseo ingresar el numero del vehiculo \n 3. Notificanos si te hicieron una prueba medica y saliste positivo al COVID-19\n4. Resumen de tus viajes")
        else:
            return userFoundProtocol(userInfo, msg)
    else:
        print("User Not Found")
        return register(phone)  # Register Process

    # if(msg is "Hola"):

        # user = requests.get('https://c773f16f.ngrok.io/api/users/' + phone).text

        # print(user)
    introMsg = "*Bienvenido al sistema de Trazabilidad del COVID19*"

    return str(resp)


def userFoundProtocol(userInfo, msg):
    stage = userInfo[1]
    phone = userInfo[2]

    print('phone: ', phone, 'stage: ', stage)

    resp = MessagingResponse()
    if stage is 1:
        if msg is "7":
            # Change stage of user to 2
            print("Msg is 7")
            body = {
                "phoneNumber": phone,
                "nationalID": 'NA',
                "stage": 2}

            r = requests.put(
                URL+"userupdate/"+phone+"/", data=json.dumps(body), headers=HEADERS)
            print(r)
            resp.message(
                "A partir de ahora solo tienes que enviar el numero del bus cuando te subas")
            # return
        else:
            try:
                idNum = int(msg)
            except ValueError:
                # Porfavor solo ingrese los digitos de su documento de identidad
                print("That's not a number!")
            else:
                # a number has been entered
                print("Updating Users ID")
                body = {
                    "phoneNumber": phone,
                    "nationalID": msg,
                    "stage": 2}

                r = requests.put(
                    URL+"userupdate/"+phone+"/", data=json.dumps(body), headers=HEADERS)
                print(r)
                resp.message(
                    "Hemos actualizado tu número de cedula con el Nro.: " + msg)
                resp.message(
                    "A partir de ahora solo tienes envíanos el número del bus cuando te subas. \n Recuerda que siempre tienes la opción de enviar 0 para ir al menú principal.")

                # if len(msg) > 12:
                # Por favor asegurese de que el numero que ingreso sea valido.
                #     print("Msg longer than 12 characters")
                # else:
                # store id number

        # expecting id
        # press 7 if you do not wish to provide your id

    elif stage is 2:
        print(stage)
        vehicle = isVehicle(msg)
        if vehicle[0]:
            print("Vehicle exists")
            createEvent(phone, vehicle[1])
            resp.message("¡Gracias! Juntos hacemos el sistema más seguro")

        else:
            resp.message("El número del bus es erróneo, por favor corrígelo")

        #expecting bus #
        # check if bus exists
        # if it does then save the event
        # if not notify the user that the bus number is innexistent

    elif stage is 8:
        if msg is "1":
            setUserStage(phone, 1)
            resp.message("Porfavor ingrese su numero de cedula o identificación. De esta manera podemos hacer un mejor trabajo identificando personas en riesgo. Si no desea ingersar su numero de identificación presione el envie el numero *7*.")
        elif msg is "2":
            setUserStage(phone, 2)
            resp.message(
                "A partir de ahora solo tienes enviarnos el número del bus cuando te subas. \nRecuerda que siempre tienes la opción de enviar 0 para ir al menú principal.")

        elif msg is "3":
            setUserStage(phone, 99)
            resp.message(
                "Presiona *1* si tu resultado a la prueba del COVID19 ha dado positivo. Presiona cualquier otro numero si ese no es el caso.")

        elif msg is "4":
            trips = requests.get(URL+"filter/?owner=" + phone)
            tripsInfo = trips.json()
            print(tripsInfo)
            for trip in tripsInfo:
                print(trip)
                veh = str(trip['vehicle'])
                time = trip['timeStamp']
                print(veh, time)
                resp.message("Vehiculo: "+veh + "\nFecha: " + time)

            return str(resp)

    elif stage is 99:
        if msg is "1":
            resp.message("Has confirmado POSITIVO al virus COVID19. Es imperativo que sigas todas las instrucciones del personal de salud y entres en una estricta cuarentena.\nTe agradecemos tu ayuda para proteger a otros usuarios. A continuacion evaluaremos quienes estuvieron cerca a ti mientras usabas el transporte publico y les recomendaremos entrar en cuarentena preventiva.\n*UNIDOS VENCEMOS EL VIRUS*")
            setUserCovid(phone, True)
            # resp.message(
            #     "Presiona el ")

        else:
            setUserCovid(phone, False)
            setUserStage(phone, 2)
            resp.message(
                "Has confirmado NEGATIVO al virus COVID19")
            resp.message(
                "Bienvenido al sistema de Trazabilidad del COVID19\nResponde con uno de los siguientes numeros:\n 1. Corrige tu numero de identificación\n 2. Deseo ingresar el numero del vehiculo \n 3. Notificanos si te hicieron una prueba medica y saliste positivo al COVID-19\n ")
    # elif stage is 100:
    #     r = requests.get(URL+'api/filter/?vehicle='+)

    else:
        print(stage)
        # show main menu with option to report(3) or to go to 2, 4
    # resp = MessagingResponse()

    return str(resp)


def setUserCovid(phone, result):
    body = {
        "phoneNumber": phone,
        "covid19": result}

    r = requests.put(
        URL+"userupdate/"+phone+"/", data=json.dumps(body), headers=HEADERS)


def setUserStage(phone, stage):
    body = {
        "phoneNumber": phone,
        "stage": stage}

    r = requests.put(
        URL+"userupdate/"+phone+"/", data=json.dumps(body), headers=HEADERS)


def isUser(phone):
    print("Checking Phone", phone)
    user = requests.get(URL+"users/" + phone)
    print("Checking Phone")
    print(user)
    userInfo = user.json()
    if user:
        stage = userInfo["stage"]
        # print('USER:', userInfo['phoneNumber'], stage)
        # print("User Found")
        return True, stage, phone
    else:
        print("User NOT Found")
        return False, None, None


def isVehicle(id):
    print("Checking Vehicle")
    vehicle = requests.get(
        URL+"vehicles/" + id)
    vehicleInfo = vehicle.json()
    if vehicle:
        print("Vehicle Found")
        return True, vehicleInfo["idVehicle"]
    else:
        print("Vehicle NOT Found")
        return False, None


def register(phone):
    # save the user to the database

    body = {
        "phoneNumber": phone,
        "stage": 1,
    }
    # url = 'https://c773f16f.ngrok.io/api/users/'
    r = requests.post(URL+"users/", data=json.dumps(body), headers=HEADERS)
    print(r)

    # ask for the user id
    resp = MessagingResponse()
    resp.message(INTRO_MSG)
    resp.message("Porfavor ingrese su numero de cedula o identificación. De esta manera podemos hacer un mejor trabajo identificando personas en riesgo. Si no desea ingresar su numero de identificación responde con el numero *7*.")
    # increment the counter by 1
    return str(resp)


def createEvent(phone, vehicleID):
    body = {
        "owner": phone,
        "vehicle": vehicleID
    }
    r = requests.post(URL+"events/", data=json.dumps(body), headers=HEADERS)
    print(r.json()['id'])

    return r.json()['id']


if __name__ == "__main__":
    app.run(debug=True)


# If the count is one then we are waiting for the id, the user can also send a 0 with which he declines to provide his/her id number
#
# If the count is 2 then the user has successfully registered
