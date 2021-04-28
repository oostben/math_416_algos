means = []
grades = []
out_ofs = []

stop = False
i = 1

while(not stop):
    print(i)
    str_in =input("enter mean: ")
    if str_in == "stop":
        stop = True
    else:
        means.append(float(str_in))
    i += 1


stop = False
i = 1

while(not stop):
    print(i)
    str_in =input("enter grade: ")
    if str_in == "stop":
        stop = True
    else:
        grades.append(float(str_in))
    i += 1

stop = False
i = 1

while(not stop):
    print(i)
    str_in =input("enter out of: ")
    if str_in == "stop":
        stop = True
    else:
        out_ofs.append(float(str_in))
    i += 1

print("length means:",len(means))
print("length grades:",len(grades))
print("length out_ofs:",len(out_ofs))

if len(grades) != len(means) != len(out_ofs):
    print("ERROR")

total_mean = 0
total_grade = 0
total_out_of= 0


for mean in means: total_mean += mean
for grade in grades: total_grade += grade
for out_of in out_ofs: total_out_of += out_of


print("total_mean:", total_mean)
print("total_grade:", total_grade)
print("total_out_of:", total_out_of)


