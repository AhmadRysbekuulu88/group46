class Computer:
    def init(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        # Пример выполнения простых вычислений
        result = self.memory * 5 - self.cpu
        print(f"Результат вычислений: {result}")

    def str(self):
        return f"Computer(cpu: {self.cpu}, memory: {self.memory})"

    def eq(self, other):
        return self.memory == other.memory

    def ne(self, other):
        return self.memory != other.memory

    def lt(self, other):
        return self.memory < other.memory

    def le(self, other):
        return self.memory <= other.memory

    def gt(self, other):
        return self.memory > other.memory

    def ge(self, other):
        return self.memory >= other.memory


class Phone:
    def init(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 <= sim_card_number < len(self.__sim_cards_list):
            carrier = self.__sim_cards_list[sim_card_number]["carrier"]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number + 1} - {carrier}.")
        else:
            print("Некорректный номер сим-карты.")

    def str(self):
        return f"Phone(sim_cards_list: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def init(self, cpu, memory, sim_cards_list):
        Computer.init(self, cpu, memory)
        Phone.init(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до: {location}")

    def str(self):
        return f"SmartPhone(cpu: {self.cpu}, memory: {self.memory}, sim_cards_list: {self.sim_cards_list})"

