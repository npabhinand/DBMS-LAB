import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["exam"]
coll=db["student"]
a={"_id":1,
"name":"Anjali",
"place":"kollam",
"phone":8582639562,
"vaccination_status":"both vaccinated",
"rtpcr":"negative",
"lab_mark":{"internal":30,"external":45},
"department":"mca"};

coll.insert_one(a)

b=[{"_id":2,
"name":"anuradha",
"place":"varkala",
"phone":9992639562,
"vaccination_status":"both vaccinated",
"rtpcr":"negative",
"lab_mark":{"internal":40,"external":48},
"department":"civil"},
{"_id":3,
"name":"bismiya",
"place":"kollam",
"phone":9446639562,
"vaccination_status":"not vaccinated",
"rtpcr":"positive",
"lab_mark":{"internal":50,"external":39},
"department":"mca"},
{"_id":4,
   "name":"vimal",
"place":"ernakulam",
"phone":8582639568,
"vaccination_status":"first dose only",
"rtpcr":"positive",
"lab_mark":{"internal":40,"external":42},
"department":"civil"},
{"_id":5,
   "name":"vivek",
"place":"kollam",
"phone":8582639777,
"vaccination_status":"both vaccinated",
"rtpcr":"negative",
"lab_mark":{"internal":50,"external":50},
"department":"mca"}]

coll.insert_many(b)

for x in coll.find({"vaccination_status":"not vaccinated"}):
	print(x["name"]+" "+str(x["phone"]))

for x in coll.find({"department":"mca"}).sort("lab_mark.external",-1).limit(2):
	print(x["name"]+" "+str(x["phone"]))

for x in coll.find({"name":{"$regex":"^[aA]"}}):
	print(str(x["_id"])+"   "+x["name"]+"   "+x["department"])

coll.update_one({"_id":4},{"$set":{"vaccination_status":"both vaccinated"}})
for x in coll.find({"_id":4}):
	print(x)

for x in coll.find({}).sort("lab_mark.external",-1):
	print(x["name"])

