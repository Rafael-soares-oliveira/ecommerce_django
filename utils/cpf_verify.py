def main(cpf):
    cpf_filtered_9digits = []
    step1_1 = []
    i1 = 0
    m1 = 10

    while i1 < 9:
        cpf_filtered_9digits.append(cpf[i1])
        cpf_filtered_9digits[i1] = int(cpf_filtered_9digits[i1])
        step1_1.append(cpf_filtered_9digits[i1] * m1)
        i1 += 1
        m1 -= 1

    step2_1 = sum(step1_1)
    step3_1 = step2_1 * 10
    step4_1 = step3_1 % 11
    if step4_1 > 7:
        step5_1 = 0
    else:
        step5_1 = step4_1

    cpf_verified = cpf_filtered_9digits
    cpf_verified.append(step5_1)
    step1_2 = []
    i2 = 0
    m2 = 11

    while i2 < 10:
        cpf_verified[i2] = int(cpf_verified[i2])
        step1_2.append(cpf_verified[i2] * m2)
        i2 += 1
        m2 -= 1

    step2_2 = sum(step1_2)
    step3_2 = step2_2 * 10
    step4_2 = step3_2 % 11
    if step4_2 > 7:
        step5_2 = 0
    else:
        step5_2 = step4_2
    cpf_verified.append(step5_2)

    cpf_test = ''
    for i in range(len(cpf)):
        cpf_test += str(cpf_verified[i])
        i += 1

    if cpf_test == cpf:
        return True
    else:
        return False
