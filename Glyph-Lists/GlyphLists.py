"""
Robofont script that prints various glyph Lists / based on RoboFab gString' glyph Lists
it imports the lists and dicts of glyphs from modules folder - these lists can be modified.
Dont change list names in modules.dicts - if you change lists and dict names in modules.dicts - you need to modify them in this script too.
by Lukas Schneider 2014-05-26

many thanks to Alexandre Saumier Demers for the improvements
"""

from vanilla import *
from mojo.UI import OpenSpaceCenter, CurrentSpaceCenter
from modules.dicts import *
from modules.tile_windows import tile

class GlyphLists(object):

	def __init__(self):

		self.font = CurrentFont()
		
		
		self.firstList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ae', 'oslash', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AE', 'Oslash']
		
		self.secondList =['uppercase_plain', 'uppercase_accents', 'uppercase_special_accents', 'uppercase_ligatures', 'uppercase', 'lowercase_plain', 'lowercase_accents', 'lowercase_special_accents', 'lowercase_ligatures', 'lowercase', 'smallcaps_plain', 'smallcaps_accents', 'smallcaps_special_accents', 'smallcaps_ligatures', 'smallcaps', 'all_accents', 'digits', 'digits_oldstyle', 'digits_superior', 'digits_inferior', 'fractions', 'currency', 'currency_oldstyle', 'currency_superior', 'currency_inferior', 'inferior', 'superior', 'accents', 'dashes', 'legal', 'ligatures', 'punctuation', 'numerical', 'slashes', 'special']
		
		self.firstList.insert(0, 'select')
		self.secondList.insert(0, 'select')

			  
		self.w = FloatingWindow((250, 330), 'Glyph Lists')
		self.w.textBox = EditText((1, 1, -1, 180), "", sizeStyle = "small")
		self.w.infotext = TextBox((5,185,300,20), text="Print glyph dependencies:", sizeStyle = "small") 
		self.w.glyphSelect = PopUpButton((5, 195, 60, 30), self.firstList, sizeStyle = "small", callback=self.selectGlyphGstring)
		self.w.infotext2 = TextBox((5,235,300,20), text="Print other glyph lists:", sizeStyle = "small") 
		self.w.glyphSelectOther = PopUpButton((5, 247, 60, 30), self.secondList, sizeStyle = "small", callback=self.selectGlyphGstringOther)						 
		self.w.removeGlyphs = CheckBox((70,200,240,20), "Remove glyphs not in Font", sizeStyle="small", callback=self.removeGlyphsNotInFont)   
		self.w.addKeyGlyph = CheckBox((70,215,240,20), "Add key glyph", sizeStyle="small", callback=self.addKeyGlyph)   
		self.w.removeGlyphsOtherLists = CheckBox((70,252,240,20), "Remove glyphs not in Font", sizeStyle="small", callback=self.removeGlyphsOtherLists)
		self.w.spaceCenterButton = Button((5,305,80,18), "SpaceCenter", sizeStyle = "small", callback=self.spaceCenter)  
		self.w.spaceCenterButton2 = Button((-135,280,125,18), "SpaceCenter allFonts", sizeStyle = "small", callback=self.spaceCenterAllFonts)	
		self.w.stripSlashes = Button((5,280,103,18), "Strip out Slashes", sizeStyle = "small", callback=self.stripOutSlashes)	
		self.w.buttonTile = Button((110,305,130,18), "Arrange spacecenters", sizeStyle = "small", callback=self.tile_windows)    
		self.w.open() 

	def perform(self):
	    glyphs = ""
	    for glyph in self.glyphlist:
	        glyphs += "/"+glyph
	    self.w.textBox.set(glyphs)
	
	def addKeyGlyph(self, sender):
	    self.selectGlyphGstring(None)


	def selectGlyphGstring(self, sender): 

		self.glyphlist = []
		
		index = self.w.glyphSelect.get()
		    
		if index == 0:
			return
		else:
		    itemList =  self.w.glyphSelect.getItems()
		    item = itemList[index]
		    if self.w.addKeyGlyph.get() == 1:
		        self.glyphlist.append(item)
		    for key, value in dependencies.items():
		        if key == item:
		            self.glyphlist.extend(value)					   
			
			self.perform()
    
			if self.w.removeGlyphs.get() == 1:
			    self.removeGlyphsNotInFont(None)
			

	def selectGlyphGstringOther(self, sender): 

		self.glyphlist = []
		
		index = self.w.glyphSelectOther.get()

		if index == 0:
			return
		else:
		    itemList =  self.w.glyphSelectOther.getItems()
		    item = itemList[index]

		    for i in globals()[item]:
		        self.glyphlist.append(i)
		    self.perform()
		    
		    if self.w.removeGlyphs.get() == 1:
		        self.removeGlyphsNotInFont(None)
			    
	def removeGlyphsNotInFont(self, sender):
	    self.font = CurrentFont()
	    if self.font == None:
	        return
	    else:
	        if self.w.removeGlyphs.get() == 1:
	            self.glyphlist = str(self.w.textBox.get()).strip("u").strip("/")
	            newglyphlist = self.glyphlist.split("/")
	            glyphListOfGlyphsInCurrentFont = []
	            for g in newglyphlist:
	                if self.font.has_key(g):
	                    glyphListOfGlyphsInCurrentFont.append(g)
	            self.glyphlist = glyphListOfGlyphsInCurrentFont
	            self.perform()
	        else:
	            self.selectGlyphGstring(None)

	def removeGlyphsOtherLists(self, sender):
	    self.font = CurrentFont()
	    if self.font == None:
	        return
	    else:
	        if self.w.removeGlyphsOtherLists.get() == 1:
	            self.glyphlist = str(self.w.textBox.get()).strip("u").strip("/")
	            newglyphlist = self.glyphlist.split("/")
	            glyphListOfGlyphsInCurrentFont = []
	            for g in newglyphlist:
	                if self.font.has_key(g):
	                    glyphListOfGlyphsInCurrentFont.append(g)
	            self.glyphlist = glyphListOfGlyphsInCurrentFont
	            self.perform()
	        else:
	            self.selectGlyphGstringOther(None)

	def spaceCenter(self, sender): 
		if CurrentFont() == None: 
			self.w.textBox.set("Open a font!")
		else:
			self.font = CurrentFont()
			textinput = self.w.textBox.get()
			if textinput == "Open a font!":
			   textinput = ""
			   sc = OpenSpaceCenter(self.font)
			   sc.setRaw(textinput)
			else:		 		  
			   sc = OpenSpaceCenter(self.font)
			   sc.setRaw(textinput)

	def spaceCenterAllFonts(self, sender): 
		if CurrentFont() == None: 
			self.w.textBox.set("Open a font!")
		else: 
			textinput = self.w.textBox.get()
			if textinput == "Open a font!":
			   textinput = ""
			   for font in AllFonts():	 
				    sc = OpenSpaceCenter(font)
				    sc.setRaw(textinput)
			else:	  
			   for font in AllFonts():	 
				    sc = OpenSpaceCenter(font)
				    sc.setRaw(textinput)

	def stripOutSlashes(self, sender): 
		textinput = self.w.textBox.get()
		if len(textinput) > 0:
		    if textinput[0] == "/":
		        strippedSlashes = textinput.strip("u").replace("/"," ")
		        self.w.textBox.set(strippedSlashes[1:])
	
	def tile_windows(self, sender): 
		tile()
		
GlyphLists()
