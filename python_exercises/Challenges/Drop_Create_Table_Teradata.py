#!/usr/bin/python2.7

import teradata
import sys

#udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",
#        logConsole=False)

#session = udaExec.connect(method="odbc", system="10.68.162.16",
#        username="mitra502", password="Kolkata@24");


file_ddl = sys.argv[1]

udaExec = teradata.UdaExec()

with udaExec.connect("${dataSourceName}") as session: 
   for row in session.execute(file=file_ddl):
      print(row)
