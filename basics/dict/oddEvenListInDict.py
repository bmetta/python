#!/usr/bin/python

def main():
  list_int = range(1, 10)
  dict_evenOdd = {}
  
  for i in list_int:
    if (i % 2) == 0: #even
      if not 'even' in dict_evenOdd:
        dict_evenOdd['even'] = [i]
      else:
        dict_evenOdd['even'].append(i)
    else:
      if not 'odd' in dict_evenOdd:
        dict_evenOdd['odd'] = [i]
      else:
        dict_evenOdd['odd'].append(i)

  print dict_evenOdd
  print dict_evenOdd.items()
  print dict_evenOdd.keys()
  print dict_evenOdd.values()

if __name__ == '__main__':
  main()
