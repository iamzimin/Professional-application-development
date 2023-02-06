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
            stringi += "<th style='color: white; border-collapse: separate; border-radius: 10px; " \
                       "background: #274524; padding: 10px; text-align:center; font-size: 30px'> "
            stringi += str(y)
            stringi += "</th>"
        stringi += "</tr>"
    return stringi





class BaseModel(Model):
    class Meta:
        database = db


class APPLab(BaseModel):
    class Meta:
        db_table = 'lab6'

    idx = PrimaryKeyField(unique=True)
    # number = IntegerField()
    fio = IntegerField()
    dateTime = DateTimeField()
    text = IntegerField()

    def Update(self, sid, fio, dateTime, text):
        appLab = APPLab.get(idx=sid)
        appLab.fio = fio
        appLab.dateTime = dateTime
        appLab.text = text
        appLab.save()

    def Add(self, fio, dataTime, text):
        APPLab(
            fio=fio,
            dateTime=dataTime,
            text=text
        ).save()

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
                <title>Лаба 6 😎️</title>
            </head>
                <body style="background: black">
                    <table  style="
                                margin-left: auto;
                                margin-right: auto;
                                text-align: left;
                                border-collapse: separate;
                                border-radius: 15px;
                                border-spacing: 5px;
                                background: #1e291d;
                                color: #c7c7c7;
                                border: 2px solid #429641;"
                    >
                        <h1 style="color: white; text-align: center; font-size: 50px;">Лаба 6 😎️</h1>
                            <tr>
                                {
                                    "".join(["<th style='color: white; text-align:center; padding: 10px; font-size: 30px;'>" + i + "</th>"
                                            for i in self.columns])
                                }
                            </tr>   
                                {stringi}
                    </table>
                </body>
        </html>
        
        '''


if __name__ == '__main__':
    db.create_tables([APPLab])
    app = APPLab()
    # app.Add("C", datetime.datetime(2023, 4, 4, 18, 50), "Hello3")
    app.Update(3, "Test", datetime.datetime(2025, 5, 5, 18, 50), "HeHeHe")

    columns = app.getColumn()
    strings = app.getStrings()

    stringi = parseToHtmlTable(strings)

    cherrypy.quickstart(Page(columns, stringi))

    db.close()
