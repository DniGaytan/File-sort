#File/Directory handler

import os, sys

ENVIRON = os.environ['USERPROFILE']
args = sys.argv[1:]

def getDestPath(args):
    '''
    Get the destion path from the arguments list given
    '''
    path = args[len(args) - 1]
    return path

def processFiles(files, destPath):
    '''
    Process each file individually
    Moves each file to the destion path given
    '''
    for file in files:
        #Move file to the destination path (destPath)
        fileName = ''
        #retrieve the filename with suffix only (doc.docx)
        for c in reversed(file):
            if ord(c) != 92:
                fileName = ''.join(c) + fileName
            else:
                break

        os.rename(file, destPath + '\\' + fileName)

def main():
    if len(args) > 1:
        '''
        If the user typed two or more arguments, the main process will take place
        '''
        #gets the destination path
        destPath = getDestPath(args)

        #Save the destPath for other py files usages
        with open('data.txt', 'w') as f:
            f.write(destPath)

        del args[len(args) - 1]

        #process files...
        processFiles(args, destPath)

    else:
        print("""
        El sistema requiere al menos dos argumentos
        El primer argumento debe de ser el archivo que quieras mover
        El segundo argumento debe de ser el directorio destino
        -------------------------------------------------------------
        Para cuando quieras mover n archivos, el ultimo argumento debe
        ser el directorio destino
        -------------------------------------------------------------
        Ejemplo: python main.py [archivo 1] [carpeta destino]
        """)


if __name__ == "__main__":
    main()
else:
    print("Error, se necesita ejecutar desde consola")
