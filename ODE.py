class Euler(object):
    def help(self):
        print """
            y(n+1) = y(n) + h * f(x(n), y(n))
            where,
                h = Step size,
                f(x, y) = Slope at (x, y)
        """

    def get_function(self, func):
        function = func

    def calculate(self, kwargs):
        step_size = kwargs["step"]
        end_time = kwargs["end_time"]
        x0 = kwargs["intial_x"]
        y0 = kwargs["initial_y"]
        iterations = end_time/step_size

        y_old = y0
        x_old = x0
        y_new = 0
        for n in range(0, iterations):
            y_new = y_old + step_size*function(x_old, y_old)
            y_old = y_new
            x_old = x_old + step_size
        return y_new
