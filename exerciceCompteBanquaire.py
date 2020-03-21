#coding:utf-8

import datetime

class Client():
    def __init__(self, nom, prenom, tel):
        self._nom = nom
        self._prenom = prenom
        self._tel = tel
        self.monCompte = Compte("012345678912")

    #Accesseurs
    def getNom(self):
        return self._nom
    def getPrenom(self):
        return self._prenom
    def getTel(self):
        return self._tel
    
    #Mutateurs
    def setNom(self, nouveauNom):
        self._nom = nouveauNom
    def setPrenom(self, nouveauPrenom):
        self._prenom = nouveauPrenom
    def setTel(self, nouveauTel):
        self._tel = nouveauTel
        
    def affichage(self):
        print(f"Nom : {self.getNom()}")
        print(f"Prénom : {self.getPrenom()}")
        print(f"Numéro de télephone : {self.getTel()}")
        print(f"Mon numéro de compte est : {self.monCompte.getNoCompte()}")
        print(f"Solde restant : {self.monCompte.getSolde()}")
        
class Compte():
    def __init__(self, numeroDeCompte):
        self._noCompte = numeroDeCompte
        self._solde = 0
        self._listeTransaction = []
        
    #Accesseurs
    def getNoCompte(self):
        return self._noCompte
    def getSolde(self):
        return self._solde
    
    def crediter(self, ajout):
        self.type = "credit"  
        self._solde += ajout
        self._listeTransaction.append(Transaction(self.type,ajout))
        
    def debiter(self, ajout):
        self.type = "credit"  
        self._solde -= ajout
        self._listeTransaction.append(Transaction(self.type,ajout))
        
    def listerTransactions(self):
        """ Ne fait encore rien mais c'est à faire """
        print(len(self._listeTransaction))


class Transaction():
    def __init__(self, leType, montantDeModification):
        self._dateTransaction = datetime.datetime.now()
        self._type = leType
        self._sommeDebitCredit = montantDeModification
        
    #Accesseurs
    def getDate(self):
        return self.dateTransaction
    def getType(self):
        return self._type
    
    def getSomme(self):
        return self._sommeDebitCredit

def choixOperation(client):
    print("""
    Quelle opération souhaitez vous faire ?
        1.Debiter mon compte
        2.Crediter mon compte
        3.Afficher mes transaction
        4.Quitter
    """)
    try:
        reponse = int(input("Faites votre choix : "))
        if   (reponse == 1):
            client.monCompte.debiter(int(input("Combien souhaitez vous retirer ?")))
        elif (reponse == 2):
            client.monCompte.crediter(int(input("Combien souhaitez vous ajouter ?")))
        elif (reponse == 3):
            client.monCompte.listerTransactions()
        elif (reponse == 4):
            pass
        else:
            print("Votre choix doit correspondre aux valeurs de la liste")
    except:
        print("Votre choix doit être un chiffre et dans la liste")

if __name__ == "__main__":
    #Creation d'un compte
    client = Client("Libert", "Gerald", "0497903620")
    #Lancement du mécanisme de gestion
    while True:
        client.affichage()
        choixOperation(client)
