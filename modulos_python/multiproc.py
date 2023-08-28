from time import sleep
from threading import Thread

class MeuThread(Thread):

    def __init__(self, texto, tempo) -> None:

        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):

        sleep(self.tempo)
        print(self.texto)


t = MeuThread('Thread 1', 5)
# Esse objeto ira executar em uma thead a parte da principal
t.start()

for i in range(20):
    print(i)
    sleep(1)
