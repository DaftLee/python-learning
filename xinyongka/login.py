# _*_coding:utf-8_*_
import pickle,Database,DB_pickle
# 账户密码数据库

loginDB=DB_pickle.load()


# print map(lambda x:x[1],loginDB.items())

def login():
    login_flag = True  # 输入账户如果输入为空 继续
    while True:
        account = raw_input("卡号：").strip()
        if len(account) == 0:
            continue
        elif account == "quit":
            login_flag = False
            print "bye"
            break
        elif loginDB.get(account) == None:
            print "卡号不存在！"
            continue
        elif account == "quit":
            login_flag = False
            print "bye"
            break
        else:
            break
            # 验证密码
    if login_flag:
        for i in range(3):
            passwd = raw_input("密码：").strip()
            if len(passwd) == 0:
                continue
            elif passwd == "quit":
                login_flag = False
                print "bye"
                break
            elif loginDB[account][0] != passwd:
                if i == 2:
                    login_flag = False
                    print "密码错误，卡已锁定!"
                    break
                print "密码错误，你还剩%s次机会!" % (2 - i)
                continue
            else:
                print "welcome use this system!!"
                break

    if login_flag==True:
        return account
    else:
        return False
if __name__ == '__main__':

    login()
