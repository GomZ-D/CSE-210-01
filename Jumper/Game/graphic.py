
class Graphic:
    """This class is responsible of drawing the parachuter

    Args:
        self (Graphic): An instance of Graphic

    Stereotype:
        Service Provider / Interfacer / Information Holder
    
    Attributes:
            parachute(list): A list of strings used to print the parachute
    """
   
    def __init__(self):
        """The class constructor.

        Args:
            self(Graphic): An instance of Graphic
        """
        self._lives = 7
        self._parachute = {
         7: [
            " ___  ",
            "/___\ ",
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         6: [
            "/___\ ",
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         5: [
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         4: [
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"], 
         3: [
            "AHHHH!",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"], 
         2: [
            " /|\   ",
            " / \   ",
            "       ",
            "^^^^^^ "], 
         1: [
            " / \  ",
            "      ",
            "^^^^^^"],  
         0: [
            "O-\//\ ",
            "^^^^^^ "],   
        }


    def print_parachute(self):
        """This function print out the parachute

        Args:
            self(Graphic): An instance of Graphic
        """
        key = self._lives
        print('')
        for i in self._parachute[key]:
            print(i)

    def get_lives(self):
        return self._lives
        
    
    def decrease_lives(self):
        self._lives -= 1