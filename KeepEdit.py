import gkeepapi
import os
import keyring

#username: brunerm99
#password: fczqbrnkjmzvptut

def createKeepObject():
    return gkeepapi.Keep()

def loginNow(self, username, password):
    return self.login(username, password)

def update(self):
    self.sync()

def addNote(self, title, info):
    self.createNote(title, info)

def main():
    keepObj = createKeepObject()
    print(loginNow(keepObj, 'brunerm99', 'fczqbrnkjmzvptut'))
    addNote(keepObj, 'title', 'info')
    update(keepObj)

if __name__ == '__main__':
    main()