
![alt text](https://media.wizards.com/2017/images/daily/41mztsnrdm.jpg)

# Overview

This project is an artifical intelligence designed to take a series of images from the trading card game Magic: The Gathering and attempt to determine their mana costs.

This will require a database of cards to use

I used the popular public project MTGJSON and downloaded a copy of their SQL Database Here:

https://mtgjson.com/downloads/all-files/

This should come with all the printings, however there are no images.

the "grab_card_art.py" seeks out the endpoint for all images from the gatherer.wizards.com page

Ex:
https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=88960&type=card
![alt text](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=88960&type=card)


The multiverseid is the unique identifier for each card on the gatherer.wizards.com database. It is also a present field within the SQL database found at MTGJSON. So, this field can be used to request images from the gatherer.wizards.com endpoint reliably.

I first query the first 1150 cards from my local db, then send Python requests to the dynamically generated endpoints.

Once an image is recieved, it is turned into Byte format and stored as a series of vectors that represent its pixels.

This is done over and over until an array of vector arrays has been established.

The vector arrays are then used in a learning algorithm where x = vector_array[i] and y = the cards color (determined while grabbing the images)


# Files

## color_indentifier_ai.py

This is the main driver of the project. It does most of the iteration and computation, as well as any learning and database queries that need ran

## db_connect.py

This is a database connection script that should be called to establish a connection to your local database. 

## config_example.py

THIS FILE SHOULD BE EITHER RENAMED OR DUPLICATED to the name of "config.py." you will want to create your config in a seperate file using this file as a templated reference.

It is important to note that config.py is ignored by git via the .gitignore file. If you use config_example.py as your main creds folder, you are liable to push up sensitive information

## grab_card_art.py

This file is in charge of retrieving the card art from the internet. There are no legitimate images without it.


# Requirements

Make sure to install python and, while in this projects root directory, run:

```
pip install -r requirements.txt
```

This will install each package within the requirements folder.


You will also need an SQL database here:

https://mtgjson.com/downloads/all-files/

I used the "AllPrintings" Index