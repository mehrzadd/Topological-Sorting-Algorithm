import sys
import os

try:
  first_arg = sys.argv[1]
  d = {}
  def main_program (data=first_arg):
      with open(data, 'r') as f:
        for line in f:
           (key, val) = line.strip().split('\t') 
           if key in d:
               d[key].append(val)
           else:
               d[key] = [val]     
           if val not in d:
                d[val] = []
      order = sort(d)
      for task in order:
        print(task)


  def visit(g, u, status, item, Final_sort, cycle):
      item=True
      if cycle[0]:
          return
      status[u] = "visit"
      for v in g[u]:
          if status[v] == "visit":
              cycle[0] = True
              return
          if status[v] == "free":
              visit(g, v, status, item, Final_sort, cycle)
      status[u] = "finish"      
      Final_sort.append(u)  
  def sort(g):
    status = { u : "free" for u in d}
    item=True         
    Final_sort = []
    cycle = [False]
    for u in g:
        if status[u] == "free":
            visit(g, u, status, item, Final_sort, cycle)
        if cycle[0]:
          print("there is a cycle")          
          sys.exit(0)  
          break
    if cycle[0]:
        print("there is a cycle")          
        sys.exit(0)                
    Final_sort.reverse()                  
    return Final_sort                     


  if __name__ == '__main__':
    main_program()


except Exception as e:
  print ("please give an input")
  sys.stdout.flush()

