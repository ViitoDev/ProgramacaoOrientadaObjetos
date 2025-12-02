from Modulos.avaluate import Evaluating

class Library:
    libraries = []

    def __init__(self, name):
        self.name = name
        self._active = False
        self.evaluation = []
        Library.libraries.append(self)

    def __str__(self):
        return self.name
    
    @classmethod
    def list_Libraries(cls):
        print(f"{'Nome da biblioteca'.ljust(25)}| {'Nota média'.ljust(25)} | {'Status'}")
        for library in Library.libraries:
            print(f"{library.name.ljust(25)}| {str(library.evaluate_media).ljust(25)} | {library.active}")

    def toggle_state(self):
        self._active = not self._active

    @property
    def active(self):
        if self._active and self.evaluation:
            return "Ativada"
        else:
            return "Desativada"

    def receive_evaluation(self, client, note):
        evaluate = Evaluating(client, note)
        self.evaluation.append(evaluate)

    @property
    def evaluate_media(self):
        if not self.evaluation:
            return "-"
        sum1 = sum(evaluate._note for evaluate in self.evaluation)
        average = round(sum1 / len(self.evaluation))
        return average