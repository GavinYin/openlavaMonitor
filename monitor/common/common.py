import os
import stat

def printError(message):
    """
    Print error message with red color.
    """
    print('\033[1;31m' + str(message) + '\033[0m')

def printWarning(message):
    """
    Print warning message with yellow color.
    """
    print('\033[1;33m' + str(message) + '\033[0m')

def stringToInt(inputString):
    """
    Switch the input string into ASCII number.
    """
    intNum = ''
    for char in inputString:
        num = ord(char)
        intNum = str(intNum) + str(num)
    intNum = int(intNum)
    return(intNum)

def drawPlot(xList, yList, xLabel, yLabel, xIsString=False, yUnit='', title='', saveName='', figureNum=1):
    """
    Draw a curve with pyplot.
    """
    from matplotlib import pyplot

    fig = pyplot.figure(figureNum)

    # Draw the pickture.
    if xIsString:
        xStringList = xList
        xList = range(len(xList))
        pyplot.xticks(xList, xStringList, rotation=30, fontsize=12)
        pyplot.plot(yList, 'ro-')
    else:
        pyplot.plot(xList, yList, 'ro-')

    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)

    pyplot.grid(True)

    if xIsString:
        pyplot.subplots_adjust(bottom=0.2)
    else:
        pyplot.subplots_adjust(bottom=0.15)

    # Set title.
    if title != '':
        pyplot.title(title)

    # Get value info.
    xMin = min(xList)
    xMax = max(xList)
    yMin = min(yList)
    yMax = max(yList)

    # Define the curve range.
    if len(xList) == 1:
        pyplot.xlim(xMin-1, xMax+1)
        pyplot.ylim(yMin-1, yMax+1)
    else:
        pyplot.xlim(xMin, xMax)
        if yMin == yMax:
            pyplot.ylim(yMin-1, yMax+1)
        else:
            pyplot.ylim(1.1*yMin-0.1*yMax, 1.1*yMax-0.1*yMin)

    # Show the peak value.
    pyplot.text(xMin, yMax, 'peak: ' + str(yMax) + str(yUnit))

    # Save fig, or show it.
    if saveName != '':
        fig.savefig(saveName)
        os.chmod(saveName, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
    else:
        fig.show()

def drawPlots(xList, yLists, xLabel, yLabel, yLabels, xIsString=False, title='', saveName='', figureNum=1):
    """
    Draw a curve with pyplot.
    """
    from matplotlib import pyplot

    fig = pyplot.figure(figureNum)

    if len(yLists) > 8:
        printError('*Error* (drawPlots) : For function "draw_plots", the length of yLists cannot be bigger than 8!')
        return(1)

    colorList = ['red', 'green', 'yellow', 'cyan', 'magenta', 'blue', 'black', 'white']

    # Draw the pickture.
    if xIsString:
        xStringList = xList
        xList = range(len(xList))
        pyplot.xticks(xList, xStringList, rotation=30, fontsize=12)
        for i in range(len(yLists)):
            pyplot.plot(yLists[i], color=colorList[i], label=yLabels[i], linestyle='-')
    else:
        for i in range(len(yLists)):
            pyplot.plot(xList, yLists[i], color=colorList[i], label=yLabels[i], linestyle='-')

    pyplot.legend(loc='upper right')

    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)

    pyplot.grid(True)

    if xIsString:
        pyplot.subplots_adjust(bottom=0.2)
    else:
        pyplot.subplots_adjust(bottom=0.15)

    # Set title.
    if title != '':
        pyplot.title(title)

    # Save fig, or show it.
    if saveName != '':
        fig.savefig(saveName)
        os.chmod(saveName, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
    else:
        fig.show()

def getJobRangeDic(jobList):
    jobRangeDic = {}

    for job in jobList:
        jobHead = (int(int(job)/10000))*10000
        jobTail = jobHead + 9999
        jobRange = str(jobHead)  + '_' + str(jobTail)
        if jobRange not in jobRangeDic:
            jobRangeDic[jobRange] = []
        jobRangeDic[jobRange].append(job)

    return(jobRangeDic)
