class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for new in asteroids:
            while res and new < 0 <res[-1]:
                if res[-1] < -new:
                    res.pop()
                    continue
                elif res[-1] == -new:
                    res.pop()
                break
            else:
                # new is positive (go right)
                res.append(new)                
        return res 