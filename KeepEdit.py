import gkeepapi
import json
import os
import keyring

def createKeepObject():
    return gkeepapi.Keep()

def loginNow(self, username, password):
    return self.login(username, password)

def update(self):
    self.sync()

def addNote(self, title, info):
    self.createNote(title, info)

def main():

if __name__ == '__main__':
    main()