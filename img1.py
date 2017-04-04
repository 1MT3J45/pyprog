import urllib
import ImageFileIO
fp = urllib.urlopen("http://www.python.org/logo.gif")
fp = ImageFileIO.ImageFileIO(fp)
im = Image.open(fp)
