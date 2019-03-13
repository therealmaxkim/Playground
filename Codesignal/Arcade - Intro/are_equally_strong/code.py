'''
Questions


Observations
1. Only four inputs. easy to hardcode
2. Both numbers must exist in both arms. If not, the result is always false.
3. The value does not matter. As long as both numbers exist in both people, the result is always true
4. 

'''


def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if (yourLeft == friendsLeft or yourLeft == friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight):
        return True
    else:
        return False
