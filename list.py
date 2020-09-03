userdataname = ["admin","default"]
userdatapwd = ["123456","456789"]
def login():
    username = input("请输入您的用户名：")
    if username in userdataname:
        userindex = userdataname.index(str(username))
        login_pwd(userindex)
    else:
        print("您的用户不存在，请返回注册")
def login_pwd(userindex):
    userpwd = input("请输入您的密码：")
    if userpwd == userdatapwd[userindex]:
        print("登录成功！")
    else:
        print("密码错误！")
        login_pwd(userindex)
login()