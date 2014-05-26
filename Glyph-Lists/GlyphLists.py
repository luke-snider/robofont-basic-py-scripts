"""
Robofont script that prints various glyph Lists / based on RoboFab gString' glyph Lists
it imports the lists and dicts of glyphs from modules folder - these lists can be modified.
Dont change list names in modules.dicts - if you change lists and dict names in modules.dicts - you need to modify them in this script too.
by Lukas Schneider 2014-05-25
"""

from dialogKit import *
from vanilla import Window
from mojo.UI import OpenSpaceCenter, CurrentSpaceCenter
from modules.dicts import *

class GlyphLists(object):
	
	def __init__(self):
		
		self.font = CurrentFont()
		self.listsList =['uppercase_plain', 'uppercase_accents', 'uppercase_special_accents', 'uppercase_ligatures', 'uppercase', 'lowercase_plain', 'lowercase_accents', 'lowercase_special_accents', 'lowercase_ligatures', 'lowercase', 'smallcaps_plain', 'smallcaps_accents', 'smallcaps_special_accents', 'smallcaps_ligatures', 'smallcaps', 'all_accents', 'digits', 'digits_oldstyle', 'digits_superior', 'digits_inferior', 'fractions', 'currency', 'currency_oldstyle', 'currency_superior', 'currency_inferior', 'inferior', 'superior', 'accents', 'dashes', 'legal', 'ligatures', 'punctuation', 'numerical', 'slashes', 'special']	  
		self.w = Window((250, 300), 'Glyph Lists', maxSize=(250,300), minSize=(250,300))
		self.w.textBox = EditText((1, 1, -1, 180), "", sizeStyle = "small")
		self.w.infotext = TextBox((5,185,300,20), text="Print glyph dependencies:", sizeStyle = "small") 
		self.w.glyphSelect = PopUpButton((5, 195, 60, 30), ['select', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ae', 'oslash', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AE', 'Oslash'], sizeStyle = "small", callback=self.selectGlyphGstring)
		self.w.infotext2 = TextBox((5,225,300,20), text="Print other glyph lists:", sizeStyle = "small") 
		self.w.glyphSelectOther = PopUpButton((5, 237, 60, 30), ['select', 'uppercase_plain', 'uppercase_accents', 'uppercase_special_accents', 'uppercase_ligatures', 'uppercase', 'lowercase_plain', 'lowercase_accents', 'lowercase_special_accents', 'lowercase_ligatures', 'lowercase', 'smallcaps_plain', 'smallcaps_accents', 'smallcaps_special_accents', 'smallcaps_ligatures', 'smallcaps', 'all_accents', 'digits', 'digits_oldstyle', 'digits_superior', 'digits_inferior', 'fractions', 'currency', 'currency_oldstyle', 'currency_superior ', 'currency_inferior', 'inferior', 'superior', 'accents', 'dashes', 'legal', 'ligatures', 'punctuation', 'numerical', 'slashes', 'special'], sizeStyle = "small", callback=self.selectGlyphGstringOther)						 
		self.w.removeGlyphs = CheckBox((70,200,240,20), "Remove glyphs not in Font", sizeStyle="small", callback=self.removeGlyphsNotInFont)   
		self.w.removeGlyphsOtherLists = CheckBox((70,240,240,20), "Remove glyphs not in Font", sizeStyle="small", callback=self.removeGlyphsOtherLists)   
		self.w.spaceCenterButton = Button((5,270,80,18), "SpaceCenter", sizeStyle = "small", callback=self.spaceCenter)  
		self.w.spaceCenterButton2 = Button((-140,270,130,18), "SpaceCenter allFonts", sizeStyle = "small", callback=self.spaceCenterAllFonts)	
		self.w.open() 
	
	def perform(self):  
			
		glyphs = "/"+str(self.glyphlist).strip('[\'\'])').replace(', ','/').replace('\'','')
		self.w.textBox.set(glyphs)


	def selectGlyphGstring(self, sender): 

		self.glyphlist = []
		selectionList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ae', 'oslash', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AE', 'Oslash']

		if self.w.glyphSelect.get() == 0:
			pass
		else:
			for index,item in enumerate(selectionList):		  
				if self.w.glyphSelect.get() == index+1:
					selectedGlyph = selectionList[index]   
			for key, value in dependencies.items():
				if key == selectedGlyph:
					self.glyphlist.append(value)					   
			self.perform()

	def selectGlyphGstringOther(self, sender): 

		self.glyphlist = []
		selectionList = self.listsList
		selection = []

		if self.w.glyphSelectOther.get() == 0:
			pass
		else:
			for index,item in enumerate(selectionList):	 
				if self.w.glyphSelectOther.get() == index+1:
						selectedGlyph = selectionList[index]					  
						selection.append(selectedGlyph)		
			for item in globals()[selectedGlyph]:			   
				self.glyphlist.append(item)
			self.perform()
		

	def removeGlyphsNotInFont(self, sender): 
		if CurrentFont() == None:
			pass
		else:
			if self.w.removeGlyphs.get() == 1:
				self.glyphlist = str(self.w.textBox.get()).strip("u").strip("/")
				newglyphlist = self.glyphlist.split("/")
				glyphListOfGlyphsInCurrentFont = []
				for g in self.font:
					if g.name in newglyphlist:
						try:
							glyphListOfGlyphsInCurrentFont.append(g.name)
						except ValueError:
							pass 
						except AttributeError:
							pass			
				self.glyphlist = glyphListOfGlyphsInCurrentFont
				self.perform()
			if self.w.removeGlyphs.get() == 0:
				self.selectGlyphGstring(self)

	def removeGlyphsOtherLists(self, sender): 
		if CurrentFont() == None:
			pass
		else:
			if self.w.removeGlyphsOtherLists.get() == 1:
				self.glyphlist = str(self.w.textBox.get()).strip("u").strip("/")
				newglyphlist = self.glyphlist.split("/")
				glyphListOfGlyphsInCurrentFont = []
				for g in self.font:
					if g.name in newglyphlist:
						try:
							glyphListOfGlyphsInCurrentFont.append(g.name)
						except ValueError:
							pass 
						except AttributeError:
							pass			
				self.glyphlist = glyphListOfGlyphsInCurrentFont
				self.perform()
			if self.w.removeGlyphsOtherLists.get() == 0:
				self.selectGlyphGstringOther(self)

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
		
GlyphLists()
