# 유니코드 > 문자열 변환
# st = "50668 47084 48516 32 54624 32 49688 32 51080 50612 50836 32 54252 44592 54616 51648 47560 49464 50836 33"

# # print(st.split()) 숫자로된 문자열들의 리스트
# s=""
# for i in st.split():
#     s+=chr(int(i))
# print(s)

# 문자열 > 유니코드 변환
# st = input("문자열을 입력하세요 : ")
# for i in st:
#     print(ord(i), end=" ")

# st="""
# """

# for i in st.split("\n"):
#     for j in i:
#         if ord(j) < 123:
#             st+=j
#     print(st)  

# 금액을 입력받고, 현재 구매가능한 제품명들을 출력하는 프로그램을 작성하세요.
# menu = "딸기 4000원\t파인애플 5000원\t포도 4000원\t사과 2000원\t감자 3000원\n수박 8000원\t감귤 4000원\t한라봉 7000원\t체리 3000원\t자두 2000원\n아메리카노 3000원\t카페라떼 4000원\t카페모카 4500원\t아인슈패너 6000원\n에스프레소 2000원\t카푸치노 3600원\t아이스티 3000원\t레몬에이드 4000원\n초코우유 1500원\t딸기우유 1500원\t바나나우유 1500원\t커피우유 1500원\n두유 2000원\t헤이즐넛 3000원\t오레오초코 4000원\t얼그레이 6000원"

# # 상품명 + 가격들의 리스트
# st = menu.replace("\n","\t").split("\t")

# money = int(input("돈 입력 : "))
# for i in st:
#     # i.split() > ['사과','2000원']
#     n=i.split()
#     name = n[0]
#     price = int(n[1][:-1])
#     if money>=price:
#         print(f"{name} 구매가능!")

# Q1. 'p', 'y', 't', 'h', 'o', 'n' 의 등장횟수를 구해주세요.
# st="""culture
# experience
# education
# symbol
# effect
# liberty
# affair
# comfort
# tradition
# subject
# object
# source
# revolution
# pollution
# system
# triumph
# respect
# communication
# foundation
# glory
# situation
# competition
# prairie
# effort
# section
# rein
# solution
# hono(u)r
# unity
# population
# direction
# dialog(ue)
# republic
# method
# increase
# decrease
# amount
# ancestor
# voyage
# sculpture
# instrument
# figure
# activity
# cause
# worth
# accident
# adventure
# view
# relative
# superstition
# habit
# wealth
# treasure
# universe
# adult
# feast
# resources
# ruin
# monument
# information
# appetite
# stethoscope
# mystery
# thermometer
# burden
# series
# oath
# appointment
# clue
# debt
# hydrogen
# control
# uniform
# design
# damage
# custom
# traffic
# sophomore
# temperature
# limit
# statue
# furniture
# parade
# public
# pilgrim
# greeting
# language
# opinion
# athlete
# supply
# surface
# electricity
# order
# spirit
# purpose
# promise
# project
# government
# exercise
# comparison
# interest
# funeral
# senior
# junior
# democracy
# general
# admiral
# edge
# biology
# danger
# advice
# practice
# mammal
# grade
# score
# pause
# pronunciation
# stress
# contest
# horizon
# principal
# might
# trouble
# scar
# balance
# proverb
# semester
# election
# inning
# hollow
# degree
# cemetery
# relay
# spot
# exchange
# merchant
# saying
# refrigerator
# crack
# judge
# slave
# settler
# fare
# gesture
# planet
# type
# secretary
# devil
# scholar
# pardon
# kindergarten
# detective
# license
# palace
# spade
# square
# fountain-pen
# harvest
# tool
# sword
# magazine
# stadium
# care
# beauty
# museum
# sentence
# memory
# delight
# passenger
# skill
# journey
# ceremony
# hobby
# president
# address
# continent
# mankind
# patient
# site
# marble
# stem
# slip
# torch
# composer
# invader
# trick
# flight
# castle
# envelope
# pal
# vacation
# desert
# event
# theater
# stage
# error
# area
# base
# basement
# evil
# atom
# poet
# petal
# chance
# mind
# climate
# suburb
# throat
# voice
# valley
# puritan
# feather
# amateur
# nation
# puzzle
# riddle
# rear
# battle
# laundry
# shower
# navy
# mars
# gallery
# guest
# folk
# problem
# jewel
# garage
# fault
# lantern
# import
# angle
# match
# stripe
# pulse
# powder
# flood
# bush
# branch
# hero
# heaven
# exit
# beast
# century
# coeducation
# twin
# wound
# metal
# insect
# track
# deserve
# survive
# create
# describe
# select
# hesitate
# declare
# pretend
# struggle
# explore
# astonish
# disappoint
# attract
# celebrate
# explode
# include
# protect
# introduce
# produce
# chase
# scratch
# crash
# stare
# gaze
# scare
# grab
# guard
# discuss
# shrug
# sniff
# scream
# rid
# surround
# cleave
# carve
# except
# invent
# search
# abuse
# owe
# bless
# graduate
# replace
# collect
# upset
# arrest
# prove
# yell
# howl
# halt
# leak
# behave
# wrap
# locate
# charge
# review
# refuse
# complain
# remain
# warn
# bend
# suffer
# whisper
# prepare
# roar
# float
# drag
# overhear
# slide
# suck
# bother
# deal
# treat
# destroy
# accept
# depend
# nod
# remove
# beat
# clap
# feed
# obtain
# drown
# remind
# occur
# ache
# repeat
# attend
# sigh
# pray
# press
# bear
# follow
# hate
# frighten
# shout
# mention
# waste
# borrow
# complete
# excellent
# competent
# religious
# favorite
# entire
# primary
# similar
# precious
# normal
# popular
# compulsory
# curious
# independent
# intimate
# delicious
# valuable
# grave
# elementary
# crazy
# contrary
# regular
# social
# straight
# noble
# anxious
# international
# greedy
# stupid
# silly
# lonely
# dirty
# various
# private
# vain
# sore
# fierce
# firm
# solar
# smart
# single
# diligent
# serious
# fresh
# empty
# mild
# amazing
# charming
# boring
# giant
# huge
# tiny
# fair
# tough
# foreign
# modern
# expensive
# harmful
# calm
# special
# steady
# hay
# revival
# million
# crop
# shade
# company
# canal
# wagon
# fact
# joy
# concert
# rule
# suitcase
# weight
# hurray
# mail
# log
# hut
# tax
# dye
# earnings
# flame
# shape
# chest
# chain
# cost
# coast
# circle
# heart
# nature
# fever
# tongue
# trust
# whisker
# prison
# blood
# loaf
# list
# fence
# enemy
# thief
# data
# soldier
# musician
# capital
# course
# diary
# squirrel
# dawn
# shadow
# ditch
# crew
# stomach
# neighbor
# servant
# hunger
# tomb
# taste
# sign
# stair
# trip
# brain
# trumpet
# speech
# thumb
# horn
# chief
# trousers
# prince
# force
# sight
# space
# wool
# expressway
# science
# examination
# jar
# salt
# death
# saw
# swing
# wish
# grain
# eraser
# alphabet
# shoulder
# nephew
# niece
# library
# factory
# giraffe
# hawk
# pigeon
# bowl
# scene
# life
# earth
# pill
# math
# ocean
# price
# row
# schedule
# machine
# route
# ivy
# gift
# candle
# joke
# art
# corn
# pet
# robber
# cheek
# clerk
# cookie
# army
# nurse
# master
# lock
# moment
# sheet
# monk
# teenager
# closet
# handle
# guide
# bar
# ostrich
# knee
# cricket
# deck
# bit
# silk
# jean
# cotton
# drum
# sand
# shock
# march
# cage
# whole
# change
# department
# office
# ticket
# energy
# idea
# hospital
# noise
# sample
# example
# lesson
# plenty
# luck
# comedy
# health
# history
# forest
# stream
# future
# state
# temple
# dictionary
# grammar
# college
# husband
# daughter
# captain
# booth
# iceberg
# bubble
# bottom
# prize
# bean
# race
# engineer
# photographer
# reason
# subway
# fog
# answer
# dinning
# step
# heat
# bone
# plant
# lamb
# rate
# report
# turtle
# bay
# holiday
# center
# cash
# wolf
# operator
# fur
# shore
# owl
# hunter
# pumpkin
# handshake
# bike
# beach
# god
# cough
# shell
# business
# restaurant
# sheep
# officer
# hometown
# coil
# ceiling
# turkey
# towel
# matter
# chopstick
# seat
# board
# goal
# drugstore
# rat
# butterfly
# flute
# couple
# beer
# background
# bottle
# body
# group
# village
# beef
# load
# coin
# bookstore
# label
# port
# quarter
# sunrise
# sunshine
# wedding
# crown
# seed
# coal
# comb
# dream
# sugar
# mile
# flashlight
# vegetable
# mouse
# wood
# war
# ground
# belt
# tourist
# airport
# passport
# plate
# stone
# downtown
# cousin
# tooth
# potato
# blanket
# creek
# nail
# letter
# date
# store
# beggar
# bedside
# deer
# bill
# doll
# pepper
# frog
# rest
# tower
# bridge
# cloth
# post
# snake
# job
# town
# fun
# bathroom
# tail
# mayor
# piece
# fruit
# british
# french
# German
# sale
# rope
# umbrella
# dollar
# mistake
# birth
# pilot
# none
# front
# present
# nickname
# telephone
# pair
# weather
# dish
# hole
# plane
# living
# gun
# meat
# cover
# grass
# watch
# word
# explain
# wear
# amuse
# suppose
# leap
# bury
# engage
# sow
# lift
# bow
# rub
# bite
# vote
# hop
# imagine
# allow
# offer
# gain
# alarm
# obey
# steal
# dig
# choose
# receive
# bet
# hurt
# burn
# sink
# decide
# beg
# reply
# tear
# flow
# remember
# appear
# breathe
# whistle
# draw
# sound
# save
# continue
# check
# sail
# wake
# agree
# hang
# record
# drop
# climb
# add
# shine
# invite
# join
# hide
# bring
# wink
# shoot
# roll
# pull
# push
# guess
# belong
# happen
# pick
# shake
# fill
# fail
# fight
# fear
# carry
# dive
# win
# ride
# turn
# need
# build
# hurry
# return
# believe
# surprise
# gather
# throw
# raise
# count
# smell
# spend
# pitch
# pop
# blow
# miss
# excuse
# hit
# tie
# touch
# stay
# enjoy
# lose
# close
# arrive
# travel
# reach
# hold
# worry
# marry
# expect
# understand
# become
# break
# smoke
# lend
# shut
# sleep
# lay
# paint
# lead
# pass
# hand
# ancient
# nuclear
# necessary
# common
# inner
# thirsty
# thin
# gray
# famous
# industrial
# silent
# absent
# flat
# main
# wild
# wet
# blind
# dumb
# sharp
# terrible
# grand
# homesick
# bound
# fat
# strange
# pleasant
# handsome
# equal
# dear
# sweet
# dull
# weak
# bright
# honest
# elder
# such
# able
# loud
# simple
# clever
# proud
# foolish
# possible
# enough
# wise
# wide
# successful
# clear
# clean
# deep
# own
# cheap
# certain
# important
# stormy
# true
# sad
# gay
# merry
# colorful
# wonderful
# peaceful
# angry
# dry
# wrong
# heavy
# quiet
# several
# alone
# crowded
# excited
# alive
# brown
# different
# difficult
# interesting
# unlike
# least
# afraid
# cool
# pretty
# kind
# sick
# useless
# busy
# early
# past
# dark
# cloudy
# short
# low
# sincerely
# fortunately
# finally
# immediately
# especially
# else
# actually
# hardly
# otherwise
# tightly
# recently
# rapidly
# however
# politely
# rudely
# further
# frankly
# properly
# haste
# rather
# together
# altogether
# suddenly
# mostly
# correctly
# ahead
# instead
# quite
# nearly
# badly
# almost
# exactly
# apart
# afterward
# later
# maybe
# perhaps
# probably
# either
# neigher
# besides
# anyway
# sometime
# forward
# since
# once
# twice
# indeed
# seldom
# upside
# whether
# unless
# though
# while
# usually
# safely
# along
# without
# behind
# beyond
# below
# toward"""
# su=0
# for i in st.split():
#     for j in "python":
#         su += i.count(j)
# print(su)

# su2=0
# for i in "python":
#     su2+=st.count(i)
# print(su2)

# print("START!!!")
# st1 = input("시작단어를 입력하세요 : ")
# while True:
#     # 전단어 출력하고 사용자에게 입력받는다
#     st2 = input(f"{st1} : ")
#     # 채점
#     if st1[-1]==st2[0]:
#         print("PASS :)")
#         st1=st2
#     else:
#         print("FAIL :(")
#         break

# 문자 랜덤 출력
# import random

# word = ["apple","banana","cookie"]

# for i in range(100):
#     r = random.randint(0,len(word)-1)
#     print(word[r])

# # 65~90 대문자
# for i in range(100):
#     print(chr(random.randint(65,90)))

# # 97~122 소문자
# for i in range(100):
#     print(chr(random.randint(97,122)))

# 함수
# input x
# func f:
# output f(x)

# def add(a,b):
# num = a+b
# return num

# argument = 입력값 = 인자 = 파라미터

# def mul(a,b):
#     num=a*b
#     return num

# print(mul(10,20))

# 두 수의 차이 구하기
# def min(a,b):
#     num = a-b
#     if num<0:
#         num=-num
#     return num

# print(min(2,5))
# print(min(5,2))

# 팩토리얼 구하기
# def fact(a):
#     num=1
#     for i in range(1,a+1):
#         num*=i
#     return num
# print(fact(6))

# 약수 구하기
# def divisor(a):
#     li=[]
#     for i in range(1,a+1):
#         if a%i==0:
#             li.append(i)
#     return li

# print(divisor(100))

# 클래스
# 객체의 속성과 특징!!
# 변수, 함수
# A는 객체
# A는 모험가 class의 인스턴스
# class 모험가():
#     힘=10
#     지력=4
#     운=5
#     덱스=7
# a=모험가()
# b=모험가()
# c=모험가()
# for i in [a,b,c]:
#     print(i.)