# Kickass Torrents Web Scraper to avoid coin miners

Kickass torrents along with many others have recently come under the radar for using coinhive javascript scripts to mine for coins using you CPU power when you browser their sites for torrents. This script will open the webpage for a very short period of time and download the list of torrents to your window for easy access and choosing. No more having to see your CPU usage spike everytime you download a torrent. 

This script can be run in any terminal window. It will ask you what you would like to torrent, and give you a list of torrent names, sizes, dates, seeders, leechers and the magnetic links. You can then simply type of the file number as it appears in the list and the torrent will open in whichever torrent client you use. 

You will need Python 2.7.12 or above to run this script. You will also need to have the libraries requests, bs4 and selenium installed. You will need the chromedriver executable, preferably in the same folder as this script for it to work, and you will finally need to change the chrome path in the script to direct to the chromedriver. If you can deal with these pains, the rest should be a breeze. 
