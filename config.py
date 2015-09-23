#!/usr/bin/env python

class config:

   def __init__(self):
      self.db_user = 'DBUSERNAME'
      self.db_pwd = 'DBPASSWORD'
      self.db_name = 'DBNAME'
      self.repo_name = "REPOSITORY"
      self.user_name = "USERNAME"
      self.github_api = u'https://api.github.com/repos/'
      self.custom_url = "CUSTOM_URL_TO_FORWARD_PAYLOAD"
      self.events_list = ['commit_comment',
                'create',
                'delete',
                'deployment',
                'deployment_status',
                'download',
                'follow',
                'fork',
                'fork_apply',
                'gist',
                'gollum',
                'issue_comment',
                'member',
                'membership',
                'page_build',
                'ping',
                'public',
                'pull_request',
                'pull_request_review_comment',
                'push',
                'release',
                'repository',
                'status',
                'team_add',
                'watch']
