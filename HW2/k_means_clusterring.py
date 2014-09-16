#!/usr/bin/python
import random
import math

class PixelImage(object):
  def __init__(self, vector_list, label):
    self.vector = vector_list
    self.label = label

def readFiles():
  pixelImageList = list()
  fp = open('mnist_data.txt', 'r').readlines()
  kp = open('mnist_labels.txt', 'r').readlines()
  if len(fp) != len(kp):
    print "not as many labels as vectors instances"
  else:
    for index, ii in enumerate(fp):
      pixelImageList.append(PixelImage(ii.strip().split(" "),kp[index].strip())) 
    return pixelImageList
  
def calculate_euclid_distance(v_one, v_two):
  #print v_one
  #print v_two
  tot = sum([(int(v_one[ii]) * int(v_two[ii]))**2 for ii in range(len(v_one))])
  return math.sqrt(tot)

def create_assignments(dataset, k_points):
  assignments = {}
  for ii in dataset:
    min_distance = float("inf")
    for centers in k_points:
      if isinstance(centers, list):
        cur_distance = calculate_euclid_distance(ii.vector, centers)
      else:
        cur_distance = calculate_euclid_distance(ii.vector, centers.vector)
      if cur_distance <= min_distance:
        min_distance = cur_distance
        try:
          assignments[centers].append(ii)
        except:
          assignments[centers] = [ii]
  return assignments 

def update_centers(assignments):
  value = list()
  for ii in assignments.values():
    vector = list()
    for index in range(0, 784):
      sum = 0
      for point in ii:
        sum += int(point.vector[index])
      sum /= len(ii)
      vector.append(sum)
    value.append(vector)
    print "=============="
    print len(vector)
    print "=============="
  return value

def k_means(dataset, k):
  k_points = [dataset.pop(random.randint(0, len(dataset))) for ii in range(0, k)]
  old_k_points = None
  counter = 0
  while k_points != old_k_points:
    counter += 1
    print "This is iteration %s" %counter
    assignments = create_assignments(dataset, k_points)
    new_k_points = update_centers(assignments)
    old_k_points = [elem.vector for elem in k_points]
    k_points = new_k_points

k_means(readFiles(), 10)
