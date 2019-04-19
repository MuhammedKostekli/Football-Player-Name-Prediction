from sklearn.preprocessing import normalize
import json

class MarkovChain:
   
    def __init__(self, dataset):
        self.X = dataset

    def markov_chain_process(self):
        # find all distinct names from input names
        all_names = self.find_distinct_names()

        # generate transition matrix from names. It includes count of connection from names
        transition_matrix = self.generate_transition_matrix(names=all_names)

        # normalize matrix to find all possibility
        transition_probability_matrix = self.normalize_transition_matrix(matrix=transition_matrix)

        # generate output json
        self.generate_json_from_matrix(matrix=transition_probability_matrix,all_names=all_names)

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

    def generate_json_from_matrix(self, matrix, all_names):
        data = {} 
        data['data'] = []
        for i,name in enumerate(all_names):
            next_names = self.find_most_repetitive_next_word(matrix[i],all_names)
            data['data'].append({  
                'name': name,
                'next_names': next_names  
            })

        with open('name_prediction.json', 'w') as outfile:  
            json.dump(data, outfile, indent=4)
    
    def find_most_repetitive_next_word(self, curr_word_line, all_names):
        temp_array = []
        for value,name in zip(curr_word_line,all_names):
            if value != 0:
                x = []
                x.append(name)
                x.append(value)
                temp_array.append(x)

        result_list = sorted(temp_array, key=lambda a_entry: a_entry[1], reverse=True)[:3]
        return [row[0] for row in result_list]


        