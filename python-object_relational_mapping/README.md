<div class="panel-body">
    <h2>Before you start…</h2>

<p><strong>Please make sure your MySQL server is in 5.7</strong> -&gt; <a href="/rltoken/Q6ygjeh74V8zBa_LEdi2XQ" title="How to install MySQL 5.7 in Ubuntu 14.04" target="_blank">How to install MySQL 5.7 in Ubuntu 14.04</a></p>

<h2>Background Context</h2>

<p>In this project, you will link two amazing worlds: Databases and Python!</p>

<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>

<p>In the second part, you will use the module <code>SQLAlchemy</code> (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). </p>

<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<p>Without ORM:</p>

<pre><code>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>

<p>With an ORM:</p>

<pre><code>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
</code></pre>

<p>Do you see the difference? Cool, right? </p>

<p>The biggest difficulty with ORM is: The syntax!</p>

<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/44QtseAaV_-ONgdH51Uwog" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
<li><a href="/rltoken/mYvCHnst1BM0W_EguB9GoQ" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don’t pay attention to <code>_mysql</code></em>)</li>
<li><a href="/rltoken/1LEw_5rGaYx77esMBUTIvA" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
<li><a href="/rltoken/ycDUJimPIbVgBkMqsRTTdw" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
<li><a href="/rltoken/vQ8oL7KmUtNs13kSwlgWyw" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
<li><a href="/rltoken/aNB2AQS4RHf_HYBGjEpmEQ" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
<li><a href="/rltoken/dyBs6au77YXeoxfSaXm0PA" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
<li><a href="/rltoken/OmnwW9fXhepm_VVfAerphg" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
<li><a href="/rltoken/DlVjzAv0RPKANUbCCJiJsQ" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
<li><a href="/rltoken/E3NsdW_3_kT3JDNoKflunQ" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
<li><a href="/rltoken/bNHxVbcn9w7FdGUBHAwr6A" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a href="/rltoken/bKtSCC_ng5bHpPczzZ6ADA" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/fHye-GrSZXxscD5J3FqYJg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Recommended editors: <code>Visual studio code</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>Your files will be executed with <code>MySQLdb</code> version <code>1.3.x</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.2.x</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (<code>version 1.7.*</code>)</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use <code>execute</code> with sqlalchemy</li>
</ul>

<h2>More Info</h2>

<h3>Install <code>MySQLdb</code> module version <code>1.3.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed: <a href="/rltoken/5eCu3yH0WBelhR_ouY54ww" title="How to install MySQL 5.7 in Ubuntu 14.04" target="_blank">How to install MySQL 5.7 in Ubuntu 14.04</a></p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.__version__ 
'1.3.10'
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.2.x</code></h3>

<pre><code>$ pip3 install SQLAlchemy==1.2.5
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
'1.2.5'
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

  </div>