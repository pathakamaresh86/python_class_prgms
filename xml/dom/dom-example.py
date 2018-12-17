from xml.dom import minidom
 
doc = minidom.parse("employee.xml")
print type(doc)
print doc
# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")
print type(name)
print name[0]
print name[0].firstChild
print(name[0].firstChild.data)
print(name[1].firstChild.data)
employees = doc.getElementsByTagName("emp")
for emp in employees:
        sid = emp.getAttribute("id")
        nickname = emp.getElementsByTagName("nickname")[0]
        salary = emp.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))


'''
D:\F DATA\python_class\xml\dom>python dom-example.py
<type 'instance'>
<xml.dom.minidom.Document instance at 0x0000000002DFDC48>
<class 'xml.dom.minicompat.NodeList'>
<DOM Element: name at 0x2dfd348>
<DOM Text node "u'Trinaha So'...">
Trinaha Solutions
Sun Algo Systems
id:1, nickname:jb, salary:10000
id:2, nickname:mp, salary:20000
id:3, nickname:kp, salary:20000
id:4, nickname:vg, salary:20000
'''