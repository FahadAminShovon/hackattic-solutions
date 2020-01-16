import requests,json,base64,gzip

def getDumpdata(token):
    link = "https://hackattic.com/challenges/backup_restore/problem?access_token="+token
    encodedDump = json.loads(requests.get(link).content).get("dump")
    compressedDump = base64.b64decode(encodedDump)
    dump = gzip.decompress(compressedDump).decode("utf-8")
    return dump

def submitAns(token,d):
    link = "https://hackattic.com/challenges/backup_restore/solve?access_token="+token
    response = requests.post(link,data=d)
    print(response.content)

def processDump(dump):
    # print(dump)
    userList = dump.splitlines()
    ansList = []
    for user in userList:
        if "alive" in user:
            tempuser = user.split('\t')
            ansList.append(tempuser[3])

    return ansList


def solve(token):
    dump = getDumpdata(token)
    ansList = processDump(dump)

    data = json.dumps({
        "alive_ssns" : ansList
    })

    submitAns(token,data)



if __name__ == "__main__":
    token = "84edafdf68f8408b"
    solve(token)
