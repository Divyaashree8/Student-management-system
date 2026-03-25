import sqlite3
co=sqlite3.connect("students.db")
cursor=co.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id integer primary key,
    name text,
    age INTEGER,
    course text)
""")
co.commit()
co.close()
def add_student(name,age,course):
    co=sqlite3.connect("students.db")
    cursor=co.cursor()
    cursor.execute("INSERT INTO students (name,age,course) Values(?,?,?)",(name,age,course))
    co.commit()
    co.close()
def view_students():
    co=sqlite3.connect("students.db")
    cursor=co.cursor()
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        co.close()
def search_student(name):
    co=sqlite3.connect("students.db")
    cursor=co.cursor()
    cursor.execute("select * from students where name=?",(name,))
    rows=cursor.fetchall()
    print(rows)
    co.close()
def update_student(name,age,course):
    co=sqlite3.connect("students.db")
    cursor=co.cursor()
    cursor.execute("""update students SET name=?,age=?,course=? where id=?""",(name,age,course,id))
    co.commit()
    co.close()
def delete_student(id):
    co=sqlite3.connect("students.db")
    cursor=co.cursor()
    cursor.execute("delete from students where id=?",(id,))
    co.commit()
    co.close()
while True:
    print("1. Add students")
    print("2. view students")
    print("3. search students")
    print("4. update students")
    print("5. Delete students")
    print("6. Exit")
    choice=input("Enter choice:")
    if choice=="1":
       name=input("Name:")
       age=int(input("Enter age:"))
       course=input("Enter course:")
       add_student(name,age,course)
    elif choice=="2":
        view_students()
    elif choice=="3":
        name=input("Enter name:")
        search_student(name)
    elif choice=="4":
        id=int(input("Enter ID:"))
        name=input("New Name:")
        age=int(input("New Age:"))
        course=input("New course:")
        update_student(name,age,course)
    elif choice=="5":
        id= int(input("Enter id:"))
        delete_student(id)
    elif  choice=="6":
        break
    else:
        print("INVALID choice")