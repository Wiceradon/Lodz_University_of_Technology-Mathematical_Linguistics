# This Python file uses the following encoding: utf-8
'''
Created on 18-12-2013

@author: Jakub Jeleński
'''

import sys
import pkg_resources
import mlprograms.commons.writers.toObject as writer
import mlprograms.rpn.parser as parser
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

class RpnGuiGTK:
    '''
    '''
    
    def __init__(self):
        self.gladeFile = pkg_resources.resource_filename('mlprograms.resources.models', 'rpnGuiModel.glade')
        self.glade = gtk.Builder()
        self.glade.add_from_file(self.gladeFile)
        self.glade.connect_signals(self)
        self.glade.get_object("Window").show_all()
        self.results = {"Default":[None, None]}
        self.liststore = gtk.ListStore(str)
        self.liststore.append(["Default"])
        self.cell = gtk.CellRendererText()
        combobox = self.glade.get_object("resultComboBox")
        combobox.set_model(self.liststore)
        combobox.pack_start(self.cell, True)
        combobox.add_attribute(self.cell, 'text', 0)
        combobox.set_active(0)
        
    def WindowDestroy(self, widget):
        gtk.main_quit()
        
    def btnStartClicked(self, widget):
        bufText = self.glade.get_object("input").get_buffer()
        inputText = bufText.get_text(bufText.get_start_iter(), bufText.get_end_iter())
        inputText = inputText.split("\n")
        
        for i in inputText:
            self.results[i] = [TextPlaceholder(), None]
            writerObj = writer.ObjectTextWriter(self.results[i][0])
            self.results[i][1] = parser.RpnParser(i.strip().split(), writerObj).parse()
            self.liststore.append([i])
    
    def btnClearClicked(self, widget):
        output = self.glade.get_object("resultOutput")
        outputBuf = output.get_buffer()
        outputBuf.set_text("")
        
        inputArea = self.glade.get_object("input")
        inputBuf = inputArea.get_buffer()
        inputBuf.set_text("")
        
        self.results = {"Default":[None, None]}
        
        self.liststore.clear()
        self.liststore.append(["Default"])
        self.glade.get_object("resultComboBox").set_active(0)
    
    def btnCloseClicked(self, widget):
        gtk.main_quit()

    def resultComboBoxChanged(self, widget):
        idn = widget.get_active()
        if idn != -1:
            currentRes = self.liststore[idn][0]
            output = self.glade.get_object("resultOutput")
            outputBuf = output.get_buffer()
            if currentRes == "Default":
                outputBuf.set_text("")
            else:
                outputBuf.set_text(self.results[currentRes][0].getText()+
                                   "\n\nResult: "+
                                   str(self.results[currentRes][1]))

class TextPlaceholder:
    
    def __init__(self):
        self.text = ""
        
    def getText(self):
        return self.text
    
    def setText(self, data):
        self.text = data
        

if __name__ == '__main__':
    hwg = RpnGuiGTK()
    gtk.main()