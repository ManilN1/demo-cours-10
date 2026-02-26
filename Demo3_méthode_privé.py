# méthodes qu'on ne veut pas rendre accessible hors de la classe

class Employe:
    TAUX_AUGMENTATION:float = 1.05
    liste_employe:list['Employe'] = []
    next_ID:int = 1000 
    
    def __init__(self,p_prenom:str, p_nom:str, p_salaire:int) -> None:
        self.prenom:str = p_prenom
        self.nom:str = p_nom
        self._salaire:int = self._valider_salaire(p_salaire)
        self._ID:int = Employe.next_ID
        
        self._incrementer_liste_employe()

    @property
    def salaire(self)->int|float : return self._salaire
    @salaire.setter
    def salaire(self, p_nvx_montant) -> None :
        self._salaire = self._valider_salaire(p_nvx_montant)


    # Méthode privé (commence par un _)
    # Cette méthode est appelé uniquement à l'intérieur de la classe.
    def _incrementer_liste_employe(self) :
        Employe.next_ID += 1
        Employe.liste_employe.append(self)

    # Méthode privé statique.
    # Méthode de validation.
    @staticmethod 
    def _valider_salaire(p_salaire:int|float) -> int|float :
        """Valide que le salaire est un float ou int"""
        if isinstance(p_salaire, (int,float)) == False:
            raise TypeError("Salaire doit être int ou float")
        return p_salaire
    

if __name__ == '__main__' :
    employe1 = Employe("Anna","Tremblay",40000)
    employe2 = Employe("Bartholemy","Duchamp",50000)

    for emp in Employe.liste_employe: 
        print(f'{emp.prenom} {emp.nom} {emp._ID}')