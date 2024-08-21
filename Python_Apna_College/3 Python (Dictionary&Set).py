#Practice for the Dictionary in pythn
myinfo={
    "name":"ahsan",
    "age":"21",
    "location":"islamabad",
    "purpose":"internship"
}
print(myinfo)
print(type(myinfo))

#WE CAN ALSO PUT THE LIST OR TUPLES IN THE DICTIONARY LETS PRACTICE
Myinfo={
    "name":"ahsan",
    "members":["ahmad","afnan","hafeez"],
    "locations":["melsi","isb","lodhran"],
    "membersage":[16,15,55]
}
print(Myinfo["name"])
print(Myinfo["members"])
print(Myinfo["locations"])

#CASE 2
Myinfo={
    "name":"ahsan",
    "members":["ahmad","afnan","hafeez"],
    "locations":("melsi","isb","lodhran"),
    "membersage":[16,15,55]
}
print(Myinfo)
Myinfo["members"][0] = "qari" # WE change value of key memeber ahmad value to qari (bcz its a list)
print(Myinfo["name"])         #if there will tuple inplace of list we cant change its value 
print(Myinfo["members"])
print(Myinfo["locations"])


