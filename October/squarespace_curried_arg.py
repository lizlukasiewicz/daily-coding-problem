"""

This problem was asked by Squarespace.

Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11


"""

from __future__ import annotations


class CurriedInt(int):
    def __init__(self, value: int) -> None:
        int.__init__(value)
        self.should_add=True
    
    def __call__(self, value: int) -> CurriedInt:
        if self.should_add:
            print(f'should add: (self){self} + (value){value} = {self+value}')
            result=CurriedInt(self + value)
        else:
            print(f'should subtract: (self){self} - (value){value}  = {self-value}')
            result = CurriedInt(self - value)
        result.update_should_add(not self.should_add)
        return result

    def update_should_add(self, should_add: bool) -> None:
        self.should_add=should_add

def add_subtract(value: int) -> CurriedInt:
    return CurriedInt(value)


if __name__ == "__main__":
    print(f'add_subtract(7):: {add_subtract(7)}')
    print(f'add_subtract(1)(2)(3):: {add_subtract(1)(2)(3)}')
    print(f'add_subtract(-5)(10)(3)(9)::  {add_subtract(-5)(10)(3)(9)}')