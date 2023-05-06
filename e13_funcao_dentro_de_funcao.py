def multiplica(multiplicador):
    def duplica(num):
        return num * multiplicador
    return duplica

duplicar_num = multiplica(2)
triplicar_num = multiplica(3)
quadruplipacar_num = multiplica(4)

print(quadruplipacar_num(8))