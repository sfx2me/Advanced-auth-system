from keyauth import api
import os, hashlib, os.path, time
os.system("cls")
print("starting...")
def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
        path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest
# for help join my discord: https://discord.gg/QbWGVZvRWc
keyauthapp = api(
	name = "",
	ownerid = ",
	secret = "",
	version = "1.0",
	hash_to_check = getchecksum()
)
key = input("Enter your license key: ")
keyauthapp.license(key)
time.sleep(10)
exit()
