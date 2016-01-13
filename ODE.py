class Euler(object):
    def __init__(self):
        self.function = 0
    def help(self):
        print """
        ===================================================================================================
            y(n+1) = y(n) + h * f(x(n), y(n))
            where,
                h = Step size,
                f(x, y) = Slope at (x, y)

            Usage :
                1) Decorate required function with 'get_function'.
                2) Call method 'calculate' with a dictionary as parameter with the following defined:-
                    a. step
                    b. end_time
                    c. initial_x
                    d. initial_y
        ===================================================================================================
        """

    def set_function(self, func):
        self.function = func

    def calculate(self, kwargs):
        step_size = kwargs["step"]
        end_time = kwargs["end_time"]
        x0 = kwargs["initial_x"]
        y0 = kwargs["initial_y"]
        iterations = end_time/step_size

        y_old = y0
        x_old = x0
        y_new = 0
        for n in range(0, int(iterations)):
            y_new = y_old + step_size*self.function(x_old, y_old)
            y_old = y_new
            x_old = x_old + step_size
        return y_new

def test():
    euler = Euler()

    @euler.set_function
    def test_func(x, y):
        return x

    step = 1
    end_time = 10
    initial_x = 0
    initial_y = 0
    ans = euler.calculate(locals())
    print ans
    euler.help()

if __name__ == '__main__':
    test()
