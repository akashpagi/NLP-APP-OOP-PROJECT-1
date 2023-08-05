import json

class Database:
    
    def add_data(self, name, email, password):
        
        # Read details in json file
        with open('db.json', 'r') as rf:
            database = json.load(rf)
        
        # Cheking current email if exists or not 
        if email in database:
            return 0
        else:
            # add new user
            database[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return 1
                    
    # checking login page detail in db
    def search(self, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)
        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0