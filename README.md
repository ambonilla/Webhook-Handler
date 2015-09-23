# Webhook-Handler
Micro service built in Python that replay requests from Github and also provides a webhook on update of issue title and/or description.

### Dependencies

- [Daemon]
- [Web.py]
- [mysql.connector]

### Installation & Configuration

It works with MySQL to keep control of the changes in the title or description of the issues stored in Github. Therefore, is necessary to create the database and modify config.py according to the defined setup.

In addition to the database, the repository name, github username, and url to forward the payload must be included as well.

### Use

```sh
$ python start.py
```

It will run the REST server and the verifier as background processes.

[Daemon]:https://pypi.python.org/pypi/python-daemon/
[Web.py]:http://webpy.org/
[mysql.connector]:https://dev.mysql.com/downloads/connector/python/2.0.html


