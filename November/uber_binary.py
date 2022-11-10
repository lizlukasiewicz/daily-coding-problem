"""

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.

"""
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def __str__(self):
    return f'{self.data}'

class BinaryTree:
  def __init__(self):
    self.root = None