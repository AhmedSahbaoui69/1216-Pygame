# 1216 : A Chuck McGill Adventure
A Mini game I made in python using the Pygame module.
## Game screenshots 
<img src="/Screenshots/preview1.gif" width="400px" height="400px"></img>
<img src="/Screenshots/preview.gif" width="400px" height="400px"></img>
<details>
<summary><b>Context</b></summary>
The inspiration for this game was drawn from a popular scene in the hit TV series "Better Call Saul", specifically S03E05, where Chuck McGill goes into a meltdown and delivers the iconic "Chicanery speech".  

As a fan of the show, I decided to take on a new challenge and put my Python skills to the test by attempting to create a fun 2D-Game project.
</details>

## Overview
In order to create this game, I employed the principles of modular programming. This programming approach involves dividing the codebase into independent modules that handle specific functions or tasks. By using this approach, I was able to make the codebase smaller, more manageable, and more readable.
```
Main.py         //Contains the main game loop.
Assets.py       //Handles the game assets, including images, sprite classes, and other resources.
Audio.py        //Handles all game sound effects.
Interface.py    //Manages the game's graphical user interface components.
Particles.py    //Contains the dust effect particles classes.
```
This approach allowed me to focus on each component separately, making it simpler to debug and optimize.
## Requirements
You only need to have <a href="https://www.python.org/downloads/">Python</a> installed as well as the Pygame module.  
I already included a ```requirements.txt``` file so you can load it easily using this command:
```
$ pip install -r requirements.txt
```
## How to play?
>You will be playing as Chuck McGill placed  in a courtroom. Your mission is to prove that it was 1216 and not 1261. In order to do this, you must collect the numbers in the correct order. Each time you do that, you will earn a point. However, if you collect the numbers in the wrong order, you will lose a life.

>As you progress through the game, your score will increase. Once you hit a score that is a multiple of 5, Huell will enter the room and start throwing batteries at you. You must dodge the batteries to avoid losing any lives.

>Use the Left / Right arrow keys on your keyboard to move around the courtroom.
