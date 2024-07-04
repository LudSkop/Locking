

def left2(sr):
  if len(sr) <= 2:
    return sr
  return sr[2:] + sr[:2]





print(left2('opera'))