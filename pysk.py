#=====================#
# PYSKRIPT TRANSPILER #
#=====================#

# - By: Ness
# - Version: 1.0.0

import re
import unidecode

class FRS: 

    def __init__ (self):
        pass
    
    class File:
        
        def __init__ (self):
            pass

        def ask (self):
            answer = input('- Fichier à transpiler > ')
            return answer

        def file (self):
            input = self.ask()
            try:
                file = open(input, encoding='UTF8')
            except:
                print('Une erreur est survenue durant la lecture du fichier.')
            return file.read()
