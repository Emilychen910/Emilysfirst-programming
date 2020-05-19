#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 01:00:17 2020

@author: chenyinghui
"""
import sqlite3
conn = sqlite3.connect('0519exam.sqlite')
cursor = conn.cursor()

ID = input("請輸入使用者名稱")
Score = input("請輸入分數")

sqlstr = "insert into Studentexamscore(ID, Score) values('{}', '{}')".format(ID,Score)

cursor.execute(sqlstr)

conn.commit()
conn.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:07:05 2020

@author: chenyinghui
"""

import sqlite3
conn = sqlite3.connect('0519exam.sqlite')
cursor = conn.cursor()

ID = input("請輸入使用者名稱")
Score = input("請輸入分數")
sqlstr = "update Studentexamscore set Score = '{}' where ID='{}'".format(ID,Score)

cursor.execute(sqlstr)

conn.commit()
conn.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:20:11 2020

@author: chenyinghui
"""

import sqlite3
conn = sqlite3.connect('0519exam.sqlite')
cursor = conn.cursor()

ID = input("請輸入使用者名稱")
sqlstr = "delete from Studentexamscore where ID='{}'".format(ID)
cursor.execute(sqlstr)

conn.commit()
conn.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:54:02 2020

@author: chenyinghui
"""
import sqlite3
conn = sqlite3.connect('0519exam.sqlite')
cursor = conn.cursor()
select max(Score) from Studentexamscore
cursor.execute(sqlstr)

conn.commit()
conn.close()

