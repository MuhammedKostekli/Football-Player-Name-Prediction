

class MarkovChain:
   
    def __init__(self, dataset):
        self.X = dataset
        self.markov_chain_process()

    def markov_chain_process(self):
        all_names = self.find_distinct_names()
        self.generate_transition_probability_matrix(names=all_names)
        
        return self.X

    def find_distinct_names(self):
        names = []
        for full_name in self.X:
            for name in full_name:
                if name not in names:
                    names.append(name)
        return names
    
    def generate_transition_probability_matrix(self, names):
        transition_matrix = [[0] * len(names) for _ in range(len(names))]
        for name in names:
            


        print("s")