from economy import Economy
from agents_builder import CreateConsumer, CreateProducer, CreateFactory, CreateAppliance
from product_list import Product
from trade_strategy import ConsumptionStrategy, ProducerStrategy

def main():
    economy = Economy()
    agents = []

    for i in range(0, 100):
        consumer = ((CreateConsumer()
                    .set_money(10)
                    .add_demand(Product("Bread", 1)))
                    .set_trade_strategy(ConsumptionStrategy())
                    .build())
        agents.append(consumer)

    bakery1 = (CreateProducer()
             .set_money(10)
             .set_supply(Product("Bread", 1))
             .add_demand(Product("Grain", 2))
             .set_factory(
                CreateFactory()
                    .set_labor(0)
                    .set_efficiency(2)
                    .set_wages(10)
                    .add_appliance(
                        CreateAppliance(2, 20)
                        .build())
                    .build())
             .set_trade_strategy(ProducerStrategy())
             .build())
    agents.append(bakery1)

    farm1 = (CreateProducer()
            .set_money(10)
            .set_supply(Product("Grain", 1))
            .set_factory(
                CreateFactory()
                    .set_labor(0)
                    .set_efficiency(2)
                    .set_wages(10)
                    .add_appliance(
                        CreateAppliance(2, 20)
                        .build())
                    .build())
            .set_trade_strategy(ProducerStrategy())
            .build())
    agents.append(farm1)

    farm2 = (CreateProducer()
             .set_money(10)
             .set_supply(Product("Grain", 1))
             .set_factory(
                CreateFactory()
                .set_labor(0)
                .set_efficiency(2)
                .set_wages(10)
                .add_appliance(
                    CreateAppliance(2, 20)
                    .build())
                .build())
             .set_trade_strategy(ProducerStrategy())
             .build())
    agents.append(farm2)

    for agent in agents:
        economy.register_agent(agent)

    for i in range(0, 10):
        economy.execute_turn()

if __name__ == '__main__':
    main()
