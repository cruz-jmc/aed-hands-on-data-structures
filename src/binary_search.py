from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = array.get(meio)

        if valor_meio == target:
            return meio
        elif valor_meio > target:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1