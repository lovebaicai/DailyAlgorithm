#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen

#https://leetcode.com/problems/reconstruct-itinerary/description/
#http://bookshadow.com/weblog/2016/02/05/leetcode-reconstruct-itinerary/

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    Example 1:
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
"""

# method one
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        rouotes = collections.defaultdict(list)
        for s, e in tickets:
            routes[s].append(e)
        def solve(start):
            left, right = [], []
            for end in sorted(routes[start]):
                if end not in routes[start]:
                    countinue
                routes[start].remove(end)
                subroutes = solve(end)
                if start in subroutes:
                    left += subroutes
                else:
                    right += subroutes
            return [start] + left + right
        return solve("JFK")

# method two
class Solution(object):        
    def findItinerary(self, tickets):        
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]
            targets[a] += b
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit("JFK")
        return route[::-1]
