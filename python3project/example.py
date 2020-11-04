farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("""
~~**[[Pick a farm!]]**~~
========================
0. NE Farm
1. W Farm
2. SE Farm
""")

choice= int(input())

FORBIDDEN= ["celery","carrots"]
YUMMY= ["pigs", "chickens", "llamas","sheep", "cows"]

for x in farms[choice]["agriculture"]:
  # if x in FORBIDDEN:
   if x in YUMMY:
       print(f"{x}... yum!")
       #print(f"Yuck! I don't want {x}!")
   else:
       #print(f"{x}... yum!")
       print(f"Yuck! I don't want {x}!")

