from flask import Flask, render_template, request, url_for
app = Flask(__name__)

import myModels as md
students, departments = md.initialize()

dept = {}
curr_idx = 0
for d in departments:
    dept[d.dept_code] = d.dept_name

# Get current 5 student list to display
def get_std_list():
    global students
    _len, prev, nxt = len(students), False, False
    dummy = []
    if _len < curr_idx + 5:
        for i in range(curr_idx, _len):
            dummy.append(students[i])
    else :
        for i in range(curr_idx, curr_idx+5):
            dummy.append(students[i])
    if curr_idx == 0:
        prev = True
    if curr_idx + 5 >= _len:
        nxt = True
    return dummy, prev, nxt

# DISPLAY ALL STUDENTS
@app.route('/')
def home():
    global students
    _len = len(students)
    # Show only 5 students at a time ->
    stdList, prev, nxt = get_std_list()
    return render_template("displayAll.html", stds = stdList, _len = len(stdList), dept = dept, status = 0, disPrev = prev, disNxt = nxt)

# ADDING A STUDENT
@app.route('/add')
def add():
    return render_template("add.html", depts = dept.values())

@app.route('/add', methods=['POST'])
def add_student():
    global students
    
    roll = int(request.form['roll'])
    dept_code = -1
    for d in departments:
        if d.dept_name == request.form['dept']:
            dept_code = d.dept_code
            break
    name = request.form['name']
    addr = request.form['addr']
    phone = request.form['phone']

    std = md.Student(roll, dept_code, name, addr, phone)
    valid, students = md.add_student(std, students)
    stdLst, prev, nxt = get_std_list()
    if valid:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = 1, disPrev = prev, disNxt = nxt)
    else:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = -1, err_msg = "Roll number already exists", disPrev = prev, disNxt = nxt)

# DELETING A STUDENT
def delete(roll):
    global students
    valid, students = md.delete_student(roll, students)
    stdLst, prev, nxt = get_std_list()
    if valid:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = 1, disPrev = prev, disNxt = nxt)
    else:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = -1, err_msg = "Roll number does not exist", disPrev = prev, disNxt = nxt)

# SEARCHING A STUDENT
def search(roll):
    global students, dept
    valid, std = md.get_student(roll, students)
    stdLst, prev, nxt = get_std_list()
    if valid:
        return render_template("single.html", std = std, dept = dept)
    else:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = -1, err_msg = "Roll number does not exist", disPrev = prev, disNxt = nxt)

# UPDATING A STUDENT
def update(roll):
    global students, dept
    valid, std = md.get_student(roll, students)
    stdLst, prev, nxt = get_std_list()
    if valid:
        return render_template("update.html", std = std, depts = dept.values(), allDepts = dept)
    else:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = -1, err_msg = "Roll number does not exist", disPrev = prev, disNxt = nxt)

@app.route('/update', methods=['POST'])
def update_student():
    global students
    roll = int(request.form['roll'])
    dept_code = -1
    for d in departments:
        if d.dept_name == request.form['dept']:
            dept_code = d.dept_code
            break
    name = request.form['name']
    addr = request.form['addr']
    phone = request.form['phone']

    std = md.Student(roll, dept_code, name, addr, phone)
    valid, students = md.update_student(std, students)
    stdLst, prev, nxt = get_std_list()
    return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = 1, disPrev = prev, disNxt = nxt)

# OPERATIONS -> SEARCH, UPDATE, DELETE
@app.route('/operations', methods=['POST'])
def operations():
    stdLst, prev, nxt = get_std_list()
    if request.form['action'] == "Delete":
        return delete(int(request.form['roll_num']))
    elif request.form['action'] == "Search":
        return search(int(request.form['roll_num']))
    elif request.form['action'] == "Update":
        return update(int(request.form['roll_num']))
    else:
        return render_template("displayAll.html", stds = stdLst, _len = len(stdLst), dept = dept, status = -1, err_msg = "Roll number does not exist", disPrev = prev, disNxt = nxt)

# DISPLAY NEXT AND PREV STUDENT LISTS ->
@app.route('/previous')
def show_prev():
    global students, curr_idx
    _len = len(students)
    if curr_idx - 5 >= 0:
        curr_idx -= 5
    stdLst, prev, nxt = get_std_list()
    return render_template (
        "displayAll.html", 
        stds = stdLst, 
        _len = len(stdLst), 
        dept = dept, 
        status = 0,
        disPrev = prev,
        disNxt = nxt
    )

@app.route('/next')
def show_next():
    global students, curr_idx
    _len = len(students)
    if curr_idx + 5 < _len :
        curr_idx += 5
    stdLst, prev, nxt = get_std_list()
    return render_template(
        "displayAll.html", 
        stds = stdLst, 
        _len = len(stdLst), 
        dept = dept, 
        status = 0,
        disPrev = prev,
        disNxt = nxt
    )

# ERROR HANDLING
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)