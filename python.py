from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon="2226979.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
    
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1),
                                 multiline=False, halign="right", font_size=55, readonly=True)

        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=32, background_color=(0.5, 0.5, 0.5, 1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            equal_backspace_layout = BoxLayout(orientation="horizontal", spacing=10)


        backspace_button = Button(
                  text="<--", font_size=32, background_color=(0.5, 0.5, 0.5, 1), )
        backspace_button.bind(on_press=self.on_backspace)
        main_layout.add_widget(backspace_button)
        
        equal_button = Button(
            text="=", font_size=32, background_color=(0.5, 0.5, 0.5, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

       
        

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
                self.last_button = button_text
                self.last_was_operator = self.last_button in self.operators
    def on_backspace(self, instance):
         current = self.solution.text
         if current:
               self.solution.text = current[:-1]
    def on_solution(self, instance):
        text = self.solution.text
        if text and not self.last_was_operator:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

    

if __name__ == "main":
    app = MainApp()
    app.run()
