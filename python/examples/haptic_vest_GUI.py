import wx

class Example(wx.Frame):

   def __init__(self, parent, title):
      super(Example, self).__init__(parent, title = title, size = (420, 270))

      self.InitUI()
      self.Centre()
      self.Show()

   def InitUI(self):
      panel = wx.Panel(self)

      hbox = wx.BoxSizer(wx.HORIZONTAL)

      fgs = wx.FlexGridSizer(2, 3, 10,10)

      elevationList = ['person', 'vehicle', 'chair']
      distanceList = ['distance_10', 'distance_15', 'distance_20', 'distance_25']
      directionList = ['0 degrees', '45 degrees', '90 degrees', '135 degrees', '180 degrees', '225 degrees', '270 degrees', '315 degrees']

      self.elevationBox = wx.RadioBox(panel, label = 'ElevationRadioBox', choices = elevationList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS)
      #self.elevationBox.Bind(wx.EVT_RADIOBOX, self.onElevationRadioBox)


      self.distanceBox = wx.RadioBox(panel, label = 'DistanceRadioBox', choices = distanceList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS)
      #self.distanceBox.Bind(wx.EVT_RADIOBOX, self.onDistanceRadioBox)

      self.directionBox = wx.RadioBox(panel, label = 'directionRadioBox', choices = directionList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS)
      #self.directionBox.Bind(wx.EVT_RADIOBOX, self.onDirectionRadioBox)

      fgs.AddMany([(self.elevationBox, 1, wx.EXPAND), (self.distanceBox, 1, wx.EXPAND), (self.directionBox, 1, wx.EXPAND)])
      fgs.AddGrowableRow(1, 1)
      fgs.AddGrowableCol(1, 1)
      hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15)
      panel.SetSizer(hbox)

app = wx.App()
Example(None, title = 'FlexiGrid Demo')
app.MainLoop()
