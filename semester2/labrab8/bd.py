import pymysql.cursors

conn = pymysql.connect(
    host='pgsha.ru', 
    user='soft0047', 
    password='8GYuyn9g', 
    db='soft0047_labrab',
    port=35006,
    cursorclass=pymysql.cursors.DictCursor)

def add_info():
    with conn.cursor() as cur:
        sql = "INSERT INTO `students` (`StudentName`, `Rating`, `Gender`, `bday`, `city`) \
        VALUES \
        ('Мишкин', 217, 1, '2002-08-23', 'Кунгур'), \
        ('Бортич', 224, 0, '2002-06-03', 'Лысьва'),\
        ('Деревянко', 182, 0, '2002-02-20', 'Оса'),\
        ('Столбова', 194, 0, '2003-01-22', 'Кунгур'),\
        ('Хомич', 205, 0, '2002-04-23', 'Кунгур'),\
        ('Круглов', 191, 1, '2002-04-23', 'Березники'),\
        ('Иванов', 192, 1, '2002-05-17', 'Кунгур'),\
        ('Петров', 191, 1, '2002-11-25', 'Кунгур'),\
        ('Сидоров', 196, 1, '2004-01-20', 'Кунгур'),\
        ('Капустин', 196, 1, '2002-06-04', 'Кунгур'),\
        ('Томатова', 201, 0, '2003-04-16', 'Кунгур'),\
        ('Ежова', 214, 0, '2001-10-07', 'Лысьва'),\
        ('Микова', 222, 0, '2001-10-07', 'Пермь'),\
        ('Мамин', 199, 1, '2001-11-10', 'Пермь'),\
        ('Комов', 195, 1, '2002-01-17', 'Пермь');"
        cur.execute(sql)
        conn.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)


def choose_name():
    with conn.cursor() as cur:    
        sql = 'SELECT `StudentName` FROM `students` WHERE `city` = "Кунгур"'
        cur.execute(sql)
        names_from_sql = list(cur)
        conn.commit()
        for name in names_from_sql:
            print(name['StudentName'])
# choose_name()

def kungurs_mens():
    with conn.cursor() as cur:    
        sql = 'SELECT `StudentName` , `Rating` FROM `students` WHERE `Gender` = 1 AND `city` = "Кунгур"'
        cur.execute(sql)
        names_from_sql = list(cur)
        conn.commit()
        for name in names_from_sql:
            print(name['StudentName'], name['Rating'])
# kungurs_mens()

def sort_kungurs_mens():
    with conn.cursor() as cur:    
        sql = 'SELECT `StudentName` , `Rating` FROM `students` WHERE `Gender` = 1 AND `city` = "Кунгур" ORDER BY `Rating` DESC'
        cur.execute(sql)
        names_from_sql = list(cur)
        conn.commit()
        for name in names_from_sql:
            print(name['StudentName'], name['Rating'])
# sort_kungurs_mens()

def not_perm():
    with conn.cursor() as cur:    
        sql = 'SELECT `StudentName` , `bday` FROM `students` WHERE `city` <> "Пермь" ORDER BY `bday` ASC'
        cur.execute(sql)
        names_from_sql = list(cur)
        conn.commit()
        for name in names_from_sql:
            print(name['StudentName'], name['bday'])
# not_perm()
 
def super_sort():
     with conn.cursor() as cur:    
        sql = ' SELECT `StudentName` , `Rating` , `city` FROM `students` ORDER BY `city` ASC , `Rating` DESC'
        cur.execute(sql)
        names_from_sql = list(cur)
        conn.commit()
        for name in names_from_sql:
            print(name['StudentName'], name['Rating'], name['city'])
super_sort()