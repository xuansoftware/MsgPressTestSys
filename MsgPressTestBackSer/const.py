# -*- coding: utf-8 -*-
'''
Created on Jan 13, 2014

@author: andy
'''
'''任务状态'''
TaskStatusWaitRun = 0
TaskStatusReady = 1
TaskStatusRunning = 2
TaskStatusComplish = 3
TaskStatusError = 1000

'''任务类型'''
TaskC2C = 1
TaskGroup = 2

'''任务id'''
TaskIdDefult = -1

sqliteDb = '/home/andy/root/dev/pro/git/MsgPressTest/MsgPressTest/sqlite.db'

'''commandline'''
Command= ''

SqlSelectTask = 'SELECT * FROM task_info WHERE task_id=%d'
SqlUpdateTaskStatus = 'UPDATE task_info SET status=%d WHERE task_id=%d'
# TaskSQL_insertTaskResult = 'INSERT INTO memory_analyze_result(id,task_id,url) VALUES (NULL,\'%d\',\'%s\')'