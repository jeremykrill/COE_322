import json
from flask import Flask
import redis as rd

app = Flask(__name__)
rd = redis.StrictRedis(host='krilljs-redis', port=6379, db=0)

# returns all animals
@app.route('/animals', methods=['GET'])
def get_animals():
   return json.dumps(getdata())

# returns all animals of a specified "head" 
@app.route('/animals/<head>', methods=['GET'])
def get_animals_by_head(head):
    animals = getdata()
    output = [x for x in animals if x['head'] == head]
    return json.dumps(output)

# removes all animals of a specified "head"
@app.route('/animals/remove/<head>', methods=['GET'])
def remove_animal_by_head(head):
    animals = getdata()
    output = [animals.remove(x) for x in animals if x['head'] == head]
    return json.dumps(output)

# gets all animals within a date range
@app.route('/animals/dates', methods=['GET'])
def get_dates():
    # get start date
    start = request.args.get('start')
    start_date = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    # get end date
    end = request.args.get('end')
    end_date = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
    animals = getdata()
    # return animals within the date range
    return json.dumps([x for x in animals if (datetime.datetime.strptime( x['created_on'], "'%Y-%m-%d_%H:%M:%S.%f'") >= start_date and datetime.datetime.strptime( x['created_on'], "'%Y-%m-%d_%H:%M:%S.%f')"<= end_date ) ])

# gets animal that matches the inputted uid
@app.route('/animals/id/<uid>', methods=['GET'])
def get_uid():
    return json.dumps([x for x in animals if x['uid'] == uid])

# edits animal based on its uid
@app.route('animals/edit', methods=['GET'])
def edit_creature():
    # collect necessary data from user
    uid = str(request.args.get('uid'))
    head = str(request.args.get('head'))
    body = str(request.args.get('body'))
    arms = int(request.args.get('arms'))
    legs = int(request.args.get('legs'))
    tail = int(request.args.get('tails'))
    
    # create a list with a single animal entry that matches the uid	
    animals = getdata()
    animal = [x for x in animal if x['uid'] == uid]

    # check to make sure animal with given uid exists
    if not animal:
        return "uid not found!"
    else:
        # set all aspects of animal
        rd.hmset(animals.index(animal[0]), {'head': head, 'body': body, 'arms': arms, 'legs': legs, 'tail': tail, 'uid': str(uid), 'created_on': str(datetime.datetime.now())})
        animals = getdata()
        # return edited animal
        return json.dumps([x for x in animals if x['uid'] == uid])

# deletes animals within date range
@app.route('animals/delete', methods=['GET'])
def delete_animals():
    # get start date
    start = request.args.get('start')
    start_date = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    # get end date
    end = request.args.get('end')
    end_date = datetime.date.time.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
    animals = getdata()
    # remove animals from database if they fall within the date range
    output = [animals.remove(x) for x in animals if (datetime.datetime.strptime( x['created_on'], "'%Y-%m-%d_%H:%M:%S.%f'") >= d1_date and datetime.datetime.strptime( x['created_on'], "'%Y-%m-%d_%H:%M:%S.%f')"<=     d2_date ) ])]
    # return removed animals so user can see what was removed
    return json.dumps(output)

# calcualte the average number of legs
@app.route('animals/avglegs', methods=['GET']
def average_legs():
    animals = getdata()
    legs = 0
    count = 0
    # sum the total number of legs
    for x in animals:
        legs += int(x['legs'])
        count += 1
    # calculate average
    avg = legs/count
    return avg

# counts the number of animals
@app.route('animals/count', methods=['GET']
def count():
    count = 0
    for x in animals:
        count += 1
    return count

# generates animals, throws into Redis database
@app.route('/generate', methods=['GET'])
def generate():
    types = ["snake", "bull", "lion", "raven", "bunny"]
	 
    # data variable to hold animals
    data = {}
    data['animals'] = []
    for i in range(20):
        # randomly generate arm and leg variables
        arm = r.randint(2,10)
        while(arm % 2 != 0):
            arm = r.randint(2,10)
        leg = r.randint(3,12)
        while(leg % 3 != 0):
            leg = r.randint(3,12)
	
        # sum arms and legs to find tails
        tails = arm + leg

        # append new animal to data
        data['animals'].append({
        "head": types[r.randint(0,4)],
        # use name method from petname to create body
        "body": p.name() + '-'+ p.name(),
        "arms": arm,
        "legs": leg,
        "tail": tails,
        "uid": str(uuid.uuid4()),
        "created_on": str(datetime.datetime.now())
        })
    # fill Redis database
    rd.set('animals', json.dumps(data, indent=2))
    
    return "successfully generated animals!"

# function to get our data from the database
def getdata():
    return rd.hgetall('animals')

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5016))
