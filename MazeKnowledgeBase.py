'''
MazeKnowledgeBase.py

Specifies a simple, Conjunctive Normal Form Propositional
Logic Knowledge Base for use in Grid Maze pathfinding problems
with side-information.
'''
from MazeClause import MazeClause
import unittest

class MazeKnowledgeBase:
    
    def __init__ (self):
        self.clauses = set()
    
    # [!] Assumes that a clause is never added that causes the
    # KB to become inconsistent
    def tell (self, clause):
        for kb_clause in self.clauses
            self.clauses.update(resolve(clause, kb_clause))
        return
        
    # [!] Queries are always MazeClauses
    def ask (self, query):
        # TODO: Implement resolution inference here!
        # This is currently implemented incorrectly; see
        # spec for details!
        return False
            
    
class MazeKnowledgeBaseTests(unittest.TestCase):
    # clause1 = MazeClause([(("P", (1, 1)), True), (("P", (1, 2)), False), (("P", (0, 1)), True)])
    # clause2 = MazeClause([(("P", (1, 3)), True), (("P", (1, 1)), False), (("P", (0, 1)), True)])
    # MazeClause.resolve(clause1, clause2)
    # def test_mazekb1(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("X", (1, 1)), True)])))
        
    # def test_mazekb2(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Y", (1, 1)), True)])))
        
    # def test_mazekb3(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True), (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("W", (1, 1)), True)])))
    #     self.assertFalse(kb.ask(MazeClause([(("Y", (1, 1)), False)])))
        
    # def test_mazekb4(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
        
    # def test_mazekb5(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), True), (("W", (1, 1)), True)])))
    
    # def test_mazekb6(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertFalse(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
    #     kb.tell(MazeClause([(("Y", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
        
        
if __name__ == "__main__":
    unittest.main()
    # clause1 = MazeClause([(("P", (1, 1)), True), (("P", (2, 1)), False), (("P", (0, 1)), True)])
    
    