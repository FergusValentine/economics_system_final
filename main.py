from economy import Economy

def main():
    economy = Economy()

    for i in range(0, 10):
        economy.execute_turn()

if __name__ == '__main__':
    main()
