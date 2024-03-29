# A452 Practical Investigation Coursework
## Research

To carry out this practical investigation, various pieces of research will need to be carried out.

### Android
**What is Android?**

> "Android is a mobile operating system (OS) currently developed by Google, based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets. Android's user interface is mainly based on direct manipulation, using touch gestures that loosely correspond to real-world actions, such as swiping, tapping and pinching, to manipulate on-screen objects, along with a virtual keyboard for text input. In addition to touchscreen devices, Google has further developed Android TV for televisions, Android Auto for cars, and Android Wear for wrist watches, each with a specialized user interface. Variants of Android are also used on notebooks, game consoles, digital cameras, and other electronics."

**Source(s):** https://en.wikipedia.org/wiki/Android_(operating_system)

![](http://cdn2.ubergizmo.com/wp-content/uploads/2015/05/android-logo.jpg)

**What Android systems will be used?**

Since a system running Android will be required, App Inventor's default emulator has been chosed as it's easy to use and set up.

![](http://courses.cs.vt.edu/~cs1004/AIemulator.PNG)

### App Inventor
**What is App Inventor?**

> "App Inventor for Android is an open-source web application originally provided by Google, and now maintained by the Massachusetts Institute of Technology (MIT).

> It allows newcomers to computer programming to create software applications for the Android operating system (OS). It uses a graphical interface, very similar to Scratch and the StarLogo TNG user interface, which allows users to drag-and-drop visual objects to create an application that can run on Android devices. In creating App Inventor, Google drew upon significant prior research in educational computing, as well as work done within Google on online development environments."

**Source(s):** https://en.wikipedia.org/wiki/App_Inventor_for_Android

**Is App Inventor suitable for the task(s)?**

When researching about App Inventor, it seems to be capable of many functions but has a few limitations:

>Advantages:

> - Access to most of the phone's functionality: phone calls, SMS texting, sensors for location, orientation, and acceleration, text-to-speech and speech recognition, sound, video.
- The ability to invoke other apps, with the ActivityStarter component
- Programming control just as with a textual language. There are blocks for conditionals (if, ifelse), foreach, and while, and a fairly comprehensive list of math and logic blocks.
- Database access, both on the device and on the web. So you can save data persistently, and with a web database share data amongst phones.
- Access to web information sources (APIs)-- you can bring in data from Facebook, Amazon, etc. See limitations below.

> Disadvantages:

> - Limited UIs. The user interface builder has improved but is still a bit buggy and limited, so you can't build any user interface. For instance, you can't create apps with multiple screens and handling orientation changes has some glitches. These problems are not fundamental to the design of App Inventor and will soon be fixed.
- Limited Access to the device. There are not yet components for all the data and functionality of the phone. For instance, you can't save and retrieve files from the file system and you have only limited access to the contact list (e.g., you cannot create groups).
- Limited Access to Web. You can only access APIs that follow a particular protocol (App-Inventor-compatible APIs). So if you want to get data from the web, you'll need to program or have a programmer create an App-Inventor-Compliant API that wraps an existing API. 
- No polymorphic components. Function blocks are tied to specific components, so there is no way to call functions on a generic component. For instance, if you create a procedure MoveXY, it has to be tied to a specific image sprite, not a general image sprite.
- Limited access to the Android Market. The apps (.apk files) generated by App Inventor lack the required configuration for direct inclusion in the market.

**Source(s):** https://sites.google.com/site/appinventor/capabilities-limitations

To come to a conclusion, it seems that App Inventor is fully capable to achieving the set tasks; it features the core basic functions required for the task as it features:
- images
- sprites
- buttons
- text

In terms of its block programming, it seems that it too is also fully capable to achieving the set tasks; it features the core basic functions required for the task as it features:
- basic variable types (booleans, strings, numbers and lists)
- procedures
- events

**Source(s):** http://appinventor.mit.edu/explore/library.html

Further research of these features can be found in the ```Planning``` stage of each task.

As an experienced programmer who has experience in may other languages (including MSI's own Scratch), App Inventor lessons wont be required. Instead, my past experience, logic and App Inventor documentation (http://appinventor.mit.edu/explore/library.html) will be used.

In terms of time, no more than an hour (of the 20 hours given) should be spent on each stage.

## Development
### Planning

### Task 1
The first part of the task required me to obtain a map of a university campus, after doing a quick search I managed to find and obtain this image:

![](http://i.imgur.com/GHGvwoF.png)

It was then required that I display the image, I decided to do this by placing a canvas on the screen and make its background image the campus. I used a canvas as it's very flexible allowing me to place buttons in it which is required for the next task:

![](http://i.imgur.com/aH1dly2.png)
### Task 2
This task required that each building was touchable and upon being touched the amount of computers available in that building is to be displayed. I thought of many ways to achieve this, but the most reasonable and logic method was to use ImageSprites as buttons.

The reasons for this is because the other option was to use balls, however, when making them invisible they're no longer touchable which was a large disappointment. However, I was able to achieve this by using ImageSrpties and making their image transparent.

I decided to place these buttons in the canvas that was created in the previous task. A label was then placed (outside of the canvas, in screen1) on top of the canvas which is to display the amount of buildings available.

![](http://i.imgur.com/6k3w9Wq.png)

In order to make these buttons worked, I created two global lists: one storing the amount of computers available in each building (each item being one building, index one would store the amount of buildings available in building one and so on) and the other one storing Booleans on whether the building has been reserved by them or not (in preparation for the other tasks).

A procedure was then made which takes the buttons/building number which then displays the amount of buildings available. The reason why a procedure was used was to save having to duplicate code multiple times making it longer, inefficient and hard to read.

And finally, multiple checks to see if each button had been pressed were made and if they were the procedure was called with the building number.

![](http://i.imgur.com/47Qwk2e.png)

### Task 3
For this task I was required to make two buttons, one button would cancel the reservation of the computer, and one button would reserve it. The aim was to make it so when a building is pressed, a cancel and reserve button is presented which then increases or decreases the amount of buildings avaliable (increase if they press cancel and decrease if they press reserve).

The task also required me to do some validation so the reserve button can't be pressed if they have already reserved and the cancel button can't be pressed if they haven't already cancelled it.

Note: since the task itself never stated how many computers each person can reserve I assumed that they could only reserve one per person.

The development:
To develop this I thought of a few various ways, the best way seemed to use App Inventor's own buttons: http://ai2.appinventor.mit.edu/reference/components/userinterface.html#Button

On the source it clearly states that "Button with the ability to detect clicks. Many aspects of its appearance can be changed, as well as whether it is clickable (Enabled), can be changed in the Designer or in the Blocks Editor.". This is very useful as we can ont only use it to increase/decrease the amount of computers avaliable in each building, but we can also change whether they are clickable or not (as spoken about in the validation).

I dragged both of these buttons onto the first screen, and used a horizonatal aligner; a horizantal aligner (as I found out through the use of expirimenting) allows you to put two elements on the same horizonatal alignment, this was very useful for the button placement as it meant users could press both of them easily.

The first one was then renamed to "Reserve" (as that will be the button which reserves the building) and the second one was renamed to "cancel" (as that was the one which would cancel the building when reserved).

Moving onto the next part, the Programming:
I then made use of the events feature in App Inventor; the events system is a system which checks if certain buttons have been clicked or not. When the "Reserve" or "Cancel" buttons were clicked an event was made to check if they were clicked or not, if they were clicked then each would have their own code block to allow something to happen.

I managed to learn this through the use of App Inventor's documentation: http://appinventor.mit.edu/explore/understanding-blocks.html teaches how blocks and events work which is what was researched.

For the reserve button a check was made to see if the user had already reserved the current building or not (which is stored on the global variable "bpc_reserved"). This was done through the use of checking if the "current_building" (the variable which stores the building number that has been clicked on) of the "bpc_avaliable" list was equal to true. If it was equal to true then it meant that it had already been reserved, this will be spoke of in more detail when we get to it.

Similar thing was also done to the cancel button, but rather than checking if the current building wasn't already reserved, it checked if it was reserved by using a "not" block which reverses the boolean condition.

Nextly I then needed to check whether the building that is trying to be reserved has enough avaliable computers to be reserved. To do this I again used "current_building" and "bpc_avaliable" and checked if the item in the list (also the building) is greater than 1.

This check was not done on the cancel button as it didn't matter whether the building had computers avaliable or not.

After that I then made it so if every check suceeded, then it would make it so the current buildings avaliablity has been reserved. This was done by using "replace" in the list section. This was also done on the cancel block but the difference is, instead of setting reserved to true, it was set to false.

The amount of computers avalibale then decreased i reserved or increase if cancelled using the math blocks; specifically the - and + symbol. And finally, the procedure to display text was called and displayed the amount of building.

And here is all of task 3 in one picture:
[insert full code block at end of it]

[insert image for every individual code block here, also add image of each element and their naming]

### Task 4
Task 4 required me to create a feature which display the location of each building that's avaliable if the one pressed has none left. To do this I decieded to display it with a label, the label would print the buildings which had computers in. For example, "There are no moe computers avaliable to book in this building, try these: B1, B2, B3, B4..." and so on. This meant that I won't need to add any complex features or confuse the user. This also means less time and code needed.

To start this, everytime a building with no computers left was pressed not only did it make the button unclickable, but it also did a for loop through each one of the buildings in the bpc_avaliable list, and those computers that are avaliable are added to the .text of the text label saying "B" + the building number to produce the result shown in the previous paragraph. This also cancelled both the reserve and cancel button from being clickable so no errors can come of it. 

[insert annotated picture here]

### Task 5
When looking at my Application, it seems like it has many purposes that would be useful for a university student: it allows students to book a computer without just a few clicks, this is a lot easier than having to make a phone call or any other form of booking. It also shows each building and its number on the map campus which makes it a lot easier to visualize with annotated buildings. It also allows you to see the amount of buildings avaliable and the amount that will be after you reserve or cancel

### Task 6
If I were to add another feature, it would be to make it so when a button is clicked, it glows so the user can remember which building number they're on. This will make things less confusing so you don't accidently click on the same building again.

### Task 7
To implement this I will need to
