import heapq
from typing import List
from collections import Counter
def topStudents(positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        p = set(positive_feedback)
        n = set(negative_feedback)
        hp = []
        res = []
        for r, i in zip(report, student_id):
            score = 0
            for s in r.split():
                if s in p:
                    score += 3
                elif s in n:
                    score -= 1
            heapq.heappush(hp, (-score, i))
        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        return res