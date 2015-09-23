#!/usr/bin/env python

import web
import urllib2
import json

import daemon
import time
import os

from config import config
from mysql_handler import mysql_handler


class py_server:

    def __init__(self):
       urls = ('/.*', 'web_hooks')
       app = web.application(urls, globals())
       app.run()
       

class web_hooks:

    def check_content_type(self):
        try:
            self.content_type = web.ctx.env.get('CONTENT_TYPE')
            self.github_event = web.ctx.env.get('HTTP_X_GITHUB_EVENT')
            return self.content_type and self.github_event
        except:
            return False

    def forward_hook(self):
        req = urllib2.Request(self.forward_url)
        req.add_header('Content-Type', 'application/json');
        req.add_header('X-GitHub-Event', self.github_event);
        response = urllib2.urlopen(req, json.dumps(self.data))
        print response.read()


    def POST(self):
        new_config = config()
        self.forward_url = new_config.custom_url
        self.events_list = new_config.events_list

        content_result = self.check_content_type()
        if(content_result):
            print "Content-Type: text/html"
            print
            self.data = web.data()
            #Check if the event is an issue, otherwise forward the payload to the custom url
            if self.github_event == "issues":
                json_data = json.loads(self.data)
                if json_data['action'] == "opened" or json_data['action'] == "reopened":
                    #Add new issue to database
                    json_data = json_data['issue']
                    issue_id = json_data['id']
                    issue_title = json_data['title']
                    issue_description = json_data['body']
                    new_mysql_handler = mysql_handler()
                    new_mysql_handler.add_new_issue(issue_id, issue_title, issue_description)
                elif json_data['action'] == "closed":
                    #As the issue is closed we can delete it from the table
                    json_data = json_data['issue']
                    issue_id = json_data['id']
                    new_mysql_handler = mysql_handler()
                    new_mysql_handler.close_issue(issue_id)
                #Forward issue
                self.forward_hook()
            elif self.github_event in self.events_list:
                self.forward_hook()
        else:
            print "Content-Type: text/html"
            print
            print "Nothing to see here"
            print

            
if __name__ == '__main__':
    py_server()
