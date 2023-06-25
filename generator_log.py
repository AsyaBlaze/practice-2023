import random

def generate_log(path):
    with open(path, 'a') as file:
        address = random.choice(["192.168.2.20", "127.0.0.1", "73.170.245.26",
                                 "191.25.177.190", "28.184.92.66",
                                 "185.162.221.41"])
        datee = generate_date()
        id = str(random.randint(1, 999))
        type_request = random.choice(["GET", "GET", "PUT", "DELETE"])
        protocol = random.choice(["200","404", "200", "200"])
        bytes_n = str(random.randint(34, 9999))
        stroka = address + " - - " + datee + " \"" + type_request + " /client/" + id + " HTTP/1.1\" " + protocol + " " + bytes_n
        file.write(stroka + "\n")
        return stroka


def generate_date():
    month = random.choice(["Jul", "May", "Apr", "Mar"])
    day = str(random.randint(1, 28))
    year = str(random.randint(2004, 2009))
    hour = str(random.randint(1, 23))
    minuts = str(random.randint(0, 59))
    secunds = str(random.randint(0, 59))
    chas_poias = random.choice(["+003", "+002"])
    rsl = "[" + day + "/" + month + "/" + year + ":" + hour + ":" + minuts + ":" + secunds + " " + chas_poias + "]"
    return rsl
            