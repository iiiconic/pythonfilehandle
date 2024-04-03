try:
  # File Creation
  with open('my_file..txt', "w") as file:
    file.write("My name is Ibrahim\n");
    file.write("I am a coder\n");
    file.write("I love python");

  # File Reading and Display
  with open("my_file.txt", "r") as file:
      print("Contents of my_file.txt:");
      print(file.read());

  # File Appending
  with open("my_file.txt", "a") as file:
      file.write("Appending line 1\n");
      file.write("Appending line 2\n");
      file.write("Appending line 3\n");

except FileNotFoundError:
  print("File not found error occurred.");
except PermissionError:
  print("Permission denied error occurred.");
except Exception as e:
  print("An error occurred:", e);
finally:
  print("Execution completed.");