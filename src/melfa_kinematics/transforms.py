import numpy as np

def Trans(x, y, z):
   T = np.array([
   [1, 0, 0, x],
   [0, 1, 0, y],
   [0, 0, 1, z],
   [0, 0, 0, 1]
   ])

   return T




def RotX(theta):
   R = np.array([
   [1, 0, 0, 0],
   [0, np.cos(theta), -np.sin(theta), 0],
   [0, np.sin(theta), np.cos(theta), 0],
   [0, 0, 0, 1]
   ])


   return R


def RotY(theta):
   R = np.array([
   [np.cos(theta), 0, np.sin(theta), 0],
   [0, 1, 0, 0],
   [-np.sin(theta), 0, np.cos(theta), 0],
   [0, 0, 0, 1]
   ])


   return R


def RotZ(theta):
   R = np.array([
   [np.cos(theta), -np.sin(theta), 0, 0],
   [np.sin(theta), np.cos(theta), 0, 0],
   [0, 0, 1, 0],
   [0, 0, 0, 1]
   ])


   return R

