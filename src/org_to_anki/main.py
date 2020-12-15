#!/usr/bin/env python3
# Script to parse differnet formated org files and upload them to Anki
import sys
import os

from .org_parser import parseData
from .ankiConnectWrapper.AnkiConnector import AnkiConnector
from .ankiConnectWrapper import AnkiPluginConnector
from . import config

def parseAndUploadOrgFile(filePath=None, embedded=False):

    if (filePath == None and embedded == True):
        raise Exception("No file path was given while running in embedded mode.")
    elif filePath is None:
        filePath = _getUploadFilePath()

    if "~" in filePath:
        filePath = filePath.replace("~", config.homePath)

    _parseAndUpload(filePath, embedded)

def _getUploadFilePath():

    firstArg = sys.argv[1:2]
    if len(firstArg) < 1 or firstArg == ['-v']:
        print("File was not given. Will upload default file.")
        filePath = config.quickNotesOrgPath
    else:
        filePath = sys.argv[1]

    return filePath


def _parseAndUpload(filePath, embedded=False):

    deck = parseData.parse(filePath)

    # Use the parent directory as the name of the parent deck
    parent_dir = os.path.abspath(filePath).split(os.sep)[-2]

    if (embedded == False):
        connector = AnkiConnector(defaultDeck=parent_dir)
    else:
        connector = AnkiPluginConnector.AnkiPluginConnector(
                defaultDeck=parent_dir)
    connector.uploadNewDeck(deck)

if __name__ == "__main__":
    parseAndUploadOrgFile()
