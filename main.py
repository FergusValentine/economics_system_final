from economy import Economy
from agent_builder import ConsumerBuilder, TransformerBuilder
from agent_supply_demand import Product

def main():
    economy = Economy()

    for i in range(0, 100):
        name = "actor" + str(i)
        consumer = (ConsumerBuilder(name)
            .add_demands(Product("bread", 1)).build())
        economy.register_consumer(consumer)

    bakery1 = (TransformerBuilder("bakery")
        .add_demands(Product("grain", 2))
        .add_supply(Product("bread", 1))).build()

    economy.register_transformer(bakery1)

    for i in range(0, 10):
        economy.execute_turn()

if __name__ == '__main__':
    main()
