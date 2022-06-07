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
keyauthapp = api(
	name = "login",
	ownerid = "nYzKOL1jYh",
	secret = "f9632df6f4d36f04ed87b13b2b73cc6726b0fd224c0f4095d4869a06fd23a8c7",
	version = "1.0",
	hash_to_check = getchecksum()
)
key = input("Enter your license key: ")
keyauthapp.license(key)
time.sleep(10)
exit()