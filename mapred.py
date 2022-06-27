from mrjob.job import MRJob,MRStep
import re

regex_word = re.compile(r"[\w']+")

class maping(MRJob):
    def steps(self):
        return[
            MRStep(mapper=self.mapperkey,reducer=self.reducerkey),
            MRStep(mapper = self.mapperval,reducer = self.reducerval)
        ]
        
    def mapperkey(self,key,line):
        words = regex_word.findall(line)
        for word in words:
            yield word.lower(),1

    def reducerkey(self,word,occurences):
        yield word,sum(occurences)

    #sorting from min to max
    def mapperval(self,word,occur):
        yield '%03d'%int(occur),word

    def reducerval(self,occur,word):
        for x in word:
            yield int(occur),x

if __name__ == "__main__":
    maping.run()