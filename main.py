# 1
def create_file(filename):
  with open(filename, 'w') as file:
     file.write("Andy, Bobby, Charlie, Frida, Lukas, Marie, Nancy, Richard, Tommy, Ulrich")
     
create_file("names.txt")
with open("names.txt", "r") as file:
    print(file.read())
    
# 2
def transform_to_row(input_file, output_file):
  with open(input_file, 'r') as file_in:
    words = file_in.read().split(',')
  with open(output_file, 'w') as file_out:
  for word in words:
    file_out.write(word.strip() + '\n')
    
transform_to_row("names.txt", "names_row.txt")
with open("names_row.txt", "r") as file:
    print(file.read())

# 3
def add_greeting(input_file, output_file):
  with open(input_file, 'r') as file_in:
    words = file_in.read().split()
  greetings = ["Hello " + word for word in words]
  
  with open(output_file, 'w') as file_out:
    for greeting in greetings:
      file_out.write(greeting + '\n')
      
add_greeting("names_row.txt", "greetings.txt")
with open("greetings.txt", "r") as file:
    print(file.read())
    
# 4
def strip_greeting(input_file, output_file):
  with open(input_file, 'r') as file_in:
    lines = file_in.readlines()
  stripped_lines = [line.strip("Hello ") for line in lines]
  
  with open(output_file, 'w') as file_out:
    for line in stripped_lines:
      file_out.write(line + '\n')

strip_greeting("greetings.txt", "names_stripped.txt")
with open("names_stripped.txt", "r") as file:
    print(file.read())
    
# 5
def combine_files(file1, file2, output_file):
  with open(file1, 'r') as file1_in, open(file2, 'r') as file2_in:
    lines1 = file1_in.readlines()
    lines2 = file2_in.readlines()
    
   if len(lines1) != len(lines2):
    print("Error: the two input files must have the same number of lines.")
    return
    
  with open(output_file, 'w') as file_out:
    for line1, line2 in zip(lines1, lines2):
      combined_line = line1.strip() + " " + line2.strip()
      file_out.write(combined_line + '\n')
      
combine_files("file1.txt", "file2.txt", "output.txt")
with open("output.txt", "r") as file:
    print(file.read())
            








