from MarkovChain import MarkovChain

def load_dataset(txt_name):
    try:
        f = open(txt_name, 'r', encoding='windows-1252')
        inputs = []

        for line in f:
            # Split on any whitespace (including tab characters)
            row = line.split("\t")
            inp = []
            entry = row[1].split(" ")
            for name in entry:
                inp.append(name.replace("\n", ""))
            inputs.append(inp)
        return inputs
    except Exception as e:
        print(e)

def main():

    # Load dataset with given txt file
    X = load_dataset(txt_name="player_name.txt")
    markov_object = MarkovChain(dataset=X)
    markov_object.markov_chain_process()
    
if __name__ == "__main__":
    main()