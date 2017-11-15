pip install autoenv
Collecting autoenv
  Downloading autoenv-1.0.0.tar.gz
Installing collected packages: autoenv
  Running setup.py install for autoenv ... done
Successfully installed autoenv-1.0.0


running python mailmanager should result in the following:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 203-770-172

[alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-crud-app (master)]$ python mailmanager.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 203-770-172
ImmutableMultiDict([('donor', 'test')])


alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-crud-app (master)]$ python mailmanager.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 203-770-172
ImmutableMultiDict([('donor', 'test')])
127.0.0.1 - - [13/Nov/2017 13:38:57] "POST / HTTP/1.1" 200 -
ImmutableMultiDict([('Donor First Name', 'Alinafe'), ('Donor Last Name', 'Matenda'), ('Donation Amount', '300')])
127.0.0.1 - - [13/Nov/2017 13:39:08] "POST / HTTP/1.1" 200 -
