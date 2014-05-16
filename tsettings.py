#! /usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sys
import os
import paramiko


class ChangePref(unittest.TestCase):
        
    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""

        if sys.exc_info()[0]:   
            print sys.exc_info()[0]


    

    def test_changer(self):

        cnt=0 #счетчик ошибок теста
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(os.getenv('HOST'),username=os.getenv('USERNAME'),password=os.getenv('PASS'))#connect to host
            ssh.exec_command('sudo cp /home/tdevel/%s/operaprefs.ini /home/terminal/.opera' % os.getenv('CHOISE'))
            ssh.exec_command('sudo cp /home/tdevel/%s/script.js /home/terminal/.opera/userjs' % os.getenv('CHOISE'))
            ssh.exec_command('sudo killall opera')
            ssh.close()
            print 'Files successfully changed'
        except:
            cnt=1
            print 'Error occurred!!!'
       
        assert cnt==0, (u'Error!!!')
