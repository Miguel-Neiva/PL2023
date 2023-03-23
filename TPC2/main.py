import tpc2
import sys
a ta prima
def main():
    somador = tpc2.Somador()
    while True:
        line = input("Insira um texto: ")
        somador.parseLine(line)

if __name__ == "__main__":
        main()