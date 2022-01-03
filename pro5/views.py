from django.shortcuts import render
from django.http import HttpResponse
from pro5.dbconnect import cus,dbconn

def tablecreate(request):
    cus.execute('create table student(id int primary key,name varchar(30),email varchar(50))')
    dbconn.commit()
    dbconn.close()
    return HttpResponse("table is created")

def insert(request,id,name,email):
    val=[id,name,email]
    cus.execute('insert into student (id,name,email) values(%s,%s,%s)',val)
    dbconn.commit()
    return HttpResponse('record is inserted')

def select(request):
    cus.execute('select * from student')
    res=cus.fetchall()
    dbconn.commit()
    return render(request,'select.html',{'res':res})

def update(request,id,name,email):
    val1=[name,email,int(id)]
    cus.execute('update student set name=%s,email=%s where id=%s',val1)
    dbconn.commit()
    return HttpResponse('record is updated')

def delete(request,id):
    val1=[int(id)]
    cus.execute('delete from studen where id=%s',val1)
    dbconn.commit()
    return HttpResponse('record is deleted')