from abc import ABC, abstractmethod

class IAppliance(ABC):
    @abstractmethod
    def get_labor_requirement(self):
        pass

    @abstractmethod
    def get_max_production(self):
        pass

class Appliance:
    def __init__(self, required_labor, max_production):
        self.required_labor = required_labor
        self.max_production = max_production

class Workplace:
    def __init__(self):
        self.appliances: list[Appliance] = []

    def add_appliance(self, appliance: Appliance):
        self.appliances.append(appliance)

    def remove_appliance(self):
        self.appliances.pop()

    def get_optimal_labor_amount(self):
        labor_requirement = 0
        for appliance in self.appliances:
            labor_requirement += appliance.required_labor
        return labor_requirement

    def get_max_production(self):
        max_production = 0
        for appliance in self.appliances:
            max_production += appliance.max_production
        return max_production

class Factory:
    def __init__(self, labor, wages, efficiency, workplace):
        self.labor = labor
        self.wages = wages
        self.efficiency = efficiency

        self.marginal_production = []
        self.total_production = []

        self.appliances: Workplace = workplace

    def get_labor(self):
        return self.labor

    def add_labor(self, amount):
        self.labor = self.labor + amount

    def remove_labor(self, amount):
        self.labor = self.labor - amount

    def set_wages(self, wages):
        self.wages = wages

    def set_efficiency(self, efficiency):
        self.efficiency = efficiency

    def get_marginal_labor(self, labor):
        return self.marginal_production[labor]

    def get_total_product(self, labor):
        return self.total_production[labor]

    def update_marginal_production(self):
        optimal_labor = self.appliances.get_optimal_labor_amount()
        maximum_production = self.appliances.get_max_production()

        total_product = 0
        total_labor = 0

        while total_product < maximum_production:
            marginal_product = pow(min(total_labor, optimal_labor)/max(total_labor, optimal_labor), 0.8) * self.efficiency
            total_product += marginal_product

            self.marginal_production.append(marginal_product)
            self.total_production.append(total_product)
            total_labor += 1