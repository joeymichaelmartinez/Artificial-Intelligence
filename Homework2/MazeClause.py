'''
MazeClause.py

Joseph Martinez
'''
import unittest
import collections
import copy

class MazeClause:
    
    def __init__ (self, props):
        self.props = {}
        self.valid = False
        for proposition in props:
            if proposition[0] in self.props and self.props[proposition[0]] != proposition[1]:
                self.valid = True
                self.props = {}
                break
            else:
                self.props.update({proposition})

    def getProp (self, prop):
        if prop in self.props:
            return self.props.get(prop)
        else:
            return None

    def isValid (self):
        return self.valid

    def isEmpty (self): 
        return (self.props == {} and not self.valid)
    
    def __eq__ (self, other):
        return self.props == other.props and self.valid == other.valid
    
    def __hash__ (self):
        return hash(frozenset(self.props.items()))
    
    def __str__ (self):
        return str(self.props) + ": " + str(self.valid)
    
    @staticmethod
    def resolve (c1, c2):
        resolved_propositions = []
        results = set()
        if c1 == c2:
            return results
        disagree_flag = False
        c1_copy = copy.deepcopy(c1)
        c2_copy = copy.deepcopy(c2)
        for proposition in c1.props:
            if proposition in c2.props and c1.props[proposition] != c2.props[proposition]:
                if (disagree_flag):
                    results = set()
                    return results
                else: 
                    disagree_flag = True
                    del c1_copy.props[proposition]
                    del c2_copy.props[proposition]
        
        if(disagree_flag):
            for proposition in c1_copy.props.items():
                resolved_propositions.append(proposition)
            for proposition in c2_copy.props.items():
                resolved_propositions.append(proposition)
            resolved_maze_clause = MazeClause(resolved_propositions)
            results.add(resolved_maze_clause)
        return results
    

class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertTrue(mc.getProp(("X", (2, 1))))
        self.assertFalse(mc.getProp(("Y", (1, 2))))
        self.assertTrue(mc.getProp(("X", (2, 2))) is None)
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.isValid())
        self.assertTrue(mc.getProp(("X", (1, 1))) is None)
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.isValid())
        self.assertTrue(mc.isEmpty())
        
    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)
        
    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)
        
    def test_mazeprops7(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)
        
    def test_mazeprops8(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)
        
    def test_mazeprops9(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)
        
    def test_mazeprops10(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True), (("W", (1, 1)), False)]) in res)
        
if __name__ == "__main__":
    unittest.main()
    