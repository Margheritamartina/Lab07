import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._dd_musei=ft.Dropdown(labe='Musei',
                                   options=[],#come opzioni vanno tutti i nomi dei musei del database
                                   width=200,
                                   hint_text="Seleziona un museo")
        self._dd_epoca = ft.Dropdown(labe='Epoca',
                                     options=[],
                                     width=200,
                                     hint_text="Seleziona un'epoca")

        # Sezione 3: Artefatti

        self.pulsante_mostra_artefatti=ft.ElevatedButton(text="Mostra Artefatti",on_click=self._on_click_mostra_artefatti)

        self.lista_artefatti=ft.Column(spacing=10,scroll=ft.ScrollMode.AUTO)
        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
               [
                   self.dd_musei,
                   self._dd_epoca,
                   self._pulsante_mostra_artefatti
               ],
               alignment=ft.MainAxisAlignment.CENTER,
               spacing=20
            ),

            ft.Divider(),

            # Sezione 3: Artefatti

            ft.Text("Elenco Artefatti", size=24, weight=ft.FontWeight.BOLD),
            self._lista_artefatti
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
