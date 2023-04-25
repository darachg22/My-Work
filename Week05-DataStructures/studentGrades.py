student_name = input("Enter student name: ")
modules = {}

while True:
    module_name = input("Enter module name (blank to exit): ")
    if not module_name:
        break
    modules[module_name] = None

for module_name in modules:
    grade = input("Enter grade for {}: ".format(module_name))
    modules[module_name] = grade


print("Student record:")
print("Name:", student_name)
for module_name, grade in modules.items():
    print("Module:", module_name, "Grade:", grade)