import webapp2
import jinja2
import os
import random

class Meme(ndb.Model):

    meme_line1 = ndb.StringProperty(required=True)
    meme_line2 = ndb.StringProperty(required=True)
    pic_type = ndb.StringProperty(required=True)

    def get_meme_url(self):
        url_list=['https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg','https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg','https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg','https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg',]
        if self.pic_type == 'old-class':
            url = (url_list[0])
        elif self.pic_type == 'college-grad':
            url = (url_list[1])
        elif self.pic_type == 'thinking-ape':
            url = (url_list[2])
        elif self.pic_type == 'coding':
            url = (url_list[3])
        else:
            url = (url_list[random.randint(0,3)])
        return url
