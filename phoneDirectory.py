from collections import deque

class PhoneDirectory(object):
  # queue and array
  # TC : O(1)
  # SC : O(n)

  def __init__(self, maxNumbers):
    """
    Initialize your data structure here
    @param maxNumbers - The maximum numbers that can be stored in the phone directory.
    :type maxNumbers: int
    """
    self.available = [True] * maxNumbers
    # use extra space deque, to get faster get() call
    self.q = deque([i for i in range(0, maxNumbers)])

  def get(self):
    """
    Provide a number which is not assigned to anyone.
    @return - Return an available number. Return -1 if none is available.
    :rtype: int
    """
    if self.q:
      self.available[self.q[0]] = False
      return self.q.popleft()
    return -1

  def check(self, number):
    """
    Check if a number is available or not.
    :type number: int
    :rtype: bool
    """
    return self.available[number]

  def release(self, number):
    """
    Recycle or release a number.
    :type number: int
    :rtype: void
    """
    if not self.available[number]:
      self.available[number] = True
      self.q.append(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
