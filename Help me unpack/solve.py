import requests,json,base64,struct


def get_bytes(token):
    try:
        PROBLEM_URL =  "https://hackattic.com/challenges/help_me_unpack/problem?access_token="+token
        getProblem = requests.get(PROBLEM_URL)
        getProblem = getProblem.json()
        return getProblem['bytes']
    except :
        return None


def find_solve(token):
    encoded_bytes = get_bytes(token)
    decoded_bytes = base64.b64decode(encoded_bytes)
    a = struct.unpack('iIhfd',decoded_bytes[:-8])
    b = struct.unpack('!d',decoded_bytes[-8:])
    data = json.dumps(
        {
            "int": a[0],
            "uint": a[1],
            "short": a[2],
            "float": a[3],
            "double": a[4],
            "big_endian_double": b[0]
        }
    )
    post_url = "https://hackattic.com/challenges/help_me_unpack/solve?access_token="+token
    response = requests.post(url=post_url,data=data)
    return(response)




if __name__ == "__main__":
    token = "84edafdf68f8408b"
    print(find_solve(token).content)