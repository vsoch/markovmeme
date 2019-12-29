"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

import random
from .namer import RobotNamer
from .utils import list_corpus, list_images, get_font
from PIL import Image, ImageDraw, ImageFont

import random
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))

class MemeImage:
    """A Meme Image includes markov (or randomly selected) text from a corpus, and
       a matching image. The image and corpus can be customized, otherwise
       the image is matched to the text. If the user selects a custom corpus,
       a custom image must also be provided. If an image doesn't exist for a 
       given corpus, the user is required to specify it.
    """
    def __init__(
        self,
        image=None,
        corpus=None,
        quiet=False,
    ):

        self.quiet = quiet
        self.corpus = corpus
        self.imagefile = self.get_image(image, corpus)
        self.image = Image.open(self.imagefile).convert("RGBA")
        self.draw = ImageDraw.Draw(self.image)

    def get_image(self, image, corpus):
        """If the image is provided, the full path must exist. Otherwise,
           we list images that come with the modula and randomly select one
           that matches the corpus.
        """
        # If a full path to an image is provided that exists, we're good
        if image is not None:
            if os.path.exists(image):
                return image

        # Otherwise, filter to subset in corpus
        options = [x for x in list_images() if corpus in x]
        if not options:
            sys.exit("No images exist for corpus %s. Please specify --image." % corpus)

        choice = random.choice(options)
        return os.path.join(here, 'data', 'images', "%s.png" % choice)


    def __str__(self):
        return "[mememl][%s]" % (self.corpus)

    def __repr__(self):
        return self.__str__()

    def print(self, message):
        """A wrapper to print to check if quiet is True, and skip if so.
        """
        if not self.quiet:
            print(message)

    def write_text(
        self,
        text,
        fontsize=32,
        rgb=(255, 255, 255),
        xcoord=10,
        ycoord=10,
        font="Anton-Regular.ttf",
    ):
        """Given a text string, font size, and output coordinates, write text
           onto the image. The default font provided with the package 
        """
        if text not in [None, ""]:
            import textwrap

            # Break image into width and height
            width, height = self.image.size
            fontfile = get_font(font)
            font = ImageFont.truetype(fontfile, fontsize)
            lines = textwrap.wrap(text, 40)

            # Keep track of y coordinate (height)
            total_height = ycoord
            for line in lines:

                # Calculate a specific width and height for the line
                w, h = font.getsize(line)

                # If we have space, honor the x coordinate, otherwise center
                xstart = (width - w) / 2
                if width - xcoord > w:
                    xstart = xcoord

                # Don't draw if we go over total height
                if total_height + 2 >= height:
                    break

                # Black outline
                self.draw.text((xstart-2, total_height-2), text,(0,0,0), font=font)
                self.draw.text((xstart+2, total_height-2), text,(0,0,0), font=font)
                self.draw.text((xstart+2, total_height+2), text,(0,0,0), font=font)
                self.draw.text((xstart-2, total_height+2), text,(0,0,0), font=font)

                # Main text
                self.draw.text((xstart, total_height), line, font=font, fill=rgb)
                total_height += h


    def save_image(self, outfile=None):
        """Save the image to an output file, if provided. Optionally add some
           text to it.
        """
        if not outfile:
            outfile = "%s.png" % self.generate_name()
        print("Saving image to %s" % outfile)
        self.image.save(outfile, "PNG")

    def generate_name(self):
        """Generate a random filename from the Robot Namer
        """
        return RobotNamer().generate()
