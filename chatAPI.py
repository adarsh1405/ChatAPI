import pymongo
import random
import flask


connection=pymongo.MongoClient('localhost',27017)
database=connection['test']
collection=database['user']

app = Flask(__name__)

msg=[]


@app.route('/create',methods=['POST'])
def create(name,msg):
	pin = ''.join(random.choice('0123456789') for _ in range(6))
	collection.insert_one({"_id":pin,"name":name,"msg":[msg]})
	return pin



def update(pin,name,msg):
	collection.update_one({"_id":pin},{"$push":{"msg" :msg}})
	return "your msg is updated"



# print(create("Adarsh","I have a query"))
# print(update("798657","adarsh", " harami"))


if __name__ == "__main__":
    app.run(debug=True)