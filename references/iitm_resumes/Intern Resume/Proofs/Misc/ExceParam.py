#Author-Gwtam
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback,os.path

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        
        # Get the root component of the active design
        rootComp = design.rootComponent

        # Specify the folder to write out the results.
        folder = 'D:/FUSION/'

        # Get the parameters named "Length" and "dia" to change.
        dialog = ui.createFileDialog()
        dialog.filter = 'Comma Separated Values (*.csv)'
        dialog.initialDirectory = os.path.dirname(os.path.realpath(__file__))
        if dialog.showOpen() != adsk.core.DialogResults.DialogOK:
            return
        
        filename=dialog.filename
        f=open(filename,'r')    
        
        firstLine = f.readline()
        firstLine = firstLine.rstrip('\n')
        paramNames = firstLine.split(',')
        paramNames = paramNames[1:]
              
        # Iterate through the value lines.
        line = f.readline()
        while line:
            #doc = app.activeDocument
            design = app.activeProduct
            params = design.allParameters        

            line = line.rstrip('\n')
            values = line.split(',')

            # Iterate through the values and change the corresponding parameter.            
            for i in range(1,len(values)):
                param = params.itemByName(paramNames[i-1])
                param.expression = values[i]
                
                # Construct the output filename.
            filename = folder + str(values)+ 'x' + '.stl'
                
            adsk.doEvents()
                
                # Save the file as STL.
            exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
            stlOptions = exportMgr.createSTLExportOptions(rootComp)
            stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
            stlOptions.filename = filename
            exportMgr.execute(stlOptions)
                
            line = f.readline()
        
        f.close()     
                
                
                
        ui.messageBox('Finished.')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))