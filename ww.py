import base64
import urllib.parse
id="admin"
id=id.encode("utf-8")
pw="nimda"
pw=pw.encode("utf-8")

for i in range(20):
    id=base64.b64encode(id)
    pw=base64.b64encode(pw)
id=id.decode()
pw=pw.decode()

id=id.replace("1","!")
id=id.replace("2","@")
id=id.replace("3","$")
id=id.replace("4","^")
id=id.replace("5","&")
id=id.replace("6","*")
id=id.replace("7","(")
id=id.replace("8",")")

pw=pw.replace("1","!")
pw=pw.replace("2","@")
pw=pw.replace("3","$")
pw=pw.replace("4","^")
pw=pw.replace("5","&")
pw=pw.replace("6","*")
pw=pw.replace("7","(")
pw=pw.replace("8",")")
print(id)
print("\n\n")
print(pw)