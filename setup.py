import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
     os.system("apt-get install docker")
     os.system("pip install torch")
     os.system("pip install wheel")
     os.system("pip install flake8 pytest")
     os.system("git pull")
elif c == "1":
     os.system("apt-get install docker")
     os.system("pip3 install torch")
     os.system("pip3 install wheel")
     os.system("pip3 install flake8 pytest")
     os.system("git pull")
     print("Done.")
