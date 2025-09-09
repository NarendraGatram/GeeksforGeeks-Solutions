class solution:
    def isRotated(self,s1,s2):
        n = len(s1)

        right_rotation = s1[2:] + s1[:2]

        left_rotation = s1[n-2:] + s1[:n-2]

        if right_rotation==s2 or left_rotation==s2:
            return True
        else:
            return False