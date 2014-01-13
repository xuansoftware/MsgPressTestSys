# -*- coding: utf-8 -*-
'''
Created on Jan 13, 2014

@author: andy
'''

import time
import const
import sqlite3


class TaskInfo(object):
    '''任务数据结构'''
    def __init__(self):
        self.task_id = const.TaskIdDefult #任务id
        self.login_uid = 0
        self.task_uid = 0
        self.msg = None
        self.type = 0 #任务类型
        self.count = 0
        self.status = const.TaskStatusWaitRun
        
def getTask():
    '''获取任务'''
    
    task = TaskInfo()

    conn=sqlite3.connect(const.sqliteDb)
    cur=conn.cursor()
    cur.execute('SELECT * FROM task_info WHERE status=0')
    result = cur.fetchone()
    if result is not None:
        task.task_id = result[1]
        print 'getTask task_id:%d'%task.task_id
        task.task_uid = str(result[2])
        print 'getTask task_uid:%s'%task.task_uid
        task.login_uid = str(result[3])
        print 'getTask login_uid:%s'%task.login_uid
        task.msg = str(result[4])
        print 'getTask msg:%s'%task.msg
        task.type = result[5]
        print 'getTask type:%d'%task.type
        task.count = result[6]
        print 'getTask count:%d'%task.count
        task.status = result[7]
        print 'getTask status:%d'%task.status
        
#         cur.execute('UPDATE task_info SET status=%d WHERE task_id=%d'%(const.TaskStatusReady, task.task_id))
        cur.execute(const.SqlUpdateTaskStatus%(const.TaskStatusReady, task.task_id))
        conn.commit();
    cur.close()
    conn.close()

    return task

def runTask():
    print 'commond is run'

if __name__ == '__main__':
    while 1:
        task = getTask()
        if task.task_id != const.TaskIdDefult:
            runTask()
        time.sleep(1)
    
    pass