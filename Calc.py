# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:21:32 2020

@author: K555D
"""


class Calculator():
    
    def Addition(self, a, b):
       c = a ^ b
       c_bin = format(c, "b").zfill(8)
       return c, c_bin
   
    def Subtraction(self, a, b):
       c = a ^ b
       c_bin = format(c, "b").zfill(8)
       return c, c_bin
   
    def Multiplication(self, a, b):
        m = int('00011011', 2) # irreducable polynomial
        mask = 2**8-1
        powers = [a]
        var = a
        for i in range(7):
            var_bin = format(var, 'b').zfill(8)
            if var_bin[0] == '1':
                var = (var << 1) & mask
                var = var ^ m
                powers.append(var)
            else:
                var = (var << 1) & mask
                powers.append(var)
        # print(powers)
        
        b_bin = format(b, 'b').zfill(8)
        one_locs = []
        for i in range(8):
            if b_bin[i] == '1':
                one_locs.append(7-i)
                
        c = 0
        for i in one_locs:
            c = c ^ powers[i]
        c_bin = format(c, "b").zfill(8)
        return c, c_bin
    
    def Division(self, a, b):
        # Find b inverse
        b_inv = b
        for i in range(253):
            b_inv, _ = self.Multiplication(b_inv, b)
        c, c_bin = self.Multiplication(a, b_inv)
        return c, c_bin
        
            
        
# calc = Calculator()
# c,c_bin =calc.Multiplication(87, 131)
# print(c,c_bin)
# q, _ = calc.Division(1,131)
# print(q)