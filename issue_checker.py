#!/usr/bin/env python

import urllib2
import json
from config import config
from mysql_handler import mysql_handler

class issue_checker:

   def verify_changes(self, id_num, title, description):
      new_mysql_handler = mysql_handler()
      stored_data = new_mysql_handler.verify_issue(id_num)
      if not (str(stored_data[0]) == title and str(stored_data[1]) == description):
         new_mysql_handler.update_issue(id_num, title, description)
         return True
      else:
         return False

   def submit_changes(self, json_data):
      new_action = ({"action" : "updated"})
      json_data = ({"issue" : json_data})
      new_action.update(json_data)
      
      req = urllib2.Request(self.forward_url)
      req.add_header('Content-Type', 'application/json');
      req.add_header('X-GitHub-Event', 'issues');
      response = urllib2.urlopen(req, json.dumps(new_action))
      print response.read()


   def __init__(self):
      config_data = config()
      self.forward_url = config_data.custom_url
      self.get_url = config_data.github_api + config_data.user_name + '/' + config_data.repo_name + '/issues'
      self.run_checker()

   def run_checker(self):
      req = urllib2.Request(self.get_url)
      response = urllib2.urlopen(req)
      try:
         self.issues_data = json.loads(response.read())
         for curr_json in self.issues_data:
            if not curr_json['state'] == 'closed':
               if self.verify_changes(curr_json['id'], curr_json['title'], curr_json['body']):
                  self.submit_changes(curr_json)
      except ValueError as err :
         print err



"""
if __name__ == '__main__':
   new_issue_checker = issue_checker()

"""
