from library import psycopg2
from generator_log import generate_log
from datetime import datetime
from logs_parser import parse
from config import host, user, password, db_name

def genarate_logs(quantity):
    for i in range(quantity):
        generate_log("C:\projects\practice-2023\logs.txt")

def main():    
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            with open("C:\projects\practice-2023\logs.txt", 'r') as file:
                for line in file.readlines():
                    log = parse(line)
                    cursor.execute("SELECT * FROM logs WHERE ip=\'{}\' AND created_at=\'{}\' AND gmt=\'{}\' AND request=\'{}\' AND adress=\'{}\' AND http=\'{}\' AND code={} AND bytes={}".format(log._ip,
                                                   log._created_at, log._gmt, log._request, log._adress, log._http, log._code, log._bytes))
                    if cursor.fetchall() == []:
                        cursor.execute(log.insert_request())
                        connection.commit()
        find_by = input("По какому критерию вы бы хотели вывести логи? Варианты: ip, дата, между двумя датами, код страницы, тип запроса   ")
        with connection.cursor() as cursor:
            if find_by == "ip":
                ip = input("Введите ip: ")
                cursor.execute("SELECT * FROM logs WHERE ip = \'{}\'".format(ip))
            elif find_by == "дата":
                print("Дату необходимо вводить в формате год-месяц-день: 2000-01-01")
                date = input("Введите дату: ")
                created_at = datetime.strptime(date + " 23:59:59", '%Y-%m-%d %H:%M:%S')
                cursor.execute("SELECT * FROM logs WHERE created_at between \'{}\' AND \'{}\'".format(datetime.strptime(date + " 00:00:00",
                                                                                                     '%Y-%m-%d %H:%M:%S'), created_at))
            elif find_by == "между двумя датами":
                print("Дату необходимо вводить в формате год-месяц-день: 2000-01-01")
                date1 = datetime.strptime(input("Введите первую дату: ") + " 00:00:00", '%Y-%m-%d %H:%M:%S')
                date2 = datetime.strptime(input("Введите вторую дату: ") + " 23:59:59", '%Y-%m-%d %H:%M:%S')
                cursor.execute("SELECT * FROM logs WHERE created_at between \'{}\' AND \'{}\'".format(date1, date2))
            elif find_by == "код страницы":
                code = int(input("Введите код страницы: "))
                cursor.execute("SELECT * FROM logs WHERE code = {}".format(code))
            elif find_by == "тип запроса":
                request = input("Введите тип запроса: ").upper()
                cursor.execute("SELECT * FROM logs WHERE request = \'{}\'".format(request))
            else:
                print("Вы не правильно ввели критерий поиска. Попробуйте ещё раз")

            logs = cursor.fetchall()
            if logs == []: print ("Логов по данному критерию не найдено")
            else:
                print("Найденные логи:" + "\n")
                for i in logs:
                    print(i)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()


main()