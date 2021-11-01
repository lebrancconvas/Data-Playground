import yaml 
with open("data/data.yaml", "r") as stream: 
  try:  
    print(yaml.load(stream, Loader=yaml.FullLoader))    
  except yaml.YAMLError as exc: 
    print(exc) 