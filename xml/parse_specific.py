from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print '  %s :: %s' % (name, url)
    else:
        print name

'''
D:\F DATA\python_class\xml>python parse_specific.py
Science and Tech
  APM: Future Tense :: http://www.publicradio.org/columns/futuretense/podcast.xml
  Engines Of Our Ingenuity Podcast :: http://www.npr.org/rss/podcast.php?id=510030
  Science & the City :: http://www.nyas.org/Podcasts/Atom.axd
Books and Fiction
  Podiobooker :: http://feeds.feedburner.com/podiobooks
  The Drabblecast :: http://web.me.com/normsherman/Site/Podcast/rss.xml
  tor.com / category / tordotstories :: http://www.tor.com/rss/category/TorDotStories
Computers and Programming
  MacBreak Weekly :: http://leo.am/podcasts/mbw
  FLOSS Weekly :: http://leo.am/podcasts/floss
  Core Intuition :: http://www.coreint.org/podcast.xml
Python
  PyCon Podcast :: http://advocacy.python.org/podcasts/pycon.rss
  A Little Bit of Python :: http://advocacy.python.org/podcasts/littlebit.rss
  Django Dose Everything Feed :: http://djangodose.com/everything/feed/
Miscelaneous
  dhellmann's CastSampler Feed :: http://www.castsampler.com/cast/feed/rss/dhellmann/
 '''