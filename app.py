from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Subject Interface
class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing observers.
    Observers can be added, removed, and notified of state changes.
    """

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.

        :param observer: The observer to attach.
        """
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.

        :param observer: The observer to detach.
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Notify all observers about a state change.
        """
        pass


# Concrete Subject
class WeatherStation(Subject):
    """
    The WeatherStation is a concrete implementation of the Subject interface.
    It stores a list of observers and the current temperature, and notifies
    observers when the temperature changes.
    """

    _observers: List[Observer] = []
    _temperature: int = None

    def add_observer(self, observer: Observer) -> None:
        """
        Attach an observer to the WeatherStation.

        :param observer: The observer to attach.
        """
        self._observers.append(observer)
        print("WeatherStation: New observer added.")

    def remove_observer(self, observer: Observer) -> None:
        """
        Detach an observer from the WeatherStation.

        :param observer: The observer to detach.
        """
        self._observers.remove(observer)
        print("WeatherStation: An observer has been removed.")

    def notify_observers(self) -> None:
        """
        Notify all attached observers of a temperature change.
        """
        print("WeatherStation: Notifying all observers...")
        for observer in self._observers:
            observer.update(self)

    def change_temperature(self, temperature: int) -> None:
        """
        Change the temperature and notify observers of the change.

        :param temperature: The new temperature to set.
        """
        print(f"\nWeatherStation: Temperature changed to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

    @property
    def temperature(self) -> int:
        """
        Get the current temperature.

        :return: The current temperature.
        """
        return self._temperature


# Observer Interface
class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects to
    notify observers of changes in state.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive an update from the subject.

        :param subject: The subject that sent the update.
        """
        pass


# Concrete Observer A
class CurrentConditionsDisplay(Observer):
    """
    The CurrentConditionsDisplay is a concrete implementation of the Observer interface.
    It displays the current temperature whenever it is updated by the WeatherStation.
    """

    def update(self, subject: Subject) -> None:
        """
        React to a temperature update from the WeatherStation.

        :param subject: The WeatherStation that sent the update.
        """
        if isinstance(subject, WeatherStation):
            print(f"CurrentConditionsDisplay: The current temperature is {subject.temperature}°C")


# Concrete Observer B
class StatisticsDisplay(Observer):
    """
    The StatisticsDisplay is another concrete implementation of the Observer interface.
    It tracks the history of temperature updates and displays statistics like average,
    maximum, and minimum temperatures.
    """

    _temperatures: List[int] = []

    def update(self, subject: Subject) -> None:
        """
        React to a temperature update from the WeatherStation and update statistics.

        :param subject: The WeatherStation that sent the update.
        """
        if isinstance(subject, WeatherStation):
            self._temperatures.append(subject.temperature)
            self._display_statistics()

    def _display_statistics(self) -> None:
        """
        Display statistics such as average, maximum, and minimum temperatures.
        """
        avg_temp = sum(self._temperatures) / len(self._temperatures)
        max_temp = max(self._temperatures)
        min_temp = min(self._temperatures)
        print(f"StatisticsDisplay: Avg/Max/Min temperatures = {avg_temp:.1f}/{max_temp}/{min_temp}°C")


# Client Code
if __name__ == "__main__":
    # Create a WeatherStation instance
    weather_station = WeatherStation()

    # Create observer instances
    current_conditions_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()

    # Attach observers to the WeatherStation
    weather_station.add_observer(current_conditions_display)
    weather_station.add_observer(statistics_display)

    # Change the temperature and see how observers react
    weather_station.change_temperature(24)
    weather_station.change_temperature(29)
    weather_station.change_temperature(15)

    # Remove an observer and change the temperature again
    weather_station.remove_observer(current_conditions_display)
    weather_station.change_temperature(21)
