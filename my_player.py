from song import Song
from binary_search_tree import TreeNode, BinarySearchTree
from hash_table import HashTable
from stack import Stack


class MyPlayer:
    def __init__(self):
        """

        :return:
        """
        self.songList = []
        self.is_sorted = False
        self.yearMemory = None

    def loadLibrary(self, filename):
        """

        :param filename:
        :return:
        """
        pass

    def quickSort(self):
        """

        :return:
        """
        # TODO: Sort your songList here...
        self.is_sorted = True

    def playSong(self, title):
        """

        :param title:
        :return:
        """
        pass

    def showLastPlayed(self):
        """

        :return:
        """
        pass

    def buildYearMemory(self):
        """

        :return:
        """
        self.yearMemory = None

    def getYearMemory(self, year, title):
        """

        :param year:
        :param title:
        :return:
        """
        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song

        # TODO: Search for the song, note, you are NOT allowed to use self.songList in this method
        # TODO: You can assume self.buildYearMemory is already called, no need to call it here

        # Do not modify the return line, assign proper values for
        # steps and song above
        return {"steps": steps, "song": the_song}

    def getSong(self, year, title):
        """

        :param year:
        :param title:
        :return:
        """
        steps = 0  # Number of steps used to search for the song
        song = None  # The song

        # TODO: Search for the song, Note, you are NOT allowed to use self.yearMemory in this method

        # Do not modify the return line, assign proper values for
        # steps and song above
        return {"steps": steps, "song": song}


# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_my_player.py
