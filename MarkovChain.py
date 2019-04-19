from sklearn.preprocessing import normalize

class MarkovChain:
   
    def __init__(self, dataset):
        self.X = dataset

    def markov_chain_process(self):
        all_names = self.find_distinct_names()
        transition_matrix = self.generate_transition_matrix(names=all_names)
        transition_probability_matrix = self.normalize_transition_matrix(matrix=transition_matrix)

    def find_distinct_names(self):
        names = []
        for full_name in self.X:
            for name in full_name:
                if name not in names:
                    names.append(name)
        return names
    
    def generate_transition_matrix(self, names):
        transition_matrix = [[0] * len(names) for _ in range(len(names))]
        for i,name in enumerate(names):
            next_words = self.find_next_word_after_input(name)
            for next_word in next_words:
                transition_matrix[i][names.index(next_word)] += 1
        return transition_matrix   

    def find_next_word_after_input(self,curr_word):
        next_words = []
        for row in self.X:
            for column in row:
                if curr_word == column:
                    if row.index(column) == len(row) - 1:
                        continue
                    else:
                        next_words.append(row[row.index(column) + 1])
        return next_words

    def normalize_transition_matrix(self, matrix):    
        normalized = normalize(matrix, norm='l1', axis=1)
        return normalized.tolist()  
