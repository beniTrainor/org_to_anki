import os
from . import config
from .ankiConnectWrapper.AnkiPluginConnector import AnkiPluginConnector
from .ankiConnectWrapper.AnkiNoteBuilder import AnkiNoteBuilder


def createQuickNotesFile(directory=None):
    if directory is None:
        directory = config.quickNotesDirectory

    if not os.path.exists(directory):
        os.makedirs(directory)

def getAnkiPluginConnector():

    return AnkiPluginConnector()

def getAnkiNoteBuilder():

    return AnkiNoteBuilder()