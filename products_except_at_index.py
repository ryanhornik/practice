def products_except_at_index(data):
    result_left = [1]*len(data)
    for i in range(1, len(data)):
        result_left[i] *= data[i - 1] * result_left[i - 1]

    result_right = [1]*len(data)
    for j in range(len(data) - 2, -1, -1):
        result_right[j] *= data[j + 1] * result_right[j + 1]

    result = []
    for k in range(0, len(data)):
        result.append(result_left[k]*result_right[k])
    return result

sorted([1, 2, 3], reverse=True)

if __name__ == "__main__":
    print(products_except_at_index([1, 2, 6, 0, 9]))
