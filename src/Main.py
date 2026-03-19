from Cpf import Cpf


class Main:
    def run(self):
        print("Brazilian CPF")

        while True:
            print("Choose an option from menu:")
            print("1. Validate a CPF")
            print("2. Generate a CPF")
            print("3. Generate x CPFs")
            print("0. Exit")

            choice = input("Type a option from menu: ")

            if choice == "1":
                cpf = input("Enter a CPF number: ")
                cpf_validator = Cpf(cpf)
                checked = cpf_validator.validate()

                if checked:
                    print("CPF is valid.")
                else:
                    print("CPF is invalid.")

            elif choice == "2":
                cpf_generator = Cpf("")
                generated_cpf = cpf_generator.generate()
                print(f"\nGenerated CPF: {generated_cpf}\n")

            elif choice == "3":
                try:
                    amount = input("Enter the number of CPFs to generate: ")

                    cpf = Cpf("")
                    generated_cpfs = cpf.generate(int(amount))

                    print()
                    for index, cpf in enumerate(generated_cpfs):
                        print(f"{cpf}")
                    print()

                except ValueError as e:
                    print(f"\nError: {e}\n")

            elif choice == "0":
                print("\nExiting the program.\n")
                break

            else:
                print("\nInvalid choice. Please enter with a value from menu.\n")


if __name__ == "__main__":
    main = Main()
    main.run()
