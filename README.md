# spell_corrector
This repo implements various spell correction approaches using python 

This is a edit distance based spell corrector. Though it is simple, it gives very good results, achieves 80-90% accuracy. 
I have modified the code to make it a bit faster than the original one. Implemented on 1 and 2 edit distances.

Note: As we go on increasing the edit distances, the time will also increase.

Reference: https://norvig.com/spell-correct.html

This is not a context based spell corrector. 
Suppose for e.g. we have a wrongly spelled word "heather" in a sentence "today's heather is sunny and awesome!", and in our corpus we have both the words "weather" and "leather", this spell corrector will not be able to choose the correct one based on the context.
Planning to implement context based spell corrector based on advanced embeddings.
