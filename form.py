#!/usr/bin/python3
import cgi
print("Content-type:text/html\r\n\r\n")
print("")
print("<html><body>")
print("<h1>My Programe</h1>")
form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>Hello Dear"+name+"welcome on my website</h1></br>")

if form.getvalue("happy"):
    print("<p> You have Nice life</p>")

if form.getvalue("sad"):
    print("<p>Life is a chance for living life so please become happy</p>")

print("<form method='post' action='form.py'>")
print("<p>Name :<input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy'/>Happy")
print("<input type='checkbox' name='sad'/>Sad")
print("<input type='submit' value='submit' />")
print("</form>")
print("</body></html>")
