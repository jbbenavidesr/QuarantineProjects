#!/usr/bin/env python3
# -*- coding: utf-8 -*-
p = [0.6, 0.2, 0.1, 0.05, 0.05]


def get_hamming(prob_list):
	"""
	"""
	ordered_list = sorted(prob_list, reverse=True)
	hamming = {k:"" for k in ordered_list}
	i = 0
	code = ""

	while True:
		temp_lis = sorted([ordered_list[i], sum(ordered_list[i:])], reverse=True)

		hamming[ordered_list[i]] +='1'
		for p in ordered_list[i+1:]: hamming[p] += "0"
		
		i += 1
		if i == len(ordered_list):
			break

	print(hamming) 

get_hamming(p)