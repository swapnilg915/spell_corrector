"""
author: Swapnil Gaikwad
date: 9th April 2021
"""

import re
letters    = 'abcdefghijklmnopqrstuvwxyz'

class SpellCorrector(object):

	def __init__(self):
		pass

	def words(self, text):
		return re.findall(r'\w+', text.lower())

	def candidates(self, word, corpus): 
		# return (known([word], corpus) or known(edits1(word), corpus) or known(edits2(word), corpus) or [word])
		
		edits1_res = self.edits1(word)
		edits1_known = self.known(edits1_res, corpus)
		if edits1_known: return edits1_known
		else: 
			edits2_res = self.edits2_new(edits1_res, corpus)
			if edits2_res: return edits2_res
			else: return [word]


	def known(self, words, corpus): 
		return set(words) & set(corpus)

	def edits1(self, word):
		splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
		
		deletes    = [L + R[1:]               for L, R in splits if R]
		transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
		replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
		inserts    = [L + c + R               for L, R in splits for c in letters]

		# dtri = [( get_deletes(R), get_transposes(R), get_replaces(R, letters), get_inserts(letters))              for L, R in splits]
		return set(deletes + transposes + replaces + inserts)

	def deletes(self, splits):
		return [L + R[1:]               for L, R in splits if R]

	def transposes(self, splits):
		return [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]

	def replaces(self, splits):
		return [L + c + R[1:]           for L, R in splits if R for c in letters]

	def inserts(self, splits):
		return [L + c + R               for L, R in splits for c in letters]

	def edits2(self, word): 
		return (e2 for e1 in edits1(word) for e2 in edits1(e1))

	def edits2_new(self, edits1_res, corpus):
		edits1_res = list(edits1_res)
		
		# for e1 in edits1_res:    
		for e1 in range(len(edits1_res)):
			# splits = [(e1[:i], e1[i:])    for i in range(len(e1) + 1)]
			splits = [(edits1_res[e1][:i], edits1_res[e1][i:])    for i in range(len(edits1_res[e1]) + 1)]

			deletes_inter = set(self.deletes(splits)) & set(corpus)
			if deletes_inter: return deletes_inter
			transpose_inter = set(self.transposes(splits)) & set(corpus)
			if transpose_inter: return transpose_inter
			replace_inter = set(self.replaces(splits)) & set(corpus)
			if replace_inter: return replace_inter
			insert_inter = set(self.inserts(splits)) & set(corpus)
			if insert_inter: return insert_inter


	def main(self, word, corpus):
		return list(self.candidates(word, corpus))


	def test(self):
		# word = "henefit" # expected="benefit"
		word="corector" # expected="corrector"
		text = "I figured they, and others, could benefit from an explanation. The full details of an industrial-strength spell corrector are quite complex (you can read a little about it here or here). But I figured that in the course of a transcontinental plane ride I could write and explain a toy spelling corrector that achieves 80 or 90% accuracy at a processing speed of at least 10 words per second in about half a page of code. "
		corpus = text.split()
		print("\n original word:",word)
		corrections = self.main(word, corpus)
		print("\n corrected spelling : ", corrections[0])


if __name__ == "__main__":
	obj = SpellCorrector()
	obj.test()