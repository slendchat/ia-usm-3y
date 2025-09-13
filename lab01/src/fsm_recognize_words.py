from enum import Enum
# States
# a(bc)^nd(de)^m ,n>=0,m>=0.
# n or m can be 0
# So there can be no bc or de or both
class State(Enum):
    STATE_START_IS_A = 0
    STATE_BC_ACCEPT = 1
    STATE_B_THEN_C = 2
    STATE_DE_ACCEPT = 3 # Final accepted state
    STATE_D_THEN_E = 4
    STATE_INVALID = 5

# The state consideed as the final accepted state
accepted_state = {State.STATE_DE_ACCEPT}

# The table of transitions
transition_table = {
    State.STATE_START_IS_A:   {'a':State.STATE_BC_ACCEPT},
    State.STATE_BC_ACCEPT:    {'b':State.STATE_B_THEN_C,'d':State.STATE_DE_ACCEPT},
    State.STATE_B_THEN_C:     {'c':State.STATE_BC_ACCEPT},
    State.STATE_DE_ACCEPT:    {'d':State.STATE_D_THEN_E},
    State.STATE_D_THEN_E:     {'e':State.STATE_DE_ACCEPT},
}

# The function that recognizes the words
def fsm_recognize_words(input_string) -> bool:
    current_state = State.STATE_START_IS_A
    for ch in input_string:
        current_state = transition_table.get(current_state, {}).get(ch,State.STATE_INVALID)
        if current_state == State.STATE_INVALID:
            return False
    return current_state in accepted_state


def main():
    print("Finite State Machine: Recognize Words")
    #Examples
    tobe_accepted = ["ad", "abcd", "abcbcd", "adde", "addede"]
    tobe_rejected = ["a", "abd", "ade", "abccd", "abcdd", "abcbcded"]

    print("[INFO] Testing the FSM with some examples")
    print("[INFO] Accepted words:")
    for str in tobe_accepted: 
        assert fsm_recognize_words(str) == True, f"[Error] {str} should be accepted"
        print(f"\"{str}\" is accepted")

    print("[INFO] Rejected words:")
    for str in tobe_rejected: 
        assert fsm_recognize_words(str) == False, f"[Error] {str} should be rejected"
        print(f"\"{str}\" is rejected")

if __name__ == "__main__":
    main()