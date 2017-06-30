#!/usr/bin/pyhton3
#-*- coding:UTF-8 -*-
import _sqlite3
import xlrd
import uuid

#init
cx = _sqlite3.connect("tickets.db")

xlsfile_early = r'list_early.xlsx'
xlsfile_benefit = r'list_benefit.xlsx'
xlsfile_normal = r'list_normal.xlsx'

book_early = xlrd.open_workbook(xlsfile_early)
book_benefit = xlrd.open_workbook(xlsfile_benefit)
book_normal = xlrd.open_workbook(xlsfile_normal)


class ticketInfo:
    def initInfo(name,enname,cell,email,city,devision,area,club,price):
        self.tid = uuid.uuid1()
        self.tname = name
        self.tenname = enname
        self.tcell = cell
        self.temail = email
        self.tcity = city
        self.tdevision = devision
        self.tarea = area
        self.tclub = club
        self.tprice = price
        self.tstatus = 0

    # db operate
    def insert_db(self):
        sql = "insert into TB_TICKETINFO(TID ,TNAME ,TENNAME ,TCELL,TEMAIL,TCITY,TDEVISION,TAREA,TCLUB,TPRICE,TSTATUS) \
               VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (self.tid,self.tname,self.tenname, self.tcell,self.temail,self.tcity,self.tdevision,self.tarea,self.tclub,self.tprice, self.tstatus)
        cx.execute(sql)
        cx.commit()
    # end

#excel operate
def read_excel():
    #early excel
    sheet = book_early.sheets()[0]  # sheets返回一个sheet列表
    nrows = sheet.nrows  # 行总数
    ncols = sheet.ncols  # 列总数


    tInfo = ticketInfo()

    for i in range(1,nrows):
        tInfo.tid =  "'" + str(uuid.uuid1()) + "'"
        tInfo.tprice = "'" + str(600) + "'"
        tInfo.tstatus = "'" + str(0) + "'"
        tInfo.tname = "'" + sheet.cell_value(i, 1) + "'"
        tInfo.tenname = "'" + sheet.cell_value(i, 2) + "'"
        tInfo.tcell = "'" + str(sheet.cell_value(i, 3)) + "'"
        tInfo.temail = "'" + sheet.cell_value(i, 4) + "'"
        tInfo.tcity = "'" + sheet.cell_value(i, 5) + "'"
        tInfo.tdevision = "'" + sheet.cell_value(i, 6) + "'"
        tInfo.tarea = "'" + sheet.cell_value(i, 7) + "'"
        tInfo.tclub = "'" + sheet.cell_value(i, 8) + "'"
        tInfo.insert_db()
    #end

     # benefit excel
    sheet = book_benefit.sheets()[0]  # sheets返回一个sheet列表
    nrows = sheet.nrows  # 行总数
    ncols = sheet.ncols  # 列总数


    for i in range(1, nrows):
        tInfo.tid = "'" + str(uuid.uuid1()) + "'"
        tInfo.tprice = "'" + str(650) + "'"
        tInfo.tstatus = "'" + str(0) + "'"
        tInfo.tname = "'" + sheet.cell_value(i, 1) + "'"
        tInfo.tenname = "'" + sheet.cell_value(i, 2) + "'"
        tInfo.tcell = "'" + str(sheet.cell_value(i, 3)) + "'"
        tInfo.temail = "'" + sheet.cell_value(i, 4) + "'"
        tInfo.tcity = "'" + sheet.cell_value(i, 5) + "'"
        tInfo.tdevision = "'" + sheet.cell_value(i, 6) + "'"
        tInfo.tarea = "'" + sheet.cell_value(i, 7) + "'"
        tInfo.tclub = "'" + sheet.cell_value(i, 8) + "'"
        tInfo.insert_db()
        # end

        # benefit excel
    sheet = book_normal.sheets()[0]  # sheets返回一个sheet列表
    nrows = sheet.nrows  # 行总数
    ncols = sheet.ncols  # 列总数


    for i in range(1, nrows):
        tInfo.tid = "'" + str(uuid.uuid1()) + "'"
        tInfo.tprice = "'" + str(750) + "'"
        tInfo.tstatus = "'" + str(0) + "'"
        tInfo.tname = "'" + sheet.cell_value(i, 1) + "'"
        tInfo.tenname = "'" + sheet.cell_value(i, 2) + "'"
        tInfo.tcell = "'" + str(sheet.cell_value(i, 3)) + "'"
        tInfo.temail = "'" + sheet.cell_value(i, 4) + "'"
        tInfo.tcity = "'" + sheet.cell_value(i, 5) + "'"
        tInfo.tdevision = "'" + sheet.cell_value(i, 6) + "'"
        tInfo.tarea = "'" + sheet.cell_value(i, 7) + "'"
        tInfo.tclub = "'" + sheet.cell_value(i, 8) + "'"
        if tInfo.tcell != "''":
            tInfo.insert_db()
    # end

read_excel()

cx.close()