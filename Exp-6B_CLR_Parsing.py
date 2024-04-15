class LR0Item:
    def __init__(self, non_terminal, production, dot_position):
        self.non_terminal = non_terminal
        self.production = production
        self.dot_position = dot_position

    def __eq__(self, other):
        return self.non_terminal == other.non_terminal and self.production == other.production and self.dot_position == other.dot_position

    def __hash__(self):
        return hash((self.non_terminal, tuple(self.production), self.dot_position))


class CLRParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.lr0_items = []
        self.construct_parsing_table()

    def closure(self, items):
        closure = items.copy()
        added = True
        while added:
            added = False
            for item in closure:
                if item.dot_position < len(item.production) and item.production[item.dot_position] in self.grammar:
                    next_symbol = item.production[item.dot_position]
                    for prod in self.grammar[next_symbol]:
                        new_item = LR0Item(next_symbol, prod, 0)
                        if new_item not in closure:
                            closure.append(new_item)
                            added = True
        return closure

    def go_to(self, item_set, symbol):
        goto_set = []
        for item in item_set:
            if item.dot_position < len(item.production) and item.production[item.dot_position] == symbol:
                goto_set.append(LR0Item(item.non_terminal,
                                item.production, item.dot_position + 1))
        return self.closure(goto_set)

    def construct_parsing_table(self):
        self.parsing_table = {}
        augmented_grammar = self.grammar.copy()
        augmented_grammar['S\''] = ['S']
        lr0_items = [self.closure(
            [LR0Item('S\'', augmented_grammar['S\''][0], 0)])]

        while lr0_items:
            item_set = lr0_items.pop(0)
            item_set_index = self.grammar_index(item_set)
            for item in item_set:
                if item.dot_position < len(item.production):
                    next_symbol = item.production[item.dot_position]
                    goto_set = self.go_to(item_set, next_symbol)
                    if goto_set:
                        goto_set_index = self.grammar_index(goto_set)
                        if next_symbol in self.grammar:
                            if next_symbol not in self.parsing_table:
                                self.parsing_table[next_symbol] = {}
                            self.parsing_table[next_symbol][(
                                item_set_index, next_symbol)] = goto_set_index
                        else:
                            if next_symbol not in self.parsing_table:
                                self.parsing_table[next_symbol] = {}
                            self.parsing_table[next_symbol][(item_set_index, next_symbol)] = (
                                'shift', goto_set_index)
            for production in self.grammar:
                for prod in self.grammar[production]:
                    if prod[-1] == '.':
                        for terminal in self.follow_set(production):
                            self.parsing_table[terminal][(item_set_index, production)] = (
                                'reduce', production)

    def grammar_index(self, item_set):
        for index, item in enumerate(self.lr0_items):
            if item == item_set:
                return index
        self.lr0_items.append(item_set)
        return len(self.lr0_items) - 1

    def follow_set(self, production):
        follows = set()
        for symbol in self.grammar:
            for prod in self.grammar[symbol]:
                index = prod.index(production)
                if index == len(prod) - 1 and symbol != production:
                    for terminal in self.follow_set(symbol):
                        follows.add(terminal)
                elif index != len(prod) - 1:
                    follows.add(prod[index + 1])
        return follows

    def parse(self, input_string):
        stack = [0]
        input_string += '$'
        input_index = 0

        while True:
            state = stack[-1]
            symbol = input_string[input_index]

            if (symbol, state) in self.parsing_table:
                action = self.parsing_table[symbol][(state, symbol)]
                if action == 'accept':
                    return True
                elif isinstance(action, tuple) and action[0] == 'shift':
                    stack.append(action[1])
                    input_index += 1
                elif isinstance(action, tuple) and action[0] == 'reduce':
                    production = action[1]
                    for _ in range(len(self.grammar[production][0].split(' ')[1])):
                        stack.pop()
                    top_state = stack[-1]
                    stack.append(
                        self.parsing_table[production][(top_state, production)])
            else:
                return False


# Example usage
grammar = {
    'S': ['E'],
    'E': ['E + T', 'T'],
    'T': ['T * F', 'F'],
    'F': ['( E )', 'id']
}

parser = CLRParser(grammar)
print(parser.parse("id + id * id"))
