#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
letter used=-1
wrong letter =-2
wrong answer=-5
correct answer=+20
"""

import random
#movies = ['harry potter','pirates of the caribbean']
movies = ['interstellar', 'matrix', 'avengers', 'the fast and the furious', 'the lord of the rings', 'star wars', 'shutter island', 'incredibles', 'mad max fury road', 'justice league']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[];
    for i in range(n):
        if ref[i]==letter:
            temp.append(letter)
        else:
            temp.append(qn_list[i])
    qn_new="".join(str(x) for x in temp)   
    return qn_new

def play():
    print("LET'S PLAY")
    p1name="GROUP 1"
    p2name="GROUP 2"
    pp1=0
    pp2=0
    turn=0
    #willing=True
    for rounds in range(10):
        if(turn%2==0):
            #player 1
            print(p1name, "its your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            modified_qn=qn
            print(qn)
            
            not_said=True
            while(not_said):
                pp1=pp1-1
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another character: "))
                    if d==1:
                        ans=input("Your answer: ")
                        if ans==picked_movie:
                            pp1=pp1+20
                            print("correct")
                            not_said=False
                            print(p1name, "your score is ", pp1)
                            print()
                        else:
                            print("wrong answer try again")
                            pp1=pp1-5
                else:
                    print(letter, "not found")
                    pp1=pp1-2
        else:
            #player2
            print(p2name, "its your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            modified_qn=qn
            print(qn)
            
            not_said=True
            while(not_said):
                pp2=pp2-1
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another character: "))
                    if d==1:
                        ans=input("Your answer: ")
                        if ans==picked_movie:
                            pp2=pp2+20
                            print("correct")
                            not_said=False
                            print(p2name, "your score is ", pp2)
                            print()
                        else:
                            print("wrong answer try again")
                            pp2=pp2-5
                else:
                    print(letter, "not found")
                    pp2=pp2-2
        turn=turn+1
        movies.remove(picked_movie)
    print()
    print(p1name, "your score: ",pp1)
    print(p2name, "your score: ",pp2)
    if pp1>pp2:
        print(p1name, "wins")
    elif pp1<pp2:
        print(p2name, "wins")
    else:
        print("MATCH TIED")
    print("THANK YOU!!!!")


play()