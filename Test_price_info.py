import price_info
from price_info import cost_of_fruits, price_list
print("test for price info")
def test_total_cost_shopping():
    expected_total_cost = 5 * 1.20 + 5 * 1.40 + 1 * 6.50 + 2 * 2.70 + 10 * 0.90 + 1 * 2.95 + 2 * 4.95
    result=price_info.total_cost_shopping()
    assert(result==expected_total_cost)



def test_cost_of_fruit():
    expected_test_cost_of_fruit=1.20*10
    result=price_info.cost_of_fruits('apple',10)
    assert(result==expected_test_cost_of_fruit)