import numpy as np
class matrix:
  def __init__(self)->None:
    pass
  def addition(self,a:list,b:list):
    a=np.array(a)
    b=np.array(b)
    return a+b
  def sub(self,a:list,b:list):
    a=np.array(a)
    b=np.array(b)
    return a-b
  def addi(self,a:list,b:list):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
      return "Matrices must be of same dimensions!"
    res=[[0 for i in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
      for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]
    return res 
  def tran(self,a:list):
    res=[[a[j][i]for j in range(len(a))]for i in range(len(a[0]))]
    return res


