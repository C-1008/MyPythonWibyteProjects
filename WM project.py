import time
import random
import os
import datetime as dt


class BadLetterError(Exception):


  def __init__(self, message = "Some of those letters are not nice"):
    self.message = message
    super().__init__(message)
  

  pass

class BadTimeError(Exception):
  pass


def readfile():
  try:
    with open("booster.txt", mode = "r") as file:
        print(file.readline())
  except FileNotFoundError:
    print("Unfortunately, you are out of luck today")


def short_form(idx, *names, **addons):
  final = ''

  try:
    for name in names:
      final = final + name[idx]

    
    for keys in addons:
      if keys == 'prefix':
        final = addons[keys] + final
      elif keys == 'suffix':
        final = final + addons[keys]
      else:
        print('You are not good at typing, are you ...')
        
  except TypeError as e:
    print('Wrong data type: ', e)
  except IndexError as e:
    print('Indexing is going wrong:', e)
  except Exception as e:
    print('Something went wrong', e)
  else:
    return final
  finally:
    print("Hope you managed to pass this stage ...")
    print("Try readfile() to see your luck")
    # write to a file
    if random.randint(1, 100) < 10:
      with open("booster.txt", mode = "w") as file:
        file.write("You're lucky")
    
  

strength = {'name':10, 'surname':20, 'nickname': 30, 'alias': 40, 'aka':50}
  
  
def name_strength(**fullname):
  result = 0
  try:
    for key, value in fullname.items():
      result += strength[key]*len(value)
  except KeyError as e:
    print('Perhaps you are giving too many fields', e)
  else: 
    return result
    




def validate(**prelimdata):
  try:
    assert prelimdata['sc'] != None
    assert prelimdata['ns'] != None
  except KeyError as e:
    print('You are really bad at typing, aren\'t you?')
    print('Validation failed due to ', e)
  except AssertionError:
    print('One of the earlier steps has gone wrong.')
    print('Validation failed')
  else:
    print('Looking good so far ...')
    print('Sending for deeper validation')
    print('opening connection to a remote server ...')
    try:
      # parameters based on your luck
      deep_validate(prelimdata)
    except ValueError:
      print('There is something deeply wrong')
      print('Validation failed ...')
    except BadLetterError as e:
      print("I was not satisfied with some of the letters ...", e)
      print("Validation Failed ....")
    except BadTimeError as e:
      print("I was not satisfied with the timing, please try again later...")
      print("Validation Failed ....")
    else:
      print('Congrats ... Validation Successful')
      print('Welcome to my world!')
    finally:
      print('Closing connection to the remote server')

def deep_validate(prelimdata):
  print(prelimdata)

  threshold_ns = random.randint(1, 200)
  threshold_sc = random.randint(10, 20)

  print()
  print(threshold_ns, threshold_sc)
  print()

  badLetters = ["a", "r", "e"]

  ct = dt.datetime.now()
  if ct.second % 2 == 0:
    raise BadTimeError

  if any(x in prelimdata["sc"] for x in badLetters):
    raise BadLetterError("Please don't input a, r and e")
  
  if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc:
    raise ValueError


print('Welcome to the Programmers\' Den')
print("I hear you have been learning Python")
print('Guess you can use the command line to create your own welcome kit')

print()

print("You may want to read the README file for instructions.")
print("Since I guess you may not have the time to read it, here are the instructions anyways ...")
print()

print('The process is simple, create a short code, check your name strength and then validate')


print('For short code, use sc = short_form(idx, a few words about youself, prefix = , suffix = ')

print('For name strength code, use ns = name_strength(name =, surname = , aka = , alias = , salutation = ')

print('For validate, use validate (sc = sc, ns = ns)')

print('Alright champ, get going ...')

# Delete booster .txt if it is present
try:
  os.remove("booster.txt")
except FileNotFoundError:
  pass


print(' ')





    
  #print(names)
  
  #return final.upper()
    
  #return str1[0].upper() + str2[0].upper()


#final = ''

#for name in names:
#  final = final + name[idx]
