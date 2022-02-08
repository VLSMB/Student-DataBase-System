import pymysql

def getuser():
    """获取用户列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from admin")
    userdb = dict(cursor.fetchall())
    cursor.close()
    conn.close()
    return userdb

def adduser(user, pwd):
    """添加用户信息"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("insert into admin(userName, userPwd) values (%s, %s)", [user, pwd])
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def delteuser(user):
    """删除用户"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM admin WHERE userName = %s", (user,))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def edituser(which, user, password):
    """修改用户名或密码，0代表修改用户，1代表修改密码"""
    print(which, user, password)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute("UPDATE admin SET userName=%s WHERE userPwd=%s", (user, password))
        elif which == 1:
            cursor.execute("UPDATE admin SET userPwd=%s WHERE userName=%s", (password, user))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def getgrade():
    """获取年级列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from grade")
    gradedb = dict(cursor.fetchall())
    cursor.close()
    conn.close()
    return gradedb

def deltegrade(id):
    """删除年级"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM grade WHERE gradeID = %s", (id,))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def addgrade(id, name):
    """添加年级信息"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("insert into grade(gradeID, gradeName) values (%s, %s)", [id, name])
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def editgrade(which, id, name):
    """修改年级编号或名称，0代表编号，1代表名称"""
    print(which, id, name)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute("UPDATE grade SET gradeID=%s WHERE gradeName=%s", (id, name))
        elif which == 1:
            cursor.execute(f"UPDATE `studentdb`.`grade` SET `gradeName` = %s WHERE `gradeID` = {int(id)}", (name, ))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def getclass():
    """获取班级列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from class")
    classdb = cursor.fetchall()
    cursor.close()
    conn.close()
    return classdb

def addclass(classID, gradeID, className):
    """添加班级"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("insert into class(classID, gradeID, className) values (%s, %s, %s)", (classID, gradeID, className))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def delteclass(id):
    """删除班级"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM class WHERE classID = %s", (id,))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def editclass(which, classID, gradeID, className):
    """修改编号或名称，0代表班级ID，1代表年级ID，2代表班级名称"""
    print(which, classID, gradeID, className)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute(f"UPDATE `studentdb`.`class` SET `classID` = {int(classID)} WHERE `gradeID` = {int(gradeID)}")
        elif which == 1:
            cursor.execute(f"UPDATE `studentdb`.`class` SET `gradeID` = {int(gradeID)} WHERE `classID` = {int(classID)}")
        elif which == 2:
            cursor.execute(f"UPDATE `studentdb`.`class` SET `className` = %s WHERE `classID` = {int(classID)}", (className, ))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def getsubject():
    """获取科目列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from subject")
    db = dict(cursor.fetchall())
    cursor.close()
    conn.close()
    return db

def deltesubject(id):
    """删除科目"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM subject WHERE subID = %s", (str(id),))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def addsubject(id, name):
    """添加科目信息"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("insert into subject(subID, subName) values (%s, %s)", [id, name])
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def editsubject(which, id, name):
    """修改编号或名称，0代表编号，1代表名称"""
    print(which, id, name)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute("UPDATE subject SET subID=%s WHERE subName=%s", (id, name))
        elif which == 1:
            cursor.execute(f"UPDATE `studentdb`.`subject` SET `subName` = %s WHERE `subID` = {int(id)}", (name, ))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def getexamkinds():
    """获取科目列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from examkinds")
    db = dict(cursor.fetchall())
    cursor.close()
    conn.close()
    return db

def delteexamkinds(id):
    """删除科目"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM examkinds WHERE kindID = %s", (str(id),))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def addexamkinds(id, name):
    """添加科目信息"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("insert into examkinds(kindID, kindName) values (%s, %s)", [id, name])
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def editexamkinds(which, id, name):
    """修改编号或名称，0代表编号，1代表名称"""
    print(which, id, name)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute("UPDATE examkinds SET kindID=%s WHERE kindName=%s", (id, name))
        elif which == 1:
            cursor.execute(f"UPDATE `studentdb`.`examkinds` SET `kindName` = %s WHERE `kindID` = {int(id)}", (name, ))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def getstudent():
    """获取学生列表"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from student")
    db = cursor.fetchall()
    cursor.close()
    conn.close()
    return db

def deltestudent(id):
    """删除学生"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM student WHERE stuID = %s", (id,))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def addstudent(addtup):
    """增加学生记录，addtup(stuID, stuName, classID, gradeID, age, sex, phone, address)"""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO `studentdb`.`student` (`stuID`, `stuName`, `classID`, `gradeID`, `age`, `sex`, `phone`, `address`) VALUES (%s, %s, {addtup[2]}, {addtup[3]}, {addtup[4]}, %s, %s, %s)", (addtup[0], addtup[1], addtup[5], addtup[6], addtup[7]))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

def editstudent(which, stuID, THING):
    """修改学生信息，0：stuID 1：stuName 2：class 3：age 4：sex 5：phone 6：address"""
    print(which, stuID)
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    try:
        if which == 0:
            cursor.execute("UPDATE `studentdb`.`student` SET `stuID` = %s WHERE `stuID` = %s", (THING, stuID))
        elif which == 1:
            cursor.execute("UPDATE `studentdb`.`student` SET `stuName` = %s WHERE `stuID` = %s", (THING, stuID))
        elif which == 2:
            cursor.execute(f"UPDATE `studentdb`.`student` SET `classID` = {THING[0]}, `gradeID` = {THING[1]} WHERE `stuID` = %s", (stuID,))
        elif which == 3:
            cursor.execute(f"UPDATE `studentdb`.`student` SET `age` = {THING} WHERE `stuID` = %s", (stuID,))
        elif which == 4:
            cursor.execute("UPDATE `studentdb`.`student` SET `sex` = %s WHERE `stuID` = %s", (THING, stuID))
        elif which == 5:
            cursor.execute("UPDATE `studentdb`.`student` SET `phone` = %s WHERE `stuID` = %s", (THING, stuID))
        elif which == 6:
            cursor.execute("UPDATE `studentdb`.`student` SET `address` = %s WHERE `stuID` = %s", (THING, stuID))
    except:
        conn.rollback()
        conn.close()
        return False
    else:
        cursor.close()
        conn.commit()
        conn.close()
        return True

class result:
    """有关result的操作，最后我才想到用类简化..."""

    def editkindID(self, kindID, ID):
        """修改种类ID"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(f"UPDATE `studentdb`.`result` SET `kindID` = {int(kindID)} WHERE `ID` = {int(ID)}")
        except:
            conn.rollback()
            conn.close()
            return False
        else:
            cursor.close()
            conn.commit()
            conn.close()
            return True
    def editsubID(self, subID, ID):
        """修改学科ID"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(f"UPDATE `studentdb`.`result` SET `subID` = {int(subID)} WHERE `ID` = {int(ID)}")
        except:
            conn.rollback()
            conn.close()
            return False
        else:
            cursor.close()
            conn.commit()
            conn.close()
            return True
    def editgrade(self, grade, ID):
        """修改学科ID"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(f"UPDATE `studentdb`.`result` SET `result` = {int(grade)} WHERE `ID` = {int(ID)}")
        except:
            conn.rollback()
            conn.close()
            return False
        else:
            cursor.close()
            conn.commit()
            conn.close()
            return True
    def getresult(self):
        """获取成绩表"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select * from result")
        db = cursor.fetchall()
        cursor.close()
        conn.close()
        return db
    def deltestudent(self, id):
        """删除成绩"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(f"DELETE FROM result WHERE ID = {int(id)}")
        except:
            conn.rollback()
            conn.close()
            return False
        else:
            cursor.close()
            conn.commit()
            conn.close()
            return True
    def addresult(self, addtup):
        """增加成绩记录，addtup(ID, stuID, kindID, subID, result)"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(
                f"INSERT INTO `studentdb`.`result` (`ID`, `stuID`, `kindID`, `subID`, `result`) VALUES ({int(addtup[0])}, %s, {int(addtup[2])}, {int(addtup[3])}, {addtup[4]:.2f})",
                (addtup[1],))
        except:
            conn.rollback()
            conn.close()
            return False
        else:
            cursor.close()
            conn.commit()
            conn.close()
            return True
    def __init__(self):
        self.examkindsdict = getexamkinds()
        self.examkindsdict_copy = dict(zip(list(self.examkindsdict.values()), list(self.examkindsdict.keys())))
        self.gradedict = getgrade()
        self.subjectdict = getsubject()
        self.subjectdict_copy = dict(zip(list(self.subjectdict.values()), list(self.subjectdict.keys())))
        classtup = getclass()
        classID, className = [], []
        for x, y, z in classtup:
            classID.append((x, y))
            className.append(z)
        self.classdict = dict(zip(classID, className))
        self.studenttup = getstudent()
        studentID, studentName, studentClass = [], [], []
        for x in self.studenttup:
            studentID.append(x[0])
            studentName.append(x[1])
            studentClass.append((x[2], x[3]))
        self.studentdict = dict(zip(studentID, studentName))
        self.studentdict_copy = dict(zip(studentName, studentID))
        self.stuclassdict = dict(zip(studentID, studentClass))
if __name__ == "__main__":
    conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subject WHERE subID = %s", ("6",))
    cursor.close()
    conn.commit()
    conn.close()