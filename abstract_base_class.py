# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Animal(metaclass = ABCMeta):
  """ Animal class """

  def __init__(self, name: str) -> None:
    self.__name = name

  @property
  def name(self) -> str:
    return self.__name

  @abstractmethod
  def speak(self) -> str:
    pass


class Dog(Animal):
  """ Dog class """

  def speak(self) -> str:
    return str('bow bow')


class Cat(Animal):
  """ Cat class """

  def speak(self) -> str:
    return str('mew mew')


dog = Dog('pochi')
print(dog.name)     # pochi
print(dog.speak())  # bow bow

cat = Cat('tama')
print(cat.name)     # tama
print(cat.speak())  # mew mew
