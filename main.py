from economy import Economy
from agents_builder import CreateConsumer, CreateProducer, CreateFactory, CreateAppliance
from product_list import Product
from market_strategy import ConsumerStrategy, ProducerStrategy

import matplotlib.pyplot as plt
import numpy as np

def main():
    economy = Economy()
    agents = []

    for i in range(0, 5):
        consumer = ((CreateConsumer()
                    .set_money(10)
                    .add_demand(Product("Bread", 1)))
                    .set_market_strategy(ConsumerStrategy())
                    .build())
        agents.append(consumer)

    bakery1 = (CreateProducer()
             .set_money(50)
             .set_supply(Product("Bread", 1))
             .add_demand(Product("Grain", 2))
             .set_factory(
                CreateFactory()
                    .set_efficiency(4)
                    .set_wages(10)
                    .add_appliance(
                        CreateAppliance(2, 40)
                        .build())
                    .build())
             .set_market_strategy(ProducerStrategy())
             .build())
    agents.append(bakery1)

    farm1 = (CreateProducer()
            .set_money(10)
            .set_price(1)
            .set_supply(Product("Grain", 2))
            .set_factory(
                CreateFactory()
                    .set_labor(0)
                    .set_efficiency(4)
                    .set_wages(10)
                    .add_appliance(
                        CreateAppliance(2, 20)
                        .build())
                    .build())
            .set_market_strategy(ProducerStrategy())
            .build())
    agents.append(farm1)

    for agent in agents:
        economy.register_agent(agent)

    for i in range(0, 100):
        economy.execute_turn()

    snapshots = economy.get_market_history()

    for category_name, category in snapshots.items():
        if category_name == "Consumer":
            continue

        for sections in category.values():
            figure, axes = plt.subplots(2, 2)
            i = 0
            for section, subsections in sections.items():
                for subsection, values in subsections.items():
                    x = i//2
                    y = i%2

                    axes[x, y].plot(values, label=subsection)
                    axes[x, y].set_title(section)
                    axes[x, y].legend()
                    axes[x, y].grid(True)
                i += 1

            plt.grid()
            plt.show()

if __name__ == '__main__':
    main()
