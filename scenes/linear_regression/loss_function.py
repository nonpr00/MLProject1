from manim import *

class LossFunctionScene(Scene):
    def construct(self):
        # Configuración inicial
        self.setup_data()
        self.setup_scene()
        self.show_initial_state()
        # self.demonstrate_parameter_change()
        self.perform_gradient_descent()

    def setup_data(self):
        """Inicializa datos y parámetros"""
        self.data = np.array([
            [1, 1.2], [2, 2.1], [3, 2.9],
            [4, 4.1], [5, 5.0]
        ])
        self.w = 0.6
        self.b = 0.6
        self.learning_rate = 0.1

    def setup_scene(self):
        """Crea los elementos visuales principales"""
        # Título
        self.title = Text("Función de Pérdida: Ajuste de Línea",
                          font_size=36, color=BLUE)
        self.play(Write(self.title))
        self.play(self.title.animate.to_edge(UP))

        # Ejes
        self.axes = Axes(
            x_range=[0, 6], y_range=[0, 6],
            x_length=7, y_length=5,
            axis_config={"color": BLUE}
        ).shift(DOWN * 0.5)
        self.play(Create(self.axes))

        # Puntos de datos
        self.dots = VGroup(*[
            Dot(self.axes.c2p(x, y), color=BLUE, radius=0.08)
            for x, y in self.data
        ])

        # UI panels
        self.create_ui_panels()

    def create_ui_panels(self):
        """Crea los paneles de información lateral"""
        # Panel de pérdida
        loss_text = Text("Función de Pérdida:", font_size=28, color=YELLOW)
        self.loss_eq = MathTex(
            r"J(w,b) = \frac{1}{2n}\sum_{i=1}^n (y_i - \hat{y}_i)^2",
            font_size=28
        )
        self.loss_label = MathTex("J(w,b) =", font_size=28, color=YELLOW)
        #self.loss_value = DecimalNumber(0, num_decimal_places=4,
        self.loss_value = DecimalNumber(self.calculate_loss(self.w, self.b), num_decimal_places=4,
                                                                        font_size=28, color=YELLOW)
        self.loss_formula = VGroup(self.loss_label, self.loss_value).arrange(RIGHT, buff=0.15)

        self.loss_group = VGroup(loss_text, self.loss_eq, self.loss_formula).arrange(
            DOWN, aligned_edge=LEFT
        ).to_edge(RIGHT, buff=0.5)

        # Panel de gradientes
        grad_title = Text("Derivadas de la pérdida", font_size=28, color=BLUE)
        self.grad_w_formula = MathTex(
            r"\frac{\partial J}{\partial w} = \frac{1}{n}\sum ( \hat{y}_i - y_i )x_i",
            font_size=26
        )
        self.grad_b_formula = MathTex(
            r"\frac{\partial J}{\partial b} = \frac{1}{n}\sum ( \hat{y}_i - y_i )",
            font_size=26
        )
        self.grad_group = VGroup(
            grad_title, self.grad_w_formula, self.grad_b_formula
        ).arrange(DOWN, aligned_edge=LEFT).next_to(self.loss_group, DOWN, buff=0.4)

        self.grad_values = MathTex(
            r"\nabla J = (", "0.00", ",", "0.00", ")",
            #r"\nabla J = (", "0.00", ",", "0.00", ")",
            font_size=26, color=YELLOW
        ).next_to(self.grad_group, DOWN, buff=0.3)

        # Panel de parámetros
        param_text = Text("Parámetros:", font_size=28, color=GREEN)
        self.w_text = Text(f"w (pendiente) = {self.w:.2f}", font_size=24)
        self.b_text = Text(f"b (intersección) = {self.b:.2f}", font_size=24)
        self.param_group = VGroup(
            param_text, self.w_text, self.b_text
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=0.5)

    def show_initial_state(self):
        """Muestra el estado inicial con la primera línea"""
        # Línea inicial
        self.line = self.create_line(self.w, self.b, RED)
        self.play(Create(self.line), FadeIn(self.dots))

        # Errores iniciales
        self.errors = self.create_error_lines(self.w, self.b)
        self.play(Create(self.errors))

        # Mostrar UI
        self.play(Write(self.loss_group))
        self.play(Write(self.param_group))
        self.wait(0.5)

        self.show_loss_and_gradient_calculation_stepwise()
        # === CÁLCULO PASO A PASO DE J ===
        #self.show_loss_calculation_stepwise()

        # Mostrar panel de gradientes
        #self.play(Write(self.grad_group))
        #self.wait(0.5)

        # === CÁLCULO PASO A PASO DE dw y db ===
        #self.show_gradient_calculation_stepwise()

        self.wait(1)

    def show_loss_and_gradient_calculation_stepwise(self):
    #def show_loss_calculation_stepwise(self):
        """Muestra el cálculo paso a paso de la función de pérdida"""
        # Hacer desaparecer la ecuación general
        self.play(FadeOut(self.loss_group))
        #self.play(FadeOut(self.loss_eq))

        # Calcular errores individuales
        errors_squared = []
        calc_steps = []

        for i, (x, y) in enumerate(self.data):
            y_hat = self.w * x + self.b
            error = y - y_hat
            error_sq = error ** 2
            errors_squared.append(error_sq)

            # Crear texto para cada término
            step = MathTex(
                f"(y_{i + 1} - \\hat{{y}}_{i + 1})^2 = ({y:.1f} - {y_hat:.2f})^2 = {error_sq:.4f}",
                font_size=20
            )
            calc_steps.append(step)

        # Posicionar los pasos
        calc_group = VGroup(*calc_steps).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        calc_group.next_to(self.loss_group[0], DOWN, buff=0.3)

        # Mostrar cada paso
        for step in calc_steps:
            self.play(Write(step), run_time=0.4)

        self.wait(0.5)

        # Mostrar la suma y división
        sum_errors = sum(errors_squared)
        final_loss = sum_errors / (2 * len(self.data))

        sum_calc = MathTex(
            f"J = \\frac{{1}}{{2n}} \\sum = \\frac{{1}}{{10}} ({sum_errors:.4f}) = {final_loss:.4f}",
            font_size=22,
            color=YELLOW
        ).next_to(calc_group, DOWN, buff=0.3)

        self.play(Write(sum_calc))
        self.wait(1)

        # Actualizar el valor en el display
        self.loss_value.set_value(final_loss)

        # Hacer que los cálculos desaparezcan y vuelva la ecuación
        self.play(
            FadeOut(calc_group),
            FadeOut(sum_calc),
            #FadeIn(self.loss_eq)
        )

        """Muestra el cálculo paso a paso de los gradientes"""
        # Hacer desaparecer las ecuaciones generales
        #self.play(FadeOut(self.grad_w_formula), FadeOut(self.grad_b_formula))
        #self.play(FadeOut(self.loss_group))

        #self.play(FadeOut(self.loss_group), run_time=0.6)

        # === CÁLCULO DE dw ===
        dw_title = Text("Cálculo de ∂J/∂w:", font_size=24, color=BLUE)
        dw_steps = []
        dw_terms = []

        for i, (x, y) in enumerate(self.data):
            y_hat = self.w * x + self.b
            term = (y_hat - y) * x
            dw_terms.append(term)

            step = MathTex(
                f"(\\hat{{y}}_{i + 1} - y_{i + 1}) \\cdot x_{i + 1} = ({y_hat:.2f} - {y:.1f}) \\cdot {x:.0f} = {term:.4f}",
                font_size=18
            )
            dw_steps.append(step)

        dw_calc_group = VGroup(dw_title, *dw_steps).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        dw_calc_group.next_to(self.grad_group[0], DOWN, buff=0.3)

        self.play(Write(dw_title))
        for step in dw_steps:
            self.play(Write(step), run_time=0.3)

        # Resultado de dw
        dw_value = sum(dw_terms) / len(self.data)
        dw_result = MathTex(
            f"\\frac{{\\partial J}}{{\\partial w}} = \\frac{{1}}{{n}} \\sum = \\frac{{1}}{{{len(self.data)}}} ({sum(dw_terms):.4f}) = {dw_value:.4f}",
            font_size=20,
            color=YELLOW
        ).next_to(dw_calc_group, DOWN, buff=0.2)

        self.play(Write(dw_result))
        self.wait(1)

        # === CÁLCULO DE db ===
        self.play(FadeOut(dw_calc_group), FadeOut(dw_result))
        #self.play(FadeOut(self.loss_group))


        db_title = Text("Cálculo de ∂J/∂b:", font_size=24, color=BLUE)
        db_steps = []
        db_terms = []

        for i, (x, y) in enumerate(self.data):
            y_hat = self.w * x + self.b
            term = y_hat - y
            db_terms.append(term)

            step = MathTex(
                f"(\\hat{{y}}_{i + 1} - y_{i + 1}) = {y_hat:.2f} - {y:.1f} = {term:.4f}",
                font_size=18
            )
            db_steps.append(step)

        db_calc_group = VGroup(db_title, *db_steps).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        db_calc_group.next_to(self.grad_group[0], DOWN, buff=0.3)

        self.play(Write(db_title))
        for step in db_steps:
            self.play(Write(step), run_time=0.3)

        # Resultado de db
        db_value = sum(db_terms) / len(self.data)
        db_result = MathTex(
            f"\\frac{{\\partial J}}{{\\partial b}} = \\frac{{1}}{{n}} \\sum = \\frac{{1}}{{{len(self.data)}}} ({sum(db_terms):.4f}) = {db_value:.4f}",
            font_size=20,
            color=YELLOW
        ).next_to(db_calc_group, DOWN, buff=0.2)

        self.play(Write(db_result))
        self.wait(1)

        # Actualizar valores del gradiente
        new_grad_values = MathTex(
            r"\nabla J = (", f"{dw_value:.4f}", ",", f"{db_value:.4f}", ")",
            font_size=26, color=YELLOW
        ).move_to(self.grad_values)

        self.play(Transform(self.grad_values, new_grad_values))

        # Hacer que los cálculos desaparezcan y vuelvan las ecuaciones
        self.play(
            FadeOut(db_calc_group),
            FadeOut(db_result),
            FadeIn(self.grad_w_formula),
            FadeIn(self.grad_b_formula)
        )

        self.play(FadeIn(self.loss_group), run_time=0.6)

    def demonstrate_parameter_change(self):
        """Demuestra el efecto de cambiar solo w"""
        self.play(FadeOut(self.errors), run_time=0.5)

        # Nuevos parámetros
        new_w, new_b = 1.0, 0.6
        old_loss = self.calculate_loss(self.w, self.b)

        # Actualizar visualización
        self.update_line_and_params(new_w, new_b, RED)

        # Mostrar nuevos errores
        new_errors = self.create_error_lines(new_w, new_b)
        self.play(Create(new_errors), run_time=1.5)

        # Notificación de cambio
        new_loss = self.calculate_loss(new_w, new_b)
        change_text = Text(
            f"¡La pérdida aumentó en {new_loss - old_loss:.3f}!",
            font_size=24, color=RED
        ).next_to(self.loss_group, DOWN, buff=0.5)

        self.play(Write(change_text))
        self.wait(1)
        self.play(FadeOut(change_text))

        # Restaurar parámetros iniciales para gradient descent
        self.update_line_and_params(self.w, self.b, RED)
        self.errors = self.create_error_lines(self.w, self.b)
        self.play(FadeOut(new_errors), Create(self.errors))

        self.wait(1)

    def perform_gradient_descent(self):
        """Ejecuta el descenso por gradiente"""
        update_rule = MathTex(
            r"\begin{aligned}"
            r"w &\leftarrow w - \alpha \frac{\partial J}{\partial w} \\"
            r"b &\leftarrow b - \alpha \frac{\partial J}{\partial b}"
            r"\end{aligned}",
            font_size=26
        ).next_to(self.grad_values, DOWN, buff=0.3)
        self.play(Write(update_rule))

        steps = 5
        for step in range(steps):
            # Calcular gradientes
            dw = self.gradient_w(self.w, self.b)
            db = self.gradient_b(self.w, self.b)

            new_grad_values = MathTex(
                r"\nabla J = (", f"{dw:.4f}", ",", f"{db:.4f}", ")",
                font_size=26, color=YELLOW
            ).move_to(self.grad_values)

            #self.play(Transform(self.grad_values, new_grad_values))
            self.grad_values.become(new_grad_values)

            # Actualizar parámetros
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

            # Animar cambios
            self.animate_gradient_step()

        self.wait(3)

    def animate_gradient_step(self):
        """Anima un paso del descenso por gradiente"""
        new_line = self.create_line(self.w, self.b, GREEN)
        new_errors = self.create_error_lines(self.w, self.b)

        # Actualizar textos
        new_w_text = Text(
            f"w (pendiente) = {self.w:.3f}", font_size=24
        ).move_to(self.w_text)
        new_b_text = Text(
            f"b (intersección) = {self.b:.3f}", font_size=24
        ).move_to(self.b_text)

        #new_loss_value = DecimalNumber(
        #    self.calculate_loss(self.w, self.b),
        #    num_decimal_places=4, color=GREEN
        #)
        new_loss_value = DecimalNumber(self.calculate_loss(self.w, self.b), num_decimal_places=4,
                                        font_size=28, color=YELLOW)
        new_loss_formula = VGroup(
            self.loss_label, new_loss_value
        ).arrange(RIGHT, buff=0.15).move_to(
            #VGroup(self.loss_label, self.loss_value)
            self.loss_formula
        )

        # Animación conjunta
        self.play(
            Transform(self.line, new_line),
            Transform(self.w_text, new_w_text),
            Transform(self.b_text, new_b_text),
            Transform(self.loss_formula, new_loss_formula),
            #Transform(VGroup(self.loss_label, self.loss_value), new_loss_formula),
            FadeOut(self.errors),
            run_time=1.2
        )

        self.play(Create(new_errors), run_time=0.8)
        self.errors = new_errors

    # Métodos auxiliares
    def create_line(self, w, b, color):
        """Crea una línea con los parámetros dados"""
        return self.axes.plot(lambda x: w * x + b, color=color, stroke_width=3)

    def create_error_lines(self, w, b):
        """Crea líneas de error para todos los puntos"""
        errors = VGroup()
        for x, y in self.data:
            y_hat = w * x + b
            errors.add(DashedLine(
                self.axes.c2p(x, y),
                self.axes.c2p(x, y_hat),
                color=YELLOW, stroke_width=2
            ))
        return errors

    def update_line_and_params(self, w, b, color):
        """Actualiza línea y parámetros en pantalla"""
        new_line = self.create_line(w, b, color)
        new_w_text = Text(
            f"w (pendiente) = {w:.2f}", font_size=24
        ).move_to(self.w_text)

        self.update_loss_display(w, b)
