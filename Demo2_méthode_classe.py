class Employe:
    TAUX_AUGMENTATION:float = 1.05
    liste_employe:list['Employe'] = []
    next_ID:int = 1000 
    
    def __init__(self,p_prenom:str, p_nom:str, p_salaire:int) -> 'Employe':
        self.prenom:str = p_prenom
        self.nom:str = p_nom
        self.salaire:int = p_salaire
        self._ID:int = Employe.next_ID
        
        Employe.next_ID += 1
        Employe.liste_employe.append(self)
    
    @classmethod # Méthode utilisé par la classe et non par l'instance
    def from_string(cls, donnees_str:str,separateur=';') -> 'Employe': # Constructeur alternatif
        "Crée un employé à partir d'un str. Retourne le nouvel employé"
        nom, prenom, salaire = donnees_str.split(separateur)
        nouvel_employe = cls(nom,prenom,int(salaire))
        return nouvel_employe
    
    def __repr__(self):
        return f"{self._ID},{self.nom}"




if __name__ == '__main__' :
    e1 = Employe("John", "Doe", 20000)
    e2 = Employe.from_string("Jane;Doe;35000")
    e3 = Employe.from_string("Eric;Trembley;45000")

    for employe in Employe.liste_employe :
        print(employe)