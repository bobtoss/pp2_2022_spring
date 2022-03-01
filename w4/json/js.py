import json
with open("sample_data.json") as str_json:
    z=json.load(str_json)
#import sample_data.json as str_json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
n=len(z["imdata"][0]["l1PhysIf"]["attributes"]["dn"])
space=len("                             ")
for i in range(len(z["imdata"])):
    if len(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"])<n:
        x=n-len(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"])
        print(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"]," "*(space+x),z["imdata"][i]["l1PhysIf"]["attributes"]["speed"],"",z["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
    elif len(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"])>n:
        x=len(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"])-n
        print(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"]," "*(space-x),z["imdata"][i]["l1PhysIf"]["attributes"]["speed"],"",z["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(z["imdata"][i]["l1PhysIf"]["attributes"]["dn"]," "*space,z["imdata"][i]["l1PhysIf"]["attributes"]["speed"],"",z["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])