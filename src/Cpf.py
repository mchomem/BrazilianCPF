from random import randint


class Cpf:
    def __init__(self, cpf: str):
        self.cpf = cpf

    def validate(self) -> bool:
        if not self.__check_cpf():
            return False

        sanitized_cpf = self.__sanitize_cpf()
        check_first_digit = self.__calculate_check_digits(sanitized_cpf)
        check_second_digit = self.__calculate_check_digits(f"{sanitized_cpf}{check_first_digit}")

        penultimate_digit = self.cpf[-2]
        last_digit = self.cpf[-1]

        if (
            check_first_digit != penultimate_digit or check_second_digit != last_digit
        ):  # Check if the calculated check digits match the last two digits of the original CPF
            return False

        return True

    def generate(self) -> str:
        cpf = ""

        for _ in range(9):
            cpf += str(randint(0, 9))

        first_check_digit = self.__calculate_check_digits(cpf)
        second_check_digit = self.__calculate_check_digits(f"{cpf}{first_check_digit}")
        cpf = f"{cpf}{first_check_digit}{second_check_digit}"

        return cpf

    def generate(self, amount: int) -> list:
        if amount <= 0 or amount is None or amount > 1001:
            raise ValueError("Amount must be a positive integer between 1 and 1000.")

        list_of_cpfs = []

        for _ in range(amount):

            cpf = ""

            for _ in range(9):
                cpf += str(randint(0, 9))

            first_check_digit = self.__calculate_check_digits(cpf)
            second_check_digit = self.__calculate_check_digits(f"{cpf}{first_check_digit}")
            cpf = f"{cpf}{first_check_digit}{second_check_digit}"
            list_of_cpfs.append(cpf)

        return list_of_cpfs

    def __check_cpf(self) -> bool:
        # Check if the CPF is empty, null, has less than 11 characters, or contains non-digit characters
        if self.cpf == "" or self.cpf is None or len(self.cpf) < 11 or self.cpf.isdigit() == False:
            return False

        return True

    def __sanitize_cpf(self) -> str:
        # Remove dots and dashes from the CPF string
        sanitized_cpf = self.cpf.strip().replace(".", "").replace("-", "")

        # Remove the last two digits (check digits)
        sanitized_cpf = sanitized_cpf[:-2]

        return sanitized_cpf

    def __calculate_check_digits(self, cpf_numbers: str) -> str:
        assistant = 11 if len(cpf_numbers) == 10 else 10
        calculated_sum = 0
        first_check_digit = 0

        for digit in cpf_numbers:
            calculated_sum += int(digit) * (assistant)
            assistant -= 1

        if calculated_sum % 11 < 2:
            first_check_digit = 0
        else:
            first_check_digit = 11 - (calculated_sum % 11)

        return str(first_check_digit)
