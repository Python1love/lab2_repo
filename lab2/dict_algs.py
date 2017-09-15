ivan = {
"name" : "ivan" ,
"age" : 34,
"children" : [{
"name" : "vasja",
"age" : 12,
}, {
"name" : "petja",
"age" : 10,
}],
}
darja = {
"name" : "darja" ,
"age" : 41,
"children" : [{
"name" : "kirill",
"age" : 21,
}, {
"name" : "pavel" ,
"age" : 15,
}],
}

emps = [ivan, darja]

for n in emps:
    for n1 in n["children"]:
        if n1["age"]>18:
            print (n["name"])