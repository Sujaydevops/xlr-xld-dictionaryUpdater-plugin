import string
import logging
from xml.dom.minidom import parse, parseString

def newEntryNode(dom,key,value):
    node = dom.createElement("entry")
    node.attributes['key']=key
    text = dom.createTextNode("DUMMY")
    node.appendChild(text)
    node.firstChild.replaceWholeText(value)
    return node

xld_info = {'url':'http://' + xldHost + ':4516','username':xldUser,'password':xldPassword}
xld_request = HttpRequest(xld_info, xldUser, xldPassword)

readResponse = xld_request.get("/deployit/repository/ci/%s" % dictionaryId, contentType = 'application/xml')
dom = parseString(readResponse.response)

print "Actual State %s" % dom
entries=dom.getElementsByTagName("entries")[0]

values = parameters.split(",")
dict_items=len(values)
index=0
while index < len(values):
    value = values[index]
    value = values[index]
    dict=value.split("=")
    print "Adding dictionaris %s" % dict[0] +" and "+ dict[1]
    entries.appendChild(newEntryNode(dom,dict[0],dict[1]))
    index +=1

#entries.appendChild(newEntryNode(dom,"key1",value1))

updatedci=str(dom.toxml())
print "updated %s " % updatedci
updateResponse = xld_request.put("/deployit/repository/ci/%s" % dictionaryId, updatedci,contentType = 'application/xml')
