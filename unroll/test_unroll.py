import unittest
import collections
import types
if __name__ == "__main__":
    #from unroll import unroll, accumulate, compose
    from unroll import unroll, compose, fmap, call, compr
else:
    #from .unroll import unroll, accumulate, compose
    from .unroll import unroll, compose, fmap, call, compr


def is_even(n):
    return n % 2 == 0
def even_triples_list(mx):
    return [
        n*3 for n in range(mx)
        if not is_even(n*3) == 0
    ]




class ComprTests(unittest.TestCase):
    def test_basic(self):
        @compr(list, 5)
        def evens(x):
            for i in range(x):
                yield 2*i
        self.assert_(isinstance(evens, list))
        self.assertEqual(evens, [0, 2, 4, 6, 8])




class UnrollTests(unittest.TestCase):
    def setUp(self):
        self.input = 5
        self.expected = even_triples_list(self.input)
    
    def test_unroll_invoke_decorator(self):
        """This is the primary use-case."""
        @call(self.input)
        @unroll(list)
        def unrolled(mx):
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield triple
        output = unrolled
        self.assert_(isinstance(output, collections.MutableSequence))
        self.assert_(isinstance(output, list))
        self.assertEquals(output, self.expected)
    def test_unroll_invoke_inline(self):
        def unrolled(mx):
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield triple
        #... the inline use-case looks ugly
        output = call(self.input)(unroll(list)(unrolled))
        self.assert_(isinstance(output, collections.MutableSequence))
        self.assert_(isinstance(output, list))
        self.assertEquals(output, self.expected)
    def test_list_decorator(self):
        mx = self.input
        @unroll(list)
        def unrolled():
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield triple
 
        self.assert_(callable(unrolled))
        output = unrolled()
        self.assert_(isinstance(output, collections.MutableSequence))
        self.assert_(isinstance(output, list))
        self.assertEquals(output, self.expected)
         
    def test_dict_decorator(self):
        mx = self.input
         
        @unroll(dict)
        def unrolled():
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield n, triple
        
        output = unrolled()
        self.assertEqual(output, {0: 0, 2: 6, 4: 12})
 
    def test_list_inline(self):
        mx = self.input
         
        def _unrolled():
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield triple
        unrolled = unroll(list)(_unrolled)
 
        self.assert_(callable(unrolled))
        output = unrolled()
        self.assert_(isinstance(output, collections.MutableSequence))
        self.assert_(isinstance(output, list))
        self.assertEquals(output, self.expected)
         
    def test_exotic_string_concat(self):
        mx = self.input
        @unroll(', '.join)
        def unrolled():
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield str(triple)
 
        output = unrolled()
        self.assertEqual(output, '0, 6, 12')

class FMapTests(unittest.TestCase):
    def test_basic(self):
        @call(5)
        @unroll(fmap(str), ''.join)
        def unR(mx):
            for n in range(mx):
                triple = n*3
                if not is_even(triple):
                    continue
                yield triple
        
        self.assertEquals(unR, '0, 6, 12')

class ComposeTests(unittest.TestCase):
    def test_basic(self):
        def P1(x):
            return x+'1'
        def P2(x):
            return x+'2'
        def P3(x):
            return x+'3'
        self.assertEqual(compose(P1,P2,P3)('Z='), 'Z=123')
        self.assertEqual(compose(P3, P1, P2)(''), '312')

class CallTests(unittest.TestCase):
    def test_call_decorator_simple(self):
        @call('john')
        def say_hi(name, extra=""):
            return "Hello " + name + extra
            
        self.assert_( say_hi == "Hello john")
    
    def test_call_decorator_complex(self):
        @call('john', '--extra--')
        def say_hi(name, extra=""):
            return "Hello " + name + extra
        self.assert_(say_hi == "Hello john--extra--")   



if __name__ == "__main__":
    unittest.main()