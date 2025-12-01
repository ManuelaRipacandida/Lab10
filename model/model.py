from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self._lista_hub=[]
        self._dizionario_hub={}

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO


        self._lista_hub = DAO.readAllHub() # Leggo tutti gli hub dal DAO
        # Ciclo sugli hub per aggiungerli al grafo e popolare il dizionario
        for hub in self._lista_hub:
            self._dizionario_hub[hub.id] = hub
            self.G.add_node(hub) # aggiungo nodi nel grafo


        hub_ids = [hub.id for hub in self._lista_hub] # Lista di tutti gli ID hub
        # Ciclo su tutte le coppie di hub  per creare archi
        for i in range(len(hub_ids)):
            for j in range(i+1,len(hub_ids)):
                    hub1=hub_ids[i]
                    hub2=hub_ids[j]
                    valore_medio = DAO.readGuadagnoMedio(hub1,hub2) # Chiamo il DAO per il guadagno medio
                    if valore_medio is None:
                        valore_medio = 0
                    if valore_medio >= threshold: #Filtro i risultati
                        u_nodo = self._dizionario_hub[hub1]
                        v_nodo = self._dizionario_hub[hub2]
                        self.G.add_edge(u_nodo, v_nodo,valore_medio=valore_medio)# Aggiungo l’arco con peso

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return list(self.G.edges(data=True))

