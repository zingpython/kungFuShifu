from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#Begin request
req = Request("http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_quotes_settlements_futures.html",
	headers={"User-Agent":"Mozilla/5.0"})

#Get requested webpage in a raw format
webpage = urlopen(req).read()

#Process raw webpage with beautifulsoup 
beautifulSoupObject = BeautifulSoup(webpage, "html.parser")

#Extract the table with the id of settlementsFuturesProductTable from the beautifulsoupobjects
table = beautifulSoupObject.find("table",{"id":"settlementsFuturesProductTable"})

#Get all rows from the table
rows = table.findAll("tr")

#Process each row with a for loop
for row in rows:
	#Get all cells of a row
	cells = row.findAll( ["th","td"] )
	
	#Create an output stringg
	output_string = ""

	#FOr each cell in the row add it's text to the output string
	for cell in cells:
		output_string = output_string + cell.get_text() + "\t |"

	#print output string for each row
	print(output_string)