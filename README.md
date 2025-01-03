# lxde on Google cloud shell
a tool for making a free vnc session on google cloud shell (with lxde)

#requeriments: 
a google account
and a ngrok account/authtoken (https://dashboard.ngrok.com/get-started/your-authtoken)

step 1:

go to https://console.cloud.google.com/home/ and click the terminal icon

step 2:

copy the script using the following command:

```
curl https://github.com/quantumnova87/lxde-vnc-gcs/raw/refs/heads/main/lxde.py && python3 lxde.py 
```

after that; use the command:

your vnc session will be ready in minutes, but you need to configure something like, vnc passwd, keyboard configuration..

then just put the vnc address in a vnc viewer,

and your machine is ready for use.

[note: unfortunately the audio doesn't work in vnc :(]


(another note: sorry if the script is messed up or something, its because i dont have any experience from python. (but i know some commands)
you can report bugs or/and problems in the issues tab, and i can *try* fixing it.
