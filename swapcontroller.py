class DFA:
    current_state = None;




    def __init__(self, alphabet, transition_function, start_state, accept_states):
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;

    def go_to_initial_state(self):
        self.current_state = self.start_state;

    # def transition_to_state_with_input(self, input_value, index):
    #     if ((self.current_state, input_value) not in self.transition_function.keys()):
    #         print("letter that was not a part of current states is :", input_value)
    #         return index

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        score = -1
        for inp in range(len(input_list)):
            print("current state :", self.current_state)
            print "left", (self.current_state, input_list[inp])
            if ((self.current_state, input_list[inp]) not in self.transition_function.keys()):
                score = inp;
                break
            else:
                self.current_state = self.transition_function.get((self.current_state, input_list[inp]))
        if score == -1:
            score = len(input_list)
        return score;


    def wordsWithWordnessScore(self, word):

        for w in range(len(word)):
            print "updated word :", word
            wordnessScore = dict()
            for a in range(len(self.alphabet)):
                print(word[w])
                print(self.alphabet[a])
                if (word[w] != self.alphabet[a]):
                    temp = word[:]
                    temp[w] = self.alphabet[a]
                    score = d.run_with_input_list(temp);
                    wordnessScore.update({"".join(temp): score})

                    # if w == 0:
                    #     if self.current_state not in start_state:
                    #         wordnessScore.update({str(temp): -1})
                    #     else:
                    #        score = d.run_with_input_list(temp);
                    #        wordnessScore.update({str(temp): score})
                    # else:
                    #     score = d.run_with_input_list(temp);
                    #     wordnessScore.update({str(temp): score})
            sorted_by_value = sorted(wordnessScore.items(), key=lambda kv: kv[1])
            print("wordnessScore :", wordnessScore)

            y = sorted_by_value.__getitem__(-1)
            print("y[0] :", y[0])

            word = list(y[0])
            print("word :", word)

        return word







word = list("ASOI")
alphabet = ['E', 'A', 'T', 'S', 'O', 'I', 'N']

tf = dict();
tf[(0, 'N')] = 1;
tf[(1, 'E')] = 2;
tf[(2, 'S')] = 3;
tf[(3, 'T')] = 3;
start_state = 0;
accept_states = {3};

d = DFA( alphabet, tf, start_state, accept_states);
originialWord =  d.wordsWithWordnessScore(word)
print("originialWord :", originialWord)


#code to check if this word is a correct english word Missing


