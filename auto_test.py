class AutoTests:
    @staticmethod
    def test_reg_ex_funcs(f, in_, expected):
        # in_ must be a value or a list of values that are expected in the function(f) in the right order.
        try:
            if isinstance(in_, list):
                out = f(*in_)
            else:
                out = f(in_)

            if out == expected:
                sign = '✅'
                info = ''
            else:
                sign = '❌'
                info = f'but the expected value was: {expected}'

            print(f'{sign} {f.__name__}{in_} returned {out} {info}')

        except TypeError as e:
            print(f'{e}: The input(s) for the test function must be a value or a list of values!')
