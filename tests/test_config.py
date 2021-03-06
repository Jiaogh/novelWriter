# -*- coding: utf-8 -*-
"""novelWriter Config Class Tester
"""

import pytest
import os

from nwtools import cmpFiles

@pytest.mark.core
def testConfigCore(tmpConf, nwTemp, nwRef):
    refConf = os.path.join(nwRef, "novelwriter.conf")
    testConf = os.path.join(tmpConf.confPath, "novelwriter.conf")

    assert tmpConf.confPath == nwTemp
    assert tmpConf.saveConfig()
    assert cmpFiles(testConf, refConf, [2])
    assert not tmpConf.confChanged

    assert tmpConf.loadConfig()
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigSetConfPath(tmpConf, nwTemp):
    assert tmpConf.setConfPath(None)
    assert not tmpConf.setConfPath(os.path.join("somewhere", "over", "the", "rainbow"))
    assert tmpConf.setConfPath(os.path.join(nwTemp, "novelwriter.conf"))
    assert tmpConf.confPath == nwTemp
    assert tmpConf.confFile == "novelwriter.conf"
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigSetDataPath(tmpConf, nwTemp):
    assert tmpConf.setDataPath(None)
    assert not tmpConf.setDataPath(os.path.join("somewhere", "over", "the", "rainbow"))
    assert tmpConf.setDataPath(nwTemp)
    assert tmpConf.dataPath == nwTemp
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigSetWinSize(tmpConf, nwTemp, nwRef):
    refConf = os.path.join(nwRef, "novelwriter.conf")
    testConf = os.path.join(tmpConf.confPath, "novelwriter.conf")
    tmpConf.guiScale = 1.0

    assert tmpConf.confPath == nwTemp
    assert tmpConf.setWinSize(1105, 655)
    assert not tmpConf.confChanged
    assert tmpConf.setWinSize(70, 70)
    assert tmpConf.confChanged
    assert tmpConf.setWinSize(1100, 650)
    assert tmpConf.saveConfig()

    assert cmpFiles(testConf, refConf, [2])
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigSetTreeColWidths(tmpConf, nwTemp, nwRef):
    refConf = os.path.join(nwRef, "novelwriter.conf")
    testConf = os.path.join(tmpConf.confPath, "novelwriter.conf")

    assert tmpConf.confPath == nwTemp
    tmpConf.guiScale = 1.0

    assert tmpConf.setTreeColWidths([10, 20, 30])
    assert tmpConf.treeColWidth == [10, 20, 30]
    assert tmpConf.setTreeColWidths([120, 30, 50])

    assert tmpConf.setProjColWidths([10, 20, 30])
    assert tmpConf.projColWidth == [10, 20, 30]
    assert tmpConf.setProjColWidths([140, 55, 140])

    assert tmpConf.confChanged
    assert tmpConf.saveConfig()

    assert cmpFiles(testConf, refConf, [2])
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigSetPanePos(tmpConf, nwTemp, nwRef):
    refConf = os.path.join(nwRef, "novelwriter.conf")
    testConf = os.path.join(tmpConf.confPath, "novelwriter.conf")

    assert tmpConf.confPath == nwTemp

    tmpConf.guiScale = 2.0
    assert tmpConf.setMainPanePos([200, 700])
    assert tmpConf.mainPanePos == [100, 350]
    assert tmpConf.getMainPanePos() == [200, 700]

    assert tmpConf.setDocPanePos([300, 300])
    assert tmpConf.docPanePos == [150, 150]
    assert tmpConf.getDocPanePos() == [300, 300]

    assert tmpConf.setViewPanePos([400, 250])
    assert tmpConf.viewPanePos == [200, 125]
    assert tmpConf.getViewPanePos() == [400, 250]

    assert tmpConf.setOutlinePanePos([400, 250])
    assert tmpConf.outlnPanePos == [200, 125]
    assert tmpConf.getOutlinePanePos() == [400, 250]

    tmpConf.guiScale = 1.0
    assert tmpConf.setMainPanePos([300, 800])
    assert tmpConf.setDocPanePos([400, 400])
    assert tmpConf.setViewPanePos([500, 150])
    assert tmpConf.setOutlinePanePos([500, 150])

    assert tmpConf.confChanged
    assert tmpConf.saveConfig()

    assert cmpFiles(testConf, refConf, [2])
    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigFlags(tmpConf, nwTemp, nwRef):
    refConf = os.path.join(nwRef, "novelwriter.conf")
    testConf = os.path.join(tmpConf.confPath, "novelwriter.conf")

    assert tmpConf.confPath == nwTemp

    assert not tmpConf.setShowRefPanel(False)
    assert tmpConf.setShowRefPanel(True)

    assert not tmpConf.setViewComments(False)
    assert not tmpConf.viewComments
    assert tmpConf.setViewComments(True)

    assert not tmpConf.setViewSynopsis(False)
    assert not tmpConf.viewSynopsis
    assert tmpConf.setViewSynopsis(True)

    assert tmpConf.confChanged
    assert tmpConf.saveConfig()

    assert cmpFiles(testConf, refConf, [2])
    assert not tmpConf.confChanged

@pytest.mark.core
def testTextSizes(tmpConf, nwTemp, nwRef):
    assert tmpConf.confPath == nwTemp

    tmpConf.guiScale = 2.0
    assert tmpConf.getTextWidth() == 1200
    assert tmpConf.getTextMargin() == 80
    assert tmpConf.getTabWidth() == 80
    assert tmpConf.getFocusWidth() == 1600
    tmpConf.guiScale = 1.0

    assert not tmpConf.confChanged

@pytest.mark.core
def testConfigErrors(tmpConf):
    nonPath = os.path.join("somewhere", "over", "the", "rainbow")
    assert tmpConf.initConfig(nonPath, nonPath)
    assert tmpConf.hasError
    assert not tmpConf.loadConfig()
    assert not tmpConf.saveConfig()
    assert not tmpConf.loadRecentCache()
    assert len(tmpConf.getErrData()) > 0

@pytest.mark.core
def testConfigInternals(tmpConf):
    assert tmpConf._checkNone(None) is None
    assert tmpConf._checkNone("None") is None
