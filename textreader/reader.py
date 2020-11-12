from subprocess import Popen

file_name = input("File name?\n")

with open(file_name, "r") as f:
    text = f.read()

Popen(["say", text])