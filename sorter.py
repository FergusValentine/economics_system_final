from abc import ABC, abstractmethod
from agent_types import IProducer

class IRegistrySorter(ABC):
    @abstractmethod
    def sort_value_ascending(self, agents):
        pass

    @abstractmethod
    def sort_value_descending(self, agents):
        pass

    @abstractmethod
    def get_average_value(self, agents):
        pass

class ConsumerSorter(IRegistrySorter):
    def sort_value_ascending(self, agents):
        pass

    def sort_value_descending(self, agents):
        pass

    def get_average_value(self, agents):
        pass

class SupplierSorter(IRegistrySorter):
    def sort_value_ascending(self, supplier: dict[str, IProducer]):
        sorted_agents = {}

        for agent in supplier.values():
            supply = agent.get_supply_name()

            if not supply in sorted_agents:
                sorted_agents[supply] = []

            sorted_agents[supply].append(agent)

        for category in sorted_agents.values():
            category.sort(key = lambda m: m.get_supply_price())

        return sorted_agents

    def sort_value_descending(self, agents):
        pass

    def get_average_value(self, agents):
        pass


# def get_price_average(self, supplier):
#     stock_sum = 0
#     price_sum = 0
#
#     for agent in supplier.values():
#         supply = agent.get_supply_name()
#         stock = agent.get_stock(supply)
#         stock_sum += stock
#         price_sum += agent.get_supply_price()
#
#     if stock_sum == 0 or price_sum == 0:
#         return 0
#
#     return price_sum / stock_sum

# class SupplierRegistrySorter(IRegistrySorter):
#     def sort_value_descending(self, agents):
#         pass
#
#     def sort_value_ascending(self, agents):
#         sorted_agents = {}
#
#         for agent in agents.values():
#             category = agent.get_supply().get_product()
#
#             if not category in sorted_agents:
#                 sorted_agents[category] = []
#
#             sorted_agents[category].append(agent)
#
#         for category in sorted_agents.values():
#             category.sort(key = lambda m: m.get_supply().get_price())
#
#     def get_average_value(self, agents):
#         sum_price = 0
#         sum_stock = 0
#         for agent in agents.values():
#             supply_name = agent.get_supply().get_product()
#             stock = agent.get_inventory().get_product_stock(supply_name)
#             sum_stock += stock
#             sum_price += agent.get_price() * stock
#
#         if sum_stock == 0 or sum_price == 0:
#             return 0
#
#         return sum_price/sum_stock
#
# class ConsumerRegistrySorter(IRegistrySorter):
#     def sort_value_descending(self, agents):
#         pass
#
#     def sort_value_ascending(self, agents):
#         pass
#
#     def get_average_value(self, agents):
#         pass