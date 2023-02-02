import random
import string

import cherrypy as cherrypy
from peewee import *
import datetime

db = SqliteDatabase('data.db')


def parseToHtmlTable(strings):
    stringi = ""
    for x in strings:
        stringi += "<tr>"
        for y in x:
            stringi += "<td>"
            stringi += str(y)
            stringi += "</td>"
        stringi += "</tr>"
    return stringi


def add(number, fio, dataTime, text):
    APPLab(
        number=number,
        fio=fio,
        dateTime=dataTime,
        text=text
    ).save()


class BaseModel(Model):
    class Meta:
        database = db


class APPLab(BaseModel):
    class Meta:
        db_table = 'lab6'

    idx = PrimaryKeyField(unique=True)
    number = IntegerField()
    fio = IntegerField()
    dateTime = DateTimeField()
    text = IntegerField()

    def getColumn(self):
        cursor = db.cursor()

        cursor.execute('PRAGMA table_info("lab6")')
        column_names = [i[1] for i in cursor.fetchall()]

        return column_names

    def getStrings(self):
        cursor = db.cursor()

        sqlite_select_query = """SELECT * from lab6"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        return records


class Page(object):
    columns = {}
    visit = ""

    def __init__(self, c, v):
        self.columns = c
        self.visit = v

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>Lab6</title>
            </head>
                <body>
                    <table border="1">
                        <caption>Lab6</caption>
                            <tr>
                                {"".join([
            "<th>" + i + "</th>"
            for i in self.columns])}
                            </tr>   
                                {stringi}
                    </table>
                </body>
        </html>
        
        '''


if __name__ == '__main__':
    db.create_tables([APPLab])
    app = APPLab()
    add(5, "F", datetime.datetime(2023, 4, 4, 18, 50), "Hello2")

    columns = app.getColumn()
    strings = app.getStrings()

    stringi = parseToHtmlTable(strings)

    cherrypy.quickstart(Page(columns, stringi))

    db.close()
