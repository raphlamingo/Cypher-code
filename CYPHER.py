# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:42:00 2022

@author: RAPHLAMINGO
"""
import logo
should_continue= True
while should_continue==True:
    print(logo.logo)



    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

        
    def crypting(text,shift,direction):
        output=''
        for letter in text:
            position=alphabet.index(letter)
            if direction=='encode':
                new_position= position + shift
                if new_position>25:
                    new_position=new_position-25
            if direction=='decode':
                new_position= position - shift
                if new_position<0:
                    new_position=new_position+25
            output= output+alphabet[new_position]
            
        print(f'THE NEW CODE IS {output}')
    crypting(text,shift,direction) 
    lo= input('DO YOU WANT TO GO ON "YES" OR "NO"\n').lower()
    if lo=='yes':
        should_continue= True
    else:
        should_continue= False

        