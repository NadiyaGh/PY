Sname = input("Enter the name of student: ")
Gr1 = float(input("Enter the first grade: "))
Gr2 = float(input("Enter the second grade: "))
Gr3 = float(input("Enter the third grade: "))

av = ((Gr1 + Gr2 + Gr3)/3)

if av>=17:
    print(Sname,"is «Great» student :) ")
elif av>=12:
    print(Sname,"is «Normal» student :| ")
else:
    print(Sname,"is «Fail» student :( ")