# Discord Rich Presence for Xbox

### This script allows you to show off what you're playing on your Xbox Series X (or other Xbox) on Discord. By default, you can connect to your Xbox account on Discord and have the Rich Presence on Discord to show what you're playing. However, this did not work on my Xbox Series X. Thus, I created this small and simple script which allows you to show off the game you're playing. I am not sure if this is just an Xbox Series X problem or other Xbox's encounter it too or if it is just a problem that only happens to me, but I have made this Rich Presence a little better to also show that you are at Home or doing something else instead of just showing if you're playing a game. Below are detailed steps to set the script up!


### The steps are as shown below: 
  1. Make a discord account if you do not already have one at https://discord.com/
  2. Once you are logged in, go to https://discord.com/developers/applications/
  3. Press New Application and give it a name (this is the small headline that shows up when people see your name on a server, like 'Listening to Spotify')
  4. On the left hand side, click Rich Presence
  5. Scroll down to Rich Presence Assets
  6. Add an image if you'd like and remember to give it a unique name. As you will see in the code, there is an area called 'large_image': 'xbox', you can simply replace 'xbox' with the name of the image you chose
  7. Using the left hand side, go to the OAuth2 dropdown menu and click the first dropdown which says "General"
  8. You will see Client ID which you can simply copy by pressing the button
  9. Place this in the config.ini file where it says "client_id" noted with NO quotes 
  10. To find your XUID, simply go to this website: https://www.cxkes.me/xbox/xuid
  11. Type in your Gamertag in the field and choose the 'Decimal' option and then click 'Resolve'
  12. Copy paste the XUID on the sceen in the config.ini file where it says "x_uid" with NO quotes
  13. To get a Open XBL Key, go to this website: https://xbl.io/
  14. Hit 'Login' on the top right and login with your **Microsoft account that is associated with your Xbox account** THIS IS IMPORTANT! If you login with an account not associated with your Xbox account, this will not work properly.
  15. Go to your profile: https://xbl.io/profile and scroll down to the "API KEYS" section
  16. Click the "CREATE +" button (just create one) and copy the key on your screen
  17. Paste the Open XBL Key you copied into the config.ini file where it says "open_xbl_key" with NO quotes
  18. You are done with setup

You can go ahead and run the script and start playing Xbox!
