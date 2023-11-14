



class MakeDocument:

    def __init__(self):
        pass

    def generate_receipt(self, user_info, service_info, total_income):
        # Создаем оглавление
        receipt = """
                Полет
            Уфа, Башкортостан
        ул, Менделеева, дом 217а
            т. 79196084582
========================================\n"""
        # Добавляем информацию о пользователе
        receipt += (f"Имя: {user_info[1]:>35}\n"
                    f"Фамилия: {user_info[2]:>31}\n"
                    f"Номер телефона: {user_info[3]:>24}\n"
                    f"Почта: {user_info[4]:>33}\n\n")

        receipt += "========================================\n"

        # Добавляем информацию об услугах
        receipt += "Услуги:\n"
        for service in service_info:
            receipt += (f"{service[0]:25}: "
                        f"{service[1]:>8} руб.\n")

        receipt += "========================================\n"

        # Добавляем общую сумму
        receipt += f"\nИтого: {total_income[1]:>28} руб."


        file = open("Out/Receipt/ReceiptVisitor" + str(user_info[0]) + ".txt", 'w')
        file.write(receipt)


    def generate_year_report(self):
        pass