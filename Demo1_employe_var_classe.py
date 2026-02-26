class Employe:
    # 3 Variables de classe
    TAUX_AUGMENTATION:float = 1.05 # Constante. Variable de classe la plus fréquente
    liste_employe:list['Employe'] = [] # Var pour accumulation d'informations
    next_ID:int = 1000 # Var utilisé pour l'instanciation
    
    def __init__(self,p_prenom:str, p_nom:str, p_salaire:int) -> None:
        self.prenom:str = p_prenom
        self.nom:str = p_nom
        self.salaire:int = p_salaire
        self._ID:int = Employe.next_ID
        
        Employe.next_ID += 1
        Employe.liste_employe.append(self)
    




if __name__ == '__main__' :
    employe1 = Employe("Anna","Tremblay", 50000)
    employe2 = Employe("Bartholemy","Duchamp", 50000)

    for emp in Employe.liste_employe: 
        emp:Employe
        print(f'{emp.prenom} {emp.nom} {emp._ID}')