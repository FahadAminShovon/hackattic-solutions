import requests,json,base64
import sqlalchemy as db

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    engine = db.create_engine('postgresql://root:1234567890@localhost/backup')
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
        

def getDumpdata(token):
    link = "https://hackattic.com/challenges/backup_restore/problem?access_token="+token
    response = requests.get(link)
    response = json.loads(response.content)
    encodedDump = response["dump"]
    decodedDump = base64.b64decode(encodedDump,)
    f = open("backup.backup","wb")
    f.write(decodedDump)

def solve(token):
    getDumpdata(token)


if __name__ == "__main__":
    token = "84edafdf68f8408b"
    solve(token)
    Database()
