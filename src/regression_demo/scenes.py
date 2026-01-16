from manim import *
from regression_demo.utils import generate_linear_data, generate_nonlinear_data


class RegressionDemo(Scene):
    def construct(self):
        self.intro()
        self.linear_regression()
        self.nonlinear_regression()
        self.outro()

    def intro(self):
        title = Text("Regression in Machine Learning", font_size=48)
        subtitle = Text("Linear vs Nonlinear Models", font_size=32).next_to(title, DOWN)

        authors = Text("Piero Pilco · Juan Diego Luque", font_size=24).to_edge(DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.play(FadeIn(authors))
        self.wait(2)
        self.play(FadeOut(title, subtitle, authors))

    def linear_regression(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-3, 5],
            axis_config={"include_numbers": True},
        )

        x, y = generate_linear_data()
        points = VGroup(
            *[Dot(axes.c2p(x[i], y[i]), radius=0.05) for i in range(len(x))]
        )

        line = axes.plot(lambda t: 0.8 * t + 1, color=YELLOW)

        label = Text("Linear Regression", font_size=32).to_edge(UP)

        self.play(Create(axes))
        self.play(FadeIn(points))
        self.play(Write(label))
        self.wait(1)
        self.play(Create(line))
        self.wait(2)
        self.play(FadeOut(axes, points, line, label))

    def nonlinear_regression(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-2, 6],
            axis_config={"include_numbers": True},
        )

        x, y = generate_nonlinear_data()
        points = VGroup(
            *[Dot(axes.c2p(x[i], y[i]), radius=0.05) for i in range(len(x))]
        )

        curve = axes.plot(lambda t: 0.3 * t**2 - 0.5 * t + 1, color=GREEN)

        label = Text("Nonlinear Regression", font_size=32).to_edge(UP)

        self.play(Create(axes))
        self.play(FadeIn(points))
        self.play(Write(label))
        self.wait(1)
        self.play(Create(curve))
        self.wait(2)
        self.play(FadeOut(axes, points, curve, label))

    def outro(self):
        text = Text(
            "Regression fits models to data\n"
            "Linear models are simple\n"
            "Nonlinear models capture complexity",
            font_size=32,
            line_spacing=1.2,
        )

        self.play(Write(text))
        self.wait(3)
