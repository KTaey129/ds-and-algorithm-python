# Sort in desceding order or ascending order the given stack
# 1. Create a temporary stack
# 2. While input stack is not empty
#   1. Pop number from input stack
#   2. While temporary stack is not empty and the top of the temporary stack is greater than the popped element:
#     Pop from temporary stack and push it to the input stack
#   3. Push popped number in temporary stack
# 3. Return sorted numbers (temporary stack)

from typing import List

def sortStack (stack: List[int], ascending: bool = True) -> List[int]:
  tmpStack = []

  while(stack):
    num = stack.pop()
    while tmpStack and ((tmpStack[-1] < num) if ascending else (tmpStack[-1] > num)) :
      stack.append(tmpStack.pop())
    tmpStack.append(num)

  return tmpStack

# Using Recursion
def sortStack(stack):
  if len(stack) == 0:
    return stack
  top = stack.pop()
  sortStack(stack)
  insertInSortedOrder(stack, top)
  return stack

def insertInSortedOrder(stack, value):
  if len(stack) == 0 or stack[-1] <= value:
    stack.append(value)
    return
  top = stack.pop()
  insertInSortedOrder(stack, value)
  stack.append(top)
