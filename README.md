# TrumpTube

A proof-of-concept experiment to pull out comments on YouTube video surrounding the 2016 Presidential election in the United States.

# Setup
The rapid prototype here runs on Flask. Put your YouTube credentials (simple API key) in a file called credentials.txt in the importers/youtube/ folder. Put the video IDs of the videos you want to harvest in sources.txt, one per line. Visualization is done by copying a CSV file into the staic folder.

# Basic usage
To harvest comments, run harvest.py. To view the visualisation, run trumptube.py. To change the content of the webpage, or create your own site, make sure to consult the documentation on Flask.

# Credits

Written by Martin Paul Eve and Alex Gil as part of a rapid prototyping workshop for the experimental methods group at Columbia and the Centre for Technology and Publishing at Birkbeck, University of London.