def read_file(file_name):
  with open(file_name, 'r') as file:
    lines = file.read().splitlines()
  
  return [line.split(',') for line in lines]

def write_file(file_name, lines):
  output = '\n'.join([','.join(line) for line in lines]) 
  with open(file_name, 'w') as file:
    file.write(output)
