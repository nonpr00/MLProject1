from manim import *
from regression_demo.utils import (
    generate_linear_data,
    generate_nonlinear_data,
)


class RegressionDemo(Scene):
    def construct(self):
        self.intro()
        self.supervised_learning()
        self.what_is_regression()
        self.linear_regression()
        self.loss_function()
        self.nonlinear_regression()
        self.training_vs_prediction()
        self.comparison()
        self.outro()

    # ------------------------
    # Intro
    # ------------------------
    def intro(self):
        title = Text("Regression in Machine Learning", font_size=48)
        subtitle = Text("A visual explanation using Manim", font_size=32).next_to(
            title, DOWN
        )

        authors = Text(
            "Piero Pilco · Juan Diego Luque · Tetsuo Momiy",
            font_size=24,
        ).to_edge(DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.play(FadeIn(authors))
        self.wait(2)
        self.play(FadeOut(title, subtitle, authors))

    # ------------------------
    # Supervised learning
    # ------------------------
    def supervised_learning(self):
        text = Text(
            "Regression is a type of\nSupervised Learning",
            font_size=40,
            line_spacing=1.3,
        )

        bullets = BulletedList(
            "We have input-output pairs",
            "The model learns from labeled data",
            "Goal: predict continuous values",
            font_size=28,
        ).next_to(text, DOWN, buff=0.7)

        self.play(Write(text))
        self.play(FadeIn(bullets, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(text, bullets))

    # ------------------------
    # What is regression
    # ------------------------
    def what_is_regression(self):
        text = Text(
            "Regression fits a function\nthat best explains the data",
            font_size=36,
            line_spacing=1.2,
        )

        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

    # ------------------------
    # Linear regression
    # ------------------------
    def linear_regression(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-3, 5],
            axis_config={"include_numbers": True},
        )

        label = Text("Linear Regression", font_size=32).to_edge(UP)

        x, y = generate_linear_data()
        points = VGroup(
            *[Dot(axes.c2p(x[i], y[i]), radius=0.05) for i in range(len(x))]
        )

        m = ValueTracker(-1.5)
        b = ValueTracker(-2.5)

        line = always_redraw(
            lambda: axes.plot(
                lambda t: m.get_value() * t + b.get_value(),
                color=YELLOW,
            )
        )

        equation = always_redraw(
            lambda: MathTex(
                rf"y = {m.get_value():.2f}x + {b.get_value():.2f}"
            ).to_corner(UR)
        )

        self.play(Create(axes), Write(label))
        self.play(FadeIn(points))
        self.wait(1)

        self.add(line, equation)

        self.play(m.animate.set_value(0.8), run_time=3)
        self.wait(1)
        self.play(b.animate.set_value(1.0), run_time=3)
        self.wait(2)

        self.play(FadeOut(axes, points, line, equation, label))

    # ------------------------
    # Loss function
    # ------------------------
    def loss_function(self):
        title = Text("Loss Function", font_size=40).to_edge(UP)

        formula = MathTex(
            r"\text{MSE} = \frac{1}{n}\sum (y - \hat{y})^2",
            font_size=36,
        )

        explanation = Text(
            "Measures how far predictions\nare from real values",
            font_size=28,
            line_spacing=1.2,
        ).next_to(formula, DOWN)

        self.play(Write(title))
        self.play(Write(formula))
        self.play(FadeIn(explanation))
        self.wait(4)
        self.play(FadeOut(title, formula, explanation))

    # ------------------------
    # Nonlinear regression
    # ------------------------
    def nonlinear_regression(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-2, 6],
            axis_config={"include_numbers": True},
        )

        label = Text("Nonlinear Regression", font_size=32).to_edge(UP)

        x, y = generate_nonlinear_data()
        points = VGroup(
            *[Dot(axes.c2p(x[i], y[i]), radius=0.05) for i in range(len(x))]
        )

        bad_line = axes.plot(lambda t: 0.5 * t + 1, color=RED)
        curve = axes.plot(
            lambda t: 0.3 * t**2 - 0.5 * t + 1,
            color=GREEN,
        )

        self.play(Create(axes), Write(label))
        self.play(FadeIn(points))
        self.wait(1)

        self.play(Create(bad_line))
        self.wait(2)

        self.play(Transform(bad_line, curve), run_time=3)
        self.wait(2)

        self.play(FadeOut(axes, points, bad_line, label))

    # ------------------------
    # Training vs Prediction
    # ------------------------
    def training_vs_prediction(self):
        text = Text(
            "Training vs Prediction",
            font_size=40,
        )

        bullets = BulletedList(
            "Training: adjust parameters",
            "Prediction: use learned model",
            font_size=28,
        ).next_to(text, DOWN, buff=0.7)

        self.play(Write(text))
        self.play(FadeIn(bullets))
        self.wait(4)
        self.play(FadeOut(text, bullets))

    # ------------------------
    # Comparison
    # ------------------------
    def comparison(self):
        text = Text(
            "Linear models are simple\nNonlinear models are more expressive",
            font_size=36,
            line_spacing=1.2,
        )

        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

    # ------------------------
    # Outro
    # ------------------------
    def outro(self):
        text = Text(
            "Regression is a fundamental tool\nin Machine Learning",
            font_size=36,
            line_spacing=1.2,
        )

        self.play(Write(text))
        self.wait(4)
