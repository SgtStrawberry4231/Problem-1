def convert_temperature(temperature, method):
    if method == "C_to_F":
        convert = temperature * 1.8 + 32
    elif method == "F_to_C":
        convert = temperature - 32 * (5/9)
    return convert
print(convert_temperature(32, 'C_to_F'))
print(convert_temperature(100, 'F_to_C'))

