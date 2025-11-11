import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
        self._popola_dropdown_musei()
        self._popola_dropdown_epoche()
    def _popola_dropdown_musei(self):
        musei=self._model.get_musei()
        self._view._dd_musei.options=[ft.dropdown.Option("Nessun filtro")]

        for museo in musei:
            self._view._dd_musei.options.append(ft.dropdown.Option(museo.nome))
        self._view._dd_musei.on_change=self._on_museo_change

    def _popola_dropdown_epoche(self):
        epoche=self._model.get_epoche()

        self._view._dd_epoca.options=[ft.dropdown.Option("Nessun filtro")]

        for epoca in epoche:
            self._view._dd_epoca.options.append(ft.dropdown.Option(epoca))
        self._view._dd_epoca.on_change=self.on_epoca_change

    # CALLBACKS DROPDOWN
    def _on_museo_change(self,e):
        self.museo_selezionato=e.control.value
    def on_epoca_change(self,e):
        self.epoca_selezionato=e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self):
        artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)

        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato con i filtri selezionati")
            return

        self._view._lista_artefatti.controls.clear()

            for a in artefatti:
                item = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(a.nome, size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Tipologia: {a.tipologia}"),
                                ft.Text(f"Epoca: {a.epoca}"),
                            ]
                        ),
                        padding=10,
                    )
                )
                self._view._lista_artefatti.controls.append(item)

            # Aggiorna la pagina
            self._view.update()



