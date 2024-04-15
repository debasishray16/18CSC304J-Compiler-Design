class SLRParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.terminals, self.non_terminals, self.productions = self.extract_grammar_info()
        self.lr_items = self.generate_lr_items()
        self.closure = self.calculate_closure()
        self.goto_table, self.action_table = self.build_slr_tables()

    def extract_grammar_info(self):
        terminals = set()
        non_terminals = set()
        productions = {}

        for production in self.grammar:
            non_terminal, rhs = production.split(' -> ')
            non_terminals.add(non_terminal)

            for symbol in rhs.split():
                if symbol.isalpha():
                    if symbol.islower():
                        terminals.add(symbol)
                    else:
                        non_terminals.add(symbol)

        return list(terminals), list(non_terminals), self.grammar

    def generate_lr_items(self):
        lr_items = []

        for production in self.grammar:
            lhs, rhs = production.split(' -> ')
            rhs_symbols = rhs.split()

            for i in range(len(rhs_symbols) + 1):
                item = (lhs, tuple(rhs_symbols[:i]), tuple(rhs_symbols[i:]))
                lr_items.append(item)

        return lr_items

    def calculate_closure(self):
        # Initial state (closure) contains the first LR(0) item
        closure = [self.lr_items[0]]

        changed = True
        while changed:
            changed = False
            for item in closure.copy():
                _, _, next_symbol = item

                if next_symbol and next_symbol[0] in self.non_terminals:
                    for production in self.grammar:
                        non_terminal, rhs = production.split(' -> ')
                        if non_terminal == next_symbol[0] and (non_terminal, (), rhs.split()) not in closure:
                            closure.append((non_terminal, (), rhs.split()))
                            changed = True

        return closure

    def goto(self, items, symbol):
        new_items = []
        for item in items:
            lhs, prefix, suffix = item
            if suffix and suffix[0] == symbol:
                new_items.append((lhs, prefix + (suffix[0],), suffix[1:]))
        return new_items

    def build_slr_tables(self):
        goto_table = {}
        action_table = {}

        # Initialize state 0
        initial_state = (0, self.calculate_closure())
        state_stack = [initial_state]

        while state_stack:
            state_number, state_items = state_stack.pop()

            # Calculate GOTO transitions
            for symbol in self.terminals + self.non_terminals:
                next_state_items = self.calculate_goto(state_items, symbol)
                if next_state_items:
                    next_state = (len(goto_table), next_state_items)
                    goto_table[state_number, symbol] = next_state
                    if next_state not in state_stack:
                        state_stack.append(next_state)

            # Calculate ACTION entries
            for item in state_items:
                lhs, prefix, suffix = item
                if not suffix:
                    if lhs == 'S':
                        action_table[state_number, '$'] = 'accept'
                    else:
                        for i, production in enumerate(self.productions):
                            if tuple(production.split(' -> ')) == item:
                                for terminal in self.terminals:
                                    if (state_number, terminal) not in action_table:
                                        action_table[state_number,terminal] = 'r' + str(i + 1)
                                break
                elif suffix[0] in self.terminals:
                    next_state = goto_table[state_number, suffix[0]][1]
                    action_table[state_number, suffix[0]] = 's' + str(next_state)

        return goto_table, action_table

    def calculate_goto(self, items, symbol):
        new_items = []
        for item in items:
            _, _, suffix = item
            if suffix and suffix[0] == symbol:
                new_items.extend(self.goto([item], symbol))
        return new_items

    def print_tables(self):
        # Print GOTO table
        print("\nGOTO Table:")
        print("{:<10} {:<10} {:<10}".format("State", "Symbol", "Next State"))
        for (state, symbol), next_state in self.goto_table.items():
            print("{:<10} {:<10} {:<10}".format(state, symbol, next_state[0]))

        # Print ACTION table
        print("\nACTION Table:")
        print("{:<10} {:<10} {:<10}".format("State", "Symbol", "Action"))
        for (state, symbol), action in self.action_table.items():
            print("{:<10} {:<10} {:<10}".format(state, symbol, action))


# Grammar for E -> E + T | T | T -> id | T -> (E)
grammar = ["E -> E + T", "E -> T", "T -> id", "T -> ( E )"]

# Create and print the SLR parser
slr_parser = SLRParser(grammar)
slr_parser.print_tables()
