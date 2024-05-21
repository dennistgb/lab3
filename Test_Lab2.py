from lab2 import lab2 as lab2

def test_min_max():
    result = []
    input_arr = ["1","100","111"]
    ans = ['max = 111', 'min = 1']
    result = lab2.calc_min_max_temperature(input_arr)

    assert (result == ans)

def test_avg():
    result = []
    input_arr = ["3","4","5"]
    result = lab2.calc_average_temperature(input_arr)

    assert (result == 4.0)

def test_median():
    input_arr = ["1","100","111"]
    result = lab2.median_temp(input_arr)

    assert (result == 100)
