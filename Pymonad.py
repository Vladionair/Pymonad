from pymonad import *

@curry

def buy(new_items, current_items):
    items = {'apples':70, 'wine':300, 'milk':80, 'eda':100}
    @State
    def state_computation(old_state):
        for i in new_items:
            if i in items:
                if items[i] <= old_state:
                    old_state -= items[i]
                    current_items.append(i)
        return current_items, old_state
    return state_computation

a = ['wine']
b = ['apples', 'milk']
c = ['chips']

shopping = unit(State, []) >> buy(a) >> buy(b) >> buy(c)

print(shopping(2000))