from .config import app_config
from .utils.math_utils import add, subtract, multiply, divide
 
def main() -> None:
    left = 10
    right = 5
    print(f'{app_config["name"]} v{app_config["version"]}')
    print("10 + 5 =", add(left, right))
    print("10 - 5 =", subtract(left, right))
    print("10 × 5 =", multiply(left, right))
    print("10 ÷ 5 =", divide(left, right))
 
if __name__ == "__main__":
    main()
