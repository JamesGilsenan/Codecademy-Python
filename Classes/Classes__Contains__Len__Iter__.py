class LawFirm:
# __init__, our constructor, which sets a the practice and list of Lawyers
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

#__len__, the length method, so when we call len(LawFirm()) it will return the length of the underlying 
# self.lawyers list.
  def __len__(self):
    return len(self.lawyers)

#__contains__, the check for containment, allows us to use lawyer in LawFirm syntax to check if a lawyer
#  exists in the lawyers we have.
  def __contains__(self, lawyer):
    if lawyer in self.lawyers:
      return True
    else:
      return False
      
#__iter__, the iterator, we use the iter() function to turn the list self.lawyers into an iterator so we can 
# use for lawyer in LawFirm syntax
  def __iter__(self):
    return iter(self.lawyers)

    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print(len(d_and_p))
if "Donelli" in d_and_p:
  print("He's part of the team")