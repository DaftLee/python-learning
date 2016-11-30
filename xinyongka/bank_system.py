# _*_coding:utf-8_*_
import Account

str_re = '''
-----输入操作-----

1.返回上层    2.退出系统

'''

str = '''
-----输入操作-----

1.查询    2.取款

3.还款    4.退出

'''

str_draw = '''
-----输入金额-----

'''

#返回上层函数
def returnlevel():

    print str_re
    while True:
        select = raw_input().strip()
        if len(select) == 0:
            continue
        elif select.isdigit() == False:
            print "非数字，请输入1-2的数字"
            continue
        else:
            select = int(select)
            if select!=1 and select!=2:
                print "请输入1-2的数字"
                continue
            elif select==1:
                return False
            else:
                return True

def bank_system(account):
    exit_flag=False
    while True:

        print str
        select=raw_input().strip()
        if len(select)==0:
            continue
        elif select.isdigit()==False:
            print "请输入1-4的数字"
            continue
        else:
            select=int(select)
            if select<1 or select>4:
                print "请输入1-4的数字"
                continue

            #查询
            elif select==1:
                Account.query_balance(account)
                exit_flag=returnlevel()
            #取款
            elif select==2:
                print str_draw
                while True:
                    money=raw_input("金额：").strip()
                    if len(money)==0:continue
                    elif money.isdigit()==False:
                        print "请输入非负数字！"
                        continue
                    else:
                        money=int(money)
                        if money<0:
                            print "请输入非负数字"
                            continue
                        else:
                            Account.draw_balance(account,money)
                            break
                exit_flag=returnlevel()

            #还款
            elif select==3:
                current_balance=Account.query_balance(account)
                print "您需还款：%s"%((10000-current_balance)*(1+0.05))
                print str_draw
                while True:
                    money = raw_input("金额：").strip()
                    if len(money) == 0:
                        continue
                    elif money.isdigit() == False:
                        print "请输入非负数字！"
                        continue
                    else:
                        money = int(money)
                        if money < 0:
                            print "请输入非负数字"
                            continue
                        else:
                            real_money=float('%.2f'%(money/1.05))
                            Account.pay_deal(account,real_money)
                            break
                exit_flag=returnlevel()
            # 退出系统
            else:
                exit_flag=True


        #flag判断是否退出系统
        if exit_flag==True:
            print "bye"
            break
        else:
            continue

if __name__ == '__main__':
    pass

