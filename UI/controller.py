import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            valore_costo = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert("Selezionare un valore numerico!")
            return
        # COSTRUISCO IL GRAFO prima di leggere nodi e archi
        self._model.costruisci_grafo(valore_costo)

            # Chiamo il model
        numero_hub = self._model.get_num_nodes()
        numero_tratte=self._model.get_num_edges()
        lista_tratte=self._model.get_all_edges()
            # Pulisco il contenitore prima di mostrare i nuovi risultati
        lista = self._view.lista_visualizzazione
        lista.controls.clear()
        lista.controls.append(ft.Text(f"Numero di Hubs: {numero_hub}"))
        lista.controls.append(ft.Text(f"Numero di tratte: {numero_tratte}"))
        # Ciclo su tutti gli archi e stampo solo quelli sopra soglia
        trovata=False
        for u,v,attr in lista_tratte:
            valore_medio=attr["valore_medio"]# dizionario degli attributi dell'arco che contiene il guadagno medio della tratta
            if valore_medio>=valore_costo:
                lista.controls.append(ft.Text(f"[{u.nome}({u.stato}) → {v.nome}({v.stato})], guadagno medio per spedizione: €{valore_medio}"))
                trovata=True
        if not trovata:
            lista.controls.append(ft.Text("Nessuna tratta trovata."))
        self._view.update()

