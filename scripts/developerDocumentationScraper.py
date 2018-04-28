#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urlparse import urljoin
import shutil
import urllib
import urlparse
import bs4
import os
import sys
import requests
import datetime
import re

# URL to the introduction 
pageURL = 'https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/1-Introduction/Introduction.html'
projectURL = 'https://github.com/erikberglund/Mobile-Device-Management-Protocol-Reference/'

titlesIgnored = []

# Updates if the newline has to be </br> in tables for example
newlineChar = '\n'

# Flag if we're currently exporting a table
isTable = False

# Get the path to the project root
projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Set and verify the 'html' directory exists in the project
htmlPath = os.path.join(projectPath, 'html')
if not os.path.exists(htmlPath):
	os.makedirs(htmlPath)

# Set and verify the 'assets' directory exists in the 'date' directory
assetsPath = os.path.join(projectPath, 'assets')
if not os.path.exists(assetsPath):
	os.makedirs(assetsPath)

# Set and verify the 'markdown' directory exists in the 'date' directory
markdownPath = os.path.join(projectPath, 'markdown')
if not os.path.exists(markdownPath):
	os.makedirs(markdownPath)

# Create a global variable for the current path
datePath = ''

# Set and verfiy the 'date' directory exists in the 'site' directory
currentDateString = datetime.date.today().strftime('%Y-%m-%d')

def deleteItemsInFolder(folderPath):
	for file in os.listdir(folderPath):
		path = os.path.join(folderPath, file)
		try:
			if os.path.isfile(path):
				os.unlink(path)
			elif os.path.isdir(path):
				shutil.rmtree(path)
		except Exception as e:
			print(e)

def downloadPage(url):

	global datePath

	# Get the page content
	page = requests.get(url)
	pageSoup = BeautifulSoup(page.content, 'html.parser')

	# Get the page version
	documentVersionTag = pageSoup.find('meta', {"id": "document-version"})
	documentVersion = unicode(documentVersionTag['content'])

	# Get the page date
	documentDateTag = pageSoup.find('meta', {"id": "date"})
	documentDate = unicode(documentDateTag['content'])

	# Extract the page folder path
	pageFolderPathName = os.path.basename(os.path.dirname(url))

	# Create the current date download path if it doesn't exist
	datePath = os.path.join(htmlPath, documentVersion + '_' + documentDate + '_' + currentDateString)
	if not os.path.exists(datePath):
		os.makedirs(datePath)

	# Create page folder path if it doesn't exist
	pageFolderPath = os.path.join(datePath, pageFolderPathName)
	if not os.path.exists(pageFolderPath):
		os.makedirs(pageFolderPath)

	# Extract the page name and extension
	pageName, pageExtension = os.path.splitext(os.path.basename(url))

	# Cobine the page filename
	pageFilename = pageName + '_' + documentVersion + '_' + documentDate + pageExtension

	# Combine the page path
	pagePath = os.path.join(pageFolderPath, pageFilename)

	# Write the contents to disk
	with open(pagePath, 'w+') as pageFile:
		pageFile.write(page.content)


	# Get the 'Next' button if it exists
	nextTag = pageSoup.find('link', {"id": "next-page"})
	nextString = unicode(nextTag['href'])

	# If we got a non empty href strng, continue
	if nextString:
		nextURL = urljoin(url, nextString)

		# Download the next page
		downloadPage(nextURL)

def stringForTable(tag):
	
	global newlineChar
	global isTable
	
	isTable = True

	# Create an empty string to add a table's content to
	tableString = ""

	if not tag.find_all('th'):
		tr = tag.find('tr')
		if tr:
			headerSeparator = ""
			for _ in range(len(tr.find_all('td'))):
				headerSeparator += '-|'
			tableString += newlineChar + '|' + re.sub('-', '', headerSeparator)
			tableString += newlineChar + '|' + headerSeparator + newlineChar

	# Get all table row tags
	for row in tag.find_all('tr'):
		tableString += '|'

		# Create an empty string to add the header separator row in
		headerSeparator = ""

		# Headers
		for headerColumn in row.find_all('th'):
			for headerColumnContent in headerColumn.contents:
				headerString = stringForElement(headerColumnContent)
				if headerString:
					tableString += headerString + '|'
				else:
					print("ERROR: No header string returned for header column: " + str(headerColumnContent))
			headerSeparator += '-|'

		# Add separator
		if headerSeparator:
			tableString += newlineChar + '|' + headerSeparator

		# Set newlinechar
		newlineChar = '</br>'

		# Content
		for column in row.find_all('td'):

			# Create an empty string to add the column contents in
			columnString = ""

			idx = 0

			# Loop through all child elements in the column
			for child in column.children:

				#print("child in table: " + child.name)
				#print(child)

				# Check if this is an unordered list
				if child.name == 'ul' or child.name == 'ol':
					columnString += stringForList(child)
					idx += 1

				# Check if this is a regular string
				elif child.name == 'p':
					pString = stringForElement(child)
					if pString:
						if pString.isspace():
							continue
						if pString and 0 < idx:
							columnString += '</br>' + pString
						elif pString:
							columnString += pString
						idx += 1

				# If not p or ul, pass it to stringForElement
				else:
					string = stringForElement(child)
					if string:
						if string.isspace():
							continue
						elif string and 0 < idx:
							columnString += '</br>' + string
						elif string:
							columnString += string
						idx += 1

				print("columnstring is: " + columnString)

			if columnString:
				tableString += columnString + '|'

		newlineChar = '\n'

		tableString += newlineChar

	#print("Returning table string: " + tableString)
	if tableString:
		tableString = newlineChar + tableString

	isTable = False

	return tableString


def stringForNavigableString(navString):
	#print("NavigableString: " + unicode(navString))
	return unicode(navString)

def stringForCodesample(tag):

	# Create an empty string to add the codesample contents
	codesampleString = ""

	# Find the table and loop through each row
	codesampleTable = tag.find('table')
	for row in tag.find_all('tr'):

		# Loop through each column in the row
		for column in row.find_all('td'):

			# Create an empty string to add the column contents
			columnString = ""

			# Loop through each tag in the column (should only be <pre> tags)
			for tag in column.children:

				if tag.name == 'pre':
					columnString += newlineChar + unicode(tag.text)

				else:
					try:
						print("FIXME - Unhandled codesample tag: " + aTag.name + " is type: " + str(type(aTag)))
						print(aTag)
					except:
						print("FIXME - Unhandled codesample tag: " + aTag.name)
						print(aTag)

			codesampleString += columnString

	if codesampleString:
		return '```' + codesampleString + newlineChar + '```'
	else:
		print("ERROR: Got no codesample string from it's elements")
		return None

def stringForFigure(tag):

	# Create an empty string to add the figure contents
	figureLinkString = ""

	for iTag in tag.find_all("img"):

		if not iTag.has_attr('src'):
			print("ERROR: img tag doesn't have a src attribute")

		# Get the img src link
		src = iTag['src']

		# Initialize srcDir variable
		srcDir = '/'

		# If it's a relative link, resolve that here
		if src.startswith(".."):
			srcURL = urljoin(fileURL, src)
			srcDir = re.sub('^[../]+', '', src).replace(os.path.basename(src), '')
		else:
			srcURL = src

		# Check if img has a height attribute
		if iTag.has_attr('height'):
			height = iTag['height']

		# Check if img has a width attribute
		if iTag.has_attr('width'):
			width = iTag['width']

		# Parse the srcURL to get the path
		srcURLParsed = urlparse.urlparse(srcURL)
		if not srcURLParsed:
			print("ERROR: Failed to parse source url: " + srcURL)
			return None

		# Get the image name
		srcName = os.path.basename(srcURLParsed.path)
		if not srcName:
			print("ERROR: Failed to get src path from url: " + srcURL)
			return None

		# Create the image download path
		if srcDir == '/':
			srcDownloadPath = os.path.join(assetsPath, srcName)
		else:
			srcDownloadPathFolder = os.path.join(assetsPath, srcDir)
			if not os.path.exists(srcDownloadPathFolder):
				os.makedirs(srcDownloadPathFolder)

			srcDownloadPath = os.path.join(srcDownloadPathFolder, srcName)

		print("Downloading img at: " + srcURL + " to path: " + srcDownloadPath)
		# Download the image to the srcDownloadPath
		try:
			srcFile = urllib.URLopener()
			srcFile.retrieve(srcURL, srcDownloadPath)
		except Exception as e:
			print("ERROR: Failed to download the src at url" + srcURL)
			return None

		# Create the path to the asset on github
		srcProjectURL = projectURL + 'blob/master/assets/' + srcDir + srcName

		# Create the markdown string
		figureLinkString += '<img src="' + srcProjectURL + '"'
		
		# If the src tag had a height attribute, add that
		if height:
			figureLinkString += ' height="' + height + '"'

		# If the src tag had a width attribute, add that
		if width:
			figureLinkString += ' width="' + width + '"'

		figureLinkString += '>'
	return figureLinkString

def stringForBox(tag):

	# Create an empty string to add the box contents
	boxString = ""

	# Loop through all p tags
	for pTag in tag.find_all("p"):
		pTagString = stringForElement(pTag)
		if pTagString and not isEmpty(pTagString):
			boxString += '> ' + pTagString + '  ' + newlineChar
		else:
			print("ERROR: Got empty string for box")

	return boxString

def stringForList(tag, htmlNewlines=False, ordered=False, level=1):

	# Create an empty string to add the list contents
	listString = ""
	if isTable:
		if not ordered:
			listString += '<ul>'

	# Loop through each li tag. We have to use a manual index here because the list 
	idx = 0
	for li in tag.children:

		if not isinstance(li, bs4.element.Tag):
			continue

		idx += 1

		# Loop through each tag child and get it's content
		for lElement in li.children:

			# Reset indent level if a box changed it in the loop
			indentLevel = ''
			if level == 2:
				indentLevel = '   '
			if level == 3:
				indentLevel = '      '
			if level == 4:
				indentLevel = '         '

			# If this element is another list, create that here
			if lElement.name == 'ol' or lElement.name == 'ul':
				lString = newlineChar + stringForList(lElement, htmlNewlines, lElement.name == 'ol', level + 1)
			else:
				# Get the elements contents
				lString = stringForElement(lElement)

			# Ignore empty lines
			if not lString or isEmpty(lString):
				continue

			indexCharacter = '*'
			if ordered:
				indexCharacter = str(idx) + '.'

			# Ignore index character if this element is a nested list 
			if lElement.name == 'ol' or lElement.name == 'ul':
				indexCharacter = ''

			# Ignore index character if this element is a box, also verify we have an indent level
			elif lElement.name == 'div' and lElement.has_attr('class') and (lElement[u'class'] == [u'notebox'] or lElement[u'class'] == [u'warningbox', u'clear']):
				indexCharacter = ''
				if level < 2:
					indentLevel = '  '

			# Check if we are insida a table, and it's not ordered
			if isTable and not ordered:
				listString += indentLevel + '<li>' + lString + '</li>'

			else:
				listString += newlineChar + indentLevel + indexCharacter + ' ' + lString + ' ' + newlineChar

	if listString and isTable and not ordered:
		listString += '</ul>'

	return listString

def hexString(string):
	return ":".join("{:02x}".format(ord(c)) for c in string)

def isEmpty(string):
	return unicode(string) == u"\n" or unicode(string) == u"" or unicode(string) == u" "

def stringForTag(tag):

	# Check if we actually got a NavigableString instead
	#if isinstance(tag, bs4.element.NavigableString):
		#return stringForNavigableString(tag)

	# Get tag name
	try:
		tagName = tag.name
		if not tagName:	
			return None
	except:
		return None

	print("TAG")
	print(tagName)
	print(tag)

	if tagName == 'br':
		return unicode(newlineChar)
	elif tagName == 'hr':
		return unicode(newlineChar + '---' + newlineChar)
	elif tagName == 'div':
		if tag.has_attr('class') and (tag[u'class'] == [u'notebox'] or tag[u'class'] == [u'warningbox', u'clear']):
			return stringForBox(tag)

		if tag.has_attr('class') and tag[u'class'] == [u'codesample', u'clear']:
			return stringForCodesample(tag)
	elif tagName == 'ol':
		return stringForList(tag, False, True)

	elif tagName == 'ul':
		return stringForList(tag, False, False)

	elif tagName == "figure":
		return stringForFigure(tag)

	# Get tag contents
	try:
		tagContents = tag.contents
		if not tagContents:
			return None
	except:
		return None

	print("TAG CONTENTS")
	print(tagContents)

	# Create an empty string to add a tag's content to
	tagString = ""

	# Check if tag contents is greater than 1
	if 1 < len(tagContents):

		# If tag is a table, return the table from stringForTable
		if tagName == 'table':
			return stringForTable(tag)

		elif tagName == 'section':
			return exportSection(tag, False)

		for tagContent in tagContents:
			contentString = stringForElement(tagContent)
			if contentString:
				tagString += contentString
		if tagString:
			return tagString
		else:
			return None

	tagContent = next(iter(tagContents or []), None)
	if not tagContent:
		return None

	# Check that tag contents is not another tag
	if isinstance(tagContent, bs4.element.Tag):
		return stringForTag(tagContent)

	# When getting here, it should be a single tag without sub tags
	if tagName == 'a':
		if tag.has_attr('href'):
			return stringForLink(tag)

	elif tagName == 'p':
		return unicode(tagContent)

	elif tagName == 'code':
		return '`' + unicode(tagContent) + '`'

	elif tagName == 'em':
		return '*' + unicode(tagContent) + '*'

	elif tagName == 'strong':
		return '**' + unicode(tagContent) + '**'

	elif tagName == 'h2':
		return '## ' + unicode(tagContent) + newlineChar

	elif tagName == 'h3':
		return '### ' + unicode(tagContent) + newlineChar

	elif tagName == 'h4':
		return '#### ' + unicode(tagContent) + newlineChar

	elif tagName == 'h5':
		return '##### ' + unicode(tagContent) + newlineChar

	elif tagName == 'h6':
		return '###### ' + unicode(tagContent) + newlineChar

	else:
		print("Unhandled tag: " + tagName)


def stringForLink(tag):
	linkURL = tag['href']
	linkTitle = unicode(tag.text)

	if linkURL.startswith("#"):
		return '[' + linkTitle + '](' + fileURL + linkURL + ')'
	elif linkURL.startswith("http"):
		return '[' + linkTitle + '](' + linkURL + ')'
	elif linkURL.startswith(".."):
		return '[' + linkTitle + '](' + urljoin(fileURL, linkURL) + ')'
	else:
		print("FIXME - Unhandled href link: " + tag)
		return None

def stringForElement(element):

	# Check if element is NavigableString
	if isinstance(element, bs4.element.NavigableString):
		return stringForNavigableString(element)

	# Check if element is Tag
	elif isinstance(element, bs4.element.Tag):
		return stringForTag(element)

def stringForSectionTitle(section):

	sectionTitleTag = section.find(re.compile("h[0-9]"))
	if sectionTitleTag:
		return stringForTag(sectionTitleTag)
	
	#if not sectionTitleTag.has_attr('title'):
	#	print("ERROR: Section title tag has no title attribute")
	#	return None
	
	#return unicode(sectionTitleTag['title'])

def stringForSectionLink(section):

	sectionTitleTag = section.find('a')
	if not sectionTitleTag.has_attr('name'):
		print("ERROR: Section title tag has no name attribute")
		return None

	return unicode(sectionTitleTag['name'])

def exportSection(section, writeToFile=True):

	sectionString = ""

	# Get the title for the section
	sectionTitleMarkdown = stringForSectionTitle(section)
	if not sectionTitleMarkdown:
		print("ERROR: Failed to get section title markdown")
		return None

	print("Exporting Section: " + sectionTitleMarkdown)

	sectionTitle = re.sub('^#+', '', sectionTitleMarkdown).strip()

	print("Exporting Section: " + sectionTitle)

	# Get the link for the section
	if writeToFile:

		# Add the title to the section
		sectionString += '# ' + sectionTitle + newlineChar

		sectionLink = stringForSectionLink(section)
		if not sectionLink:
			print("ERROR: Failed to get section link")
			return None

		# Add the link to the section
		sectionString += newlineChar + ' [' + 'Configuration Profile Reference - ' + sectionTitle + '](' + fileURL + '#' + sectionLink + ')  ' + newlineChar

	for tag in section.children:
		tagString = stringForTag(tag)

		# If we didn't get a string back, continue with next tag
		if not tagString:
			continue

		# Verify we still got contents in the tagString
		if tagString == '\n':
			sectionString += tagString
		else:
			sectionString += '  ' + newlineChar + newlineChar + tagString

	# Verify we got a non empty string
	if sectionString and writeToFile:

		# Set the section markdown path
		sectionMarkdownPath = os.path.join(articlePath, sectionTitle + '.md')

		# Write the section contents to articlePath
		with open(sectionMarkdownPath, 'w+') as sectionFile:
			sectionFile.write(sectionString.encode('utf-8'))

	return sectionString

def exportArticle(article):

	articleString = ""

	# Get the title for the article
	try:
		articleTitle = unicode(article.find('h1', {"id": "pageTitle"}).text)
	except Exception as e:
		print("Failed to get the article title")
		return None

	articleString += '# ' + articleTitle + newlineChar

	# Add the link to the section
	articleString += newlineChar + ' [' + 'Configuration Profile Reference - ' + articleTitle + '](' + fileURL + ')  ' + newlineChar

	# Export all tags in the article tag
	for tag in article.children:
		tagString = stringForTag(tag)

		# If we didn't get a string back, continue with next tag
		if not tagString:
			continue

		# Verify we still got contents in the tagString
		if tagString == '\n':
			articleString += tagString
		else:
			articleString += '  ' + newlineChar + tagString

	# Verify we got a non empty string
	if articleString:

		# Set the article's markdown path
		articleMarkdownPath = os.path.join(articlePath, os.path.basename(fileURLPath) + '.md')

		# Write the article contents to articlePath
		with open(articleMarkdownPath, 'w+') as articleFile:
			articleFile.write(articleString.encode('utf-8'))

# Download the introduction page and all subsequent pages on this site
downloadPage(pageURL)

if not datePath:
	print("ERROR: variable datePath was not set. Etiher set it manually or uncomment the download function call")

# Delete the current generated files
deleteItemsInFolder(assetsPath)
deleteItemsInFolder(markdownPath)

# Export each html file found in the html folder
for dirpath, dirnames, filenames in os.walk(datePath):
	for fileName in [f for f in filenames if f.endswith('.html')]:

		# Get the path to the current file
		filePath = os.path.join(dirpath, fileName)

		# Get the url to the html parent folder
		fileURLPath = urljoin(os.path.dirname(pageURL), os.path.basename(dirpath))

		# Get the url to the current html page
		fileURL = fileURLPath + '/' + re.sub('(^[0-9.]+-|_[0-9.]+_[0-9]{4}-[0-9]{2}-[0-9]{2})', '', fileName)

		# Set the article local path
		articlePath = os.path.join(markdownPath, os.path.basename(dirpath))

		# Creat the path if it doesn't exist
		if not os.path.exists(articlePath):
			os.makedirs(articlePath)

		# Open the file and read it's contents
		with open(filePath, 'r') as file:
			fileContent = file.read().decode('utf-8')

			# Get the page content
			fileSoup = BeautifulSoup(fileContent, 'html.parser')

			# Get the <article> element
			fileArticle = fileSoup.find('article')

			# Export the main article
			exportArticle(fileArticle)

			# Loop thorugh all sections in the article and export those aswell
			for section in fileArticle.find_all('section', recursive=False):

				# Export the section
				exportSection(section)
