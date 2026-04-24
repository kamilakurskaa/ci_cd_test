from app import power_ab

def test_power_ab():
  assert power_ab(4, 3) == 64, "4 ** 3 = 64 !!!"
  assert power_ab(3, 4) == 81, "3 ** 4 = 81 !!!"
  print("Success!")

if __name__ == ""__main__":
  test_power_ab()
