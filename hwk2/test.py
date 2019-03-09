import string

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

THRESHOLD = 1
BASE_PROB = 0.5


class BayesSpam:

    def __init__(self, ham, spam):

        self.threshold = THRESHOLD
        self.unknown_probability_value = BASE_PROB
        self.ngood = len(ham)
        self.nbad = len(spam)

        self.ham_hash = self.hash_occurances(ham)
        self.spam_hash = self.hash_occurances(spam)

        # get a list of all words, from either corpus
        # Credit to https://stackoverflow.com/a/16902603
        self.token_list = set().union(*[self.ham_hash, self.spam_hash])

        # Create the combined score hashmap
        self.score_hash = {}

        for word in self.token_list:
            # Ternary operation to assign good value
            g = (2 * self.ham_hash[word] if word in self.ham_hash else self.unknown_probability_value)
            # Ternary operation to assign bad value
            b = (self.spam_hash[word] if word in self.spam_hash else self.unknown_probability_value)

            if g + b > self.threshold:
                self.score_hash[word] = max(0.01, min(0.99, min(1.0, b / self.nbad) /
                                                      (min(1.0, g / self.ngood) + min(1.0, b / self.nbad))))

        print("Scores:")
        print(self.score_hash)

    @staticmethod
    def hash_occurances(corpus):
        new_hash = {}
        for i in corpus:
            for v in i:
                if v in new_hash:
                    new_hash[v.upper()] += 1
                else:
                    new_hash[v.upper()] = 1
        return new_hash

    def filter_spam(self, mail):
        mail = mail.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
        words = mail.upper().split()
        prod_list = 1
        compliment_list = 1

        for word in words:
            if word in self.score_hash:
                prob = self.score_hash[word]
            else:
                prob = self.unknown_probability_value

            prod_list *= prob
            compliment_list *= (1 - prob)

        return prod_list / (prod_list + compliment_list)


if __name__ == '__main__':
    spam_filter = BayesSpam(ham_corpus, spam_corpus)
    print(spam_filter.filter_spam("i"))
    print(spam_filter.filter_spam("I am sam, sam I am, do you like green eggs and ham?"))
    print(spam_filter.filter_spam("spamiam"))
    print(spam_filter.filter_spam("I am spam, spam I am"))
