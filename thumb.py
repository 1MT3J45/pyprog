import os, sys
import Image
for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0] + ".thumbnail"
	if infile != outfile:
		try:
			im = Image.open(infile)
			im.thumbnail((128, 128))
			im.save(outfile, "JPEG")
		except:
			print "cannot create thumbnail for", infile
