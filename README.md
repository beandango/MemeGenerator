# MemeGenerator

This is a very short and simple script I made that goes through a specified folder path and writes all the individial file
paths to a .txt file. I use this in combination with Mix It Up to create a "random meme generator" for my twitch streams.

Language: python
Uses: python-dotenv, os

super simple :)

### Overly Detailed Explanation of How to Make Random Meme Channel Point Redeems for Twitch

#### 1. Get [Mix it Up](https://mixitupapp.com/)
#### 2. Connect your Twitch account to Mix It Up (its pretty self-explanatory, just follow the prompts and stuff)
#### 3. Within Mix It Up, go to the menu on the left -> Services -> Overlay and follow those instructions
   ![MixItUp_VAkda4qo02](https://user-images.githubusercontent.com/106944445/222673049-3a1a5bb4-8b14-44f5-b7a6-f53be0cd1c7d.png)
#### 4. Go back to that menu on the top left -> Twitch Channel Points -> Click "Create New Channel Point Reward"
I'll name it Meme2 since I already have "Meme" set up. Ignore that.

And then click the command editor button (next to the trash can)

   ![uamZR5oxfH](https://user-images.githubusercontent.com/106944445/222673775-b9af9892-6705-4892-93c0-ffdd9ca54915.png)
#### 5. Using my script, replace "os.getenv('FOLDER_PATH')" with the path of whatever your meme folder is. 
Or, if youre using a .env file, you can just make a key in the .env with the contents being

`"FOLDER_PATH = "[your folder path]"`

Run it once. This should create a file called "file_paths.txt". Copy the path of this file. 
     
#### 7. Back to Mix It Up. Add two different actions. One being "File (Read & Write)" and another for "Overlay (Images & Video)"
The "File (Read & Write)" should come first. 

Should look something like:

![MixItUp_xOIrk7BdI8](https://user-images.githubusercontent.com/106944445/222675745-131d5f6c-e12b-4f13-818f-10a1e9d6ff9e.png)

#### 8. Look at this screenshot
Note that the action at the top is "Read Random Line From File". This is wjat makes it... uh... random. Yeah.
You can also change Images to Videos, Youtube, Text, whatever fits the format of whatever files you want to randomly show. 

![i7nlCTeFD2](https://user-images.githubusercontent.com/106944445/222677223-388dd5bd-f605-43b6-9973-9813c6d7867a.png)

#### 9. Set the duration for the image to whatever you want.

### And that's it! You can save it and then hit the play button to test it.

If you have any other questions or concerns, Google is free. 
LOL But you can also shoot me a message at beanDango#4916 on discord. I dont bite.



