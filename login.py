import cgi
import sqlite3


print("Content-type:text/html\r\n")

form = cgi.FieldStorage()

un= form.getvalue("un")
up = form.getvalue("pwd")

if un=="priya" and up=="053":
	print("<script>window.location.href='http://localhost:8000/test.html';</script>")
else:
	print("WRONG USERNAME")

