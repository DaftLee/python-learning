# _*_coding:utf-8_*_
import pickle

import time

import DB_pickle

#取款
def draw_balance(account,money):
    database=DB_pickle.load()
    if money>database[account][1]:
        print "余额不足"
    else:
        database[account][1] -=money
        DB_pickle.dump(database)
        deal_str=time.strftime("%Y-%m-%d %X",time.localtime())+" "+"取出%s元，当前余额%s元 \n"%(money,database[account][1])
        deal_f = file("deal_%s.txt" % account,'a')
        deal_f.write(deal_str)
        deal_f.close

#查询余额
def query_balance(account):
    database = DB_pickle.load()
    print "您的余额为：%s"%database[account][1]
    return database[account][1]

#还款
def pay_deal(account,money):
    database = DB_pickle.load()
    database[account][1] += money
    DB_pickle.dump(database)
    deal_str = time.strftime("%Y-%m-%d %X", time.localtime()) + " " + "还款%s元，当前余额%s元 \n" % (money, database[account][1])
    deal_f = file("deal_%s.txt" % account, 'a')
    deal_f.write(deal_str)
    deal_f.close

if __name__ == '__main__':
    pass
