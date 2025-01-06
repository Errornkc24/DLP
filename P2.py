# Finite Automata Implementation

def finite_automata():
    while True:
        # Step 1: Take inputs from the user
        print("Finite Automata Setup")
        num_inputs = int(input("Number of inputs: "))
        input_symbols = input(f"Input symbols (space-separated, {num_inputs} symbols): ").split()
        
        num_states = int(input("Number of states: "))
        initial_state = int(input("Initial state: "))
        num_accepting_states = int(input("Number of accepting states: "))
        accepting_states = set(map(int, input(f"Accepting states (space-separated, {num_accepting_states} states): ").split()))

        # Transition table setup
        transition_table = {}
        print("\nEnter the transition table:")
        for i in range(num_states):
            state = i + 1
            transition_table[state] = {}
            for symbol in input_symbols:
                next_state = int(input(f"State {state} to {symbol}: "))
                transition_table[state][symbol] = next_state

        while True:
            # Step 2: Process the input string
            input_string = input("\nEnter input string: ")

            # Step 3: Traverse the automaton
            current_state = initial_state
            for char in input_string:
                if char not in input_symbols:
                    print(f"Invalid symbol '{char}' in input string.")
                    return
                current_state = transition_table[current_state][char]

            # Step 4: Check if the final state is accepting
            if current_state in accepting_states:
                print("\nInput string is ACCEPTED by the finite automaton.")
            else:
                print("\nInput string is REJECTED by the finite automaton.")

            # Step 5: Ask if the user wants to check another string
            check_again = input("\nDo you want to check another string with the same inputs? Press 1 for Yes or 0 for No: ")
            if check_again != '1':
                break

        # Step 6: Ask if the user wants to enter new inputs
        new_inputs = input("\nDo you want to enter new inputs? Press 1 for Yes or 0 to Exit: ")
        if new_inputs != '1':
            print("Exiting...")
            break

# Main function
if __name__ == "__main__":
    finite_automata()
