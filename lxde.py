import os
print("executing 'sudo apt-get update'...")
os.system('sudo apt-get update')
print("installing lxde..")
os.system('sudo apt install lxde -y')
print("installing tight vnc server...")
os.system('sudo apt install -y tightvncserver libdbus-glib-1-dev libgbm-dev')
res = input("what resolution could you like to use?")
os.system(f"vncserver -geometry {res} :1")
print("executing lxde on :1...")
os.system('DISPLAY=:1 startlxde > /tmp/lxde.log &')
print("downloading ngrok..")
os.system('wget -c https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -O - | tar -xz')
os.system("chmod +x ngrok")
auth = input("please, enter your ngrok authtoken. (it can be found on https://dashboard.ngrok.com/get-started/your-authtoken")
os.system(f"./ngrok config add-authtoken {auth}")    
print("using ngrok to redirect vnc session...")
os.system("./ngrok tcp 5901")