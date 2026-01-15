from manim import *

class LossFunctionScene(Scene):
    def construct(self):
        # Título
        title = Text("Función de Pérdida: Ajuste de Línea", font_size=36, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Ejes
        axes = Axes(
            x_range=[0, 6],
            y_range=[0, 6],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE}
        ).shift(DOWN * 0.5)

        self.play(Create(axes))

        # Datos
        data = np.array([
            [1, 1.2], [2, 2.1], [3, 2.9],
            [4, 4.1], [5, 5.0]
        ])

        # Puntos
        dots = VGroup(*[
            Dot(axes.c2p(x, y), color=BLUE, radius=0.08)
            for x, y in data
        ])

        # Parámetros iniciales
        w = 0.6
        b = 0.6

        # Línea inicial
        line = axes.plot(lambda x: w * x + b, color=RED, stroke_width=3)

        self.play(Create(line), FadeIn(dots))

        # Mostrar errores iniciales
        errors = VGroup()
        for x, y in data:
            y_hat = w * x + b
            error_line = DashedLine(
                axes.c2p(x, y),
                axes.c2p(x, y_hat),
                color=YELLOW,
                stroke_width=2
            )
            errors.add(error_line)

        self.play(Create(errors))


        # Función para calcular pérdida
        def calculate_loss(w_val, b_val):
            total = 0
            for x, y in data:
                y_pred = w_val * x + b_val
                total += (y - y_pred) ** 2
            return total / (2 * len(data))

        # Display de pérdida
        loss_text = Text("Función de Pérdida:", font_size=28, color=YELLOW)
        loss_eq = MathTex(r"J(w,b) = \frac{1}{2n}\sum_{i=1}^n (y_i - \hat{y}_i)^2", font_size=28)

        # valor de loss_val
        loss_preformula = MathTex(
            r"J(w,b) =",
            font_size=28,
            color=YELLOW
        )

        loss_value = DecimalNumber(
            calculate_loss(w, b),
            num_decimal_places=4,
            font_size=28,
            color=YELLOW
        )

        loss_formula = VGroup(loss_preformula, loss_value).arrange(RIGHT, buff=0.15)

        loss_group = VGroup(loss_text, loss_eq, loss_formula).arrange(DOWN, aligned_edge=LEFT)
        #loss_group = VGroup(loss_text, loss_eq, loss_value).arrange(DOWN, aligned_edge=LEFT)
        loss_group.to_edge(RIGHT, buff=0.5)

        self.play(Write(loss_group))

        # Display de parámetros
        param_text = Text("Parámetros:", font_size=28, color=GREEN)
        w_text = Text(f"w (pendiente) = {w:.2f}", font_size=24)
        b_text = Text(f"b (intersección) = {b:.2f}", font_size=24)

        param_group = VGroup(param_text, w_text, b_text).arrange(DOWN, aligned_edge=LEFT)
        param_group.to_edge(LEFT, buff=0.5)

        self.play(Write(param_group))

        self.wait(1)

        # Animación 1: Cambiar solo la pendiente
        self.play(
            FadeOut(errors),
            run_time=0.5
        )

        # Nueva línea con w diferente
        new_w = 1.0
        new_b = 0.6
        new_line = axes.plot(lambda x: new_w * x + new_b, color=RED, stroke_width=3)

        # Actualizar texto de w
        new_w_text = Text(f"w (pendiente) = {new_w:.2f}", font_size=24)
        new_w_text.move_to(w_text)

        # Nuevos errores
        new_errors = VGroup()
        for x, y in data:
            y_hat = new_w * x + new_b
            error_line = DashedLine(
                axes.c2p(x, y),
                axes.c2p(x, y_hat),
                color=YELLOW,
                stroke_width=2
            )
            new_errors.add(error_line)

        # Nueva pérdida
        new_loss = calculate_loss(new_w, new_b)
        new_loss_value = DecimalNumber(
            new_loss,
            num_decimal_places=4,
            color=YELLOW
        )

        new_loss_formula = VGroup(loss_preformula, new_loss_value).arrange(RIGHT, buff=0.15)
        new_loss_formula.move_to(loss_formula)
        #new_loss_value.move_to(loss_value)

        # Transformar
        self.play(
            Transform(line, new_line),
            Transform(w_text, new_w_text),
            Transform(loss_formula, new_loss_formula),
            #Transform(loss_value, new_loss_value),
            run_time=2
        )

        # Mostrar nuevos errores
        self.play(Create(new_errors), run_time=1.5)

        # Mostrar cómo cambió la pérdida
        change_text = Text(
            f"¡La pérdida aumentó en {new_loss - calculate_loss(0.6, 0.6):.3f}!",
            font_size=24,
            color=RED
        ).next_to(loss_group, DOWN, buff=0.5)

        self.play(Write(change_text))
        self.wait(1)
        self.play(FadeOut(change_text))

        self.wait(1)

        # Animación 2: Mejorar el ajuste
        self.play(FadeOut(new_errors), run_time=0.5)

        # Nueva línea mejor ajustada
        better_w = 0.95
        better_b = 0.1
        better_line = axes.plot(lambda x: better_w * x + better_b, color=GREEN, stroke_width=3)

        # Actualizar textos
        better_w_text = Text(f"w (pendiente) = {better_w:.2f}", font_size=24)
        better_w_text.move_to(w_text)

        better_b_text = Text(f"b (intersección) = {better_b:.2f}", font_size=24)
        better_b_text.move_to(b_text)


        # Nuevos errores
        better_errors = VGroup()
        for x, y in data:
            y_hat = better_w * x + better_b
            error_line = DashedLine(
                axes.c2p(x, y),
                axes.c2p(x, y_hat),
                color=YELLOW,
                stroke_width=2
            )
            better_errors.add(error_line)

        # Nueva pérdida
        better_loss = calculate_loss(better_w, better_b)
        better_loss_value = DecimalNumber(
            better_loss,
            num_decimal_places=4,
            color=GREEN
        )
        better_loss_formula = VGroup(loss_preformula, better_loss_value).arrange(RIGHT, buff=0.15)
        better_loss_formula.move_to(loss_formula)

        # Transformar
        self.play(
            Transform(line, better_line),
            Transform(w_text, better_w_text),
            Transform(b_text, better_b_text),
            Transform(loss_formula, better_loss_formula),
            #Transform(loss_value, better_loss_value),
            run_time=2
        )

        # Mostrar nuevos errores
        self.play(Create(better_errors), run_time=1.5)

        # Mostrar mejora
        improvement_text = Text(
            f"¡La pérdida disminuyó en {calculate_loss(1.0, 0.6) - better_loss:.3f}!",
            font_size=24,
            color=GREEN
        ).next_to(loss_group, DOWN, buff=0.5)

        self.play(Write(improvement_text))
        self.wait(1)

        # Mostrar resumen
        summary_box = Rectangle(
            width=5, height=2.5,
            color=WHITE, stroke_width=2
        ).next_to(improvement_text, DOWN, buff=0.5)

        summary_text = Text(
            "La función de pérdida J(w,b) mide\n"
            "la distancia de los puntos a la linea.\n",
            #"↓ J(w,b) = mejor ajuste",
            font_size=2,
            color=YELLOW
        ).move_to(summary_box)

        self.play(Create(summary_box), Write(summary_text))

        self.wait(3)

        # Final: Mostrar valores numéricos de errores
        self.play(
            FadeOut(summary_box),
            FadeOut(summary_text),
            FadeOut(improvement_text),
            run_time=0.5
        )

        # Mostrar valores de error para cada punto
        error_values = VGroup()
        for i, (x, y) in enumerate(data):
            y_hat = better_w * x + better_b
            error = abs(y - y_hat)
            error_val = Text(
                f"e{i + 1} = {error:.2f}",
                font_size=18,
                color=YELLOW
            ).next_to(dots[i], UP, buff=0.1)
            error_values.add(error_val)

        self.play(FadeIn(error_values), run_time=2)

        # Mostrar cálculo final de pérdida
        final_calc = MathTex(
            r"J = \frac{1}{10}(",
            r"+".join([f"{error ** 2:.2f}" for error in [abs(y - (better_w * x + better_b)) for x, y in data]]),
            r") =",
            f"{better_loss:.4f}",
            font_size=24
        ).next_to(loss_group, DOWN, buff=0.5)

        self.play(Write(final_calc))

        self.wait(3)
