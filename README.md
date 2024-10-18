# lxde on Google cloud shell
a tool for making a free vnc session on google cloud shell (with lxde)

(some info: i was the author of the original repository, but i ended up losing the email address for the account where i created it. 
So, i promise to bring updates soon.)


#requeriments: 
a google account
and a ngrok account/authtoken (https://dashboard.ngrok.com/get-started/your-authtoken)


step 1:

go to https://console.cloud.google.com/home/ and click the terminal icon

step 2:

clone the repository by copying and pasting this command into the terminal:

git clone https://github.com/quantumnova87/lxde-vnc-gcs

after that; use the command:

cd lxde-vnc-gcs

edit the script (to put the authtoken), using: nano gui.sh

then copy your ngrok authtoken code in place of (token)

then, use: chmod +x gui.sh & bash gui.sh 

your vnc session will be ready in minutes, 

then just put the vnc address in a vnc viewer,

and your machine is ready for use.

[note: unfortunately the audio doesn't work in vnc :(]
